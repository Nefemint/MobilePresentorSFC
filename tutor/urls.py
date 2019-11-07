"""tutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]



# -*- coding: utf-8 -*-
import pymysql
import csv

def csv_writer(data, path):
    """
    Функция для записи данных в CSV
    """
    with open(path, "a", newline='') as csv_file:
        '''
        csv_file - объект с данными
        delimiter - разделитель
        '''
        writer = csv.writer(csv_file, delimiter=';')
        print(data)
        writer.writerow(data)
        #for line in data:
            #writer.writerow(line)




def pars(name, mail):
    connection = pymysql.connect(host='localhost',
                             user='parser',
                             password='Wzfuv175',
                             db='newsite',
                             charset='utf8',
                             unix_socket= '/var/lib/mysql/mysql.sock')
    with connection.cursor() as cursor:
        i = 0
        sql = "SELECT name FROM users"
        cursor.execute(sql)
        for row in cursor:
            name1 = str(row)
            name1 = name1.replace("(", "")
            name1 = name1.replace(")", "")
            name1 = name1.replace("'", "")
            name1 = name1.replace(",", "")
            #print(row)
            name.append(name1)
        sql = "SELECT mail FROM users"
        cursor.execute(sql)
        for row in cursor:
            name1 = str(row)
            name1 = name1.replace("(", "")
            name1 = name1.replace(")", "")
            name1 = name1.replace("'", "")
            name1 = name1.replace(",", "")
            mail.append(name1)
        connection.close
            #print(row)
    return name, mail


print('start parsing')
path = "output11.csv"
name = []
mail = []
pars(name, mail)
fields = ['username', 'email', 'first_name', 'last_name']
i = 0
csv_writer(fields, path)
'''
while (i < len(name)):
    t = []
    print(name[i], mail[i])
    t.append(name[i])
    t.append(mail[i])
    csv_writer(t, path)
    i = i + 1
    '''
data = ['odu37308@eveav.com','odu37308@eveav.com','vasiliy', 'severyanov']
csv_writer(data, path)
