from django.db import models
import pytz
from django.urls import reverse
from datetime import datetime
# Create your models here.

class ModelName(models.Model):
	pass


class Customer(models.Model):

	first_name = models.CharField(max_length=32, blank=True, null=False)
	last_name = models.CharField(max_length=32, blank=True, null=False)
	phone = models.CharField(unique=True, max_length=32, blank=True, null=False)
	email = models.EmailField(unique=True, blank=True)
	street = models.CharField(max_length=128, blank=True, null=False)
	city = models.CharField(max_length=128, blank=True, null=False)
	state = models.CharField(max_length=56, blank=True, null=False)
	z_code = models.CharField(max_length=10, blank=True, null=False)

	lic_class = (('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), ('D', 'Class D-Operator'))
	d_lic_num = models.CharField(max_length=56, blank=True)
	d_lic_class = models.CharField(max_length=1, choices=lic_class, blank=True, null=False)
	d_lic_exp = models.CharField(max_length=56, blank=True)
	d_dob = models.CharField(max_length=56, blank=True)

	name_on_cc = models.CharField(max_length=128,blank=True, null=False)
	cc_num = models.CharField(max_length=16, blank=True, null=False)
	cc_exp = models.CharField(max_length=56, blank=True)
	cc_cv = models.CharField(max_length=4, blank=True, null=False)


	def get_absolute_url(self):
		return reverse('basic_app:customer_detail', kwargs={'pk':self.pk})

	def __str__(self):
		output = f'{self.last_name}   {self.first_name}'
		return output

class AdditionalDriver(models.Model):
	pass 
# 	additional_driver_01_first_name = models.CharField(max_length=32, blank=True, null=False)
# 	additional_driver_01_last_name = models.CharField(max_length=32, blank=True, null=False)
# 	additional_driver_01_phone = models.CharField(unique=True, max_length=32, blank=True, null=False)
# 	additional_driver_01_email = models.EmailField(unique=True, blank=True)
# 	additional_driver_01_z_code = models.CharField(max_length=10, blank=True, null=False)
# 	additional_driver_01_lic_class = (('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), ('D', 'Class D-Operator'))
# 	additional_driver_01_d_lic_num = models.CharField(max_length=56, blank=True)
# 	additional_driver_01_d_lic_class = models.CharField(max_length=1, choices=lic_class, blank=True, null=False)
# 	additional_driver_01_d_lic_exp = models.DateField(blank=True, null=False)
# 	additional_driver_01_d_dob = models.DateField(blank=True, null=False)

# 	def __str__(self):
# 		display = f'{self.last_name}, {self.first_name}'
# 		return display



class AdobeDriver(models.Model):

	first_name = models.CharField(max_length=32, blank=True, null=False)
	last_name = models.CharField(max_length=32, blank=True, null=False)
	phone = models.CharField(unique=True, max_length=32, blank=True, null=False)
	email = models.EmailField(unique=True, blank=True)
	street = models.CharField(max_length=128, blank=True, null=False)
	city = models.CharField(max_length=128, blank=True, null=False)
	state = models.CharField(max_length=56, blank=True, null=False)
	z_code = models.CharField(max_length=10, blank=True, null=False)

	lic_class = (('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), ('D', 'Class D-Operator'))
	d_lic_num = models.CharField(max_length=56, blank=True)
	d_lic_class = models.CharField(max_length=1, choices=lic_class, blank=True, null=False)
	d_lic_exp = models.CharField(max_length=56, blank=True)
	d_dob = models.CharField(max_length=56, blank=True)

	def get_absolute_url(self):
		return reverse('basic_app:driver_detail', kwargs={'pk':self.pk})

	def __str__(self):
		output = f'{self.last_name}   {self.first_name}'
		return output


class Van(models.Model):
	van_num = models.CharField(max_length=4, blank=True)
	vin = models.CharField(max_length=60, blank=True)
	year_make_model = models.CharField(max_length=128, blank=True)
	plate = models.CharField(max_length=10, blank=True)
	tag_exp = models.CharField(max_length=56, blank=True)

	def __str__(self):
		return	self.van_num

	def get_absolute_url(self):
		return reverse('basic_app:van_detail', kwargs={'pk':self.pk})


class Rental(models.Model):
	
	active_inactive = (('InA', 'Inactive'), ('ACT', 'Active'), ('InH', 'In Holding'), ('Cmp', 'Completed'), ('OpR', 'Open Rental'))
	gas_gage = (('F', 'Full'), ('7/8', '7/8'), ('3/4', '3/4'), ('5/8', '5/8'), ('H', 'Half'),('3/8', '3/8'), ('1/4', '1/4'), ('1/8', '1/8'), ('E', 'Empty'))
	yes_and_no = (('Y', 'YES'), ('N', 'NO'))


	### initial process
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
	rental_date = models.DateTimeField(blank=True, null=False, auto_now_add=False)
	return_date = models.DateTimeField(blank=True, null=False, auto_now_add=False)
	van_rented = models.ForeignKey(Van, on_delete=models.CASCADE, blank=True, null=False)
	
	status_type = models.CharField(max_length=10, blank=False, choices=active_inactive)

	##initial charges
	daily_rate = models.DecimalField(max_digits=6, decimal_places=2, default=144.95, blank=True, null=False)
	allowed_daily_miles = models.PositiveIntegerField(default=200, blank=True, null=False)
	mileage_over_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.50, blank=True, null=False)
	additional_driver_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	mexico_insurance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	roadside_assistance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)


	## additional driver add on ## ForeignKey model was throwing errors
	lic_class = (('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), ('D', 'Class D-Operator'))
	additional_driver_01_first_name = models.CharField(max_length=32, blank=True, null=False)
	additional_driver_01_last_name = models.CharField(max_length=32, blank=True, null=False)
	additional_driver_01_phone = models.CharField(max_length=32, blank=True, null=False)
	additional_driver_01_email = models.EmailField(blank=True)
	additional_driver_01_z_code = models.CharField(max_length=10, blank=True, null=False)
	additional_driver_01_d_lic_num = models.CharField(max_length=56, blank=True)
	additional_driver_01_d_lic_class = models.CharField(max_length=1, choices=lic_class, blank=True, null=False)
	additional_driver_01_d_lic_exp = models.CharField(max_length=56, blank=True)
	additional_driver_01_d_dob = models.CharField(max_length=56, blank=True)

	additional_driver_02_first_name = models.CharField(max_length=32, blank=True, null=False)
	additional_driver_02_last_name = models.CharField(max_length=32, blank=True, null=False)
	additional_driver_02_phone = models.CharField(max_length=32, blank=True, null=False)
	additional_driver_02_email = models.EmailField(blank=True)
	additional_driver_02_z_code = models.CharField(max_length=10, blank=True, null=False)
	additional_driver_02_d_lic_num = models.CharField(max_length=56, blank=True)
	additional_driver_02_d_lic_class = models.CharField(max_length=1, choices=lic_class, blank=True, null=False)
	additional_driver_02_d_lic_exp = models.CharField(max_length=56, blank=True)
	additional_driver_02_d_dob = models.CharField(max_length=56, blank=True)

	
	surcharge = models.DecimalField(max_digits=6, decimal_places=2, default=4.50, null=False)
	lic_tax = models.DecimalField(max_digits=4, decimal_places=3, default=0.05, null=False)
	city_sales_tax = models.DecimalField(max_digits=4, decimal_places=3, default=0.081, null=False)
	airport_access_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	drop_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	
	### secondary process
	date_returned = models.DateTimeField(blank=True, null=True, auto_now_add=False)
	late_charge = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	
	miles_over_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	cleaning_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	other_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	
	fuel_charge = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False, default=0)
	notes = models.TextField(blank=True, null=False)

	## Van Pre and Post insepction
	gas_out = models.CharField(max_length=3, choices=gas_gage, blank=True, null=False, default='Full')
	odometer_out = models.PositiveIntegerField(default=0, blank=True, null=False)
	van_out_text = models.TextField(blank=True, null=False)


	odometer_in = models.PositiveIntegerField(default=0, null=False, blank=True)
	gas_in = models.CharField(max_length=3, choices=gas_gage, blank=True, null=False)
	van_in_text = models.TextField(blank=True, null=False)

	damage_type = (('0', 'Undamaged'), ('1', 'Damaged'), ('2', 'Preexisting Damage') )

	windshield_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	grill_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	front_bumper_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	rear_bumper_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	backdoor_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	backdoor_widow_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	seats_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	carpet_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_seat_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_front_tire_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_rear_tire_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_window_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_rear_window_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_mid_window_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_front_quarter_panel_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_mid_panel_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_rear_quarter_panel_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_seat_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_front_tire_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_rear_tire_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_window_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_rear_window_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_mid_window_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_front_quarter_panel_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_mid_panel_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_rear_quarter_panel_out = models.CharField(max_length=1, choices=damage_type, blank=True)
	windshield_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	grill_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	front_bumper_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	rear_bumper_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	backdoor_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	backdoor_widow_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	seats_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	carpet_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_seat_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_front_tire_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_rear_tire_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_window_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_rear_window_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_mid_window_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_front_quarter_panel_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_mid_panel_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	driver_side_rear_quarter_panel_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_seat_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_front_tire_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_rear_tire_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_window_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_rear_window_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_mid_window_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_front_quarter_panel_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_mid_panel_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)
	pass_side_rear_quarter_panel_retrun = models.CharField(max_length=1, choices=damage_type, blank=True)

	

	def __str__(self):
		title = f'{self.customer} : {self.rental_date.date().month}-{self.rental_date.date().day}-{self.rental_date.date().year} : {self.rental_date.time()}'
		return title

	def invoice_number(self):
		self.customer.last_name[0:2].upper()


	def total_days(self):
		num_of_days = self.return_date - self.rental_date
		return num_of_days

	def daily_sub(self):
		init_sum = self.daily_rate + self.additional_driver_fee + self.mexico_insurance + self.roadside_assistance + self.airport_access_fee + self.drop_fee
		return init_sum

	def subtotal(self):
		init_sum = self.daily_rate + self.additional_driver_fee + self.mexico_insurance + self.roadside_assistance + self.airport_access_fee + self.drop_fee
		days = self.total_days().days
		final_sub = init_sum * days
		return final_sub
		
	def sales_tax_sub(self):
		init_sum = self.daily_rate + self.additional_driver_fee + self.mexico_insurance + self.roadside_assistance + self.airport_access_fee + self.drop_fee
		days = self.total_days().days
		final_sub = init_sum * days
		st_sub = self.city_sales_tax * final_sub
		st_round = round(st_sub, 2)
		return st_round

	def license_tax_sub(self):
		init_sum = self.daily_rate + self.additional_driver_fee + self.mexico_insurance + self.roadside_assistance + self.airport_access_fee + self.drop_fee
		days = self.total_days().days
		final_sub = init_sum * days
		lt_sub = self.lic_tax * final_sub
		lt_round = round(lt_sub, 2)
		return lt_round

	def ancillary_total(self):
		s_tax = self.sales_tax_sub()
		l_tax = self.license_tax_sub()
		s_charge = self.surcharge
		at_sub = s_tax + l_tax + s_charge
		return at_sub

	def total_due(self):
		d_sub = self.subtotal()
		at_sub = self.ancillary_total()
		td_due = d_sub + at_sub
		return td_due

	# def subtotal(self):

	# 	num_of_days = self.return_date - self.rental_date
	# 	daily_sub_rate = (self.daily_rate + self.mexico_insurance + self.additional_driver_fee + self.roadside_assistance)
	# 	daily_subtotal = num_of_days.days * daily_sub_rate
		
	# 	sales_tax = self.city_sales_tax * daily_subtotal
	# 	license_tax = self.lic_tax * daily_subtotal
	# 	# ten_percent_airport_access = .1 * airport_access_fee##+ ten_percent_airport_access

	# 	initial_total = self.surcharge + self.drop_fee + sales_tax + license_tax  + self.other_fee
	# 	grand_total = initial_total + daily_subtotal
	# 	return grand_total


	def get_absolute_url(self):
		return reverse('basic_app:rental_detail', kwargs={'pk':self.pk})


