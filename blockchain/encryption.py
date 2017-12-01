# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 08:06:19 2017

@author: Sharan Amutharasu
"""

import hashlib
import uuid
from .cipher_class import AESCipher
import os
import _pickle as cPickle
from datetime import datetime
import ast

def hash_it(key):
    """
    input: string
    output: string 
    hashes the key string using SHA256 algorithm
    """
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + key.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    """
    input: string, string
    output: boolean
    compares the hash of the second string with the raw first string and returns result
    """
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    
def get_chain_indices():
    """
    input: 
    output: list
    Returns list of indices in the chain.pkl file
    """
    #read blockchain file
    bc_file = os.path.join(os.getcwd(),'app_sc/blockchain/chain.pkl')
    with open(bc_file, 'rb') as f:
        chain = cPickle.load(f)
    indices = list(chain['contracts'].keys())
    return indices

def add_to_blockchain(key, contract_dict):
    """
    input: string, dict
    output: string
    encrypts the contract details using the passed key and adds it to chain.pkl file
    """
    #create id string for contract
    contract_id = str('0'*(16 - len(str(contract_dict['details']['trans_id']))) +str(contract_dict['details']['trans_id'])) 
    now = str(datetime.now().strftime('%Y%m%d%H%M%f'))
    id_str = str(now + 'x' + contract_id + 'xa')
    #encrpyt contract details
    cip = AESCipher(key)
    enc = cip.encrypt(str(contract_dict['details']))
    contract_dict['details'] = enc
    #read blockchain file
    bc_file = os.path.join(os.getcwd(),'app_sc/blockchain/chain.pkl')
    with open(bc_file, 'rb') as f:
        chain = cPickle.load(f)
    #add contract to blockchain file
    chain['contracts'][id_str] = contract_dict
    chain['length'] += 1
    #save updated blockchain file
    with open(bc_file, 'wb') as f:
            cPickle.dump(chain, f)
    return 'done'
    
def get_contract_status(contract_id):
    """
    input: int
    output: string
    checks the status of the passed contract and returns it
    """
    indices = get_chain_indices()
    id_str_sub = str('0'*(16 - len(str(contract_id))) +str(contract_id)) 
    filtered_indices = [i for i in indices if id_str_sub in i]
    if len(filtered_indices) == 0:
        status = 'm'
    elif len(filtered_indices) == 1:
        status = 'a'
    elif len(filtered_indices) > 1:
        if len(filtered_indices) > 2:
            status = 'x'
        else:
            sub_indices = [i[-2:] for i in filtered_indices]
            indices1 = [i for i in sub_indices if 'x1' in i]
            indices2 = [i for i in sub_indices if 'x2' in i]
            if len(indices1) == 1:
                status = '1'
            elif len(indices2) == 1:
                status = '2'    
    return status
    
    
def confirm_contract(contract_id, pk, up):
    """
    input: int, string, string
    output: string
    Takes in the contract id, public access key and contract password, checks credentials and updates the status of the contract in the chain.pkl file
    """
    #read blockchain file
    bc_file = os.path.join(os.getcwd(),'app_sc/blockchain/chain.pkl')
    with open(bc_file, 'rb') as f:
        chain = cPickle.load(f)
    indices = list(chain['contracts'].keys())
    #filter contract
    id_str_sub = str('0'*(16 - len(str(contract_id))) + str(contract_id) + 'xa') 
    filtered_indices = [i for i in indices if id_str_sub in i]
    contract = chain['contracts'][filtered_indices[0]]
    #validate passwords and add encrypted confirmations to chain
    if check_password(contract['hash_pk'],pk):
        if check_password(contract['hash_u1'],up):
            enc = AESCipher(up).encrypt('half stub heehaw')
            #create id string for contract
            id_sub_str = str('0'*(16 - len(str(contract_id))) +str(contract_id)) 
            now = str(datetime.now().strftime('%Y%m%d%H%M%f'))
            id_str = str(now + 'x' + id_sub_str + 'x1')
            #add contract to blockchain file
            chain['contracts'][id_str] = enc
            chain['length'] += 1
            #save updated blockchain file
            with open(bc_file, 'wb') as f:
                    cPickle.dump(chain, f)
            return 'done'
        elif check_password(contract['hash_u2'],up):
            enc = AESCipher(up).encrypt('half stub heehaw')
            #create id string for contract
            id_sub_str = str('0'*(16 - len(str(contract_id))) +str(contract_id)) 
            now = str(datetime.now().strftime('%Y%m%d%H%M%f'))
            id_str = str(now + 'x' + id_sub_str + 'x2')
            #add contract to blockchain file
            chain['contracts'][id_str] = enc
            chain['length'] += 1
            #save updated blockchain file
            with open(bc_file, 'wb') as f:
                    cPickle.dump(chain, f)
            return 'done'
    return 'not done'
    
    
#get_contract_status(17)
#c = confirm_contract(16,pk,up)
#y = 'NzEeU5U0R0EwSNGh'
#x = hash_it(y)
#x.encode('utf-8')
#a = str(x)
#ast.literal_eval(str(contract_dict))