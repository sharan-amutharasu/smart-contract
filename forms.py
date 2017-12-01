from django import forms
from .models import mt_transactions
from django.forms import ModelForm
from .choices import *

# Create the form class.
class TransactionForm(ModelForm):

	f_ft_quantity_unit = forms.ChoiceField(choices = QUANTITY_UNIT_CHOICES, label = "Unit of Measurement", widget=forms.Select())
	f_pt_quantity_unit = forms.ChoiceField(choices = QUANTITY_UNIT_CHOICES, label = "Unit of Measurement", widget=forms.Select())
	f_ft_type = forms.ChoiceField(choices = TRANS_TYPE_CHOICES, label = "Type of Transaction", initial = "p", widget=forms.Select())
	f_pt_type = forms.ChoiceField(choices = TRANS_TYPE_CHOICES, label = "Type of Transaction", initial = "m", widget=forms.Select())
	
	class Meta:
		model = mt_transactions
		fields = ['f_trans_id', 'f_user_id1', 'f_user_id2', 'f_creator', 'f_ft_type', 'f_ft_quantity_unit', 'f_ft_quantity_number', 'f_ft_category', 'f_ft_description', 'f_pt_type', 'f_pt_quantity_unit','f_pt_quantity_number','f_pt_category', 'f_pt_description', 'f_hash_pk', 'f_hash_u1', 'f_hash_u2']
		labels = { 'f_user_id2': ('User ID of contract partner'), 'f_ft_quantity_unit': ('Unit of measurement'), 'f_ft_quantity_number': ('Quantity'), 'f_ft_category': ('Category'), 'f_ft_description': ('Description'),  'f_pt_quantity_unit': ('Unit of measurement'), 'f_pt_quantity_number': ('Quantity'), 'f_pt_category': ('Category'), 'f_pt_description': ('Description')}
		widgets = {'f_trans_id': forms.HiddenInput(), 'f_creator': forms.HiddenInput(), 'f_hash_pk': forms.HiddenInput(), 'f_hash_u1': forms.HiddenInput(), 'f_hash_u2': forms.HiddenInput()}