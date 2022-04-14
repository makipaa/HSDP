# Weight, Hemoglobin level (male and female), donation interval, blood pressure and Age

def condition(donation_interval, age, weight, blood_pressure, hemoglobin, gender):
    if donation_interval >= 8 and age >= 17:
        if weight >= 50:
            if blood_pressure >=50 <= 180:
                if hemoglobin >= 12.5 <= 20 and gender == 'female':
                    print('You are eligible to donate')
                elif hemoglobin >= 13 <= 20 and gender == 'male':
                    print('You are eligible to donate')
                else:
                    print('Not eligible')
            else:
                print('Not eligible: your blood pressure is not within the acceptable limits 50-180mmHg')
        else:
            print('Not eligible: You must weigh above 50kg')
    else:
        print('Not eligible: Your last blood donation should be at least 8 weeks ago and you must be atleast 17yo')
