# Blog
## * Overview
    This website for blog posts you can create, read, edit, delete (CRUD Operations) 
    your Own posts and review others blogs, make a favorite blogs list.
    Also there's API for the project using REST Framework.
    using django framework as back-end.

## * Operations 
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
