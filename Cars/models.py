# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class UserService(models.Model):
	system_user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
	nameuser = models.CharField(max_length=20,db_index=True,verbose_name='Имя')
	emailuser = models.EmailField()
	def __str__(self):
		return self.nameuser
	class Meta:
		verbose_name_plural = 'Пользователи'
		verbose_name = 'Пользователи'
		ordering=['-nameuser']

class MarkaCars(models.Model):
	marka = models.CharField(max_length=20,db_index=True,verbose_name='Марка')
	def __str__(self):
		return self.marka
	class Meta:
		verbose_name_plural = 'Марки автомобилей'
		verbose_name = 'Марки автомобилей'
		ordering=['-marka']	

class ModelCars(models.Model):
	model = models.CharField(max_length=20,db_index=True,verbose_name='Модель')
	marka_car = models.ForeignKey('MarkaCars',null=False,on_delete=models.PROTECT,verbose_name = 'Марка') 
	def __str__(self):
		return self.model
	class Meta:
		verbose_name_plural = 'Модели автомобилей'
		verbose_name = 'Модели автомобилей'
		ordering=['-model']	

class Cars(models.Model):
	name_car = models.CharField(max_length=20,db_index=True,verbose_name='Автомобиль')
	user_car = models.ForeignKey('UserService',on_delete=models.PROTECT,verbose_name = 'Автовладелец') 
	reg_number = models.CharField(max_length=20,db_index=True,verbose_name='Гос.Номер')
	marka_car = models.ForeignKey('MarkaCars',null=False,on_delete=models.PROTECT,verbose_name = 'Марка') 
	model_car = models.ForeignKey('ModelCars',null=False,on_delete=models.PROTECT,verbose_name = 'Модель') 

	def __str__(self):
		return self.name_car
	class Meta:
		verbose_name_plural = 'Автомобили'
		verbose_name = 'Автомобили'
		ordering=['-name_car']

class Details(models.Model):
	name_detail = models.CharField(max_length=40,db_index=True,verbose_name='Деталь/Работа')
	car = models.ForeignKey('Cars',null=False,on_delete=models.PROTECT,verbose_name = 'Автомобиль')
	def __str__(self):
		return self.name_detail
	class Meta:
		verbose_name_plural = 'Деталь/Работа'
		verbose_name = 'Деталь/Работа'
		ordering=['name_detail']		

class Resources(models.Model):
	car = models.ForeignKey('Cars',null=False,on_delete=models.PROTECT,verbose_name = 'Автомобиль')
	detail = models.ForeignKey('Details',null=False,on_delete=models.PROTECT,verbose_name = 'Деталь/Работа') 
	resource = models.PositiveIntegerField(null=True, blank=True,verbose_name='Ресурс')
	last_date = models.DateField(null=True,blank=True,verbose_name='Дата ремонта')
	sm_work = models.PositiveIntegerField(null=True, blank=True,verbose_name='Спидометр')
	planned_date = models.DateField(null=True,blank=True,verbose_name='Планируемая дата замены')
	comment = models.TextField(null=True, blank=True,verbose_name='Комментарии')
	class Meta:
		verbose_name_plural = 'ресурс деталей'
		verbose_name = 'ресурс деталей'
		ordering=['-detail']

class Journal(models.Model):
	date = models.DateField(db_index=True,verbose_name='Дата ремонта')
	CHOICES = (
		(1,"Начало эксплуатации"),
		(2,"Ремонт"),
		(3,"Сверка спидометра"))
	type_event = models.SmallIntegerField(choices=CHOICES,default=3)
	title = models.CharField(max_length=20,null=True, blank=True,verbose_name='Описание')
	description = models.TextField(null=True, blank=True,verbose_name='Полное описание')
	car = models.ForeignKey('Cars',null=False,on_delete=models.PROTECT,verbose_name = 'Автомобиль')
	speedometer = models.PositiveIntegerField(null=True, blank=True,verbose_name='Спидометр')
	def __str__(self):
		#return self.title+' '+self.date.strftime('%d-%m-%Y')
		return self.date.strftime('%d-%m-%Y')
	class Meta:
		verbose_name_plural = 'Журнал'
		verbose_name = 'Журнал'
		ordering=['-date']	

class WorkOrReplace(models.Model):
	event = models.ForeignKey('Journal',null=True,on_delete=models.CASCADE,verbose_name = 'Событие')
	datail = models.ForeignKey('Details',null=True,on_delete=models.CASCADE,verbose_name = 'Работа/Деталь')	
	class Meta:
		verbose_name_plural = 'Журнал - записи'
		verbose_name = 'Журнал - записи'

#class TemporaryResourceTable(models.Model):
#	car = models.ForeignKey('Cars',null=False,on_delete=models.PROTECT,verbose_name = 'Автомобиль')