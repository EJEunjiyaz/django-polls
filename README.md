# Django Polls Application

Web application from the Django Tutorial project where users can vote on polls.

## Requirements

This project requires:

* Python 3.6 or newer
* other Python modules as in [requirements.txt](requirements.txt)

## First setup

1. Clone this repository to your local machine.
2. Use your shell, set the directory where "`requirements.txt`" is located. Run the following command:
    ```python
    pip install -r requirements.txt
    ```
3. Set the directory to "`\django-polls\mysite\`". First, you need to create the database in your local machine. Run the following command:
    ```python
    python manage.py migrate
    ```
4. Run "python manage.py runserver". Normally the server start at http://127.0.0.1:8000/, you can access http://127.0.0.1:8000/polls and http://127.0.0.1:8000/admin from these url.

## Setup Administrator

After you completed setting up on the first run, you will unable to manage this site. So let's setup for the admin account.

1. Open the shell in "`\django-polls\mysite\`"
2. Run the following command: 
    ```python
    python manage.py createsuperuser
    ```
3. Enter your desired username and press enter.
    ```
    Username: admin
    ```
4. You will then be prompted for your desired email address:
    ```
    Email address: admin@example.com
    ```
5. The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
    ```
    Password: **********
    Password (again): *********
    Superuser created successfully.
    ```

## Start the development server

The Django admin site is activated by default. Let’s start the development server and explore it.

If the server is not running start it like so:

```python
python manage.py runserver
```

Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen:

## Sites

This project have two sites

1. `/polls`

    This site can vote any questions and view the results.

2. `/admin`

    Can manage everything, such as,  question, answer, time posted, result value, users, admin password.

## License

Vichyawat Nakarugsa

Department of Computer Engineering

Kasetsart University