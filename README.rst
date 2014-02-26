{{ app_name|title }} Documentation
{% for char in app_name|make_list %}#{% endfor %}##############

Delete this line and anything below it

django-app-skel
---------------

Django skeleton for standalone apps to be distributed on Pypi.

Contains the project "demo", which demonstrates the use of the app.

How to use the skeleton:

1. Either download and run::

      django-admin.py startapp --template=/Your/path/to/django-app-skel -epy -ehtml -erst -ebat -etxt --name Makefile MYAPP

  Or use it directly::

      django-admin.py startapp --template=https://github.com/kaleissin/django-app-skel/archive/master.zip -epy -ehtml -erst -ebat -etxt --name Makefile MYAPP

2. Author in the docs is hardcoded to "YOURNAME" so sed it away with::

      sed -i "s/YOURNAME/Your Name/g" docs/conf.py

3. Edit `setup.py`, remember to set "description", "author" and
   "author_email". Change the line `'License :: OSI Approved :: MIT
   License',` if your app will not be using the MIT license.

Django wish-list: have author_name as part of the context for "startapp".
