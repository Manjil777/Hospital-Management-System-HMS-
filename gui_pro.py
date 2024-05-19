from tkinter import*
from tkinter  import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()

root.title("Hospital Management System")
root.geometry('340x440')
root.configure(bg='#333333')

doctors = [
    {"name": "John Smith", "speciality": "Internal Med."},
    {"name": "Jane Smith", "speciality": "Pediatrics"},
    {"name": "Jane Carlos", "speciality": "Cardiology"}
]

def main_system():
  system = Tk()
  system.title("Main System")
  menu_frame = Frame(system)
  menu_frame.pack(expand=True)
  menu_frame.configure(bg='#333333')


    # Create buttons for each operation
  operations = [
        ("Register/view/update/delete doctor", doctor_management),
        ("Discharge patients", discharge),
        ("View discharged patient", view_discharge),
        ("Assign people", assign_people),
        ("Update admin details", update_details),
        ("Group patient by family", group_patient_data),
        ("Patient Records", record_patient),
        ("Manage Report", manage_report),
        ("Quit", quit_system)
    ]

    # Calculate number of rows and columns
  num_rows = (len(operations) + 1) // 2  # Add 1 for the Quit button
  num_columns = 2

    # Create and place buttons
  for i, (text, command) in enumerate(operations):
        button = Button(
            menu_frame, text=text, font=("Arial", 12), command=command,
            bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5,
            relief=RIDGE, borderwidth=3, width=30
        )

        row = i // num_columns
        column = i % num_columns
        button.grid(row=row, column=column, padx=5, pady=5)

def doctor_management():
    # Create a new window
    doctor_window = Toplevel()
    doctor_window.title("Doctor Management")
    doctor_window.geometry('400x300')
    doctor_window.configure(bg='#333333')

    doctor_frame = Frame(doctor_window, bg='#333333')
    doctor_frame.pack(expand=True)

    # Create buttons for each doctor operation
    operations = [
        ("Register Doctor", register_doctor),
        ("View Doctors", view_doctors),
        ("Update Doctor", update_doctor),
        ("Delete Doctor", delete_doctor)
    ]

    # Calculate number of rows and columns for button placement
    num_rows = len(operations)
    num_columns = 1

    # Create and place buttons
    for i, (text, command) in enumerate(operations):
        button = Button(
            doctor_frame, text=text, font=("Arial", 12), command=command,
            bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5,
            relief=RIDGE, borderwidth=3, width=30
        )

        row = i
        column = 0
        button.grid(row=row, column=column, padx=5, pady=5)
        
    back_button = Button(
        doctor_frame, text="Back to Main Menu", font=("Arial", 12), command=doctor_window.destroy,
        bg="#ff3399", fg="white", bd=0, padx=10, pady=5,
        relief=RIDGE, borderwidth=3, width=30
    )
    back_button.grid(row=num_rows, column=0, padx=5, pady=5)
        
def register_doctor():
    register_window = Toplevel()
    register_window.title("Register Doctor")
    register_window.geometry('300x200')
    register_window.configure(bg='#333333')

    register_frame = Frame(register_window, bg='#333333')
    register_frame.pack(expand=True)

    title_label = Label(register_frame, text="Register Doctor", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    first_name_label = Label(register_frame, text="First Name", fg="#ffffff", bg="#333333", font='Arial,12')
    first_name_label.grid(row=1, column=0)
    first_name_entry = Entry(register_frame)
    first_name_entry.grid(row=1, column=1, pady=10)

    surname_label = Label(register_frame, text="Surname", fg="#ffffff", bg="#333333", font='Arial,12')
    surname_label.grid(row=2, column=0)
    surname_entry = Entry(register_frame)
    surname_entry.grid(row=2, column=1, pady=10)

    speciality_label = Label(register_frame, text="Speciality", fg="#ffffff", bg="#333333", font='Arial,12')
    speciality_label.grid(row=3, column=0)
    speciality_entry = Entry(register_frame)
    speciality_entry.grid(row=3, column=1, pady=10)

    def add_doctor():
        first_name = first_name_entry.get()
        surname = surname_entry.get()
        speciality = speciality_entry.get()

        if first_name and surname and speciality:
            doctor = {"name": f"{first_name} {surname}", "speciality": speciality}
            doctors.append(doctor)
            messagebox.showinfo("Success", "Doctor registered successfully!")
            register_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    register_button = Button(register_frame, text="Register", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=add_doctor)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)


def view_doctors():
    view_window = Toplevel()
    view_window.title("View Doctors")
    view_window.geometry('400x300')
    view_window.configure(bg='#333333')

    view_frame = Frame(view_window, bg='#333333')
    view_frame.pack(expand=True)

    title_label = Label(view_frame, text="List of Doctors", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    id_label = Label(view_frame, text="ID", fg="#ffffff", bg="#333333", font='Arial,12', width=5)
    id_label.grid(row=1, column=0)
    name_label = Label(view_frame, text="Name", fg="#ffffff", bg="#333333", font='Arial,12', width=20)
    name_label.grid(row=1, column=1)
    speciality_label = Label(view_frame, text="Speciality", fg="#ffffff", bg="#333333", font='Arial,12', width=15)
    speciality_label.grid(row=1, column=2)

    def display_doctor_details():
        for i, doctor in enumerate(doctors, start=2):
            id_label = Label(view_frame, text=i-1, fg="#ffffff", bg="#333333", font='Arial,12')
            id_label.grid(row=i, column=0)
            name_label = Label(view_frame, text=doctor["name"], fg="#ffffff", bg="#333333", font='Arial,12')
            name_label.grid(row=i, column=1)
            speciality_label = Label(view_frame, text=doctor["speciality"], fg="#ffffff", bg="#333333", font='Arial,12')
            speciality_label.grid(row=i, column=2)

    display_doctor_details()
    
def update_doctor():
    update_window = Toplevel()
    update_window.title("Update Doctor")
    update_window.geometry('300x200')
    update_window.configure(bg='#333333')

    update_frame = Frame(update_window, bg='#333333')
    update_frame.pack(expand=True)

    title_label = Label(update_frame, text="Update Doctor", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    select_label = Label(update_frame, text="Select Doctor", fg="#ffffff", bg="#333333", font='Arial,12')
    select_label.grid(row=1, column=0)
    select_entry = Entry(update_frame)
    select_entry.grid(row=1, column=1, pady=10)

    first_name_label = Label(update_frame, text="First Name", fg="#ffffff", bg="#333333", font='Arial,12')
    first_name_label.grid(row=2, column=0)
    first_name_entry = Entry(update_frame)
    first_name_entry.grid(row=2, column=1, pady=10)

    surname_label = Label(update_frame, text="Surname", fg="#ffffff", bg="#333333", font='Arial,12')
    surname_label.grid(row=3, column=0)
    surname_entry = Entry(update_frame)
    surname_entry.grid(row=3, column=1, pady=10)

    speciality_label = Label(update_frame, text="Speciality", fg="#ffffff", bg="#333333", font='Arial,12')
    speciality_label.grid(row=4, column=0)
    speciality_entry = Entry(update_frame)
    speciality_entry.grid(row=4, column=1, pady=10)

    def find_doctor():
        index = int(select_entry.get()) - 1
        if 0 <= index < len(doctors):
            doctor = doctors[index]
            first_name_entry.delete(0, END)
            first_name_entry.insert(0, doctor["name"].split()[0])
            surname_entry.delete(0, END)
            surname_entry.insert(0, doctor["name"].split()[1])
            speciality_entry.delete(0, END)
            speciality_entry.insert(0, doctor["speciality"])
        else:
            messagebox.showerror("Error", "Invalid doctor ID.")

    def update_doctor_details():
        index = int(select_entry.get()) - 1
        if 0 <= index < len(doctors):
            first_name = first_name_entry.get()
            surname = surname_entry.get()
            speciality = speciality_entry.get()

            if first_name and surname and speciality:
                doctor = {"name": f"{first_name} {surname}", "speciality": speciality}
                doctors[index] = doctor
                messagebox.showinfo("Success", "Doctor details updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Invalid doctor ID.")

    select_button = Button(update_frame, text="Select", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=find_doctor)
    select_button.grid(row=1, column=2, pady=10)

    update_button = Button(update_frame, text="Update", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=update_doctor_details)
    update_button.grid(row=5, column=0, columnspan=2, pady=10)

def delete_doctor():
    delete_window = Toplevel()
    delete_window.title("Delete Doctor")
    delete_window.geometry('300x200')
    delete_window.configure(bg='#333333')

    delete_frame = Frame(delete_window, bg='#333333')
    delete_frame.pack(expand=True)

    title_label = Label(delete_frame, text="Delete Doctor", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Function to display the list of doctors
    def display_doctors():
        doctors_listbox.delete(0, END)
        for i, doctor in enumerate(doctors, 1):
            doctors_listbox.insert(END, f"{i}. {doctor['name']} - {doctor['speciality']}")

    select_label = Label(delete_frame, text="Select Doctor to Delete:", fg="#ffffff", bg="#333333", font='Arial,12')
    select_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    # Listbox to display doctors
    doctors_listbox = Listbox(delete_frame, bg="#ffffff", fg="#333333", font='Arial,12', selectmode=SINGLE, height=5, width=30)
    doctors_listbox.grid(row=2, column=0, columnspan=2, pady=(0, 5))

    display_doctors()

    def delete_selected_doctor():
        selected_index = doctors_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this doctor?")
            if confirm:
                del doctors[index]
                messagebox.showinfo("Success", "Doctor deleted successfully!")
                display_doctors()
        else:
            messagebox.showerror("Error", "Please select a doctor to delete.")

    delete_button = Button(delete_frame, text="Delete", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=delete_selected_doctor)
    delete_button.grid(row=3, column=0, columnspan=2, pady=10)


discharged_patients = []

def discharge():
 pass



# Function to view discharged patients
def view_discharge():
 pass

def assign_people():
    assign_window = Toplevel()
    assign_window.title("Assign People")
    assign_window.geometry('400x300')
    assign_window.configure(bg='#333333')

    assign_frame = Frame(assign_window, bg='#333333')
    assign_frame.pack(expand=True)

    title_label = Label(assign_frame, text="Assign People", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Function to handle assigning doctor to patient
    def assign_doctor():
        selected_patient = patient_listbox.get(ACTIVE)
        selected_doctor = doctor_listbox.get(ACTIVE)

        for patient in patients:
            if patient["first_name"] == selected_patient.split(" ")[0] and patient["surname"] == selected_patient.split(" ")[1]:
                patient["assigned_doctor"] = selected_doctor
                messagebox.showinfo("Success", f"{selected_doctor} has been assigned to {selected_patient}")
                break

    # Function to handle changing assigned doctor
    def change_doctor():
        selected_patient = patient_listbox.get(ACTIVE)
        selected_doctor = doctor_listbox.get(ACTIVE)

        for patient in patients:
            if patient["first_name"] == selected_patient.split(" ")[0] and patient["surname"] == selected_patient.split(" ")[1]:
                patient["assigned_doctor"] = selected_doctor
                messagebox.showinfo("Success", f"{selected_patient}'s doctor has been changed to {selected_doctor}")
                break

    patient_label = Label(assign_frame, text="Patients", fg="#ffffff", bg="#333333", font='Arial,12')
    patient_label.grid(row=1, column=0, padx=10, pady=5)

    doctor_label = Label(assign_frame, text="Doctors", fg="#ffffff", bg="#333333", font='Arial,12')
    doctor_label.grid(row=1, column=1, padx=10, pady=5)

    patient_listbox = Listbox(assign_frame, selectmode=SINGLE, bg="#cccccc", fg="#333333", font='Arial,12')
    patient_listbox.grid(row=2, column=0, padx=10, pady=5)

    doctor_listbox = Listbox(assign_frame, selectmode=SINGLE, bg="#cccccc", fg="#333333", font='Arial,12')
    doctor_listbox.grid(row=2, column=1, padx=10, pady=5)

    for patient in patients:
        patient_listbox.insert(END, f"{patient['first_name']} {patient['surname']}")

    for doctor in doctors:
        doctor_listbox.insert(END, doctor)

    assign_button = Button(assign_frame, text="Assign Doctor", bg='#ff3399', fg='#fff', font='Arial,12', command=assign_doctor)
    assign_button.grid(row=3, column=0, padx=10, pady=10)

    change_button = Button(assign_frame, text="Change Doctor", bg='#ff3399', fg='#fff', font='Arial,12', command=change_doctor)
    change_button.grid(row=3, column=1, padx=10, pady=10)

admin_details = {"username": "admin", "password": "password123"}

def update_details():
    update_window = Toplevel()
    update_window.title("Update Admin Details")
    update_window.geometry('300x200')
    update_window.configure(bg='#333333')

    update_frame = Frame(update_window, bg='#333333')
    update_frame.pack(expand=True)

    title_label = Label(update_frame, text="Update Admin Details", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Labels and entry widgets for username and password
    username_label = Label(update_frame, text="Username:", fg="#ffffff", bg="#333333", font='Arial,12')
    username_label.grid(row=1, column=0, pady=5, sticky='e')
    username_entry = Entry(update_frame, bg="#ffffff", fg="#333333", font='Arial,12')
    username_entry.grid(row=1, column=1, pady=5)

    password_label = Label(update_frame, text="Password:", fg="#ffffff", bg="#333333", font='Arial,12')
    password_label.grid(row=2, column=0, pady=5, sticky='e')
    password_entry = Entry(update_frame, bg="#ffffff", fg="#333333", font='Arial,12', show='*')
    password_entry.grid(row=2, column=1, pady=5)

    def update_details():
        new_username = username_entry.get()
        new_password = password_entry.get()

        if new_username.strip() and new_password.strip():
            admin_details['username'] = new_username
            admin_details['password'] = new_password
            messagebox.showinfo("Success", "Admin details updated successfully!")
        else:
            messagebox.showerror("Error", "Please fill in both username and password fields.")

    update_button = Button(update_frame, text="Update Details", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=update_details)
    update_button.grid(row=3, column=0, columnspan=2, pady=10)


patients = [
        {"first_name": "Sara", "surname": "Smith", "symptoms": "Fatigue", "age": 20, "number": "07012345678", "address": "B1 234"},
        {"first_name": "Mike", "surname": "Jones", "symptoms": "Fatigue", "age": 37, "number": "07555551234", "address": "L2 2AB"},
        {"first_name": "David", "surname": "Smith", "symptoms": "Nausea", "age": 15, "number": "07123456789", "address": "C1 ABC"}
    ]
# Function to group patient data
def group_patient_data():
    group_patient_window = Toplevel()
    group_patient_window.title("Group Patient Data")
    group_patient_window.geometry('400x300')
    group_patient_window.configure(bg='#333333')

    group_patient_frame = Frame(group_patient_window, bg='#333333')
    group_patient_frame.pack(expand=True)

    title_label = Label(group_patient_frame, text="Group Patient Data", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Function to handle grouping patient data
    def group_data():
        family_groups = {}  # Dictionary to hold patients grouped by family name

        for patient in patients:
            surname = patient["surname"]
            if surname not in family_groups:
                family_groups[surname] = [patient]
            else:
                family_groups[surname].append(patient)

        # Displaying grouped patient data
        row_counter = 2
        for surname, family_members in family_groups.items():
            family_label = Label(group_patient_frame, text=f"Family: {surname}", fg="#ffffff", bg="#333333", font='Arial,12')
            family_label.grid(row=row_counter, column=0, columnspan=2, padx=10, pady=5)
            row_counter += 1

            for member in family_members:
                member_label = Label(group_patient_frame, text=f"{member['first_name']} (Age: {member['age']})", fg="#ffffff", bg="#333333", font='Arial,10')
                member_label.grid(row=row_counter, column=0, columnspan=2, padx=10, pady=2)
                row_counter += 1

    group_button = Button(group_patient_frame, text="Group Data", bg='#ff3399', fg='#fff', font='Arial,12', command=group_data)
    group_button.grid(row=1, column=0, columnspan=2, pady=20)

def record_patient():
    def store_records():
        # Get patient details from the input fields
        first_name = first_name_entry.get()
        surname = surname_entry.get()
        age = age_entry.get()
        mobile = mobile_entry.get()
        postcode = postcode_entry.get()

        # Check if any field is empty
        if not all([first_name, surname, age, mobile, postcode]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Store the patient record in the text file
        with open('patients_records.txt', 'a') as file:
            file.write(f"{first_name},{surname},{age},{mobile},{postcode}\n")
        
        messagebox.showinfo("Success", "Patient record has been stored.")

    def load_records():
        # Clear existing patient records
        patient_list.delete(0, END)

        try:
            # Load patient records from the text file
            with open('patients_records.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    patient_list.insert(END, f"Name: {data[0]} {data[1]}, Age: {data[2]}, Mobile: {data[3]}, Postcode: {data[4]}")
        except FileNotFoundError:
            messagebox.showerror("Error", "File patients_records.txt not found.")

    # Create a new window for recording patient details
    record_window = Toplevel()
    record_window.title("Record Patient")
    record_window.geometry('400x300')
    record_window.configure(bg='#333333')

    # Frame to contain input fields
    input_frame = Frame(record_window, bg='#333333')
    input_frame.pack(pady=20)

    # Labels and Entry widgets for patient details
    first_name_label = Label(input_frame, text="First Name:", fg="#ffffff", bg="#333333", font='Arial,12')
    first_name_label.grid(row=0, column=0, padx=10, pady=5)
    first_name_entry = Entry(input_frame)
    first_name_entry.grid(row=0, column=1, padx=10, pady=5)

    surname_label = Label(input_frame, text="Surname:", fg="#ffffff", bg="#333333", font='Arial,12')
    surname_label.grid(row=1, column=0, padx=10, pady=5)
    surname_entry = Entry(input_frame)
    surname_entry.grid(row=1, column=1, padx=10, pady=5)

    age_label = Label(input_frame, text="Age:", fg="#ffffff", bg="#333333", font='Arial,12')
    age_label.grid(row=2, column=0, padx=10, pady=5)
    age_entry = Entry(input_frame)
    age_entry.grid(row=2, column=1, padx=10, pady=5)

    mobile_label = Label(input_frame, text="Mobile:", fg="#ffffff", bg="#333333", font='Arial,12')
    mobile_label.grid(row=3, column=0, padx=10, pady=5)
    mobile_entry = Entry(input_frame)
    mobile_entry.grid(row=3, column=1, padx=10, pady=5)

    postcode_label = Label(input_frame, text="Postcode:", fg="#ffffff", bg="#333333", font='Arial,12')
    postcode_label.grid(row=4, column=0, padx=10, pady=5)
    postcode_entry = Entry(input_frame)
    postcode_entry.grid(row=4, column=1, padx=10, pady=5)

    # Button to store patient record
    store_button = Button(record_window, text="Store Record", bg='#ff3399', fg='#fff', padx=10, pady=5, font='Arial,12', command=store_records)
    store_button.pack(pady=10)

    # Button to load patient records
    load_button = Button(record_window, text="Load Records", bg='#2E8BC0', fg='#fff', padx=10, pady=5, font='Arial,12', command=load_records)
    load_button.pack(pady=5)

    # Listbox to display patient records
    patient_list = Listbox(record_window, width=50, height=10, bg="#cccccc", fg="#333333", font='Arial,12')
    patient_list.pack(pady=10)

def manage_report():
  pass


def  quit_system():
  root.quit()
        

def login():
    if username_entry.get() == 'admin' and password_entry.get() == '123':
      messagebox.showinfo(title="Login Successful", message="Welcome to the Hospital Management System!")
      root.withdraw()
      main_system() 
      
    else:
      messagebox.showinfo(title='Error', message=f"Username or Password is incorrect.\nPlease try again.")

frame = Frame(bg='#333333')

# creating Widgets
login_label = Label(frame, text="Login", fg="#ffffff", bg="#333333", font='Arial,30')
username_label = Label(frame, text="Username", bg='#333333', fg='#fff', font='Arial,16')
username_entry = Entry(frame)
password_label = Label(frame, text="Password", fg="#fff", bg='#333333', font='Arial,16')
password_entry = Entry(frame, show='*')
login_button = Button(frame, text="Log In", bg='#ff3399', fg='#fff',padx=10,pady=0, font='Arial,16', command=login)

# placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()  # Add this line to associate the frame with the root window

root.mainloop()
