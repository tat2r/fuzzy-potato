from django.shortcuts import render
from basic_app import models
from django.urls import reverse_lazy  
from django.views.generic import (TemplateView, 
								ListView, 
								DetailView, 
								CreateView, 
								UpdateView,
								DeleteView)





class HomeView(TemplateView):
	template_name = 'basic_app/home.html'

class CustomerListView(ListView):
	model = models.Customer 





class CustomerDetailView(DetailView):
	context_object_name = 'customer_detail'
	model = models.Customer
	template_name = 'basic_app/customer_detail.html' 



class CustomerCreateView(CreateView):
	fields = ('first_name', 'last_name', 'phone', 'email')
	model = models.Customer

class CustomerUpdateView(UpdateView):
	fields = ('first_name', 'last_name', 'phone', 'email')
	model = models.Customer

class CustomerDeleteView(DeleteView):
	model = models.Customer
	success_url = reverse_lazy('basic_app:customer_list')




class RentalListView(ListView):
	model = models.Rental

class RentalDetailView(DetailView):
	context_object_name = 'rental_detail'
	model = models.Rental
	template_name = 'basic_app/rental_detail.html' 

class RentalCreateView(CreateView):
	fields = ('customer', 
			'rental_date', 
			'return_date', 
			'van_rented', 
			'daily_rate', 
			'allowed_daily_miles',
			'mileage_over_rate',
			'additional_driver_fee',
			'mexico_insurance',
			'roadside_assistance',
			'airport_access_fee',
			'drop_fee',
			'other_fee')
	model = models.Rental
	

class RentalUpdateView(UpdateView):
	fields = ('customer', 
		'rental_date', 
		'return_date', 
		'van_rented', 
		'daily_rate', 
		'allowed_daily_miles',
		'mileage_over_rate',
		'additional_driver_fee',
		'mexico_insurance',
		'roadside_assistance',
		'airport_access_fee',
		'drop_fee',
		'other_fee')
	model = models.Rental


class RentalDeleteView(DeleteView):
	model = models.Rental
	success_url = reverse_lazy('basic_app:home')




class VanListView(ListView):
	model = models.Van

class VanDetailView(DetailView):
	context_object_name = 'van_detail'
	model = models.Van
	template_name = 'basic_app/van_detail.html' 

class VanCreateView(CreateView):
	fields = ('van_num', 'vin', 'year_make_model', 'plate', 'tag_exp')
	model = models.Van



class VanUpdateView(UpdateView):
	fields = ('van_num', 'vin', 'year_make_model', 'plate', 'tag_exp')
	model = models.Van

class VanDeleteView(DeleteView):
	model = models.Van
	success_url = reverse_lazy('basic_app:home')

###################################################################################
'''

class ModelNameCreateView(CreateView):
	fields = ('first_name', 'last_name', 'phone', 'email')
	model = models.ModelName

## create modelname_form.html 

## add to app.models.ModelName:	

def get_absolute_url(self):
		return reverse_lazy('basic_app:list_or _detail', kwargs={'pk':self.pk})
'''






#####################################################################################
'''
class ModelNameUpdateView(UpdateView):
	fields = ('field_1', 'field_2', 'field_4',)  ## choose the fields to be updated
	model = models.ModelName

## in urls.py in urlpatterns:

path('update_nodelname/<int:pk>', views.ModelNameUpdateView.as_view(), name='update_nodelname'),

## in modelname_detail.html:

<div class="container">

	<p><a class="btn btn-danger" href="{% url 'basic_app:modelname_update' pk=modelname_detail.pk %}">UPDATE</a></p>
</div>

'''




#####################################################################################
'''
from django.urls import reverse_lazy  
class ModelNameDeleteView(DeleteView):
	model = models.ModelName
	success_url = reverse_lazy("basic_app:model_list")

## in urls.py in urlpatterns:

path('delete_modelname/<int:pk>', views.ModelNameDeleteView.as_view(), name='delete_modelname'),

## in templates/basic_app create modelname_confirmdelete.html

'''


#####################################################################################