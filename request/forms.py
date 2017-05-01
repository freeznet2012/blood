from django import forms

from .models import Request

class RequestCreationForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ('name', 'contact', 'blood','units', 'district', 'particulars', 'date_of_request')