from django.shortcuts import render
from .models import Room
import random

rooms_lst = [ 'bathroom', 'bedroom', 'childroom', 'diningroom', 'kitchen', 'lounge' ]

def main(request):
    return render(request, 'main_app/main.html')

def rooms(request):
    total_voltage = 0
    for room in rooms_lst:
        if Room.objects.filter(name=room).count() == 0:
            Room.objects.create(name=room)
        else:
            r = Room.objects.get(name=room)
            devices_quantity = 0
            r.voltage = random.randint(30, 120)
            total_voltage += r.voltage

            if r.fan:
                devices_quantity += 1
            if r.light:
                devices_quantity += 1
            if r.heater:
                devices_quantity += 1
            if r.player:
                devices_quantity += 1
            
            r.devices_quantity = devices_quantity
            r.save()

    rooms = Room.objects.all()
    return render(request, 'main_app/rooms.html', { 'rooms' : rooms, 'total_voltage' : total_voltage })


def room_page(request, room):
    r = Room.objects.get(name=room)
    r.temperature = random.randint(20, 30)
    r.humidity = random.randint(70, 80)

    if request.POST.get('device_btn') == 'fan':
         r.fan = False if r.fan else True
    elif request.POST.get('device_btn') == 'light':
         r.light = False if r.light else True
    elif request.POST.get('device_btn') == 'heater':
         r.heater = False if r.heater else True
    elif request.POST.get('device_btn') == 'player':
         r.player = False if r.player else True

    r.save()
    return render(request, 'main_app/room_page.html', { 'room' : r })
