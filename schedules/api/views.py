from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import mSchadules
from .serializers import ser_schedule
from .forms import fSchedules

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .functions import Spinner

# api operation.
@csrf_exempt
def scheduleApi(request,id=0):
    if request.method == 'GET':
        schedule = mSchadules.objects.all()
        sch_ser = ser_schedule(schedule,many=True)
        return JsonResponse(sch_ser.data,safe=False)
    elif request.method == 'POST':
        sch_data = JSONParser().parse(request)
        sch_ser = ser_schedule(data=sch_data)
        if sch_ser.is_valid():
            sch_ser.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        sch_data = JSONParser().parse(request)
        sch_data_id = mSchadules.objects.get(id=id)
        sch_ser = ser_schedule(sch_data_id, data=sch_data)
        if sch_ser.is_valid():
            sch_ser.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        sch_data = mSchadules.objects.get(id=id)
        sch_data.delete()
        return JsonResponse('Delete Successfully',safe=False)
    
# rander operation.
def index(request):
    schedule = mSchadules.objects.all()
    p = Paginator(schedule,5)
    page = request.GET.get('page')
    vanues = p.get_page(page)
    nums = "i"*vanues.paginator.num_pages

    try:
        items = p.page(page)
    except EmptyPage:
        items = p.page(1)
    except PageNotAnInteger:
        items = p.page(1)
        
    context = {
        'items': items,
        'vanues':vanues,
        'nums':nums
    }
    
    return render (request, 'index.html', context)        

def add(request):
    if request.method == 'GET':
        add_form = fSchedules(request.POST or None)
        print("GET method")
        context = {
            'add_form': add_form
        }
        return render (request, 'form_add.html', context)
    elif request.method == 'POST':
        print("POST method")
        print(request.POST)
        add_form = fSchedules(request.POST or None)
        if add_form.is_valid():
            add_form.save()
            print("Add success")
        return redirect('list')

def update(request,id_sch=0):
    schedule = mSchadules.objects.get(id=id_sch)
    if request.method == 'GET':
        print(schedule)
        data = {
            'schedule_name': schedule.schedule_name,
            'schedule_time': schedule.schedule_time
        }
        update_form = fSchedules(request.GET or None, initial=data)
        print("GET method")
        context = {
            'update_form': update_form,
            'ids':id_sch
        }
        return render (request, 'form_update.html', context)
    elif request.method == 'POST':
        print("POST method")
        print(request.POST)
        update_form = fSchedules(request.POST or None,instance=schedule)
        if update_form.is_valid():
            update_form.save()
            print("Update success")
        return redirect('list')
    

def delete(request,id_sch):
    sch_data = mSchadules.objects.get(id=id_sch)
    sch_data.delete()
    return redirect('list')
        