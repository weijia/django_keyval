============================================
django_keyval - a very basic key-value store
============================================

Django Keyval is a very basic key-value store that uses Django's database
backend. Other than django and the standard python function pickle, there are
no dependencies. Django Keyval does not rely on a browser, it has no views.
Django Keyval provides a simple way to store settings and temporary values in 
your Django app that are persistent between requests, without having to deal
with running an external server such as redis. The drawback, compared to redis,
is that it is much slower and less flexible.

A typical usage example is::

    from django_keyval.models import KeyVal

    kv = KeyVal('store_name_1')
    kv.set(key1, value1)
    value2 = kv.get(key2)
    kv.disconnect() # prevents further access


Why yet another key value store?
================================

Two reasons:

1. I needed something simple and most of the ones I found were either very
   complex, or had external dependencies that I did not want to worry about.

2. (The real reason) I needed a simple project to learn about packaging, pypi,
   git, virtualenv, etc.

More Detail
===========

Django KeyVal stores *key*-*value* pairs in a *store*, where the *key* and the
*store* name can be any string. Because Django Keyval uses the standard Python
Pickle function, the *value* can be any python type that can be pickled.

Connecting and disconnecting
----------------------------

In order to prevent clashes between different packages/functions using the same
key, you first need to connect to a *store name*. Make sure you choose
a unique name. The name can be any Python string.

Before you can store or retrieve any values, you need to connect to a store::

    kv = KeyVal.connect(store_name)

Which is equivalent to ``kv = KeyVal(store_name)``.
Once you are done with this store you can disconnect to prevent further access::

    kv.disconnect(store_name)

You can have multiple stores connected at once.
**Note:** Any operations on kv after disconnection result in a NameError, except
for flush_all()

Storing
-------

Setting a value for a key is as simple as::

    kv.set(key, value)

If that key already has a value, it is silently overwritten. If you want to
detect that, the return value is a boolean that indicates whether the key was
new (True) or overwritten (False).

Retrieving
----------

There are several ways to get a value of a key:

* Use **get** if you are sure a key exists, it raises an exception if not::

    value = kv.get(key)

* Use **get_default** to provide a default value and/or to prevent exceptions::

    value = kv.get_default(key, default_value)

If you want to retrieve a value and then delete it, you can use **pop** or 
**pop_default**, they work identically to get and get_default.


Checking if a key exists
------------------------

If you just need to know if a key exists, without retrieving the value, the
``exists`` method can be used. This is just a convenience method, because it is
no more efficient than retrieving::

    if kv.exists(key):
        do_something()

Deleting
--------

A key-value pair is deleted by using::

    kv.delete(key)

If the key does not exist a KeyError is raised, if you want to ignore errors,
use the ``ignore_keyerror`` argument::

    deleted = kv.delete(key, ignore_keyerror=True)

If the key existed, the return value is True, else False.
For deleting all key-value pairs in one ``name``, use::

    kv.flush()

This will not raise exceptions if no key-values exist in ``name``

To delete all key-value pairs in the database, use::

    KeyVal.flush_all()

Note that ``kv.flush_all()`` also works, provided ``kv`` is an instance of 
KeyVal.


Django Admin & Command line
===========================

For testing and debugging purposes the kv store can be accessed from the 
Django Admin site. If you have no server running, or you are using Django 
KeyVal stand-alone, you can use the command line to access the database,
by running the following commands::

    $python manage.py keyval -c set -n name -k key -V value
    $python manage.py keyval -c get -n name -k key
    $python manage.py keyval -c del -n name -k key

Note the capital V to avoid conflict with -verbose.
