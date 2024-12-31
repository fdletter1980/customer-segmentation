#!/usr/bin/env python
# coding: utf-8

import pickle


# Load from file if needed
pkl_filename = "KMeans.pkl"
with open(pkl_filename, 'rb') as file:
    clustering_model = pickle.load(file)


print("Enter the following details to make the predictions:")

Avg_Credit_Limit = int(input("Enter The Average Credit Limit:- "))
Total_Credit_Cards = int(input("Enter Total # of Credit Cards:- "))
Total_visits_bank = int(input("Enter Total Visits to Bank:- "))
Total_visits_online = int(input("Enter Total Visits Online:- "))
Total_calls_made = int(input("Enter Total Calls Made:- "))

customer_prediction = clustering_model.predict([[Avg_Credit_Limit,Total_Credit_Cards,Total_visits_bank,Total_visits_online,Total_calls_made]])

print(customer_prediction)

