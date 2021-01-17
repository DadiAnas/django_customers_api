# Customer Management Api
# Description

This is a simple Django REST API which provides information about customers.

This API provides two endpoints: one for listing all customers `/customers` and, another
one for getting a single customer by its id `customers/<int:id>`. 

As a `view` it uses `GenericAPIView` provided by the library `rest_framework` in order to consume the REST API.

It Includes two django management `custom commands`. The first one is `load_customers` which give the ability to import the `customers.csv` file into
database, this command can be used like that:

    $ python manage.py load_customers --path //projectpath/datasets/customers.csv 
    
Using an absolute path will work efficiently.

The second custom command is `fill_addressses`, this command will consume the Phone API to get latitude and longitude of the city of the customer and then update customers's address. It can be used like this:

    $ python manage.py load_customers

It use `geopy` libraries which provide a set of API (Google, Nominatim, Photon, TomTom...).
I chose to work with photon because it's fully free and well worked. Of course, Google's api may work better but it needs an API KEY.

This application is well tested using `rest_framework.test` library and ready for deployment.


# Usage

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/DadiAnas/django_customers_api/
    $ cd django_customers_api
    

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/DadiAnas/django_customers_api/ \
      --extension=py,md \
      django_customers_api
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      ---template=https://github.com/DadiAnas/django_customers_api/ \
      --extension=py,md \
      django_customers_api
      
      
After that just install the local dependencies, run migrations, and start the server.
Go to Install requirements section.
### Create your own Virtual environment

If you want to use a virtual environment then the virtualenv package is required. You can install it with pip:
    
    pip install virtualenv
    
Assuming that you installed virualenv package. you can, activate the virtualenv for your project.
    
    $ virtualenv venv
    
Activate the virtual environment

    source venv/bin/activate
    
### Install requirements

Now you are ready to install all project dependencies in your host machine or virtual environment, to do so use `pip install`:

    $ pip install -r requirements.txt
    
### Migration and execution
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
In case another app use the default port you can specify a free port:

    $ python manage.py runserver 8485
    
### Stop project from execution
To stop project press ctrl+c:

    ctrl^c

To desativate the virtual environment and use your original Python environment, simply type ‘deactivate’.

    deactivate
