# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 08:06:19 2017

@author: Sharan Amutharasu
"""

import hashlib
import uuid
from .cipher_class import AESCipher

def hash_it(key):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + key.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def add_to_blockchain(key, contract_dict):
    
    return None
    
def decrypt_transaction(key, contract_enc):
    
    return None
    
    
y = 'eHkdsicrkxHTcJUf'
x = hash_it(y)
#x.encode('utf-8')
#a = str(x)