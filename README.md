# About and how to use

This is my first repository on github, my first project ever on internet, so if there is some mistakes please sorry for that, and sorry for bad english.
Idea was to play with django and create simple blog site

It's not finished yet, I need to add page for adding post, and I need to add option to select color of post title,
because right now is black and sometimes it can cause troubles with post thumbnail, if thumbnail is dark then you can't clearly see
post publisher and date. Right now you can add post through admin only with ckeditor.
Also I added some JavaScript and AJAX code for like, comment, register and login options.
If you find any bugs here, feel free to tell me.
Probably there is a better way to make this kind of website, but I didn't bother about this alot.

If you have any questions, and or if you find any bugs, or you have idea what to add to this feel free to tell.

This use Django 2.2.9 and django-ckeditor 5


First you need to install Django 2.2.9 and django-ckeditor, to do that you need to type
pip3 install -r requirements.txt or pip install -r requirements.txt

Then navigate to blog folder and type command python3 manage.py runserver or python manage.py runserver
And that's it you should see on which address is website running and try it.
There are two users created, superuser with username admin and password admin12345
And two normal users one have username test23 and password 123456
You can add posts only with admin user through admin page.
If you are running on for example localhost:8000 then go to localhost:8000/admin and login.
Then go to Posts and hit Add post button. And there it is. First you select user, that shoud be automatically but it's not, I left it that way just for testing.
Don't change number of likes or comments. Post thumbnail is first huge image that appears at the top of post you are reading.
Title is place where you put title of your post, and preview field is field to insert text you want to use as post previews, and that is displayed
in home page where are few posts listed, and in page where are all posts listed. Then there is a huge text area where you can
add post content, I used ckeditor. You can add images to post as well.
If you want to add images, click on image button in TextArea field, then go to upload click browse button, then find picture you want to add
and send it to server with button, or you can in image info section search for pictures on server.
In image info set image width to 600 (but don't touch that lock, so height resize automatically).
Thumbnail images are renamed to title of post + 10 random generated letters.
