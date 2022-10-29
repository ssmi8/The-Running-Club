# The Running Club

## About
The Running Club is a platform for avid runners.  The aim of this project is to join the running community in sharing thoughts, ideas and experiences they have faced.  Each user can add an article they feel can help the community, where other users can comment, like they content.




The live site can be found [here](https://the-running-club.herokuapp.com/).

## Table of Contents

- [About](#about)
- [User Experience](#user-experience)
    - [Admin](#admin)
    - [Member User](#member-user)
    - [General User](#general-user)
-[Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [Wireframes](#wireframes)
- [Structure](#structure)
- [Databases](#databases)
    - [Post Model](#post-model)
    - [Comment Model](#comment-model)
- [Technologies Used](#technologies-used)
- [Frameworksm, Libraries & Tools Used](#frameworks-libraries--tools-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)



## User Experience

The website was designed with the design thinking approach.  The website only contains necessary content and information for the user.  The user can flow through the website easily and get to the information they are looking for.
The defined user stories can be found here.

### Admin

- As a Site Admin I can approve posts that I can filter out obejectionable posts.
- As a Site Admin I can create, read, update and delete posts so that the articles can be managed.
- As a Site Admin I can approve posts before they are published.

### Member User

- As a Member User I can register an account so that I can manage my posts, comment and like articles.
- As a Member User I can post/add/edit/delete articles so that I can share and manage my posts.
- As a Member User I can like or unlike a post to interact with articles.
- As a Member User I can leave comments on a post to interact with other users.
- As a Member User I can view my posts status of approval so I can manage my articles.

### General User

- As a Site User I can view a list of posts so I can select one to read.
- As a Site User I can click on a post to read the full article.
- As a Site User / Admin User I can view comments on an article.
- As a Site User / Admin User I can view the number of likes on each post.

## Features

### Existing Features

- Home Page
    - The home page has minimal content which gives a brief overview to the website, and doesn't overload the user with information.  There is a simple navigation bar for the user to navigate through the site easily.  If the user is not registered, the navigation bar will allow users to log in register.  If the user is registered and logged in, the can access their account or logout.

    ![Home Page - top](/documentation/home_page1.jpg "Home Page")
    ![Home Page - bottom](/documentation/home_page2.jpg "Home Page")

    - The account button takes the users to their profile.

- Article Page
    - The Article page is where the articles are shown.
    - The articles are shown with an image as a background for that post, along with the author.
    - The title, excerpt, date of publication and number of likes are visible for each post.

    ![Article Page](/documentation/articles_page.jpg "Article Page")

    - This feature helps the user to choose a particular article to view and gives them an idea as to what the article is about.
    - The Article page has pagination feature with each page upto 6 posts.

    ENTER NEXT & PREVIOUS

- Sign Up
    - Users can register and create their own account.
    - The sign-up form check if the uusername is used already and alerts the user if any information is incorrect, as an example: passwords don't match or required fields being empty.
    - Creating an account enables access to more features.
    - Registered users can publish and manage their article posts.
    - Registered users can like and comment on other articles.

    ![Sign Up Page](/documentation/signup_page.jpg "Sign Up Page")

- Sign In
    - Users can access their account via sign-in and login feature.
    - Once logged in, the users can publish and manage their articles, as well as like and comment on posts.
    - Users can login from the menu or homepage.
    - If the user has not got an account, they can signup using the link on the login page.

    ![Sign In Page](/documentation/signin_page.jpg "Sign In Page")

- Logout
    - The user can logout from the Menu and their accounts page.
    - When the user wants to logout a pop-up modal is triggered for confirmation.

- User Account/Profile Page
    - Once the user is registered or logged in, they have a user profile page.
    - In this page users can publish an article, or manage their articles.
    - If they want, they can access the logout feature through the logout button.

    ![Profile Page](/documentation/profile_page.jpg "Profile Page")

- Publish an article
    - Creating and adding an article by a registered user is possible.
    - The user can publish an article after signing in and from the profile page.
    - The user needs to enter the title, content and image to post the article.  THe excerpt is optional.

    ![Publish Page](/documentation/publish_page.jpg "Publish Page")

    - Once the article is published te user can view, edit or delete the article in the Manage Articles page.

- Manage Articles Page
    - User has the control to their published and pending approval articles.
    - The user can see the list of their articles.
    - Each article listed has information to that article.
    - Status of article: If the article is sent for approval and yet to be published, the display shows 'pending approval'.  Once approved by admin, it is published a message "Published" is displayed.
    - The buttons for editng and deleting are given for the user.

    ![Manage Page](/documentation/manage_articles_page.jpg "Manage Page")

- Edit an Article
    - An authenicated/owner of an article can edit only.
    - Either pending or approved articles can be edited.
    - When editing, form is prepopulated and ready for editing.

    ![Edit Page](/documentation/edit_page.jpg "Edit Page")

- Delete an Article
    - An authenicated/owner of an article can delete the article.
    - Either pending or approved articles can be edited.
    - If an article is selected for deletion, the user is asked for confirmation via pop-up alert.

    ![Delete Page](/documentation/delete_page.jpg "Delete Page")

- Like and Comment on an Article
    - All site users can view comments and likes.
    - Unregistered users cannot add a comment (no comment box to write in is visible).
    - Once users are registered the box is visible and users will have the ability to write a comment.
    - Registered users will also be able to like/unlike a post.

    ![Comment Page](/documentation/comment_page.jpg "Comment Page")
    ![Likes Page](/documentation/likes_page.jpg "Likes Page")

### Future Features
- Booking feature so users can join in nearby running groups.
- Account holders will be able to save their favourite articles or to read later.
- Users can set up their own profile page.
- Follow other Users.

## Wireframes

- When designing my project, I wanted to focus more of layout rather than detail, due to my overall goal of keeping the site simple and clean.  I made a few slight changes during the project updates, but kept to the design overall.

    - Home Page:
    ![Home Page Mockup](/documentation/home_page_mockup.jpg "Home Page Mockup")

    - Articles Page:
    ![Articles Page Mockup](/documentation/articles_page_mockup.jpg "Articles Page Mockup")

    - Manage Articles Page:
    ![Manage Page Mockup](/documentation/manage_page_mockup.jpg "Manage Page Mockup")

    - Account Page:
    ![Account Page Mockup](/documentation/my_articles_mockup.jpg "Account Page Mockup")

    - Publish Page:
    ![Publish Page Mockup](/documentation/publish_mockup.jpg "Publish Page Mockup")

    - Edit Page:
    ![Edit Page Mockup](/documentation/edit_article_mockup.jpg "Edit Page Mockup")

    - Register Page:
    ![Register Page Mockup](/documentation/register_page_mockup.jpg "Register Page Mockup")

    - Login Page:
    ![Login Page Mockup](/documentation/login_page_mockup.jpg "Register Page Mockup")



## Structure
The structure idea for The Running Club was to keep it clean and simple, avoiding content that filled up the whole page.  The idea was to keep it slick and allow the simplicity to help users access the content and navigate through the application easily.

Clean colours of white and black/dark grey have been used to create a crisp look and allow users to focus on the relevant content and important alerts.

The main app for this projects is Running Club Articles blog app.

Throughout the project development, GitHub projects was used.  Click here to view.

ENTER LINK TO PROJECTS ISSUE PAGES

## Databases

As The Running Club requires a database, I have created two database models:

![Post Model](/documentation/post_model.jpg "Post Model")

![Comment Model](/documentation/comment_model.jpg "Comment Model")

### Post Model:

The Post Model handles article details: title, status, date created/updated, featured image, excerpt and likes.  This model handles the base for confirming user authentication to manage their articles.

### Comment Model:

The Comment Model handles the content of the comment, the username of the commentor and time/date of the comment being issued.

## Technologies Used:

- HTML
- CSS
- JavaScript
- Python

## Frameworks, Libraries & Tools Used

- Bootstrap - grid, layout, columns, cards and forms structure.
- Django - django frameworks to manage apps.
- GitHub - to store the overall project repository.
- GitPod - used as workspace for the coding.
- Figma - To design the wireframe of the complete project.
- Google Fonts - For the written content and logo.
- Fontawesome - for social media icons.
- Heroku - for deployment of the project.
- PostgreSQL - database storage.
- Cloudinary - image and static files storage.
- AmIResponsive - responsiveness of the site.
- Lighthouse - used for testing site functionality.
- W3C Markup Validation Service - HTML testing.
- W3C CSS Validation Service - CSS testing.
- PEP8 - Python testing.

## Testing


### Unit Testing

I have used django TestCase for automated testing views, forms and models files.

### Testing Views

- Tested if the views are functioning as expected and returns pages that ther user needs to be at.
    - Testing Index/Home Page view:

    ```ruby
    class TestIndexViews(TestCase):   
        def test_get_index_page(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')
            


- Testing Article Page View:

    ```ruby
    class TestPostListViews(TestCase):
        def test_get_post_list_page(self):
            response = self.client.get('/article/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'article.html')
            



- Testing Profile Page View:

    ```ruby
    class TestProfileViews(TestCase):
        def test_profile_page(self):
            response = self.client.get('/profile')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'profile.html')
            


- Testing Adding/Publish Articles Page View:

   ```ruby
    class TestPublishPoemViews(TestCase):
        def test_can_publish_poem(self):
            response = self.client.get('/publish')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'publish.html')
            

Result:

ENTER TERMINAL RESULT

### Testing Forms:

- Tested Articles Post Form and Comment Form to ensure fields are as expected and the form is submitted to where it should:

    - Testing Article Form:

   ```ruby 
   class TestArticleForm(TestCase):
    def test_post_title_is_required(self):
        form = ArticleForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = ArticleForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ArticleForm()
        self.assertEqual(form.Meta.fields, ('title', 'content', 'excerpt',
        'featured_image'))

- Testing Comment Form:
    ```ruby 
    class TestCommentForm(TestCase):
    def test_post_title_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))

Result:
![Test Forms Result](/documentation/test_forms.jpg "Test Forms Result")

### Testing Models:

- Models are tested while testing views and forms as well. But in addition, I tested if the models shows that featured image is a requirement and successfully sent to the database:

    ```ruby 
    class TestModels(TestCase):
    def test_has_featured_image(self):
        self.assertTrue(Post.featured_image)

        

Result:
![Test Models Result](/documentation/test_models.jpg "Test Models Result")


## Validator Testing

### Lighthouse

- Testing results:

![Lighthouse Report](/documentation/lighthousereport.jpg "Lighthouse Report")

## W3C Markup Validation Service

- Errors and Warnings found and issues resolved with all tests passing.

    - Home Page:
    ![Home Validation](/documentation/html_home.jpg "Home Validation")

    - Article Page:
    ![Article Validation](/documentation/html_article.jpg "Article Validation")

    - Article Detail:
    ![Detail Validation](/documentation/html_detail.jpg "Detail Validation")

    - SignUp Page:
    ![Signup Validation](/documentation/html_signup.jpg "SignUp Validation")

    - Login Page:
    ![Login Validation](/documentation/html_login.jpg "Log In Validation")

    - Logout Page:
    ![Logout Validation](/documentation/html_logout.jpg "Log Out Validation")

    - Publish Page:
    ![Publish Validation](/documentation/html_publish.jpg "Publish Validation")

    - Profile Page:
    ![Profile Validation](/documentation/html_profile.jpg "Profile Validation")


- Errors and Warnings found but resolved:

![Errors](/documentation/bugs.jpg "Errors")

## W3C CSS Validation Service

![CSS Validation](/documentation/css_validator.jpg "CSS Validation")

## PEP8 Python Validator

PEP8 compliance was checked with pycodestyle due to PEP Online Validator currently down.

I used the following steps to check the compliance:

    1. Run the command pip3 install pycodestyle
    2. In the workspace, press Ctrl+Shift+P (Cmd+Shift+P on Mac).
    3. Type the word linter inot the search bar that appears, and clikc on Pythin: Select Linter from the filtered results.
    4. Select pycodestyle from the list.
    5. PEP8 errors will be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

Once I completed these steps, I did not have an errots underlined, nor any added to the PROBLEMS tab.

## BUGS

## User Story Testing

### Admin

    - As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
    - As a Site Admin I can create, read, update and delete posts so that i can manage the content.
    - As a Site Admin I can approve posts before it's published so the site can be consistent.
    - As a Site Admin I can aprove comments before it's published.

    ENTER ADMIN POST SCREEN FOR APPROVALS
    ENTER ADMIN COMMENTS SCREEN FOR APPROVALS

ADD TESTING PAGES

## Deployment:

This project was deployed to Heroku. 

## Credits

During the project development process, I have used various sources to aid my development and help me overcome particular features/bugs.  The following are the sources I got my knowledge from:

- Stack Overflow
- Django Project Documentation
- Code Institute - Course materials and Django Blog Walkthrough Project.
- Bootstrap Modal
- Cripsy Forms
- Youtube videos - User Registration & Admin approvals - Corey Schafer & Code.My

## Acknowledgements









