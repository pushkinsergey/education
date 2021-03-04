from django import forms
from .models import UserService
from .models import MarkaCars
from .models import ModelCars
from .models import Cars
from .models import Details
from .models import Resources
from .models import Journal
from .models import WorkOrReplace
"""
from django.forms import ModelForm
from .models import UserService
from .models import MarkaCars
from .models import ModelCars
from .models import Cars
from .models import Details
from .models import Resources
from .models import Journal
from .models import WorkOrReplace

class CarsForm(ModelForm):
	name_car = forms.CharField(label='Автомобиль')
	reg_number = forms.CharField(label='Гос.Номер')
	marka_car = forms.ModelChoiceField(
		queryset=MarkaCars.objects.all(),
		label = 'Марка',
		widget=forms.widgets.Select()
		) 
	model_car = forms.ModelChoiceField(
		queryset=ModelCars.objects.all(),
		label = 'Модель',
		widget=forms.widgets.Select()
		) 
	user_car = forms.ModelChoiceField(
		queryset=UserService.objects.all(),
		widget=forms.widgets.HiddenInput()
		) 

	class Meta:
		model = Cars
		fields = ['name_car','reg_number','marka_car','model_car','user_car']

class JournalForm(ModelForm):
	date = forms.DateField(label='Дата ремонта',widget=forms.widgets.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'Select a date'}))
	type_event = forms.ChoiceField(label="Тип",
                                initial=3,
                                widget=forms.Select(),
                                required=True)
	speedometer = forms.IntegerField(min_value=0,label='Спидометр')
	title = forms.CharField(label='Описание')
	description = forms.CharField(label='Полное описание')
	car = forms.ModelChoiceField(
		queryset=Cars.objects.all(),
		widget=forms.widgets.HiddenInput()
		) 

	class Meta:
		model = Journal
		fields = ['date','title','speedometer','description','car']		

"""		