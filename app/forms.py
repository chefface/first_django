from django import forms 
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions

from models import City, State

class CitySearchForm(forms.Form):
	letters_only = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
	city = forms.CharField(required=True, initial= "Orem", validators=[letters_only])
	state = forms.CharField(required=True, initial= "Utah", validators=[letters_only])

	def __init__(self, *args, **kwargs):
	    	super(CitySearchForm, self).__init__(*args, **kwargs)
	        self.helper = FormHelper()
	        self.helper.form_method = 'get'
	        self.helper.form_action = 'city_search'
	        # self.helper.add_input(Submit('submit', 'Search'))
	        self.helper.layout = Layout(
	                    Div(
	                        Div('city', css_class='col-sm-6 col-md-6'),
	                        Div('state', css_class='col-sm-6 col-md-6'),
	                        css_class='row'),
	                    Div(
	                        Div(
	                            FormActions(
	                                Submit('submit', 'Search')
	                                ),
	                            css_class='col-sm-12 col-md-12',
	                            ),
	                        css_class='row'
	                        )
	                )

class EditState(forms.ModelForm):
	class Meta:
		model = State
		fields = '__all__'

		def __init__(self, *args, **kwargs):
			super(CitySearchForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper(self)
			self.helper.form_method = 'post'
			self.helper.form_action = reverse('edit_state', kwargs={'pk': self.instance.pks})
			self.helper.layout = Layout(
				Div(
					Div('name', css_class='col-md-10'),
					Div('abbreviation', css_class='col-md-2'),
					css_class='row'
					),
				Div(
					Div(FormActions(Submit('submit', 'Submit')), css_class="col-md-12"),
					css_class='row'
					)
				)


class StateCreateForm(forms.ModelForm):
	class Meta:
		model = State
		fields = '__all__'


class EditCity(forms.ModelForm):
	class Meta:
		model = City
		fields = '__all__'

# class CitySearchForm(forms.Form):
# 	letters_only = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# 	city = forms.CharField(required=True, initial= "Orem", validators=[letters_only])
# 	state = forms.CharField(required=True, initial= "Utah", validators=[letters_only])

class CityCreateForm(forms.ModelForm):
	class Meta:
		model = City
		fields = '__all__'
