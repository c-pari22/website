from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re
from users.models import *
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone
from datetime import date

import calendar



def index(request):
    template = loader.get_template('website/index.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)
    # context = RequestContext(request, { 'officers': officers })
    # return HttpResponse(template.render(context))
    return render(request, 'website/index.html', { 'officers': officers })

def oh(request):
    return render(request, 'website/oh.html', {})

def ir(request):
    return render(request, 'website/ir.html', {})

def interview(request):
    time_dict = {9: "9:00am - 10:00am", 10: "10:00am - 11:00am", 11: "11:00am - 12:00pm", 12: "12:00pm - 1:00pm", 13: "1:00pm - 2:00pm",
                14: "2:00pm - 3:00pm", 15: "3:00pm - 4:00pm", 16: "4:00pm - 5:00pm"}
    start_times = {0: 9, 1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
    interview_slot_list = InterviewSlot.objects.all()

    now = timezone.localtime(timezone.now())

    current_week = _get_first_week(now)
    days = [day.strftime('%A') for day in current_week]
    current_week_dates = [date.strftime('%b %d, %Y') for date in current_week]

    next_week = _get_second_week(now)
    next_week_dates = [date.strftime('%b %d, %Y') for date in next_week]

    days_of_week_order = [day.weekday() for day in current_week]

    first_time_slot_dict = {}
    second_time_slot_dict = {}
    start_time = 9
    for _ in range(len(time_dict)):
        filter_start_time = interview_slot_list.filter(hour=start_time)
        imputed_start_time = [None for i in range(14)]
        for i in range(len(days_of_week_order)):
            slots = filter_start_time.filter(day_of_week=days_of_week_order[i])
            if len(slots) == 0:
                imputed_start_time[i] = None
                imputed_start_time[i + 7] = None
            else:
                #There should be two slots from this filter, one for this weeks and next weeks
                #sorted by date 
                slots = sorted(list(slots), key=lambda slot: slot.date)
                
                today_slot = slots[0]
                if (timezone.localtime(today_slot.date).date() <= now.date()):
                    #today's column will be displayed but none of the slots will be available                    
                    today_slot.availability = False
                    today_slot.save()

                imputed_start_time[i] = slots[0]
                imputed_start_time[i + 7] = slots[1]

        first_time_slot_dict[start_time] = imputed_start_time[:7]
        second_time_slot_dict[start_time] = imputed_start_time[7:]
        start_time += 1    

    context = {'interview_slot_list': interview_slot_list, 'day': now.strftime("%b %d, %Y"), 
    "time_dict": time_dict, "days": days, "first_time_slot_dict": first_time_slot_dict, 
    "second_time_slot_dict": second_time_slot_dict, "start_times": start_times, 
    "range": range(len(start_times)), "current_week": current_week_dates, "next_week": next_week_dates}

    return render(request, 'website/interview.html', context)

def _get_first_week(now):
    this_week = [now]
    for i in range(1, 7):
        add_date = now + timezone.timedelta(days=i)
        this_week.append(add_date)
    return this_week
def _get_second_week(now):
    next_week = []
    for i in range(7, 14):
        add_date = now + timezone.timedelta(days=i)
        next_week.append(add_date)
    return next_week

def _get_dates_of_week(now):
    this_week = ['date' for i in range(7)]
    current_day = now.weekday()
    if current_day == 6:
        this_week[0] = now
        for i in range(1, 7):
            add_date = now + timedelta(days=i)
            this_week[i] = add_date
    else:
        num_things_before = current_day + 1
        num_things_after = 5 - current_day
        sunday = now - timedelta(days=current_day + 1)
        this_week[0] = sunday

        for i in range(0, current_day):
            diff = current_day - i
            add_date = now - timedelta(days=diff)
            this_week[i + 1] = add_date
        for j in range(current_day + 1, 7):
            diff = j - current_day - 1           
            add_date = now + timedelta(days=diff)
            this_week[j] = add_date
    return this_week

def book_interview(request, slot_id):
    all_slots = InterviewSlot.objects.all()
    for slot in all_slots:
        if slot.slot_id == slot_id:
            context = {'time_slot': slot}
            break
    return render_to_response('website/book_interview.html', RequestContext(request, context))

def confirm_interview(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')

        all_slots = InterviewSlot.objects.all()
        num_student_has = len(all_slots.filter(student=name))
        if num_student_has < 2 and _validate_name(name) and _validate_berkeley_email(email):
            booked_slot = None
            for slot in all_slots:
                if slot.get_date() == request.POST['date'] and slot.hour == int(request.POST['day_hour'][1:]):
                    booked_slot = slot
                    break
            #if booked_slot == None:
            #   return oh(request)
            booked_slot.student = request.POST['name']
            booked_slot.student_email = request.POST['email']
            booked_slot.availability = False
            booked_slot.save()
            #_send_confirmation_email(booked_slot)
            return interview(request)
        else:
            return interview(request)       
    else:
        return interview(request)

def _validate_name(name):
    return name is not None

def _validate_berkeley_email(email):
    try:
        validate_email(email)
    except ValidationError as e:
        return False
    else:
        if "@berkeley.edu" not in email:
            return False
    return True

def _send_confirmation_email(slot):
    student_email = slot.student_email
    interviewer = slot.officer_username
    profiles = UserProfile.objects.all()
    interviewer_email = None
    for profile in profiles:
        if profile.user.username == interviewer:
            interviewer_email = profile.user.email
    if interviewer_email == None:
        print('oops')
        return
    send_mail(
        'UPE Technical Interview Confirmation',
        '{} has successfully booked an interview with UPE {}, {}, at {}.'.format(slot.student, slot.day_of_week, 
            timezone.localtime(slot.date), slot.hour),
        'webdev.upe@berkeley.edu',
        [interviewer_email, student_email],
        fail_silently=False,
    )
