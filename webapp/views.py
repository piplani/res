# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render, HttpResponse
from .forms import adddata
from .models import status, data
import smtplib, json


# Create your views here.


def sendmail(reciever, mes):
    message = 'Subject: {}\n\n{}'.format('Confirmation Mail', mes)
    sender = 'akshaykumar.90447@gmail.com'  # place your email id here
    sender_pswd = 'piplani@786'  # place your pswd here
    # reciever = 'piplani.rohan@gmail.com'

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender, sender_pswd)
    mail.sendmail(sender, reciever, message)
    mail.close()


def index(request):
    form = adddata(request.POST or None, request.FILES)
    x = ""
    activity_score = 0
    potency = 0
    efficacy = 0
    st = False
    dirname = ''
    email = ""
    stat = False
    query = False
    is_correct = False
    try:
        s = int(request.POST[u'job_id'])
        print(s)
        query = True
        print(query)
    except:

        pass
    try:
        stat = status.objects.filter(status_id=s)[0].status
        print(stat)
        activity_score = status.objects.filter(status_id=s)[0].activity_score
        potency = status.objects.filter(status_id=s)[0].potency
        efficacy = status.objects.filter(status_id=s)[0].efficacy
        is_correct = True

    except:
        is_correct = False

    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        s = status(status_id=new_data.id)
        s.save()
        dirname = str(new_data.id)
        old_dir = os.getcwd() + '/media/' + str(new_data.file.name)
        new_dir = os.getcwd() + '/media/' + dirname + '/' + '1.sdf'
        os.mkdir(os.path.join(os.getcwd() + '/media', dirname))
        os.rename(old_dir, new_dir)
        print(os.getcwd())
        # os.system('java -jar PaDEL-Descriptor.jar -2d -3d -dir hse/false/ -file false.csv')
        # x, st, activity_score, potency, efficacy = processing(dirname)
        # print(activity_score, potency, efficacy)
        sendmail(new_data.email, 'your job id is    ' + dirname)
        st = True
        email = new_data.email
        os.system('python3 process.py ' + dirname + " " + email)
    return render(request, 'index.html',
                  {'form': form, 'st': st, 'dirname': dirname, 'email': email, 'stat': stat, 'query': query,
                   'is_correct': is_correct, 'activity_score': activity_score, 'potency': potency,
                   'efficacy': efficacy})


def submitAJAX(request):
    if request.method == 'POST':
        post_file = request.POST.get('id_file')
        post_email = request.POST.get('id_email')

        # Logging
        print("Post File: " + str(post_file))
        print("Post Email: " + str(post_email))

        response_data = {'result': 'Create post successful!', 'file': post_file, 'email': post_email}

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
