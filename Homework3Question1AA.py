#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:06:31 2018

@author: Arsalan
"""

class Patient:
    def __init__(self,name):
        """
        :param name:helps identify the patient's name
        """
        self.name = name
    def discharge(self):
        """
        :return:print the name and type of patient
        """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")



class EmergencyPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self,name)
        self.supercost = 1000

    def discharge(self):
        emergency_discharge = 'is an Emergency Patient'
        discharge_information = [self.name, emergency_discharge]
        return discharge_information


class HospitalizedPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self,name)
        self.supercost = 2000

    def discharge(self):
        hospitalized_discharge = 'is a Hospitalized Patient'
        discharge_information =[self.name,hospitalized_discharge]
        return discharge_information



class Hospital:
    def __init__(self,cost):
        self.cost = cost
    def admit(self,patientnames):
        self.patientnames = patientnames

    #discharge_all needs to print the name and type when called
    def discharge_all(self):
        #keep an open list
        list_discharge = []
        for patient in self.patientnames:
            #the function below appends by listing all the individual patient
            #NAMES because self.cost is in class 'Hospital'
            list_discharge.append(patient.discharge())

        #the list_discharge = patient Names + type
        return list_discharge


    def get_total_cost(self):
        nettotalcost=0
             #the function below adds up all the individual patients' COSTS
            #because self.cost is in class 'Hospital'
        for patient in self.patientnames:
            nettotalcost += patient.supercost

        return nettotalcost

#Remember... 2H/3E. As seen by the elite clientele, this must be the Mayo Clinic..."
jeff = HospitalizedPatient("Jefferson")
roose = HospitalizedPatient("Roosevelt")
vandy = EmergencyPatient("Vanderbilt")
wash = EmergencyPatient("Washington")
ken = EmergencyPatient("Kennedy")

#we're building a hospital to feed into our functions. I wanted to simply put
#an input in there e.g. simulation_hospital = Hospital (admit=2,3) but the
#code wasn't having it. To fulfill this assignment I just named the 5 patients
#but this wouldn't be ideal with a larger dataset.
simulation_hospital=Hospital(0)
simulation_hospital.admit([jeff, roose, vandy, wash, ken])

#Printout discharge + costs
print("The names and type of discharged patients are...")
print(simulation_hospital.discharge_all())
print("The total cost in USD($) is...")
print(simulation_hospital.get_total_cost())
