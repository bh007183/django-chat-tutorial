from django.shortcuts import render

def index(reqest):
    return (render(reqest, 'chat/index.html'))
    
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })