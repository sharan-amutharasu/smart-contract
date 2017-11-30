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
from .blockchain.cipher_class import AESCipher
from .blockchain.contract import contract_to_dict
from .blockchain.encryption import hash_it, check_password
from django.db.models import Q
from django.shortcuts import redirect, reverse, get_object_or_404
import pickle

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
	contracts_c = mt_transactions.objects.filter(Q(f_user_id1=user_object.f_user_id) | Q(f_user_id2=user_object.f_user_id), f_status = 'c').values()
	contracts_a = mt_transactions.objects.filter(Q(f_user_id1=user_object.f_user_id) | Q(f_user_id2=user_object.f_user_id), f_status = 'a').values()
	contracts_h = mt_transactions.objects.filter(Q(f_user_id1=user_object.f_user_id) | Q(f_user_id2=user_object.f_user_id), f_status = 'h').values()
	contracts_x = mt_transactions.objects.filter(Q(f_user_id1=user_object.f_user_id) | Q(f_user_id2=user_object.f_user_id), f_status = 'x').values()
	return render(request,'sc_home.html', {'user':user, 'user_id':user_object.f_user_id, 'contracts_c':contracts_c, 'contracts_a':contracts_a, 'contracts_h':contracts_h, 'contracts_x':contracts_x})
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
		updated_data.update({'f_user_id1': int(updated_data['f_user_id1']), 'f_user_id2': int(updated_data['f_user_id2']), 'f_creator': int(updated_data['f_creator']), 'f_ft_quantity_number': int(updated_data['f_ft_quantity_number']), 'f_pt_quantity_number': int(updated_data['f_pt_quantity_number'])})
		
		#verify user
		try:
			user1 = mt_users.objects.get(f_user_id=updated_data['f_user_id1'], f_verification_status=True)
			user2 = mt_users.objects.get(f_user_id=updated_data['f_user_id2'], f_verification_status=True)
		except ObjectDoesNotExist:
			return render(request,'sc_create_contract.html', {'user':user, 'user_id':updated_data['f_creator'], 'form':form, 'filler':'Invalid ID'})
		if updated_data['f_user_id1'] == updated_data['f_user_id2']:
			return render(request,'sc_create_contract.html', {'user':user, 'user_id':updated_data['f_creator'], 'form':form, 'filler':'Invalid  ID. Both IDs cannot be same.'})
		if updated_data['f_creator'] != updated_data['f_user_id1'] and updated_data['f_creator'] != updated_data['f_user_id2']:
			return render(request,'sc_create_contract.html', {'user':user, 'user_id':updated_data['f_creator'], 'form':form, 'filler':'Invalid  ID. One ID has to be yours.'})

		pk = updated_data['f_hash_pk']
		pk_hash = hash_it(pk)
		updated_data.update({'f_hash_pk': pk_hash})
		if updated_data['f_creator'] == updated_data['f_user_id1']:
			u1 = updated_data['f_hash_u1']
			u1_hash = hash_it(u1)
			updated_data.update({'f_hash_u1': u1_hash})
		else:
			u2 = updated_data['f_hash_u1']
			u2_hash = hash_it(u2)
			updated_data.update({'f_hash_u2': u2_hash})
			updated_data.update({'f_hash_u1': 'u1'})
		
		
		form2 = TransactionForm(data=updated_data)
		if form2.is_valid():
			form2.save()
			return render(request, 'sc_contract_created.html', {'user':user, 'user_id':updated_data['f_creator'], 'contract_id':updated_data['f_trans_id']} )
		else:
			return render(request,'sc_create_contract.html', {'user':user, 'user_id':updated_data['f_creator'], 'form':form2, 'filler':'Invalid inputs. Refill the form'})
			
def sc_access_contract(request):
	user = str(request.user).strip()
	return render(request,'sc_access_contract.html', {'user':user, 'filler':''})
	
	
def sc_contract(request):
	user = str(request.user).strip()
	if request.method == 'GET':
		return render(request,'sc_access_contract.html', {'user':user, 'filler':''})
	elif request.method == 'POST':
		try:
			user_object = mt_users.objects.get(f_user_name=user)
		except ObjectDoesNotExist:
			max_user_id = mt_users.objects.all().aggregate(Max('f_user_id'))['f_user_id__max']
			user_object = mt_users(f_user_id=max_user_id + 1, f_user_name=user)
			user_object.save()
		
		post_data = request.POST.copy()
		try:
			contract = mt_transactions.objects.get(f_trans_id = post_data['contract_id'])
		except ObjectDoesNotExist:
			return render(request,'sc_access_contract.html', {'user':user, 'filler':'Invalid contract ID'})
			
		pak = post_data['pk']
		if check_password(contract.f_hash_pk, pak):
			type_mapping = {'p':"Product", 's':"Service", 'm':"Money"}
			ft_type = type_mapping[contract.f_ft_type]
			pt_type = type_mapping[contract.f_pt_type]
			unit_mapping = {'sc':"Seconds", 'mn':"Minutes", 'hr':"Hours", 'un':"Units", 'kg':"Kilograms", 'cm':"Cubic Meter", 'rp':"Rupees", 'dl':"Dollars", 'eu':"Euros"}
			ft_unit_type = unit_mapping[contract.f_ft_quantity_unit]
			pt_unit_type = unit_mapping[contract.f_pt_quantity_unit]
			return render(request,'sc_contract.html', {'user':user, 'user_id':user_object.f_user_id, 'contract':contract, 'ft_type':ft_type, 'pt_type':pt_type, 'ft_unit_type':ft_unit_type, 'pt_unit_type':pt_unit_type})
		else:
			return render(request,'sc_access_contract.html', {'user':user, 'filler':'Invalid public access key'})

			
def sc_approve_contract(request):
	user = str(request.user).strip()	
	try:
		user_object = mt_users.objects.get(f_user_name=user)
	except ObjectDoesNotExist:
		max_user_id = mt_users.objects.all().aggregate(Max('f_user_id'))['f_user_id__max']
		user_object = mt_users(f_user_id=max_user_id + 1, f_user_name=user)
		user_object.save()
	if request.method == 'GET':
		return render(request,'sc_approve_contract.html', {'user':user, 'user_id':user_object.f_user_id, 'filler':''})
	elif request.method == 'POST':		
		
		post_data = request.POST.copy()
		try:
			contract = mt_transactions.objects.get(f_trans_id = post_data['contract_id'])
		except ObjectDoesNotExist:
			return render(request,'sc_approve_contract.html', {'user':user, 'user_id':user_object.f_user_id, 'filler':'Invalid contract ID'})
			
		pak = post_data['pk']
		up = post_data['up']
		up_hash = hash_it(up)
		if check_password(contract.f_hash_pk, pak):
			if user_object.f_user_id == contract.f_user_id2:
				contract.f_hash_u2 = up_hash
			elif user_object.f_user_id == contract.f_user_id1:
				contract.f_hash_u1 = up_hash
			contract.f_status = 'a'
			contract.save()
			#add_to_blockchain(contract, pak)
			return render(request,'sc_contract_approved.html', {'user':user, 'user_id':user_object.f_user_id, 'contract_id':contract.f_trans_id})
		else:
			return render(request,'sc_approve_contract.html', {'user':user, 'user_id':user_object.f_user_id, 'filler':'Invalid public access key'})