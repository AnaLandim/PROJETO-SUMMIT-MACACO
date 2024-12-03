#!/usr/bin/env python
import os
import sys


def create_default_user():
    from schools.models import School

    if not School.objects.filter(username="teste@gmail.com").exists():
        School.objects.create_user(username="teste@gmail.com", password="123123", email="teste@gmail.com")
        print("Usuário padrão criado com sucesso.")
    else:
        print("Usuário padrão já existe.")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "muay_thai_school.settings")
    try:
        import django
        from django.core.management import execute_from_command_line

        django.setup()
        if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
            create_default_user()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
