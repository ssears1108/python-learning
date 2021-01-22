import os 
import sys
import time
import requests
import json
#import openpyxl
#from openpyxl import load_workbook
import pandas 


print("checkpoint 1")
# CONSTANTS   
URL = 'https://www.virustotal.com/vtapi/v2/file/report' #this link not working
# COVERT this to {'apikey': USER_APIKEY, 'resource': None}
PARAMS = {'apikey': 'df5a2bfb15a3e4188db6c26d114a6c11cf1d701b75c18863f310f153efc3bd42', 'resource': None} 

WORK_DIR=os.getcwd()
PROJECT_DIR="soc-automations"
print("checkpoint 2")

