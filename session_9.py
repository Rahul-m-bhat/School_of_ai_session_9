#importing packages
from faker import  Faker
from collections import namedtuple  
import datetime
from datetime import date 
from decimal import Decimal
import numpy as np
import statistics
import random

fake = Faker()



#######################################################################################################################

def get_named_tuple(population):
    '''
    This function generates list of fake person details.
    Attributes : 'name','blood_type','current_location','DOB'
    '''
    profile =  fake.profile()
    info_list = []
    person = namedtuple('person',['name','blood_type','current_location','DOB']) 
    for i in range(population):
        p = person(profile['name'],profile['blood_group'],profile['current_location'],profile['birthdate'])
        info_list.append(p)
    return info_list

def calculateAge(birthDate): 
    '''
    This functions returns the age as we input the date of birth of the person
    '''
    today = date.today() 
    current_age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return current_age 

def named_tuple_calculator(population):
    '''
    This function calculates and returns the largest blood type, mean-current_location,
     oldest_person_age ,average age and time taken for calculation using named tuple also it calls 
     the get_named_tuple and calulateAge functions.
    '''
    t0 = datetime.datetime.now()
    named_tuple_list = get_named_tuple(population)
    current_lan = []
    current_lon = []
    age = []
    blood_group = []
    for i in named_tuple_list:
        current_lan.append(i.current_location[0])
        current_lon.append(i.current_location[1])
        age.append(calculateAge(i.DOB))
        blood_group.append(i.blood_type)

    try:
        largest_blood_type = statistics.mode(blood_group)
    except:
        largest_blood_type = statistics.multimode(blood_group)

    mean_location = (np.mean(current_lan),np.mean(current_lon))
    maximum_age = np.max(age)
    average_age = np.mean(age)

    results = largest_blood_type,mean_location,maximum_age,average_age

    t1 = datetime.datetime.now()
    time_elapsed = (t1-t0).total_seconds()

    return results , time_elapsed, named_tuple_list 




##########################################################################################################################


def get_dict_list(population) :
    """This function will give out the information list like name, bloodtype, current location
    and blood type using dictionary method"""
    info_list = []
    for i in range(population):
        profile =  fake.profile()
        d = {'name':profile['name'],"blood_type":profile['blood_group'],"current_location":profile['current_location'],
            "DOB": profile['birthdate']}
        info_list.append(d)
    return info_list


"""def cal_mean_current_location(name_tuple_list):
    """
    This function returns the mean current location.
    """
    current_lan = []
    current_lon = []
    for i in name_tuple_list:
        current_lan.append(i.current_location)
        current_lon.append(i.current_location)
    return np.mean(current_lan),np.mean(current_lon)"""


def dict_cal(population):
    '''
    This function calculates and returns the
    largest blood type, mean-current_location,
    oldest_person_age ,average age and time taken for calculation using Dictionary.
    '''
    t2 = datetime.datetime.now()
    dict_list = get_dict_list(population)
    current_lan = [] 
    current_lon = []
    age = []
    blood_group = []

    for i in dict_list:
        current_lan.append(i['current_location'][0])
        current_lon.append(i['current_location'][1])
        age.append(calculateAge(i['DOB']))
        blood_group.append(i['blood_type'])
    try:
        largest_blood_type = statistics.mode(blood_group)
    except:
        largest_blood_type = statistics.multimode(blood_group)

    mean_location = (np.mean(current_lan),np.mean(current_lon))
    maximum_age = np.max(age)
    average_age = np.mean(age)
    result = largest_blood_type,mean_location,maximum_age,average_age

    t3 = datetime.datetime.now()
    time_elapsed = (t3-t2).total_seconds()
    return result,time_elapsed ,dict_list