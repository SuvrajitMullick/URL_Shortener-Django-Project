from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import requests

# Create your views here.

from .models import *


def example_view(request, name):
    # print("\n\nhello world\n\n")

    # return HttpResponse("hello world")

    # data = {
    # "first_name": 'Suvo'
    # }
    # return render(request, 'index.html', data)

    # names = ['A', 'B', 'C', 'D']
    # data = {
    #     "list": names
    # }
    # return render(request, 'index.html', data)

    data = {
        "first_name": name
    }
    return render(request, 'index.html', data)


def task_view(request):
    data = {
        "name": 'Suvrajit'
    }
    return render(request, 'task.html', data)


def shorten_url(request):
    context = {
        "submitted": False,
        "error": False
    }
    if request.method == "POST":
        user_data = request.POST

        long_url = user_data['longurl']
        custom_name = user_data['custom_name']

        # push to the db
        try:
            obj = URL_Table(long_url=long_url, custom_name=custom_name)
            obj.save()

            data = {
                "longurl": obj.long_url,
                "shorturl": obj.custom_name,
                "date": obj.created_date,
                "clicks": obj.visit_count
            }

            context["submitted"] = True
            context["data"] = data

            # return HttpResponse("Saved to DB")
        except Exception as e:
            print(e)
            # return HttpResponse("The custom name is already taken")
            context["error"] = True

        # print(long_url, custom_name)
    return render(request, 'home.html', context)


def all_analytics(request):
    rows = URL_Table.objects.all()
    context = {
        "rows": rows
    }
    return render(request, "all-analytics.html", context)


def deep_analytics(request, name):
    row = URL_Table.objects.get(custom_name=name)
    country_data = Country.objects.filter(table=row)
    device_data = Device.objects.filter(table=row)
    context = {
        "row": row,
        'country_data': country_data,
        'device_data': device_data
    }
    return render(request, "deep-analytics.html", context)


def redirect_url(request, name):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"

    # ip = '172.217.22.14'
    location = requests.get('http://api.ipstack.com/' + ip +
                            '?access_key=bcfe38a0465bd0cf6319ddf96efdd0e9&format=1').json()
    # g = GeoIP2()
    # location = g.city(ip)
    location_country = location["country_name"]
    if location_country is None:
        location_country = 'Not Valid'

    try:
        # row = URL_Table.objects.filter(custom_name = custom_name) # returns a list
        row = URL_Table.objects.get(
            custom_name=name)  # returns a object

        try:
            c_obj = Country.objects.get(
                table=row, country_name=location_country)
        except Country.DoesNotExist:
            c_obj = Country(table=row, country_name=location_country)
        c_obj.country_count += 1
        c_obj.save()

        try:
            d_obj = Device.objects.get(
                table=row, device_name=device_type)
        except Device.DoesNotExist:
            d_obj = Device(table=row, device_name=device_type)
        d_obj.device_count += 1
        d_obj.save()

        long_url = row.long_url
        # print(row)
        row.visit_count += 1
        row.save()
        return redirect(long_url)
    except:
        return HttpResponse("This custom name has no mapping")

# Reference - https://medium.com/@arrosid/get-visitor-location-using-geoip2-in-django-32ad3d417115
