# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:46:38 2019

@author: Michael Akinosho
"""

class Customers:
    
    def __init__(self):
        
        self.customers = []
        self.load_custs()
        
    def __str__(self):
        pass
    
    def load_custs(self):
        try:
            fct = open("customers.txt")
            for x in fct:
                customers_dict = {"Id":x.split(",")[0],
                                  "Firstname":x.split(",")[1],"Lastname":x.split(",")[2],
                                  "DateAdded":x.split(",")[3]}