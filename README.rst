{{ app_name|title }} Documentation
{% for char in app_name|make_list %}#{% endfor %}##############


Delete this line and anything below it

django-app-skel
---------------

How to use the skeleton:

Either download and run::

    django-admin.py startapp --template=/Your/path/to/django-app-skel -epy -ehtml -erst -ebat -etxt --name Makefile myapp

Or use it directly::

    django-admin.py startapp --template=https://github.com/kaleissin/django-app-skel/archive/master.zip -epy -ehtml -erst -ebat -etxt --name Makefile myapp

Author in the docs is hardcoded to "kaleissin" so sed it away with::

    sed -i "s/kaleissin/Your Name/g" docs/conf.py

Django wish-list: have author_name as part of the context
