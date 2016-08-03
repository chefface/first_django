from django.contrib import admin
from app.models import State, StateCapital, City
# Register your models here.

class StateAdmin(admin.ModelAdmin):
	list_display = ("name", "abbreviation", )
	search_fields = ["name"]

class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ("capital", "capital_population" )
	search_fields = ("state")



admin.site.register(State , StateAdmin)
admin.site.register(StateCapital)
admin.site.register(City)