# Blog
## * Overview
    This website for blog posts you can create, read, edit, delete (CRUD Operations) 
    your Own posts and review others blogs, make a favorite blogs list.
    Also there's API for the project using REST Framework.
    using django framework as back-end.

## * [Operations](#website-sections)
        1- Building a custom User and Admin panel for Register, update, authenticate, delete users. 
            I- Also change password & reset it.
            II- User authentication via Django "TokenAuthentication".
            III- Generating Auth Tokens from a mobile app.
        2- For Blogs (Create, Retrieve, Update, Delete - CRUD operations).
            I- Create blog posts
            II- Retrieve blog posts
            III- Update blog posts
            IV- Delete blog posts
        3- API for Users & blogs.
        4- Serialization of data.
        5- Pagination (very important for mobile apps).

## * How to run
  - Open requirements.txt file and install all required libraries.
    
    if you're using Linux OS :
    
        1- cd to your requirements.txt location.
      
        2- then run " pip install -U -r requirements.txt "

### 1- Note (Very importannt about run in Development env)
   - if you're using Windows go to your settings.py file:
   
          replace " 'NAME': BASE_DIR / 'db.sqlite3', "

          with " 'NAME': str(BASE_DIR / 'db.sqlite3'), "

      in DB section for Sqlite Db , so you can run it on windows OS.
 
#website-sections
## Home Page 
    - go to (http://127.0.0.1:8000/) "Link".
![Home1](https://user-images.githubusercontent.com/29886682/109367788-bbc03080-789f-11eb-9966-e1c2ffd26952.png)

### 1- Register (Create) a new user
    - go to (http://127.0.0.1:8000/account/register/) "Link".
![Register](https://user-images.githubusercontent.com/29886682/109367795-be228a80-789f-11eb-903d-bc381350d16f.png)
![Register2](https://user-images.githubusercontent.com/29886682/109367796-bebb2100-789f-11eb-9b50-69121918071a.png)

### 2- Create new post
    - go to (http://127.0.0.1:8000/blog/create/) "Link".
![CreatePost1](https://user-images.githubusercontent.com/29886682/109367782-b7941300-789f-11eb-8ba6-74bb6e43106e.png)
![CreatePost2](https://user-images.githubusercontent.com/29886682/109367783-b7941300-789f-11eb-8381-6fef0808ba9b.png)
   - Note
   If you're trying to create a new post without register or login to your accout 
    the site will tell you that you must be authenticated first by resiter or login.
   - go to (http://127.0.0.1:8000/must_authenticate/) "Link".
![Must_Authenticate](https://user-images.githubusercontent.com/29886682/109367794-be228a80-789f-11eb-8248-e668a1168fc7.PNG)

### 3- View Details of the post
    - go to (http://127.0.0.1:8000/blog/<slug of your post>/) "Link".
![Details1](https://user-images.githubusercontent.com/29886682/109367784-b82ca980-789f-11eb-9632-d178f2d1bb7f.png)

### 4- Edit (Update) post data
    - go to (http://127.0.0.1:8000/blog/<slug of your post>/update) "Link".
![Update1](https://user-images.githubusercontent.com/29886682/109367798-bf53b780-789f-11eb-8851-62cd29893384.png)

### 5- Delete post
    If you are the owner of this post you're the only one authorized to delete or update thos post
    after delete you'll be redirected to the home Page.
![Home2](https://user-images.githubusercontent.com/29886682/109367791-bc58c700-789f-11eb-8b9c-6582b389102a.png)

### 6- Loved posts
    You can love or like posts of any user.

### 7- Login
    If you logedout of your accout you can login agin.
    - go to (http://127.0.0.1:8000/account/login/) "Link".
![Login](https://user-images.githubusercontent.com/29886682/109367793-bd89f400-789f-11eb-8429-26321246c6a7.png)
 
### 8- Reset Password
    In case you forget your password or want to reset it by sending reset password to your email.
            - go to (http://127.0.0.1:8000/password_reset/) "Link".
![ResetPassword](https://user-images.githubusercontent.com/29886682/109367797-bf53b780-789f-11eb-951e-881b39557e55.png)

### 9- Account Operations
    - go to (http://127.0.0.1:8000/account/update/) "Link".
![Account1](https://user-images.githubusercontent.com/29886682/109367778-b662e600-789f-11eb-8ca6-dfce0a2ee077.png)

    * You can update your account info.
 ![Update2](https://user-images.githubusercontent.com/29886682/109367775-b531b900-789f-11eb-8905-0f1d21a3549f.png)
        
        * Also Change password.
        * go to (http://127.0.0.1:8000/password_change/) "Link".
![ChangePassword](https://user-images.githubusercontent.com/29886682/109367779-b6fb7c80-789f-11eb-9641-0510e5f06bc0.png)

        * List for your own posts.
![CreatedPosts](https://user-images.githubusercontent.com/29886682/109367781-b6fb7c80-789f-11eb-9f18-e6fc8c64f404.png)

 
 ## 10- REST API Operations ( for account & posts )
 

 


