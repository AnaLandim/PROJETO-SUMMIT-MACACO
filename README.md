# Muay Thai School

This is a straightforward CRUD (Create, Read, Update, Delete) application built with Django 4, Bootstrap 4, and PostgreSQL.

## Getting Started

Follow these steps to get the project up and running on your local environment:

### Prerequisites

Make sure you have Python and PostgreSQL installed on your system.
    ```
    sudo apt-get install python3.12-venv
    python3.12 -m venv .venv
    source .venv/bin/activate
    sudo apt-get install build-essential libpq-dev python3.12-dev
    pip install -r requirements.txt
    ```

### Installation

1. Install the project dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

2. Create the PostgreSQL database by running migrations:

    ```
    python manage.py migrate
    ```

3. Start the development server:

    ```
    python manage.py runserver
    ```

### Accessing the Django Admin

To access the Django admin panel, you'll need to create a superuser account:


Follow the prompts to set up your admin account, and then you can access the admin panel at `/admin`.

## Usage

You can use this CRUD application as a foundation for building your own web applications. It provides basic Create, Read, Update, and Delete functionality that can be extended and customized to suit your specific needs.

## Acknowledgments

- Django - The web framework used
- Bootstrap - The front-end framework used
- PostgreSQL - The database system used

Feel free to customize and expand upon this project to create your own Django-based web applications. If you have any questions or run into any issues, please refer to the project's [GitHub Issues](https://github.com/yourusername/django-crud-example/issues) for assistance.
