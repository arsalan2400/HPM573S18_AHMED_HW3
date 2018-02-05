#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:59:58 2018

@author: Aslan
"""

class Patient:
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost

    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class HospitalizedPatient(Node):

    def __init__(self, name, cost):
        Node.__init__(self, name, cost)
    def discharge(self):
        return self.cost
    print("Hospitalized Patient")

class EmergencyPatient(Node):
    def __init__(self, name, cost):
        Node.__init__(self, name, cost)
    def discharge(self):
        return self.cost
    print("Emergency Patient")


class Hospital:
    def _init_(self, cost, admit, discharge_all, get_total_cost):

        self.admit = admit

        def cost(self):
            if HospitalizedPatient:
                exp_cost=2000
            elif EmergencyPatient:
                exp_cost=1000
            return exp_cost

        def getTotalCost(self):
             thetotalcost = sum()
             for patient in self.get_total_cost:
                 thetotalcost[patient.cost] = sum(patient.cost())
             return thetotalcost

        def discharge_all(self):
            discharge_all_AA = self.discharge
            return discharge_all_AA

# create the terminal nodes
simulationHospital = Hospital(admit=[2,3])
# print the expect cost of this chance node
print(simulationHospital.get_expected_cost())
