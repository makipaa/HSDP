from datetime import date


def calculate_age(birth_date):
    birth_date = date.fromisoformat(birth_date)
    current_time = date.today()
    return current_time.year - birth_date.year - ((current_time.month, current_time.day) < (birth_date.month, birth_date.day))


def condition(user, weight, diastolic, systolic, hemoglobin, gender, age):
    prefixes = ['You are', 'your', 'you']

    if user == 'doctor':
        prefixes = ['The patient is', 'the patients', 'the patient']

    if weight == 'No data' or diastolic == 'No data' or systolic == 'No data' or hemoglobin == 'No data' or gender == 'No data' or age == 'No data':
        return 'Not enough data to determine eligibility.'
    if age >= 17:
        if weight >= 50:
            if systolic <= 180 and diastolic >= 50:
                if hemoglobin >= 12.5 <= 20 and gender == 'female':
                    #return 'You are eligible to donate!'
                    return f'{prefixes[0]} eligible to donate!'
                elif hemoglobin >= 13 <= 20 and gender == 'male':
                    #return 'You are eligible to donate!'
                    return f'{prefixes[0]} eligible to donate!'
                else:
                    #return 'You are not eligible to donate: The value of your hemoglobin does not allow you to donate your blood.'
                    return f'{prefixes[0]} not eligible to donate: The value of {prefixes[1]} hemoglobin does not allow {prefixes[2]} to donate blood.'
            else:
                #return 'You are not eligible to donate: The value of your blood pressure does not allow you to donate your blood.'
                return f'{prefixes[0]} not eligible to donate: The value of {prefixes[1]} blood pressure does not allow {prefixes[2]} to donate blood.'
        else:
            #return "You are not eligible to donate: You must weigh more than 50kg to donate your blood."
            return f'{prefixes[0]} not eligible to donate: {prefixes[2]} must weigh more than 50kg to donate blood.'
    else:
        #return "You are not eligible to donate: You are not old enough to donate your blood."
        return f'{prefixes[0]} not eligible to donate: {prefixes[0]} not old enough to donate blood.'
