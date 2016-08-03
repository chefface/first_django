from django.shortcuts import render, redirect

from django.http import HttpResponse

from app.models import State, City, StateCapital

from django.utils.html import escape

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app.forms import CitySearchForm, CityCreateForm, EditCity, StateCreateForm, EditState

@login_required
def delete_state(request, pk):

	State.objects.get(pk=pk).delete()

	return redirect('/state_list/')



@login_required
def edit_state(request, pk):

	context = {}

	state = State.objects.get(pk=pk)

	context['state'] = state

	form = EditState(request.POST or None, instance=state)

	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect(state_list)

	return render(request, 'edit_state.html', context)

@login_required
def create_state(request):

	context = {}

	form = StateCreateForm(request.GET)

	context['form'] = form

	if request.method == "POST":

		if form.is_valid():
			form.save()

			return redirect('/state_list/')

	return render(request, 'create_state.html', context)


@login_required
def delete_city(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_list/')


@login_required
def city_edit(request, pk):
	context = {}

	city = City.objects.get(pk=pk)

	context['city'] = city

	form = EditCity(request.POST or None, instance=city)

	context['form'] = form 

	if form.is_valid():
		form.save()

		return redirect('/city_list/')

	return render(request, 'city_edit.html', context)


def create_city(request):
	
	context = {}

	form = CityCreateForm(request.GET)

	context['form'] = form

	if form.is_valid():
		form.save()



	return render(request, 'create_city.html', context)

def city_search_post(request):

	context = {}

	form = CitySearchForm(request.POST)

	context['form'] = form 

	if request.method == 'POST':

		if form.is_valid():
			city = form.cleaned_data.get('city', 'Orem')
			state = form.cleaned_data.get('state', 'Utah')

			context['cities'] = City.objects.filter(name=city, state__name=state)


	return render(request, 'city_search_post.html', context)








def city_search(request):

	context = {}

	form = CitySearchForm(request.GET)

	context['form'] = form

	if form.is_valid():

		city = form.cleaned_data.get("city", "Orem")
		state = form.cleaned_data.get("state", "Utah")

		cities = City.objects.filter(name=city, state__name=state)

		context['cities'] = cities


	return render(request, 'city_search.html', context)

def city_search_old(request):

	context = {}

	form = CitySearchForm(request.GET)

	form.data

	print form.is_valid()

	print form.cleaned_data

	city = form.cleaned_data.get('city', 'Orem')
	state = form.cleaned_data.get('state', 'Utah')
	

	cities = City.objects.filter(name=city, state__name=state)

	context['cities'] = cities
	context['form'] = form



	return render(request, 'city_search.html', context)




class StateListView(ListView):
	model = State
	template_name = "index.html"
	context_object_name = 'states'

class StateDetailView(DetailView):
	model = State
	template_name = "detail.html"
	context_object_name = 'state'

class CityListView(ListView):
	model = City
	template_name = "cities.html"
	context_object_name = "cities"

	def get_context_data(self, **kwargs):
		context = super(CityListView, self).get_context_data(**kwargs)
		print context
		context['states'] = State.objects.all()
		context['cities'] = City.objects.filter(state__pk=self.request.GET.get('state_number', 60))

		return context

class CityDetailView(DetailView):
	model = City
	template_name = "city_detail.html"
	context_object_name = 'city'

def capital_detail(request, pk):

	context = {}

	context['capital'] = StateCapital.objects.get(pk=pk)

	return render(request, 'capital_detail.html', context)

def capital_list(request):

	context = {}

	context['capitals'] = StateCapital.objects.all()

	return render(request, 'capital_list.html', context)

def city_detail(request, pk):

	context = {}

	context['city'] = City.objects.get(pk=pk)

	return render(request, 'city_detail.html', context)



def city_list(request):

	state_number = request.GET.get('state_number', 96)
	#check pks!!!!!!

	context = {}

	context['states'] = State.objects.all()
	context['cities'] = City.objects.filter(state__pk=state_number)

	return render(request, 'cities.html', context)


def state_list(request):

	context = {}

	states = State.objects.all()

	context['states'] = states

	return render(request, 'index.html', context)


def detail(request, pk):

	context = {}

	states = State.objects.get(pk=pk)

	context['states'] = states

	return render(request, 'detail.html', context)


def list(request):

	context = {}

	states = State.objects.all()

	context['states'] = states

	return render(request, 'list.html', context)


def template_view2(request):

	context = {}
	state_city = {}


	states = State.objects.all()

	for state in states:
		cities = state.city_set.filter(name__startswith='A')

		state.name = { state.name : cities }

		state_city.update(state.name)

	context['states'] = state_city

	return render(request, 'base2.html', context)





def form_view(request):
	state = request.GET.get('state', 'C')
	# state = request.GET['state']
	city = request.GET.get('city', 'C')

	city_state_string = """
	<form action="/form_view/" method="GET" >

	State: <input type="text" name="state">

	<br>

	City: <input type="text" name="city" >

	<br>

	<input type="submit" value="FIND THEM!" >

	</form>
	<dir align=center>

	<u><b> State </b> </u> | <u> City </u> | <u> ZipCode </u>

	</dir>

	"""

	states = State.objects.filter(name__startswith=state)

	for state in states:
		cities = state.city_set.filter(name__startswith=city)
		for city in cities:
			city_state_string += """

			<dir align=center>

			 <b>%s</b> | %s | %s <br> </dir>

			 """ % (state.name, city.name, city.zipcode)

	return HttpResponse(city_state_string)

# @csrf_exempt
# def form_view(request):

# 	get_state = request.GET.get('state', 'C')
# 	get_city = request.GET.get('city', 'C')

# 	city_state_string = """
	


# 	<div align=left>

# 	<form action="/form_view/" method="POST">

# 	State: <input type="text" name="state" >

# 	<br>

# 	City: <input type="text" name="city" >

# 	<br>

# 	<input type="submit" value="Search" >

# 	</form>

# 	<br>

# 	</div>

# 	<div align=center> 

# 	<u> State </u> | <u> City </u> | <u> Zip Code </u> 

# 	</div>

# 	<br> 

# 	""" 

# 	states = State.objects.filter(name__startswith=get_state)

# 	for state in states:
# 		cities = state.city_set.filter(name__startswith=get_city)

# 		for city in cities:
# 			city_state_string += "<div align=center> <b>%s</b> | %s | %s <br> </div>" % (state, city.name, city.zipcode)



# 	return HttpResponse(city_state_string)


def get_post(request):


	

	starts_with = request.GET['state_name']

	states = State.objects.filter(name__startswith=starts_with)

	state_string = ''

	for state in states:
		state_string += '%s <br>' % state.name

	return HttpResponse(state_string)


def first_view(request, starts_with):

	states = State.objects.all()

	text_string = '<u>State | City</u> <br>'

	for state in states:

		cities = state.city_set.filter(name__startswith=starts_with)

		for city in cities:

			text_string += '<b>%s</b> | %s <br>' % (state.name, city.name)


	return HttpResponse(text_string)


# def state_list(request, letter):

# 	states = State.objects.filter(name__startswith=letter).order_by('name')

# 	# states = State.objects.filter(name__contains=letter).order_by('name')

# 	# states = State.objects.filter(capital_population__lt=).order_by('name')



# 	state_list = []

# 	for state in states:
# 		state_list.append('%s | %s <br>' % (state.name, state.abbreviation))

# 	return HttpResponse(state_list)