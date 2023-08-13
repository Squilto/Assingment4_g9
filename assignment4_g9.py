from typing import Any


class Doctor:
    def __init__(self, doctor_id = "", name = "", specialization = "", working_time = "", qualification = "", room_num = ""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_num = room_num

    def __get_doctor_id__(self):
        return self.doctor_id
    
    def __set_doctor_id__(self, new_id):
        self.doctor_id = new_id

    def __get_doctor_name__(self):
        return self.name
    
    def __set_doctor_name__(self, new_name):
        self.name = new_name
    
    def __get_doctor_sepcialization__(self):
        return self.specialization
    
    def __set_doctor_specialization__(self, new_specialization):
        self.specialization = new_specialization

    def __get_doctor_working_time__(self):
        return self.working_time
    
    def __set_doctor_working_time__(self, new_working_time):
        self.working_time = new_working_time

    def __get_doctor_qualification__(self):
        return self.qualification
    
    def __set_doctor_qualification__(self, new_qualification):
        self.qualification = new_qualification

    def __get_doctor_room_num__(self):
        return self.room_num
    
    def __set_doctor_room_num__(self, new_room_num):
        self.room_num = new_room_num

    def __str__(self):
        result = (self.__get_doctor_id__ + "_" + self.__get_doctor_name__ + "_" + self.__get_doctor_qualification__ +
                   "_" + self.__get_doctor_room_num__ + "_" + self.__get_doctor_sepcialization__ + "_" + self.__get_doctor_working_time__)
        
        return result


class DoctorManager:
    def __init__(self, e_list):
        self.e_list = e_list
        e_list = []
        
    def read_doctors_file(self):
            doc_txt = open("Project Data (1)\Project Data\patients.txt")

        
    def format_dr_info(self, doctor):

        
    def enter_dr_info(self, new_dctor):
        new_doctor = Doctor()
        new_id = input("Enter the doctor’s ID:")
        new_name = input("Enter the doctor’s name:")
        new_speciality = input("Enter the doctor’s specility:")
        new_time = input("Enter the doctor’s timing (e.g., 7am-10pm):")
        new_qualification = input("Enter the doctor’s qualification:")
        new_room_num = input("Enter the doctor’s room number:")
        new_doctor 
        return self.new_doctor


class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender =  gender
        self.age = age

    def __get_patient_id__(self):
        return self.pid
    
    def __set_patient_id__(self, new_id):
        self.pid = new_id

    def __get_patient_name__(self):
        return self.name
    
    def __set_patient_name__(self, new_name):
        self.name = new_name
    
    def __get_patient_disease__(self):
        return self.disease
    
    def __set_patient_disease__(self, new_disease):
        self.disease = new_disease

    def __get_patient_gender__(self):
        return self.gender
    
    def __set_patient_gender__(self, new_gender):
        self.gender = new_gender
    
    def __get_patient_age__(self):
        return self.age
    
    def __set_patient_age__(self, new_age):
        self.age = new_age

    def __str__(self, result):
        result = (self.__get_patient_id__ + "_" + self.__get_patient_name__ + "_" + self.__get_patient_disease__ +
                   "_" + self.__get_patient_gender__ + "_" + self.__get_patient_age__)
        
        return result

class PatientManager:
    def __init__(self):


class Management:
    def __init__(self):
       choice = input(print(f"Welcome to Alberta Hospital (AH) Managment system \n Select from the following options, or select 3 to stop: \n1 - 	Doctors\n2 - 	Patients\n3 -	Exit Program"))

    for n in range(2):
           
       if choice == 3:
           break
       
       elif choice == 1:
           DoctorManager()

        elif choice == 2:
           