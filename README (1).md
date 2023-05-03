
# CDC Placement Portal

This is my completed task of iris recruitment, CDC Placement Portal. All major features are included in this project.



## Guide


I will give all the details of the project in this file in the following order.


1. `About the portal`

2. `Documenttation`

3. `Installation guide`

4. `Features available (Sample Users and companies list here)`

5. `Feature that are not covered yet`

6. `Bugs`

7. `Video demo`

8. `Relevant screenshots`



## About the Portal


A placement portal created using Django is a web-based platform that facilitates job seekers to search and apply for jobs and enables employers to post job openings and manage their recruitment process. The portal is designed to simplify the entire hiring process, making it more efficient and effective.

#### User can create an Account and login, also User can register for jobs, can upload his resume and see in how many companies he has applied. 

#### A POC can be created by the admin for a company which will manage that particulate from the start of the process till the end



## Documentation

Django framework is used to create this platform.
everything that is used to create this application is given in the folllowing Documentation

[Django Framework](https://docs.djangoproject.com/en/4.2/)

, in this Documentation everything is covered including Installation, however i will still discuss about the Installation part.  


## Installation and setup Guide

1. Since Django is python based framework make sure you have python installed. Click here to Install [Python](https://www.python.org/downloads/)

2. in you virtual environment, write the following command

            python -m pip install Django
### Setup

1. before setup make sure python folder and python script folder is added in environment variable and install the latest version of django
2. clone this repo in an empty folder and open in an IDE,open the terminal doing 

        git clone https://github.com/anshumanNitk/IRIS_Rec23_211ME109_Django.git

Then write the command

`python manage.py runserver`

3. Now click the the link and use the application 

# Features available

This Application have covered Features like

## For Student
1. Sign-up and Log In
2. applying to company
3. uploading your resume and other details
4. able to see where you have applied

## For POC
1. Can Manage Company details like roles,Salary,Start date,End date and description
2. Can see who have applied and download their resume.
3. Can also do all other the things a student can do

## For Admin
1. can Create Company, delete Company
2. Can select POC for each company
3. Can create and delete User 
4. can see user personal Data and resume.

# Sample Data i have created some sample users,POCS and Companies to see how portal works

### Admin
#### name - anshuman password-Anshuman@009
### User
#### name- mac, anshum, anshum1, anshum2, anshum3, anshum4, .......anshum14   password-ansh (for all of them)
### few company names and their POC
#### exxnmobil-anshum, debsoc-mac , amazon-anshum1 
(rest you can see by logging with other id or by admin)


## Feature Planned but Not Implemented yet

1. A feature For POC to set qualification and cut-offs is Planned.
2. A more user-Friendly UI is Planned.

## Bugs

1. In POC page, after the POC updates the company details and send the data, the updated value on the form don't immediately show but after refreshing the page it is displayed.

2. While creating an account, please create account with different usernames, i have the unique username constraint set but i was not able to do the error handling when an account is created with same username (it is also a Planned feature).
