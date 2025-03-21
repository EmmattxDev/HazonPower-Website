import os
import sys

# Add the directory containing your Django project to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# # If you're using a virtual environment, uncomment and modify these lines:
# INTERP = os.path.join(os.environ['HOME'], 'virtualenv/hazon/3.13/bin/python')
# if sys.executable != INTERP:
#     os.execl(INTERP, INTERP, *sys.argv)

# Set the Django settings module (adjust if your settings are in a different location)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

from backend.wsgi import application