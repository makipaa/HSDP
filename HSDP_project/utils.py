#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import config
import fhir_client

current_user = None

def validate_user(username, password):
    if (username == config.DONOR["username"]) & (password == config.DONOR["password"]):
        current_user = config.DONOR
        config.DONOR["logged_in"] = True
        return "donor"
    elif (username == config.DOCTOR["username"]) & (password == config.DOCTOR["password"]):
        current_user = config.DOCTOR
        config.DOCTOR["logged_in"] = True
        return "doctor"
    else:
        return None


"""
hemodonor_client = fhir_client.SimpleFHIRClient(
    server_url="http://tutsgnfhir.com",
    server_user="tutfhir",
    server_password="tutfhir1")
all_patients = hemodonor_client.get_all_patients()


patients_id = []

for patient_record in all_patients:
    patient_id = patient_record["id"]
    patients_id.append(patient_id)
    patient_given = patient_record["name"][0]["given"][0]
    patient_family = patient_record["name"][0]["family"][0]

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

# Useful data for hemodonor application

hemodonor_data = []
for data in my_data:
    if len(data) != 0:
        hemodonor_data.append(data)
    else:
        pass
"""