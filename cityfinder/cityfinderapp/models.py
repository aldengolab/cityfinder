from __future__ import unicode_literals

from django.db import models

class Walk(models.Model):
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=5, blank=True, null=True)
    walk_score = models.FloatField(max_length=5, blank=True, null=True)
    transit_score = models.FloatField(max_length=5, blank=True, null=True)
    bike_score = models.FloatField(max_length=5, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.city

class Weather(models.Model):
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=5, blank=True, null=True)
    avg_temp_jan = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_april = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_july = models.FloatField(max_length=5, blank=True, null=True)
    avg_temp_oct = models.FloatField(max_length=500, blank=True, null=True)
    avg_annual_precip_in = models.FloatField(max_length=500, blank=True, null=True)
    avg_annual_precip_in_days = models.FloatField(max_length=500, blank=True, null=True)
    avg_annual_precip_snowfall = models.FloatField(max_length=500, blank=True, null=True)

class Rent(models.Model):
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=5, blank=True, null=True)
    bed_1_med_price = models.FloatField(max_length=500, blank=True, null=True) 
    bed_2_med_price = models.FloatField(max_length=500, blank=True, null=True) 


class Crime(models.Model):
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=5, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    violent_crime = models.IntegerField(blank=True, null=True)
    murder = models.IntegerField(blank=True, null=True)
    rape = models.IntegerField(blank=True, null=True)
    robbery = models.IntegerField(blank=True, null=True)
    aggrev_assault = models.IntegerField(blank=True, null=True)
    property_crime = models.IntegerField(blank=True, null=True)
    bulglary = models.IntegerField(blank=True, null=True)
    larceny_theft = models.IntegerField(blank=True, null=True)
    car_theft = models.IntegerField(blank=True, null=True)
    arson = models.IntegerField(blank=True, null=True)

class COL(models.Model):
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=5, blank=True, null=True)
    total_index = models.FloatField(max_length=500, blank=True, null=True) 
    grocery = models.FloatField(max_length=500, blank=True, null=True) 
    housing = models.FloatField(max_length=500, blank=True, null=True) 
    utilities = models.FloatField(max_length=500, blank=True, null=True) 
    transport = models.FloatField(max_length=500, blank=True, null=True) 
    health = models.FloatField(max_length=500, blank=True, null=True) 
    misc = models.FloatField(max_length=500, blank=True, null=True) 

class academic(models.Model):
    institution_id = models.IntegerField(primary_key=True, default=None)
    institution_name = models.CharField(max_length=20, blank=True, null=True)
    institution_add = models.CharField(max_length=20, blank=True, null=True)
    institution_city = models.CharField(max_length=20, blank=True, null=True)
    institution_state = models.IntegerField( blank=True, null=True)
    institution_zip = models.CharField(max_length=7, blank=True, null=True)
    campus_name = models.CharField(max_length=20, blank=True, null=True)
    campus_add = models.CharField(max_length=20, blank=True, null=True)
    campus_city = models.CharField(max_length=20, blank=True, null=True)
    campus_state = models.CharField(max_length=5, blank=True, null=True)
    campus_zip = models.IntegerField(blank=True, null=True)
    accreditation = models.CharField(max_length=20, blank=True, null=True)
    agency_name = models.CharField(max_length=20, blank=True, null=True)
    accreditation_status = models.CharField(max_length=20, blank=True, null=True)
    accreditation_date_type = models.CharField(max_length=20, blank=True, null=True)

