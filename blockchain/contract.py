# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:03:51 2017

@author: Sharan Amutharasu
"""
import pickle
import os        

def contract_to_dict(contract):
    x = {}
    x['hash_pk'] = contract.f_hash_pk
    x['hash_u1'] = contract.f_hash_u1
    x['hash_u2'] = contract.f_hash_u2
    x['details'] = {}
    x['details']['trans_id'] = contract.f_trans_id
    x['details']['user_id1'] = contract.f_user_id1
    x['details']['ft_type'] = contract.f_ft_type
    x['details']['ft_id'] = contract.f_ft_id
    x['details']['ft_qu'] = contract.f_ft_quantity_unit
    x['details']['ft_qn'] = contract.f_ft_quantity_number
    x['details']['user_id2'] = contract.f_user_id1
    x['details']['pt_type'] = contract.f_pt_type
    x['details']['pt_id'] = contract.f_pt_id
    x['details']['pt_qu'] = contract.f_pt_quantity_unit
    x['details']['pt_qn'] = contract.f_pt_quantity_number
    return x
    
        
#x = 'asdfsdf'
#pickle.dump( enc, open( "enc.pkl", "wb" ) )
#os.chdir(str_project_folder)
#os.chdir(str_bc_folder)
#contract = pickle.load( open( "contract_dict.pkl", "rb" ) )
#x == y