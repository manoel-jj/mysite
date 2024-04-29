import os
import django
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
