from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, ArticleForm, UserRegisterForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib import messages


def index(request):

    return render(request, "index.html")


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "article.html"
    paginate_by = 6

def profile(request):

    return render(request, "profile.html")


def publish(request):

    if request.method == 'POST':
        ArticleForm(request.POST, request.FILES)

        if article_form.is_valid():
            form = article_form.save(commit=False)
            form.author = User.objects.get(username=request.user.username)
            form.slug = form.titile.replace(" ", "-")
            messages.SUCCESS(request, 'Your article post has been submitted for approval')
            form.save()
        
        return redirect('my_articles')

    article_form = ArticleForm()
    context = {'article_form': article_form}

    return render(request, 'publish.html', context)


def my_articles(request):

    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=logged_in_user)
    return render(request, 'my_articles.html', {'posts': logged_in_user_posts})


def edit_article(request, posy_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=post)
        if article_form.is_valid():
            form = article_form.save(commit=False)
            form.approved = False
            messages.SUCCESS(request, 'Updated article post has been submitted for approval')
            form.save()

            return redirect('my_articles')
    article_form = ArticleForm(instance=post)
    context = {'article_form': article_form}

    return render(request, 'edit_article.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")

            return redirect('profile')
        
        else:
            form = UserRegisterForm()
        return render(request, 'account/signup.html', {'form': form})
