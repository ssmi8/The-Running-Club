# The Running Club

## About
The Running Club is a platform for avid runners.  The aim of this project is to join the running community in sharing thoughts, ideas and experiences they have faced.  Each user can add an article they feel can help the community, where other users can comment, like they content.  Users can also join group runs through the booking form based on their level of ability.




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
    - [Booking Model](#booking-model)
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


### CRUD Functionality

The site offers a feature to Creade, Read, Update and Delete articles they post, as well as any bookings a user has made.

- Create - new (un-authenticated) users can register with The Running Club to create a user account, and members (authenticated users) can comment/like articles and book runs with groups.

- Read - authenticated users can view all of the runs they have booked.

- Update - authenticated users can edit their articles and reschedule any of their bookings by changing a booking to their new preferred time and date.

- Delete - authenticated users can cancel any of their bookings, as well delete articles they have published.

## Features

### Existing Features

- Home Page
    - The home page has minimal content which gives a brief overview to the website, and doesn't overload the user with information.  There is a simple navigation bar for the user to navigate through the site easily.  If the user is not registered, the navigation bar will allow users to log in register.  If the user is registered and logged in, the can access their account or logout.

    ![Home Page - top](/documentation/home_page1.jpg "Home Page")
    
    - The account button takes the users to their profile.

- Article Page
    - The Article page is where the articles are shown.
    - The articles are shown with an image as a background for that post, along with the author.
    - The title, excerpt, date of publication and number of likes are visible for each post.

    ![Article Page](/documentation/articles_page.jpg "Article Page")

    - This feature helps the user to choose a particular article to view and gives them an idea as to what the article is about.
    - The Article page has pagination feature with each page upto 6 posts.

   ![Next Button](/documentation/next.jpg "Next Button")
   
   ![Previous Button](/documentation/prev.jpg "Previous Button")


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

- Booking a Run, with reschedule/delete options
    - Users can only access this page once registered and logged in
    - If a user is not logged in, the page will redirect to the sign in page
    - Users can submit a level category based on their ability (Beginner, Intermediate, Advanced)
    - Once booking is confirmed, they booked runs are displayed, with the ability to edit or delete

    ![Booking Page](/documentation/booking_page.png "Booking Page")

### Future Features
- Account holders will be able to save their favourite articles or to read later.
- Users can set up their own profile page.
- Follow other Users.

## Agile Development

### Wireframes

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


- As the project developed some details of the User stories were reviewed and revised. Changes were made to ensure the delivery of a Miminum Viable Product. As one example, I was unable to create a schedule for users to be able to select a date to run, so this was moved into to a fututre featurecolumn of the kanban board. Click [here](https://github.com/users/ssmi8/projects/2) to visit this Github page


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

### Booking Model:

The Booking Model handles the booking of runs, the session type and date/time of the run booked.

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
            

Result:

![Test Views Result](/documentation/test_views.jpg "Test Views Result")

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

## Python Validator

[CI Python Linter](https://pep8ci.herokuapp.com/) was the validator used. All the Python code passed without errors, except for the following files:

- article/views.py
- booking/views.py

Which gave E501 'line too long' and W293 'contains whitespace' warnings.  These have been corrected where possible.

![article python linter](/documentation/article_views_test.png "CI Python Linter")

![booking python linter](/documentation/booking_views_test.png "CI Python Linter")




## User Story Testing

### Admin

- As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
- As a Site Admin I can create, read, update and delete posts so that i can manage the content.
- As a Site Admin I can approve posts before it's published so the site can be consistent.
- As a Site Admin I can aprove comments before it's published.

![Admin Approve](/documentation/admin_approve.jpg "Admin Approve")

![Comment Approve](/documentation/comment_approve.jpg "Comment Approve")

### Member User

- As a Member User I can register an account so that I can manage my posts, comment and like.

![Sign Up](/documentation/signup_page.jpg "Sign Up")

- As a Member User I can post/add/edit/delete articles and manage my articles.

![Profile](/documentation/profile_page.jpg "Profile")

- As a Member User I can like/unlike a post.
- As a Member User I can leave comments on a post.

![Comments](/documentation/comment_page.jpg "Comments")

- As a Member User I can view my posts.

![Manage Page](/documentation/manage_articles_page.jpg "Manage Page")


### General User

- As a Site User I can view a list of posts and select one to read.
- As a Site User I can view comments and likes

![Article Page](/documentation/articles_page.jpg "Article Page")


## Deployment:

This project was deployed to Heroku,using an ElephantSQL Postgres database.

Steps to open an account in Heroku:

- Sign Up, if you don't already have an account already.
- After you fill in all require information, and sign in you will be able to create an app.
- Click on New -> Create nee app
- Choose a name for your application and select location you are based.

The initial deployment was immediately after cretaing all the file directories within the repository. This is to ensure and overcome any deployment error before hand and resolve the issue before it gets more complicated.

Steps to Deployment

- Fork or clone this repository in GitHub.

- You will need a Cloudinary account to host user images and static files.

- Login to Cloudinary.

- Select the 'dashboard' option.

 - Copy the value of the 'API Environment variable' from the part starting cloudinary:// to the end. You may need to select the eye icon that allows you to view the full environment variable. copy and paste this value to a document or file until it is needed.

- Log in to Heroku.

- Select 'Create new app'.

- Enter a name for the app and select the appropriate region (Eurpoe, in the case of this project).

- Select 'Create app'.

- Select 'Settings'.

- Login to ElephantSQL.

- Click 'Create new instance' on the dashboard.

- Name the 'plan' and select the 'Tiny Turtle' option.

- Select 'select region'.

- Choose the nearest data centre to your location.

- Click 'Review'.

- Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.

- Copy the ElephantSQL database URL to your clipboard.

- Return to the Heroku dashboard.

- Select the 'settings' tab.

- Locate the 'reveal config vars' link and select.

- Enter the following config var names and values:

    - CLOUDINARY_URL: 'value'
    - DATABASE_URL: 'value'
    - PORT: 8000
    - SECRET_KEY: 'value'
    - Select the 'Deploy' tab.

- Select 'GitHub' and confirm you wish to deploy using GitHub. If prompted, enter your GitHub password.

- Find the 'Connect to GitHub' section and locate your repository.

- Select 'Connect' when found.

- If you decide that your deployed site be automatically redeployed every time you push changes to GitHub then choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' option.

- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.

- Your site will be deployed once the build is complete.


I have followed Code Institute's [Django Blog Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

### Step 1: Installing Django and supporting libraries

In the Terminal:

![Step1](/documentation/step_1.jpg "Step1")

In the settings.py file:

![Step1_2](/documentation/step_1_2.jpg "Step1_2")

In the Terminal:

![Step1](/documentation/step_1_1.jpg "Step1")


### Step 2: Deploying an app to Heroku

Here there are 4 stages:
1. Create the Heroku App
2. Attach the database
3. Prepare the environment and settings.py file
4. Get our static and media files stored on Cloudinary

2.1 Create the Heroku app

In Heroku:

![Step2](/documentation/step2_1.jpg "Step2")

2.2 Attach the Database:

In gitpod

![Step2](/documentation/step2_2.jpg "Step2")

2.3 Prepare our environment and settings.py file:

![Step2](/documentation/missingsteps.jpg "Step2")

2.4 Get our static and media files stored on Cloudinary:

![Step2](/documentation/step2_3.jpg "Step2")

![Step2](/documentation/step2_31.jpg "Step2")

![Step2](/documentation/step2_4.jpg "Step2")

![Step2](/documentation/step2_41.jpg "Step2")

![Step2](/documentation/step2_5.jpg "Step2")

Before the final Deployement: Remove the "DISABLE_COLLECTSTATIC" from Heroku Config vars, and Change Debug to "False" in settings.py

## Bugs/Errors

During this project, I have run into a few problems, which has helpped me develop my skills in coding as well as troubleshooting potential issues.

- An issue I had was that my original database was corrupt, which was causing many issues in my project, where I could not add a Booking page, nor add any new articles/comments.  THis was rectified by creating a new database in Elephant SQL, and relinking to the project and Heroku.

- Another issue I faced was that comments would not be posted, even after approval.  I identified the issue, which was caused by the save command, lacking the () afterwards.  This was fixed and subsequently I was able to post comments.

- Another issue that I found, was that posts would not appear on the page, even after approval.  I decided to remove the approve requests in the model.py and this worked.  Posts can still be approved on the admin page, by using the dropdown menu and selecting publish, rather than draft.


## Credits

During the project development process, I have used various sources to aid my development and help me overcome particular features/bugs.  The following are the sources I got my knowledge from:

- Stack Overflow
- Django Project Documentation
- Code Institute - Course materials and Django Blog Walkthrough Project.
- Bootstrap Modal
- Cripsy Forms
- Youtube videos - User Registration & Admin approvals - Corey Schafer & Code.My

## Acknowledgements

I would like to acknowledge and present my thanks to Rahul, my mentor from Code Insitute for his guidance and constant support. It wouldn't have been possible without the amazing community in Slack, Tutors of Code insitute Tutor supports, and my friends who constantly motivated and supported me.

