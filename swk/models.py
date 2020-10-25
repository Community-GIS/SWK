from django.db import models
from django import forms
from django.forms import ModelForm

from wagtail.core.models import Page

# from wagtail.core.fields import RichTextField
# from modeltranslation.translator import TranslationOptions

# Create your models here.
# class Drywaste(models.Model):
#     category    = models.CharField(max_length=200, blank = False)
#     category_id  = models.AutoField(primary_key=True)
#     sp_per_kg   = models.DecimalField(decimal_places = 2, max_digits = 10 , null = False) 
#     sp_on_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.category


class HomePage(Page):

    template = "HomePage.html"


# /* Tracksheet  Model */
timeslot= [

            ('7:30am - 8:30 am','Morning'),
            ('7:30pm - 8:30 pm','Evening'),

]

atten_name = [
    ('Amrapali','Amrapali'),
    ('Jana pote','Jana pote'),
    ('Kaushalya', 'Kaushalya'),
    ('Parvati','Parvati'),
    ('Sakuntala','Sakuntala'),
    ('Asha','Asha'),

]


demarcated_lane = [
    ('Waras lane to Hira Seth chawl','Waras lane - Hira Seth chawl'),
    ('Navneet Lane to Tare Galli','Navneet Lane - Tare Galli'),
    ('BhandarWada to Amar Prem Chowk','BhandarWada - Amar Prem Chowk'),
    ('Shankar Mandir to Bhagat Galli ','Shankar Mandir - Bhagat Galli '),
    ('Gonta Galli to Kranti Galli','Gonta Galli - Kranti Galli'),
    ('Kranti Galli to Navjeevan Chauk','Kranti Galli - Navjeevan Chauk'),
    ('Pakhari Galli ','Pakhari Galli '),
    ('Vada pav Galli to Fish market','Vada pav Galli - Fish market'),
    ('Payari','Payari'),
    ('Sonapur to Dukkur Galli','Sonapur - Dukkur Galli'),
    ('Dukkur to Taak Galli','Dukkur - Taak Galli'),
    ('Nagobacha Ghumat to Achanak','Nagobacha Ghumat - Achanak'),
    ('Golfadevi','Golfadevi'),
    

]
class TracksheetModel(Page):

    template = "TracksheetForm.html"

class Tracksheet(models.Model):
    date =models.DateField()
    num_houses_reached = models.IntegerField(default= 20)
    num_houses_doing_segg = models.IntegerField()
    num_houses_giving_mixwaste = models.IntegerField()
    drywaste_bf = models.IntegerField()
    drywaste_af = models.IntegerField()
    wetwaste_bf = models.IntegerField()
    wetwaste_af = models.IntegerField()
    lane_name = models.CharField(choices=demarcated_lane,max_length=200, blank = False)
    num_attendants = models.IntegerField(default = 2)
    first_attendants_name = models.CharField(choices=atten_name,max_length=100,default='Amrapali')
    second_attendants_name = models.CharField(choices=atten_name,max_length=100,default='Jana pote')
    time_of_visit = models.CharField(choices=timeslot,max_length=100,default='Morning')
    track_id = models.AutoField(primary_key=True)

    def __str__(self):
        
        return self.lane_name

# class TracksheetForm(ModelForm):
#     class Meta:
#         model = Tracksheet
#         fields = ['num_houses_reached','date','num_houses_doing_segg','num_houses_giving_mixwaste','drywaste_bf',
#         'drywaste_af','wetwaste_bf','wetwaste_af','lane_name','num_attendants',
#         'first_attendants_name','second_attendants_name','time_of_visit']
#         labels = {
#                 "date":"Enter Date",
#                 "num_houses_reached": "Number of houses reached",
#                 "num_houses_doing_segg": "Number of houses giving segregated waste",
#                 "num_houses_giving_mixwaste":"Number of houses giving mixed waste",
#                 "drywaste_bf":"Amount of dry waste before sorting(in Kgs)",
#                 "drywaste_af":"Amount of dry waste after sorting(in Kgs)",
#                 "wetwaste_bf":"Amount of wet waste before sorting(in Kgs)",
#                 "wetwaste_af":"Amount of wet waste after sorting(in Kgs)",
#                 "lane_name":"Name of the lane/area",
#                 "first_attendants_name":"First Attendant's Name",
#                 "second_attendants_name":"Second Attendant's Name",
#                 "time_of_visit_morning":"Morning or Evening",
                
#             }
#         widgets = {
#             'date': DatePickerInput(format='%d-%m-%Y'), # default date-format %m/%d/%Y will be used
            
#         }


# class TracksheetForm(forms.ModelForm):
#         class Meta:
#             model = Tracksheet
#             labels = {
#                 "num_houses_reached": "Number of houses reached",
#                 "num_houses_doing_segg": "Number of houses giving segregated waste",
#                 "num_houses_giving_mixwaste":"Number of houses giving mixed waste",
#                 "drywaste_bf":"Amount of dry waste before sorting",
#                 "drywaste_af":"Amount of dry waste after sorting",
#                 "wetwaste_bf":"Amount of wet waste before sorting",
#                 "wetwaste_af":"Amount of wet waste after sorting",
#                 "lane_name":"Name of the lane/area",
#                 "attendants_name":"Attendant's Name",
#                 "time_of_visit_morning":"Morning or Evening",
                
#             }
#             fields = '__all__'


# class Lanedetails(models.Model):
#     lane_name = models.CharField(max_length=200, blank= False, primary_key = True)
#     num_houses_lane = models.IntegerField()

#     def __str__(self):
#         return self.lane_name

# class LaneCordinator(models.Model):
#     cordinator_name = models.CharField(max_length=200, primary_key=True)
#     mentor_name = models.CharField(max_length=200)
#     attendants_name = models.CharField(max_length = 200)
#     attendants_lane_name  = models.CharField(max_length=200)

#     def __str__(self):
#         return self.cordinator_name

# class TextPage(TranslatablePage):
#     text = RichTextField(blank=True)

#     content_panels = TranslatablePage.content_panels + [
#     FieldPanel('text',classname='full')
#     ]