# Job-application-review-system
Project for an interview assignment

# Getting Started

First clone the repository from GitHub and switch to the new directory

## Installation and Setup Instructions for Django

    $ cd JARC
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Make migrations:

    $ python manage.py makemigrations

Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

To check swagger docs:
http://127.0.0.1:8000/swagger/

To check APIs overview:
http://127.0.0.1:8000/job_portal/
