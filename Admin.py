import matplotlib.pyplot as plt
from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def  view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        return self.__username == username and self.__password == password
    
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        speciality = input("Enter the Speciality: ")
        
        
        return first_name, surname, speciality
    
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input("Input: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()
            
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')   
                    #ToDo5
                    break # save time and end the loop

            #ToDo6
            doctors.append(Doctor(first_name, surname, speciality ))# add the doctor ...
                                                         # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8
            if op == 1:
                new_first_name = input("Enter the new first name: ")
                doctors[index].set_first_name(new_first_name)
                
            elif op == 2:
                new_surname = input("Enter the new surname: ")
                doctors[index].set_surname(new_surname)
                
            elif op == 3:
                new_speciality = input("Enter the new speciality: ")
                doctors[index].set_speciality(new_speciality)

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9
            doctor_index = int(doctor_index)
            
            if doctor_index in range(1, doctor_index+1):
                del doctors[doctor_index-1]
                return
            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                print(patients[patient_index].get_doctor())
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        #ToDo12
        try:
            # patient_index is the patient ID minus one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

            # Move patient to the discharged list
            discharge_patients.append(patients.pop(patient_index))
            print('Patient discharged successfully.')

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            if username == input('Enter the new username again: '):
                self.__username = username
            print('Username has been updated successfully!')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
            print("Password has been updated  successfully.")

        elif op == 3:
            #ToDo15
            address = input('Enter the new address: ')
            if address == input('Enter the new address again: '):
                self.__password = address
            print("Address has been updated successfully")    
            
        else:
            #ToDo16
            print('Invalid operation choosen. Check your spelling!')

    def link_by_family(self,patients):
        
        family_groups = {}  # Dictionary to hold patients grouped by family name

        for patient in patients:
            surname = patient.get_surname()  # Using the get_surname method to get the surname
            if surname not in family_groups:
                family_groups[surname] = [patient]
            else:
                family_groups[surname].append(patient)

        for surname, family_members in family_groups.items():
            print(f"Family: {surname}")
            print()
            print('          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            print()
            for member in family_members:
                print(member)  # Assuming there's a method in the Patient class to print patient details  
            print()
    
    def store_patients_data(self,patients,filename):
        with open (filename,'w') as file:
            for patient in patients:
                file.write(f"{patient.get_first_name()},{patient.get_surname()},{patient.get_symptoms()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.get_doctor()}\n")
        print("Patients  data stored successfully.")
    
    def load_patients_data(self, filename):
        with open (filename, 'r') as file:
            patient = []
            for line in file:
                if line[-1] == '\n':
                    patient.append(line[:-1])
            
                else:
                    patient.append(line)
        print(patient)
        
        print()        
         
        print("Patient Records has been loaded from file")
    
    def relocate_patients(self,patients, doctors):
        
        print('-----Relocate  Patients------')
        print("Select the patient to relocate:")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        
        patient_index = input('Enter the ID of the patient: ')
        
        try:
            patient_index = int(patient_index)- 1
            
            if patient_index not in range(len(patients)):
                print('Invalid Patient ID.')
                return
            
            print('Select the doctor who will take care of this patient:')
            print('ID |          Full Name           |  Speciality   ')
            self.view(doctors)
            
            doctor_index = input('Enter the ID of the doctor: ')
            
            try: 
                doctor_index = int(doctor_index)-1
                
                if doctor_index not in range(len(doctors)):
                    print('Invalid Patient ID.')
                    return
                
                patient = patients[patient_index]
                doctor = doctors[doctor_index]
                
                patient.link(doctor.full_name())
                doctor.add_patient(patient.full_name())
                
                print(f"Patient {patient.full_name()} relocated successfully to {doctor.full_name()}.")

            except ValueError:
                print('Invalid doctor ID.')

        except ValueError:
            print('Invalid patient ID.')
    
    
    def total_doc(self, doctors):
        
        print("Management Report:")     
        # total number of doctors
        total_doctors =  len(doctors)
        
        print(f"Total number of doctors in the system: {total_doctors}")
        
    def patients_per_doctor_total(self, doctors):
        
        print("Total number of patients per doctor: ")
        for doctor in doctors:
            print(f"{doctor.full_name()}: {len(doctor.get_patient())} patients")
            
    def monthly_appo(self, doctors):
        
        print("Monthly appointments per doctor")
        
        
        for doctor in doctors:
            print(doctor.full_name())
            appointments = doctor.get_appointments()
            for month, appointment in appointments.items():
                print(f"{month}: {len(appointment)} patients")
                
    def type_illness(self, patients):
        
        print("\nTotal number of patients based on the illness type: ")
        symptoms_per_patient = {}   
        for patient in patients:
            symptom = patient.get_symptoms()
            # print(symptoms)
            
            
            if symptom not in symptoms_per_patient:
                symptoms_per_patient[symptom] = 1
                
            else:
                symptoms_per_patient[symptom] += 1
                    
        for symptom,patient_no in symptoms_per_patient.items():
            print(f"{symptom}: {patient_no} patients")
            
            
            
    def manage_report(self, patients, doctors):
        print("Management Report:")     
        # Total number of doctors
        total_doctors = len(doctors)
        print(f"Total number of doctors in the system: {total_doctors}")

        # Total number of patients per doctor
        doctor_names = [doctor.full_name() for doctor in doctors]
        patients_count = [len(doctor.get_patient()) for doctor in doctors]
        self.plot_bar(doctor_names, patients_count, "Doctors", "Number of Patients", "Total number of patients per doctor")

        # Monthly appointments per doctor
        appointments_data = {}
        for doctor in doctors:
            doctor_name = doctor.full_name()
            appointments = doctor.get_appointments()
            for month, appointment in appointments.items():
                if doctor_name not in appointments_data:
                    appointments_data[doctor_name] = {}
                if month not in appointments_data[doctor_name]:
                    appointments_data[doctor_name][month] = 0
                appointments_data[doctor_name][month] += len(appointment)

        for doctor, data in appointments_data.items():
            months = list(data.keys())
            appointments = list(data.values())
            self.plot_bar(months, appointments, "Months", "Number of Appointments", f"Monthly appointments for {doctor}")

        # Total number of patients based on the illness type
        symptoms_per_patient = {}
        for patient in patients:
            symptom = patient.get_symptoms()
            if symptom not in symptoms_per_patient:
                symptoms_per_patient[symptom] = 1
            else:
                symptoms_per_patient[symptom] += 1

        symptoms = list(symptoms_per_patient.keys())
        patients_count = list(symptoms_per_patient.values())
        self.plot_pie(symptoms, patients_count, "Patients Based on Illness Type")

    def plot_bar(self, x_data, y_data, xlabel, ylabel, title):
        plt.bar(x_data, y_data)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.show()

    def plot_pie(self, labels, sizes, title):
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.axis('equal')
        plt.show()
            

