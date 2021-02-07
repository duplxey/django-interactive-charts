# Django Interactive Charts

## Want to learn how to build this?

Check out the [post](x).

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

1. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
   
1. Visit [http://localhost:8000/admin/statistics/](http://localhost:8000/admin/statistics/) to see the charts.
