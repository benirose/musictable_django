## Music Table

As a way to (re)teach myself Django, I wanted to recreate the functionality of [http://music.circleofhope.net](http://music.circleofhope.net). It ends up this is a great project for learning, as it includes many peices of core functionality one would need for building a fully featured web application.

While the primary goal of this project is to learn Django, secondary hopeful goals are to replace the Music Table at Circle of Hope, and also to open source the code base so other churches could use it.

## Installation

This project is build on [Django](https://www.djangoproject.com/), using Python v2.7. The easiest way to install Django on your machine is via [PIP](https://pypi.python.org/pypi/pip).

`pip install Django`

MySQL is also required. You may need to install a Python library to make that work, mysqlclient is the easiest and most recommended.

`pip install mysqlclient`

Once your environment is set up and you have the code base, create a database called `musictable` and then run the following command from the project root to generate the database tables.

`./django migrate`

### Getting Data

There is no way to sync content, but a dump from the current music table is provided in this project. If you import this data into a database called `musictable_php`, you can then use the provided SQL queries to translate the data into the database tables Django generates for us (run them from that database).

### Project Structure

I'm not a big fan of frameworks that force you to modularize your code. Most modern web apps cross polinate their features and having a single app with all the code felt silly to me. I re-arrange the project structure so the [app and project](http://stackoverflow.com/questions/4879036/django-projects-vs-apps) folder are the same. This also allowed me to run the site at `/` instead of `/app`. Additionally, it solved a lot of the "is this app or project level" questions and helped me focus on writing code instead of fighting Django to get things to load from two different places.

I also spend a lot of time in the Symfony framework, which uses `./symfony` as the entry point for the CLI tool. For this reason, I renamed `manage.py` to `./django`, which I find a million times easier to type than `python manage.py`.

Django is a bit different than other frameworks. Models go in a single file, routes are called urls, controllers are called views, views are called templates! It shouldn't take too long to get the hang of.

## Running the Project

I haven't configured this project to run from a proper web server yet, so just use `./django runserver` to start the app.

