# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import UserService
from .models import MarkaCars
from .models import ModelCars
from .models import Cars
from .models import Details
from .models import Resources
from .models import Journal
from .models import WorkOrReplace

class UserServiceAdmin(admin.ModelAdmin):
	list_display = ('nameuser','emailuser','system_user')
	list_display_link =  ('nameuser','emailuser','system_user')
	search_fields =  ('nameuser','emailuser','system_user')
class MarkaCarsAdmin(admin.ModelAdmin):
	list_display = ('id','marka',)
	list_display_link =  ('id','marka',)
	search_fields =  ('id','marka',)
class ModelCarsAdmin(admin.ModelAdmin):
	list_display = ('id','marka_car','model',)
	list_display_link =  ('id','marka_car','model',)
	search_fields =  ('id','marka_car','model',)
class CarsAdmin(admin.ModelAdmin):
	list_display = ('id','name_car','reg_number','marka_car','model_car','user_car')
	list_display_link =  ('id','name_car','reg_number','marka_car','model_car','user_car')
	search_fields =  ('id','name_car','reg_number','marka_car','model_car','user_car')
class DetailsAdmin(admin.ModelAdmin):
	list_display = ('id','name_detail','car',)
	list_display_link =  ('id','name_detail','car',)
	search_fields =  ('name_detail',)
class ResourcesAdmin(admin.ModelAdmin):
	list_display = ('id','car','detail','resource',)
	list_display_link =  ('id','car','detail','resource',)
	search_fields =  ('id','car','detail','resource',)
class JournalAdmin(admin.ModelAdmin):
	list_display = ('id','date','type_event','car','title','description','speedometer',)
	list_display_link =  ('id','date','type_event','car','title','description','speedometer',)
	search_fields =  ('id','date','car',)
class WorkOrReplaceAdmin(admin.ModelAdmin):
	list_display = ('id','event','datail') #,'datail'
	list_display_link =  ('id','event','datail')#,'datail'
	search_fields =  ('id','event',)
admin.site.register(UserService,UserServiceAdmin)
admin.site.register(MarkaCars,MarkaCarsAdmin)
admin.site.register(ModelCars,ModelCarsAdmin)
admin.site.register(Cars,CarsAdmin)
admin.site.register(Details,DetailsAdmin)
admin.site.register(Resources,ResourcesAdmin)
admin.site.register(Journal,JournalAdmin)
admin.site.register(WorkOrReplace,WorkOrReplaceAdmin)

"""
from .models import UserService
from .models import MarkaCars
from .models import ModelCars
from .models import Cars
from .models import Details
from .models import Resources
from .models import Journal
from .models import WorkOrReplace


class UserServiceAdmin(admin.ModelAdmin):
	list_display = ('nameuser','emailuser','system_user')
	list_display_link =  ('nameuser','emailuser','system_user')
	search_fields =  ('nameuser','emailuser','system_user')
class MarkaCarsAdmin(admin.ModelAdmin):
	list_display = ('id','marka',)
	list_display_link =  ('id','marka',)
	search_fields =  ('id','marka',)
class ModelCarsAdmin(admin.ModelAdmin):
	list_display = ('id','marka_car','model',)
	list_display_link =  ('id','marka_car','model',)
	search_fields =  ('id','marka_car','model',)
class CarsAdmin(admin.ModelAdmin):
	list_display = ('id','name_car','reg_number','marka_car','model_car','user_car')
	list_display_link =  ('id','name_car','reg_number','marka_car','model_car','user_car')
	search_fields =  ('id','name_car','reg_number','marka_car','model_car','user_car')
class DetailsAdmin(admin.ModelAdmin):
	list_display = ('id','name_detail',)
	list_display_link =  ('id','name_detail',)
	search_fields =  ('name_detail',)
class ResourcesAdmin(admin.ModelAdmin):
	list_display = ('id','car','detail','resource',)
	list_display_link =  ('id','car','detail','resource',)
	search_fields =  ('id','car','detail','resource',)
class JournalAdmin(admin.ModelAdmin):
	list_display = ('id','date','type_event','car','title','description','speedometer',)
	list_display_link =  ('id','date','type_event','car','title','description','speedometer',)
	search_fields =  ('id','date','car',)
class WorkOrReplaceAdmin(admin.ModelAdmin):
	list_display = ('id','event','datail')
	list_display_link =  ('id','event','datail')
	search_fields =  ('id','event',)

admin.site.register(UserService,UserServiceAdmin)
admin.site.register(MarkaCars,MarkaCarsAdmin)
admin.site.register(ModelCars,ModelCarsAdmin)
admin.site.register(Cars,CarsAdmin)
admin.site.register(Details,DetailsAdmin)
admin.site.register(Resources,ResourcesAdmin)
admin.site.register(Journal,JournalAdmin)
admin.site.register(WorkOrReplace,WorkOrReplaceAdmin)

"""

