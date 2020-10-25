from django import forms
from .models import Tracksheet
# from datetimepicker.widgets import DateTimePicker


class TracksheetForm(forms.ModelForm):
        class Meta:
            model = Tracksheet
            labels = {
                "date":"Select Date",
                "num_houses_reached": "Number of houses reached",
                "num_houses_doing_segg": "Number of houses giving segregated waste",
                "num_houses_giving_mixwaste":"Number of houses giving mixed waste",
                "drywaste_bf":"Amount of dry waste before sorting(in Kgs)",
                "drywaste_af":"Amount of dry waste after sorting(in Kgs)",
                "wetwaste_bf":"Amount of wet waste before sorting(in Kgs)",
                "wetwaste_af":"Amount of wet waste after sorting(in Kgs)",
                "lane_name":"Name of the lane/area",
                "num_attendants":"Number of Attendants",
                "first_attendants_name":"First Attendant's Name",
                "second_attendants_name":"Second Attendant's Name",
                "time_of_visit":"Morning or Evening",
            }
         
            fields = ('date','lane_name','num_attendants','first_attendants_name','second_attendants_name',
            'time_of_visit','num_houses_reached','num_houses_doing_segg','num_houses_giving_mixwaste','drywaste_bf',
            'drywaste_af','wetwaste_bf','wetwaste_af')

       

            
# demarcated_lane = [
#     ('Waras lane to Hira Seth chawl','Waras lane - Hira Seth chawl'),
#     ('Navneet Lane to Tare Galli','Navneet Lane - Tare Galli'),
#     ('BhandarWada to Amar Prem Chowk','BhandarWada - Amar Prem Chowk'),
#     ('Shankar Mandir to Bhagat Galli ','Shankar Mandir - Bhagat Galli '),
#     ('Gonta Galli to Kranti Galli','Gonta Galli - Kranti Galli'),
#     ('Kranti Galli to Navjeevan Chauk','Kranti Galli - Navjeevan Chauk'),
#     ('Pakhari Galli ','Pakhari Galli '),
#     ('Vada pav Galli to Fish market','Vada pav Galli - Fish market'),
#     ('Payari','Payari'),
#     ('Sonapur to Dukkur Galli','Sonapur - Dukkur Galli'),
#     ('Dukkur to Taak Galli','Dukkur - Taak Galli'),
#     ('Nagobacha Ghumat to Achanak','Nagobacha Ghumat - Achanak'),
#     ('Golfadevi','Golfadevi'),
    

# ]

# class TracksheetForm(forms.Form):
#         date = forms.CharField(max_length=50)
#     #     date = forms.DateTimeField(
#     #     input_formats=['%d/%m/%Y %H:%M'], 
#     #     widget=BootstrapDateTimePickerInput()
#     # )
#     #     date = forms.DateTimeField(
#     #     input_formats=['%d/%m/%Y %H:%M'],
#     #     widget=forms.DateTimeInput(attrs={
#     #         'class': 'form-control datetimepicker-input',
#     #         'data-target': '#datetimepicker1'
#     #     })
#     # )
#         lane_name = forms.CharField(
#                     max_length=100,
#                     widget=forms.Select(choices=demarcated_lane),
#         )
#         num_houses_reached = forms.CharField(max_length=30)

             