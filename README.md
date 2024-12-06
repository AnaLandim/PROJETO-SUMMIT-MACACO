# PROJETO SUMMIT MACACO

Here are available the codes used to create the website for the NGO Summit Macaco

## Getting Started

Follow these steps to get the project up and running on your local environment:

### Prerequisites

Make sure you have Python and PostgreSQL installed on your system.
    ```
    sudo apt-get install build-essential libpq-dev python3.12-dev python3.12-venv -y
    python3.12 -m venv .venv
    source .venv/bin/activate
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



- Django - The web framework used
- Bootstrap - The front-end framework used
- PostgreSQL - The database system used

