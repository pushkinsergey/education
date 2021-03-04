# -*- coding: utf-8 -*-
import datetime
from django.db.models import Avg, F, Max, Min, Window
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .models import UserService
from .models import MarkaCars
from .models import ModelCars
from .models import Cars
from .models import Details
from .models import Resources
from .models import Journal
from .models import WorkOrReplace
from django.views.generic.edit import CreateView
#from .forms import CarsForm
#from .forms import JournalForm
from django.shortcuts import render


@login_required
def index(request):
	ObjUserService=UserService.objects.get(system_user=request.user.id)
	ObjCars=Cars.objects.filter(user_car=ObjUserService.id)
	ObjJournal=Journal.objects.filter(car__user_car=ObjUserService.id)
	max_speedometer=Journal.objects.filter(car__user_car=ObjUserService.id).aggregate(Max('speedometer'))#['speedometer__max']
	sm_max=max_speedometer['speedometer__max']
	ObjWorks=WorkOrReplace.objects.filter(event__car__user_car=ObjUserService.id)
	ObjSpr=Resources.objects.filter(car__user_car=ObjUserService.id) #.order_by(Resources.name_detail)
	for item in ObjSpr:
		#Resources.objects.filter(car__user_car=ObjUserService.id).filter(id=item.id).filter(id=item.id).update(planned_date=datetime.datetime.now())
		# item.detail_id это id детали
		last_date=Journal.objects.filter(id__in=WorkOrReplace.objects.values_list('event_id', flat=True).filter(datail=item.detail_id)).aggregate(Max('date')) 
		list_date=Journal.objects.filter(id__in=WorkOrReplace.objects.values_list('event_id', flat=True).filter(datail=item.detail_id)).values('date','speedometer') 
		comment=''
		sm_work=0
		for di in list_date:
			comment+='{}, '.format(di['date'])
			#comment=comment+'+'
			if di['speedometer']>sm_work:
				sm_work=di['speedometer']
				date_work=di['date']
		if comment=='':
			last_date=Journal.objects.filter(car__user_car=ObjUserService.id,type_event=1).aggregate(Max('date')) 
			comment='начало эксплуатации'#+str(max_speedometer['speedometer__max'])
			list_date=Journal.objects.filter(car__user_car=ObjUserService.id,type_event=1).values('date','speedometer')
			sm_work=list_date[0]['speedometer']
			date_work=list_date[0]['date']
		Resources.objects.filter(car__user_car=ObjUserService.id).filter(id=item.id).update(
			last_date=last_date['date__max'],
			sm_work=sm_work,
			planned_date=datetime.datetime.now()+datetime.timedelta((sm_work-sm_max+item.resource)/int((sm_max+1-sm_work)/(datetime.datetime.now().date()-date_work).days)),
			comment=comment)
	#(sm_work-sm_max+item.resource)/int((sm_max+100-sm_work)/(datetime.datetime.now().date()-date_work).days)
	ObjSpr=Resources.objects.filter(car__user_car=ObjUserService.id).order_by('detail')
	context={'userservis':ObjUserService,'cars':ObjCars,'journal':ObjJournal,'details':ObjWorks,'spr':ObjSpr} 
	return render(request, 'index.html', context)
"""

@login_required
def addcar(request):
	if request.method=='POST':
		form = CarsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			return render(request, 'addcar.html', {'form':form })
	else:
		form = CarsForm(initial={'user_car':UserService.objects.get(system_user=request.user.id).id})
		#form.fields['user_car'].initial=UserService.objects.get(system_user=request.user.id).id
		return render(request, 'addcar.html', {'form':form })

@login_required
def deletecar(request, idcar: int):
	car=Cars.objects.get(id=idcar)
	car.delete()
	return HttpResponseRedirect('/')

@login_required
def viewcar(request, idcar: int):
	ObjUserService=UserService.objects.get(system_user=request.user.id)
	ObjCar=Cars.objects.get(id=idcar)
	ObjCars=Cars.objects.filter(user_car=ObjUserService.id)
	ObjJournal=Journal.objects.filter(car=idcar)
	ObjReplacments=Replacments.objects.filter(event__car_id=idcar)
	ObjWorks=Work.objects.filter(event__car_id=idcar)
	context={'userservis':ObjUserService,'cars':ObjCars,'journal':ObjJournal,'cardcar':ObjCar,'details':ObjReplacments,'works':ObjWorks}
	return render(request, 'viewcar.html', context)

@login_required
def addjournal(request, idcar: int):
	if request.method=='POST':
		form = JournalForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			return render(request, 'addjournal.html', {'form':form })
	else:
		form = JournalForm(initial={'car':Cars.objects.get(id=idcar).id})
		#form.fields['user_car'].initial=UserService.objects.get(system_user=request.user.id).id
		return render(request, 'addjournal.html', {'form':form })

@login_required
def deletejournal(request, idcar: int):
	car=Cars.objects.get(id=idcar)
	car.delete()
	return HttpResponseRedirect('/')

@login_required
def viewjournal(request, idcar: int):
	ObjUserService=UserService.objects.get(system_user=request.user.id)
	ObjCar=Cars.objects.get(id=idcar)
	ObjCars=Cars.objects.filter(user_car=ObjUserService.id)
	ObjJournal=Journal.objects.all().filter(car=idcar)
	context={'userservis':ObjUserService,'cars':ObjCars,'journal':ObjJournal,'cardcar':ObjCar}
	return render(request, 'viewcar.html', context)

"""