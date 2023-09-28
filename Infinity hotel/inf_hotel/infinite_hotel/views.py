from django.shortcuts import render
from django.http import HttpResponse
import pymongo

url = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.1'

client = pymongo.MongoClient(url)	#Client connection

db = client['test']		#Database connection 1

admin_collec = db['hotel_admin']	#staff collection
customer_collec = db['hotel_customer']

# Create your views here.
def page1(request):
    addCustomer(request)
    return render(request,'registration.html')

def page2(request):
    password_checker(request)
    return render(request,'login.html')

def password_checker(request):
    a = request.POST
    email = a.get('email')
    passwd = a.get('passwd')
    dbpasswd = admin_collec.find_one({'email':email})
    try:
        if passwd == dbpasswd['passwd']:
            print("!!!SUCCESSFULL!!!")
    except:
        print("!!!FAILED!!!")

def addCustomer(request):
    a = request.POST
    name = str(a.get('name'))
    email = str(a.get('email'))
    contact_number = str(a.get('contact_number'))
    state = str(a.get('state'))
    nationality = str(a.get('nationality'))
    try:
        customer_collec.insert_one({'name':name,'email':email,'contact_number':contact_number,'state':state,'nationality':nationality})
        print("!!!SUCCESSFULL!!!")
    except:
        print("!!!FAILED!!!")