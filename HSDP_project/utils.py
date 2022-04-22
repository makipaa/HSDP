#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import fhir_client




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

 
        
# this is the exact same function as before but simply collects the recods in separate lists according to the 
# type of record 

def patient_data_organized (patient_id):

    data = {
        'heart_rate' : [],
        'weight' : [],
        'bp' : [],
        'systolic' : [],
        'diastolic' : [],
        'oxygen_saturation' : [],
        'hemoglobin' : []
    }

    all_data = hemodonor_client.get_all_data_for_patient(patient_id)
    for index in all_data:
            resource = index['resource']
            if resource.get('id', {}).endswith('heartrate'):
                data['heart_rate'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('weight'):
                data['weight'].append(resource['valueQuantity']['value'])
            
            #if resource.get('id', {}).endswith('bp'):
               # data['bp'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('systolic'):
                data['systolic'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('diastolic'):
                data['diastolic'].append(resource['valueQuantity']['value'])
            
            elif resource.get('id', {}).endswith('oxygen_saturation'):
                data['oxygen_saturation'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('lab') :
                lab = index['resource']
                if lab.get('code', {}).get('text') == 'Hgb Bld-mCnc':         
                    data['hemoglobin'].append(resource['valueQuantity']['value'])

    return data



