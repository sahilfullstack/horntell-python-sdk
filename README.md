Horntell SDK for Python
=======================

This SDK allows you to easily integrate Horntell in your Python applications.

## Requirements

**Python 2.6+, Python 3.1+ and PyPy**

**`hmac` and `hashlib` compiled with your Python installation**

**requests(>= 0.8.8), simplejson**

## Installation

You don't need this source code unless you want to modify the package. If you just want to use the Horntell Python SDK, you
should run:

```
pip install --upgrade horntell
```

or

```
easy_install --upgrade horntell
```

See [http://www.pip-installer.org/en/latest/index.html](http://www.pip-installer.org/en/latest/index.html) for instructions on installing `pip`. If you are on a system with `easy_install` but not pip, you can use `easy_install` instead. If you're not using `virtualenv`, you may have to prefix those commands with `sudo`. You can learn more about `virtualenv` at [http://www.virtualenv.org/](http://www.virtualenv.org/)

To install from source, run:

```
python setup.py install
```

## Getting Started

You need to `init`ialize the SDK with the app's key and secret, which you can find in your account at [http://app.horntell.com](http://app.horntell.com). Sample usage looks like this.

```python
import horntell

horntell.App().init('YOUR_APP_KEY', 'YOUR_APP_SECRET')

horntell.Profile().create({
     'uid': '1337',
     'first_name': 'John',
     'last_name': 'Doe',
     'email': 'john@example.com',
     'signedup_at': 1383350400
 })
```

## Documentation

Please see [http://docs.horntell.com/api](http://docs.horntell.com/api/?python) for up-to-date documentation.
