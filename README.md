# Django Interactive Charts

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-charts/).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Populate the database with randomly generated data (amount = number of purchases):

    ```sh
    (venv)$ python manage.py populate_db --amount 2500
    ```

1. Create a superuser, and run the server:

    ```sh
    (venv)$ python manage.py createsuperuser
    (venv)$ python manage.py runserver
    ```

1. You can then see the charts here:

    - [http://127.0.0.1:8000/shop/statistics/](http://127.0.0.1:8000/shop/statistics/) - stats view
    - [http://127.0.0.1:8000/admin/statistics/](http://127.0.0.1:8000/admin/statistics/) - new admin view
    - [http://127.0.0.1:8000/admin/shop/](http://127.0.0.1:8000/admin/shop/) - extended admin view
