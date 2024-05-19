# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith',"Fatigue", 20, '07012345678','B1 234'), Patient('Mike','Jones',"Fatigue", 37,'07555551234','L2 2AB'), Patient('Daivd','Smith',"Nausea", 15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            print("You have now logged in. Welcome!")
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- view/discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign People')
        print(' 5- Update admin detais')
        print(' 6- Group patient by family')
        print(' 7- Patient Records')
        print(' 8- Manage Report')
        print(' 9- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            print('Choose the operation: ')
            print("1- View Patients")
            print("2- Discharge Patients")
            select = input("Option: ")
            
            if select == '1':
                admin.view_patient(patients)
            elif select == '2':
                admin.view_patient(patients)
                while True:
                    op = input('Do you want to discharge a patient(Y/N):').lower()

                    if op == 'yes' or op == 'y':
                        #ToDo3
                        admin.discharge(patients, discharged_patients)
                        break

                    elif op == 'no' or op == 'n':
                        break

                    # unexpected entry
                    else:
                        print('Please answer by yes or no.')
            else:
                print("'Invalid Option: Try Again!'")
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            print('Choose the operation')
            print('1- Assign doctor to a patient')
            print('2- Assign patient to a doctor')
            select = input('option: ')
            print()
            
            if select == '1':
                # 1- Assign doctor to a patient
                admin.assign_doctor_to_patient(patients, doctors)
            elif select == '2':
                admin.relocate_patients(patients, doctors)
            else:
                print('Invalid Option: Try Again!')
        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            # 6 - Group patients by family
            admin.link_by_family(patients)
            
        elif op == '7':
            print('Choose the operation:')
            print('1- Store Records')
            print('2- load Records')
            
            select = input('option: ')
            print()
                        
            if select == '1':
                admin.store_patients_data(patients, 'patients_records.txt')
            elif select == '2':
                admin.load_patients_data('patients_records.txt')
            else:
                print('Invalid Option: Try Again!')
        
        elif op == '8':
            # 8 - manage report
            print("Choose the operation:")
            print('1-Block View')
            print('2-Diagram View')
            select = input('option: ')
            print()
            
            if select == '1':
                print("------Block View------")
                print('1-Total number of Doctors')
                print('2-Total number of patients per doctors ')
                print('3-Monthly appointments per doctor')
                print('4-Total number of patients based on illness type ')
                print()
                select = input('Input: ')
                
                if select == '1':
                    admin.total_doc(doctors)
                    
                elif select == '2':
                    admin.patients_per_doctor_total(doctors)
                    
                elif select == '3':
                    admin.monthly_appo(doctors)
                    
                elif select == '4':
                    admin.type_illness(patients)
                    
                else:
                    print("Invalid Option: Try Again!")
            elif select == '2':
                admin.manage_report(patients, doctors)
            else:
                print('Invalid Option: Try Again!')
            
        elif op == '9':
            # 9 - Quit
            #ToDo5
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()


# make the delete print out of the range

