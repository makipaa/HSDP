import config

def validate_user(username, password):
    if (username == config.DONOR["username"]) & (password == config.DONOR["password"]):
        return "donor"
    elif (username == config.DOCTOR["username"]) & (password == config.DOCTOR["password"]):
        return "doctor"
    else:
        return None


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:11:16 2022

@author: sqemch
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:56:12 2022

@author: marti
"""

#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import json
import requests
from pprint import pprint
import sys
import fhir_client

hemodonor_client = fhir_client.SimpleFHIRClient(
    server_url="http://tutsgnfhir.com",
    server_user="tutfhir",
    server_password="tutfhir1")
all_patients = hemodonor_client.get_all_patients()

# List all found patients
pprint("Listing all ({}) found patients...".format(len(all_patients)))

patients_id = []

for patient_record in all_patients:
    patient_id = patient_record["id"]
    patients_id.append(patient_id)
    patient_given = patient_record["name"][0]["given"][0]
    patient_family = patient_record["name"][0]["family"][0]
    pprint("Patient record id=({}) name=({})"
           .format(patient_id, patient_given + " " + patient_family))

# Get all data for first patient
pprint("Getting all data for first patient in the list...")
all_data_patient_0 = hemodonor_client.get_all_data_for_patient(all_patients[0]["id"])
pprint(all_data_patient_0)

# select a patient; patient_id is a string

def select_patient(patient_id):
   
    for one_dic in all_patients:
        # index gets '1', item_dict gets the rest
        if one_dic['id'] == patient_id:
            patient= one_dic
            break
    return patient




# select data for a specific patient; patient_id is a string

def patient_data (patient_id):
    relevant_data = []
    the_patient = select_patient(patient_id)
    all_data = hemodonor_client.get_all_data_for_patient(the_patient['id'])
    
    for index in all_data:
        if index['resource'].get('id', {}).endswith('heartrate' ):
            relevant_data.append(index)
        if index['resource'].get('id', {}).endswith('weight' ):
            relevant_data.append(index)
        if index['resource'].get('id', {}).endswith('bp' ):
            relevant_data.append(index)
        if index['resource'].get('id', {}).endswith('systolic' ):
            relevant_data.append(index)
        if index['resource'].get('id', {}).endswith('diastolic' ):
            relevant_data.append(index)
        if index['resource'].get('id', {}).endswith('oxygen_saturation' ):
            relevant_data.append(index)
        if index['resource'].get('id', {}).endswith('lab' ) :
            lab = index['resource']
            if lab.get('code', {}).get('text') == 'Hgb Bld-mCnc':         
                relevant_data.append(index)
                
    return relevant_data       
        
my_data = [patient_data(patients_id[i]) for i in range(len(patients_id))]