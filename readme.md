# Django-Introduction
How to get started with Django

## Useful Pip Commands
Pip install pip-tools

## Getting Virtual Environment Started (macOS users)
1. python3 -m venv virtual-env
2. source virtual-env/bin/activate

Your virtual environment should now be activated!

# Now we should install pip

## Install Django's package manager => pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

### You can inspect pip for any security flaws using
```
python get-pip.py
```

### If for any reason you need to uninstall all versions of pip or in case of system inconsistencies use:
```
sudo pip uninstall pip
```

# Installing Django using pip
```
pip install django
```



pip install django

If you need to upgrade pip
pip install --upgrade pip



### sidenotes: Intro to Pip freeze
To see what dependencies are installed use:
<code>pip freeze</code>
# Actual Django Commands
<code>pip install django</code>
# Getting Started with a New Django Project
1. <code>django-admin.py startproject tryTen</code>
2. <code>python manage.py migrate</code>
3. <code>python manage.py runserver</code>
4. You will get the following message!
<code>Starting development server at http://127.0.0.1:8000/</code>
5. Now you can visit http://127.0.0.1:8000/ to view your django project :+1:
# Admin Site
1. <code>python manage.py createsuperuser</code>
2. Fill out username and password to create a admin user account
3. Now you can run your server
<code>python manage.py runserver</code>
4. Then to get to admin site use
http://127.0.0.1:8000/admin/login/?next=/admin/
