#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State, StateCapital

import django
django.setup()


csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")



csv_file = open(csv_path, 'r')


reader = csv.DictReader(csv_file)

for row in reader:

	new_state, created = State.objects.get_or_create(abbreviation=row['abbrev'])


	new_state.abbreviation = row['abbrev']
	new_state.name = row['state']

	new_state.save()

	new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])

	new_capital.state = new_state
	new_capital.latitude = row['latitude']
	new_capital.longitude = row['longitude']
	new_capital.capital_population = row['population']

	new_capital.save()