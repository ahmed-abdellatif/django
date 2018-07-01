# **Django-Introduction**
How to get started with Django

### Useful Pip Commands
Pip install pip-tools

### Getting Virtual Environment Started (macOS users)
1. python3 -m venv virtual-env
2. source virtual-env/bin/activate

Your virtual environment should now be activated,
Let's Begin!

# **Installing _pip_ - Django's package manager**

### Install Django's package manager => pip
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

### If you get a message saying pip should be updated, then you can use :

```
pip install --upgrade pip
```


#### Installing Django using pip
```
pip install django
```
# Creating a Django Project

```
django-admin startproject myProject
```
# Creating a Django App

```
python manage.py startapp myApp
```


# Django's Development Server

run using
```
python manage.py runserver
```

# Django startapp directory

### views.py
renders front end

### urls.py
application routing

