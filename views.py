from django.shortcuts import render

# Create your views here.

#add_to_end: 2017-11-22 11:04:20.581523
from django.db import models
from django.views import generic
import datetime
from django.db.models import Max
from .models import mt_users, mt_transactions
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .forms import TransactionForm

def sc_home(request):
	user = str(request.user).strip()
	#max_user_id = mt_users.objects.all().aggregate(Max('f_user_id'))['f_user_id__max']
	#return render(request,'sc_home.html', {'user':user, 'max':max_user_id + 1})
	#"""
	try:
		user_object = mt_users.objects.get(f_user_name=user)
	except ObjectDoesNotExist:
		max_user_id = mt_users.objects.all().aggregate(Max('f_user_id'))['f_user_id__max']
		user_object = mt_users(f_user_id=max_user_id + 1, f_user_name=user)
		user_object.save()
	open_contracts = mt_transactions.objects.filter(f_user_id2 = user_object.f_user_id, f_status = 'c').values()
	return render(request,'sc_home.html', {'user':user, 'user_id':user_object.f_user_id, 'open_contracts':open_contracts})
	#"""

#add_to_end: 2017-11-22 11:04:20.581548

def sc_create_contract(request):
	user = str(request.user).strip()
	if request.method == 'GET':
		try:
			user_object = mt_users.objects.get(f_user_name=user)
		except ObjectDoesNotExist:
			max_user_id = mt_users.objects.all().aggregate(Max('f_user_id'))['f_user_id__max']
			user_object = mt_users(f_user_id=max_user_id + 1, f_user_name=user)
			user_object.save()
		user_object = mt_users.objects.get(f_user_name=user)
		if user_object.f_verification_status == False:
			return render(request,'sc_not_verified.html', {'user':user})
		else:
			form = TransactionForm()
			return render(request,'sc_create_contract.html', {'user':user, 'user_id':user_object.f_user_id, 'form':form, 'filler':'Enter contract details:'})
	elif request.method == 'POST':
		form = TransactionForm(data=request.POST)
		max_trans_id = mt_transactions.objects.all().aggregate(Max('f_trans_id'))['f_trans_id__max']
		updated_data = request.POST.copy()
		updated_data.update({'f_trans_id': max_trans_id + 1})
		updated_data.update({'f_user_id1': int(updated_data['f_user_id1']), 'f_user_id2': int(updated_data['f_user_id2']), 'f_ft_quantity_number': int(updated_data['f_ft_quantity_number']), 'f_pt_quantity_number': int(updated_data['f_pt_quantity_number'])})
		form2 = TransactionForm(data=updated_data)
		#verify user
		try:
			user2 = mt_users.objects.get(f_user_id=updated_data['f_user_id2'], f_verification_status=True)
		except ObjectDoesNotExist:
			return render(request,'sc_home.html', {'user':'Invalid partner ID'})
		if updated_data['f_user_id1']== updated_data['f_user_id2']:
			return render(request,'sc_home.html', {'user':'Invalid partner ID. Both IDs cannot be same.'})			
		if form2.is_valid():
			form2.save()
			return render(request,'sc_home.html', {'user':'Valid form'})
		else:
			return render(request,'sc_create_contract.html', {'user':user, 'user_id':updated_data['f_user_id1'], 'form':form, 'filler':'Invalid inputs. Refill the details.'})
			
def sc_confirm_transaction(request):
	user = str(request.user).strip()
	return render(request,'sc_home.html', {'user':user})
	
	
def sc_contract(request):
	user = str(request.user).strip()
	try:
		user_object = mt_users.objects.get(f_user_name=user)
	except ObjectDoesNotExist:
		max_user_id = mt_users.objects.all().aggregate(Max('f_user_id'))['f_user_id__max']
		user_object = mt_users(f_user_id=max_user_id + 1, f_user_name=user)
		user_object.save()
	open_contracts = mt_transactions.objects.filter(f_user_id2 = user_object.f_user_id, f_status = 'c').values()
	return render(request,'sc_home.html', {'user':user, 'user_id':user_object.f_user_id, 'open_contracts':open_contracts})