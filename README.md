# The Running Club

## About
The Running Club is a platform for avid runners.  The aim of this project is to join the running community in sharing thoughts, ideas and experiences they have faced.  Each user can add an article they feel can help the community, where other users can comment, like they content.





The live site can be found here.

## Table of Contents

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

## Future Features
- Booking feature so users can join in nearby running groups.
- Account holders will be able to save their favourite articles or to read later.
- Users can set up their own profile page.
- Follow other Users.

## Wireframes

## Structure
The structure idea for The Running Club was to keep it clean and simple, avoiding content that filled up the whole page.  The idea was to keep it slick and allow the simplicity to help users access the content and navigate through the application easily.

Clean colours of white and black/dark grey have been used to create a crisp look and allow users to focus on the relevant content and important alerts.

The main app for this projects is Running Club Articles blog app.

Throughout the project development, GitHub projects was used.  Click here to view.

ENTER LINK TO PROJECTS ISSUE PAGES

## Databases

As The Running Club requires a database, I have created two database models:

ENTER POST MODEL

ENTER COMMENT MODEL

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

Unit Testing, Validator Testing and Bugs are found here.

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









