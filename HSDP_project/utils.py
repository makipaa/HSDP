from datetime import date


def calculate_age(birth_date):
    birth_date = date.fromisoformat(birth_date)
    current_time = date.today()
    return current_time.year - birth_date.year - ((current_time.month, current_time.day) < (birth_date.month, birth_date.day))


def condition(weight, diastolic, systolic, hemoglobin, gender, age):
    if age >= 17:
        if weight >= 50:
            if systolic <= 180 and diastolic >= 50:
                if hemoglobin >= 12.5 <= 20 and gender == 'female':
                    return 'You are eligible to donate!'
                elif hemoglobin >= 13 <= 20 and gender == 'male':
                    return 'You are eligible to donate!'
                else:
                    return 'You are not eligible to donate: The value of your hemoglobin does not allow you to donate your blood.'
            else:
                return 'You are not eligible to donate: The value of your blood pressure does not allow you to donate your blood.'
        else:
            return "You are not eligible to donate: You must weigh more than 50kg to donate your blood."
    else:
        return "You are not eligible to donate: You are not old enough to donate your blood."

def condition_doctor_view(weight, diastolic, systolic, hemoglobin, gender, age):
    if age >= 17:
        if weight >= 50:
            if systolic <= 180 and diastolic >= 50:
                if hemoglobin >= 12.5 <= 20 and gender == 'female':
                    return 'The patient is eligible to donate!'
                elif hemoglobin >= 13 <= 20 and gender == 'male':
                    return 'The patient is eligible to donate!'
                else:
                    return 'The patient is not eligible to donate: the value of the hemoglobin does not allow you to donate your blood.'
            else:
                return 'The patient is not eligible to donate: the value of your blood pressure does not allow you to donate your blood.'
        else:
            return "The patient is not eligible to donate: the patient must weigh more than 50kg to donate your blood."
    else:
        return "The patient is not eligible to donate: You are not old enough to donate your blood."
