import requests
from utils import calculate_age


class hemodonor_FHIR_client(object):
    def __init__(self, server_url, server_user, server_password):
        self.server_url = server_url
        self.server_user = server_user
        self.server_password = server_password
        self.all_patients = self.get_all_patients()
        
    
   
    def get_all_patients(self):
        requesturl = self.server_url + "/Patient?_format=json"
        entries = self._get_json(requesturl)["entry"]
        return [entry["resource"] for entry in entries]

   
    def get_all_data_for_patient(self, patient_id):
        requesturl = self.server_url + "/Patient/" + \
            patient_id + "$everything?_format=json"
        return self._get_json(requesturl)["entry"]
    
    def _get_json(self, requesturl):
        response = requests.get(requesturl,
                                auth=(self.server_user, self.server_password))
        response.raise_for_status()
        result = response.json()
        return result
    
    # Get relevant data for the patient
    def get_relevant_data(self, patient_id):

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
        patients = self.all_patients
        for patient in patients:
            if patient.get('id', {}) == patient_id:
                data['gender'] = patient['gender']
                birth_date = patient['birthDate']

        age = calculate_age(birth_date)
        data['age'] = age
        
        # Fetch medical data
        all_data = self.get_all_data_for_patient(patient_id)
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
        
    def get_latest_measurements(self, patient_id):
        latest_data = {
            'weight' : '',
            'systolic' : '',
            'diastolic' : '',
            'oxygen_saturation' : '',
            'hemoglobin' : ''
        }
        all_data = self.get_relevant_data(patient_id)
        for key, item in all_data.items():
            # Check if there are any measurements
            if not item:
                latest_data[key] = 'No data'
            elif key == 'gender' or key == 'age':
                latest_data[key] = item
            else:
                latest_data[key] = item[0]
        return latest_data
    
    def get_measurement(self, patient_id,measurement):
        all_data = self.get_relevant_data(patient_id)
        return all_data[measurement]

hemodonor_client = hemodonor_FHIR_client(
    server_url="http://tutsgnfhir.com",
    server_user="tutfhir",
    server_password="tutfhir1"
)