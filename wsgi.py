#!/usr/bin/env python
from app import app

# Redefine as 'wapp' for uwsgi
# If needed, a wrapper function can be written around this, which 
# does stuff, then returns the app module
wapp = app

