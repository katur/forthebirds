#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forthebirds.settings")

    from django.core.management import execute_from_command_line

    if 'test' in sys.argv:
        DATABASE_ENGINE = 'sqlite3'

    execute_from_command_line(sys.argv)
