from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
from stata.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def errormsg():
    message={'status':'failure','reason':'explanation'}
    return HttpResponse(json.dumps(message),status=400)

def notfound():
    message={'status':'failure','reason':'Record not found'}
    return HttpResponse(json.dumps(message),status=404)


def search(request,people_id):
    person = Person.objects.filter(UserName=people_id)
    if not person:
        return notfound()
    email=Email.objects.filter(person=person[0])
    address=Address.objects.filter(person=person[0])
    output={}
    for key,value in person[0].__dict__.items():
        output[key]=value
    mailarray=[]
    for item in email:
        mailarray.append(item.Name)
    output["Emails"]=mailarray
    addrarray = []
    for item in address:
        cityarr={}
        city=item.city
        for key,value in city.__dict__.items():
            cityarr[key]=value
        cityarr.pop('_state')
        cityarr.pop('id')
        addrarray.append({"Address": item.address,"City":cityarr})

    output["AddressInfo"]=addrarray
    output.pop('_state')
    output.pop('id')
    return HttpResponse(json.dumps(output), content_type='json', status=200)








def create(request):
    try:
        data = json.load(request)
    except:
        return errormsg()
    p=Person(UserName=data["UserName"],FirstName=data["FirstName"],LastName=data["LastName"],Age=data["Age"])
    p.save()
    if(len(data['Emails'])>0):
        for i in data['Emails']:
            e=Email(person=p,Name=i)
            e.save()
    if (len(data['AddressInfo']) > 0):
        for item in data['AddressInfo']:
            address=Address(person=p,address=item['Address'])
            city=City(Name=item['City']['Name'],CountryRegion=item['City']['CountryRegion'],Region=item['City']['Region'])
            city.save()
            address.city=city
            address.save()
    output = {"Success":"True","Message":"User created successfully","id": p.id, "name":p.UserName}
    return HttpResponse(json.dumps(output), content_type='json', status=201)



def filter(request):
    data={}
    data["UserName"]=request.GET.get('UserName')
    data["FirstName"]=request.GET.get('FirstName')
    data["LastName"]=request.GET.get('LastName')
    data["MiddleName"] = request.GET.get('MiddleName')
    data["Gender"] = request.GET.get('Gender')
    data["Age"] = request.GET.get('Age')

    s="select * from stata_person where "
    for i,j in data.items():
        if j:
            s=s+i+"='"+j+"' and "
    s=s[0:len(s)-4]
    persons = Person.objects.raw(s)
    if not persons:
        return notfound()
    result=[]
    for person in persons:
        email = Email.objects.filter(person=person)
        address = Address.objects.filter(person=person)
        output = {}
        for key, value in person.__dict__.items():
            output[key] = value
        mailarray = []
        for item in email:
            mailarray.append(item.Name)
        output["Emails"] = mailarray
        addrarray = []
        for item in address:
            cityarr = {}
            city = item.city
            for key, value in city.__dict__.items():
                cityarr[key] = value
            cityarr.pop('_state')
            cityarr.pop('id')
            addrarray.append({"Address": item.address, "City": cityarr})

        output["AddressInfo"] = addrarray
        output.pop('_state')
        output.pop('id')
        result.append(output)
    return HttpResponse(json.dumps(result), content_type='json', status=200)