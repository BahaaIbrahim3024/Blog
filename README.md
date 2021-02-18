# Blog

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
