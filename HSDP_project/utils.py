#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import config
import fhir_client



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


# this is the exact same function as before but simply collects the recods in separate lists according to the 
# type of record 

def patient_data_organized (patient_id):
    heartrate_data =[]
    weight_data =[]
    bp_data =[]
    systolic_data =[]
    diastolic_data =[]
    oxigen_saturation =[]
    emoglobin_data =[]
    the_patient = select_patient(patient_id)
    all_data = hemodonor_client.get_all_data_for_patient(the_patient.get('id'))
    for index in all_data:
            if index['resource'].get('id', {}).endswith('heartrate' ):
                heartrate_data.append(index)
            if index['resource'].get('id', {}).endswith('weight' ):
                weight_data.append(index)
            if index['resource'].get('id', {}).endswith('bp' ):
                bp_data.append(index)
            if index['resource'].get('id', {}).endswith('systolic' ):
                systolic_data.append(index)
            if index['resource'].get('id', {}).endswith('diastolic' ):
                diastolic_data.append(index)
            if index['resource'].get('id', {}).endswith('oxygen_saturation' ):
                oxigen_saturation.append(index)
            if index['resource'].get('id', {}).endswith('lab' ) :
                lab = index['resource']
                if lab.get('code', {}).get('text') == 'Hgb Bld-mCnc':         
                    emoglobin_data.append(index) 
    relevant_data=[*heartrate_data, *weight_data, *bp_data, *systolic_data, *diastolic_data, *oxigen_saturation, *emoglobin_data]    
    if len(relevant_data)==0:
        print('No relevant data for patient {}'.format(patient_id))
        return 0,0,0,0,0,0,0  #this is just random values I put to make it work even when there's no data to return
    elif len(heartrate_data)==0 or len(weight_data)==0 or len(bp_data)==0 or len(systolic_data)==0 or len(diastolic_data)==0 or len(oxigen_saturation)==0 or len(emoglobin_data)==0:
        print( 'Informations missing for patient : {}'.format(patient_id))
        return 0,0,0,0,0,0,0 #this is just random values I put to make it work even when there's no enough data to conduct the analysis of eligibility of that patient
    else :
        return heartrate_data, weight_data, bp_data, systolic_data ,diastolic_data, oxigen_saturation, emoglobin_data 