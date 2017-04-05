---
layout: docs
title: Development
permalink: /docs/development/
---

# RapidPro Development Server

RapidPro comes with everything you need to quickly get started with
development. Note that development and deployment has only been tested on OSX
and Ubuntu, you'll likely need to modify the directions below if using Windows.

## Prerequisites

You'll need the following to get started:

 * PostgreSQL 9.3 or later along with the PostGIS extensions. You probably want
   to refer to Django's [installation instructions](https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/)
   to help get this working.
 * [Redis](https://redis.io) 2.8 or later installed and listening on localhost.
   By default the development server uses database 15.
 * [lessc](http://lesscss.org), the Less compiler.
 * [coffee](http://coffeescript.org), the Coffee script compiler.
 * [bower](http://bower.io), package manager for javascript libraries.

## Create temba user for PostgreSQL

{% highlight bash %}
$ createuser temba --pwprompt -d
Enter password for new role:
Enter it again:
{% endhighlight %}

## Create temba database, add PostGIS

Create the database as temba user:
{% highlight bash %}
$ psql --user=temba postgres
postgres=> create database temba;
CREATE DATABASE
{% endhighlight %}

Now connect as a superuser that can install extensions:
{% highlight bash %}
$ psql
postgres=# \c temba
You are now connected to database "temba" as user "psql".
temba=# create extension postgis;
CREATE EXTENSION
temba=# create extension postgis_topology;
CREATE EXTENSION
temba=# create extension hstore;
CREATE EXTENSION
{% endhighlight %}

## Clone RapidPro

Now clone the RapidPro repository and link up the development settings:

{% highlight bash %}
$ git clone git@github.com:rapidpro/rapidpro.git
$ cd rapidpro
$ ln -s temba/settings.py.dev temba/settings.py
{% endhighlight %}

## Build virtual environment

You should always use a virtual environment to run your RapidPro installation. The
pinned dependencies for RapidPro can be found in ```pip-freeze.txt```. You can
build the needed environment as follows (from the root rapidpro directory):

{% highlight bash %}
$ virtualenv env
$ source env/bin/activate
(env) $ pip install -r pip-freeze.txt
{% endhighlight %}

## Sync your database

You should now be able to run all the migrations and initialize your development
server. This takes a little while on RapidPro as migrate also creates and
initializes all the user groups and permissions.

{% highlight bash %}
$ python manage.py migrate
{% endhighlight %}

## Install bower scripts

Before you can run your server, you will need the web-tier dependencies. These
are managed by bower (see bower.json in the root for more details).

{% highlight bash %}
$ bower install
{% endhighlight %}


## Run development server

At this point you'll be able to run the development server and run RapidPro. It
will be available at ```http://localhost:8000```

{% highlight bash %}
$ python manage.py runserver
{% endhighlight %}


# Testing with the RapidPro SMS Channel Android app

## Configure to connect to your development server

There is a hidden feature of the [RapidPro SMS Channel Android app](https://github.com/rapidpro/android-channel) for testing your
RapidPro development instance on a local network.

If you tap the rapidpro logo in the app 11 times you can unlock the advanced settings,
which will let you enter any an IP address. The app will attempt to connect to RapidPro
using the given IP address on port 8000 so you can claim the relayer and test
sending/receiving with real SMS messages. If you need to use a different port, you can
append it to the IP address like: ```192.168.1.15:80```.

Android only allows a single app to send a certain number of messages per hour.
However, you can increase your message throughput by installing "SMS Channel Pack" apps,
which effectively raise the allowed number of messages for the RapidPro SMS Channel Android app.
On the RapidPro SMS Channel app's page in the Play Store, click on 'More by Nyaruka Ltd.' and
install up to 9 of the SMS Channel Packs to increase your message volume.