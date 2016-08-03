#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State, City

import django
django.setup()


csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv")



csv_file = open(csv_path, 'r')


reader = csv.DictReader(csv_file)

City.objects.all().delete()
for row in reader:

	state, created = State.objects.get_or_create(abbreviation=row['state'])

	try:
		new_city, created = City.objects.get_or_create(latitude=row['latitude'])


		new_city.state = state
		new_city.name = row['city']
		new_city.county = row['county']
		new_city.longitude = row['longitude']
		new_city.zipcode = row['zip_code']

		new_city.save()

		print new_city.name

	except Exception, e:
		print e


	
	
	