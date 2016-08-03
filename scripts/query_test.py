#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State

import django
django.setup()


# states = State.objects.all().order_by('name')

# states = State.objects.all().exclude(name__startswith="A").order_by('name')

# states = State.objects.all().exclude(name__lt=10000).order_by('-capital_population')

states = State.objects.all().values_list('name', 'abbreviation', 'capital_population')

for state in states:
	print state

# for state in states:
	# print "%s | %s | %s" % (state.name, state.capital ,state.capital_population)