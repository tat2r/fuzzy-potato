from django.urls import path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
	# path('', views.HomeView.as_view(), name='home'),
	path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
	path('customer_list/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
	path('create_customer/', views.CustomerCreateView.as_view(), name='create_customer'),
	path('update_customer/<int:pk>', views.CustomerUpdateView.as_view(), name='update_customer'),
	path('delete_customer/<int:pk>', views.CustomerDeleteView.as_view(), name='delete_customer'),

	path('', views.RentalListView.as_view(), name='home'),
	path('<int:pk>/', views.RentalDetailView.as_view(), name='rental_detail'),
	path('create_rental/', views.RentalCreateView.as_view(), name='create_rental'),
	path('update_rental/<int:pk>', views.RentalUpdateView.as_view(), name='update_rental'),
	path('delete_rental/<int:pk>', views.RentalDeleteView.as_view(), name='delete_rental'),

	path('van_list/', views.VanListView.as_view(), name='van_list'),
	path('van_list/<int:pk>', views.VanDetailView.as_view(), name='van_detail'),
	path('create_van/', views.VanCreateView.as_view(), name='create_van'),
	path('update_van/<int:pk>', views.VanUpdateView.as_view(), name='update_van'),
	path('delete_van/<int:pk>', views.VanDeleteView.as_view(), name='delete_van'),
]