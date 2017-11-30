# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:03:51 2017

@author: Sharan Amutharasu
"""
import pickle
import os        

def contract_to_dict(contract):
    x = {}
    x['trans_id'] = contract.f_trans_id
    x['user_id1'] = contract.f_user_id1
    x['ft_type'] = contract.f_ft_type
    x['ft_id'] = contract.f_ft_id
    x['ft_qu'] = contract.f_ft_quantity_unit
    x['ft_qn'] = contract.f_ft_quantity_number
    x['user_id2'] = contract.f_user_id1
    x['pt_type'] = contract.f_pt_type
    x['pt_id'] = contract.f_pt_id
    x['pt_qu'] = contract.f_pt_quantity_unit
    x['pt_qn'] = contract.f_pt_quantity_number
    return x
    
        
#x = 'asdfsdf'
#pickle.dump( enc, open( "enc.pkl", "wb" ) )
#os.chdir(str_project_folder)
#os.chdir(str_bc_folder)
#contract = pickle.load( open( "contract_dict.pkl", "rb" ) )
#x == y