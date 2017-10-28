from django import forms
from django.forms import ModelForm
from .models import EventType, Event, Location, GeneralUser
import html5.forms.widgets as html5_widgets
#form for creating event
class EForm(ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time',
                  'location_name', 'location', 'event_type']
        widgets = {'date': html5_widgets.DateInput,
                   'time': html5_widgets.TimeInput,
                   }
    def __init__(self, *args, **kwargs):
        super(EForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control'})
        self.fields['date'].widget.attrs.update({'class' : 'form-control'})
        self.fields['time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['location_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['location'].widget.attrs.update({'class' : 'form-control'})
        self.fields['event_type'].widget.attrs.update({'class' : 'form-control'})



#for for searching the event
class SearchForm(forms.Form):
    # name = forms.CharField(max_length=100, attrs={'class':'form-control'})
    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(), widget =forms.Select(attrs={'class':'form-control'}))
    date = forms.DateField(widget=html5_widgets.DateInput(attrs={'class':'form-control'}))
    location = forms.ModelChoiceField(queryset=Location.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))

    # widgets = {
    #         'event_type': forms.TextInput(attrs={'class':'form-control'}),
    #         'date': forms.Textarea(attrs={'class':'form-control'}),
    #         'location' : forms.FileInput(attrs={'class':'form-control'}),
    #     }


class SubscriptionForm(ModelForm):

    class Meta:
        model = GeneralUser
        fields = ['phone', 'facebook', 'twitter', 'subscription']

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class' : 'form-control'})
        self.fields['facebook'].widget.attrs.update({'class' : 'form-control'})
        self.fields['twitter'].widget.attrs.update({'class' : 'form-control'})
        self.fields['subscription'].widget.attrs.update({'class' : 'form-control'})
