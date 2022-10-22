from cgi import print_form
import requests
import os
from time import sleep
import socket

def Menu():
    os.system('cls')
    print("-"*10,"IP Lookup",'-'*10)
    menu = ['1.Get Victim IP Details','2.Get my IP Details','3.Exit']
    for i in menu:
        print(i)
    print('-'*31)
    option = int(input("Enter Option: "))
    if option == 1:
        VictimIp()
    elif option == 2:
        myIP()
    elif option == 3:
        exit
    else:
        print("Invalid Input!")
        sleep(0.8)
        Menu()
def VictimIp():
    os.system('cls')
    print("-"*10,"IP Lookup",'-'*10)
    ip = input("Enter Victim IP: ")
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    print('>Getting IP Information...')
    sleep(1)
    data = {
        'IP':response.get('ip'),
        'IP Version':response.get('version'),
        'City':response.get('city'),
        'Region':response.get('region'),
        'Country':response.get('country_name'),
        'Country Code': response.get('country_code'),
        'Country Capital': response.get('country_capital'),
        'Continent':response.get('continent'),
        'Postal Code': response.get('postal'),
        'Latitude': response.get('latitude'),
        'Longitude':response.get('longitude'),
        'TimeZone':response.get('timezone'),
        'ISP':response.get('org')
    }
    os.system('cls')
    print("-"*10,"IP Lookup",'-'*10)
    for key, value in data.items():
        print(key," : ",value)
    print('-'*31)
    opt=input("Back to Menu? y/n : ")
    if 'y' in opt:
        Menu()
    else:
        quit()

def myIP():
    os.system('cls')
    print("-"*10,"IP Lookup",'-'*10)
    myip = requests.get('https://api.ipify.org').text 
    response = requests.get(f'https://ipapi.co/{myip}/json/').json()
    print('>Getting IP Information...')
    sleep(1)
    data = {
        'IP':response.get('ip'),
        'IP Version':response.get('version'),
        'City':response.get('city'),
        'Region':response.get('region'),
        'Country':response.get('country_name'),
        'Country Code': response.get('country_code'),
        'Country Capital': response.get('country_capital'),
        'Continent':response.get('continent'),
        'Postal Code': response.get('postal'),
        'Latitude': response.get('latitude'),
        'Longitude':response.get('longitude'),
        'TimeZone':response.get('timezone'),
        'ISP':response.get('org')
    }
    os.system('cls')
    print("-"*10,"IP Lookup",'-'*10)
    for key, value in data.items():
        print(key," : ",value)

    print('-'*31)
    opt=input("Back to Menu? y/n : ")
    if 'y' in opt:
        Menu()
    else:
        quit()
Menu()
