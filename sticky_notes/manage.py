#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """
    Main entry point for running administrative tasks such as:
    - starting the development server
    - running migrations
    - creating apps
    - running tests
    """
    # Set default Django settings module for the 'sticky_notes' project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')
    try:
        # Import Django's command line utility function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or cannot be imported,
        # raise a helpful error message
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command line arguments (like runserver, migrate, etc.)
    execute_from_command_line(sys.argv)


# If this script is run directly, call the main function
if __name__ == '__main__':
    main()
