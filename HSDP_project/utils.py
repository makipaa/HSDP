#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import fhir_client
from datetime import date



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

def calculate_age(birth_date):
    current_time = date.today()
    return current_time.year - birth_date.year - ((current_time.month, current_time.day) < (birth_date.month, birth_date.day))

# select a patient; patient_id is a string
def select_patient(patient_id):
   
    for one_dic in all_patients:
        # index gets '1', item_dict gets the rest
        if one_dic['id'] == patient_id:
            patient= one_dic
            break
    return patient

 
        
# Get relevant data for the patient
def get_relevant_data(patient_id):

    data = {
        'weight' : [],
        'systolic' : [],
        'diastolic' : [],
        'oxygen_saturation' : [],
        'hemoglobin' : [],
        'gender' : '',
        'age' : ''
    }
    birth_date = ''
    # Fetch gender and age
    patients = hemodonor_client.get_all_patients()
    for patient in patients:
        if patient.get('id', {}) == patient_id:
            data['gender'] = patient['gender']
            birth_date = patient['birthDate']

    age = calculate_age(date.fromisoformat(birth_date))
    data['age'] = age

    # Fetch medical data
    all_data = hemodonor_client.get_all_data_for_patient(patient_id)
    for index in all_data:
            resource = index['resource']
            if resource.get('id', {}).endswith('weight'):
                data['weight'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('systolic'):
                data['systolic'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('diastolic'):
                data['diastolic'].append(resource['valueQuantity']['value'])
            
            elif resource.get('id', {}).endswith('oxygen_saturation'):
                data['oxygen_saturation'].append(resource['valueQuantity']['value'])

            elif resource.get('id', {}).endswith('lab'):
                lab = index['resource']
                if lab.get('code', {}).get('text') == 'Hgb Bld-mCnc':         
                    data['hemoglobin'].append(resource['valueQuantity']['value'])

    return data


def get_latest_measurements(patient_id):
    latest_data = {
        'heart_rate' : '',
        'weight' : '',
        'bp' : '',
        'systolic' : '',
        'diastolic' : '',
        'oxygen_saturation' : '',
        'hemoglobin' : '',
        'gender' : '',
        'age' : ''
    }
    all_data = get_relevant_data(patient_id)
    for key, item in all_data.items():
        # Check if there are any measurements
        if len(item) != 0:
            # Take the most recent measurement
            latest_data[key] = item[0]

        return latest_data
