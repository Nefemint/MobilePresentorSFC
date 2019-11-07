"""
WSGI config for tutor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutor.settings")

application = get_wsgi_application()
import csv
path = "output11.csv"
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
        
        writer.writerow(data)
        #for line in data:
            #writer.writerow(line)
fields = ['username', 'email', 'first_name', 'last_name']
#test = ['antoha.danchenkov@yandex.ru', 'antoha.danchenkov@yandex.ru', 'Антон', 'Данченко']
csv_writer(fields, path)
#csv_writer(test, path)

with open('/Users/pp/Downloads/list.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    '''for row in spamreader:
        print(' '.join(row))'''
    #reader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
    i = 0
    for row in spamreader:
        temp = ' '.join(row)
        #print(temp)
        
        arr = temp.split(';')
        name = arr[0]
        last_name = arr[1]
        email = arr[3]

        status = arr[12]
       # data = [email, email, name, last_name]
        
        s = status.split('.')
        i += 1
        '''if(i >= 2 and s[0] != ""):
            if (int(s[0]) >= 300):
                csv_writer(data, path)
                print(name, last_name, email, status)'''
        '''if(i >= 2):
            if ((s[0]) == ''):
                csv_writer(data, path)
                print(name, last_name, email, status)
            if (s[0] != ""):
                if(int(s[0]) <= 299):
                    csv_writer(data, path)
                    print(name, last_name, email, status)

        i += 1
        '''


    #print(list(reader)[1])
    #print(dir(reader))
  
    
    
