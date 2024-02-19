from django.shortcuts import render
from .models import CanvasModel


def start(request):
    return render(request, 'main_app/start.html', { 
        'canvas_list' : CanvasModel.objects.all()
    })


def main(request, canvas_id):
    if canvas_id == 0:
        if request.POST.get('save_canvas_btn') == 'pushed':
            # сохраняем новый холст
            CanvasModel.objects.create(
                pen_color=request.POST.get('pen_color-btn'),
                pen_width=int(request.POST.get('pen_width-btn')),
                title=f'canvas_{len(CanvasModel.objects.all())}'
            )
            color = f"\'{request.POST.get('pen_color-btn')}\'"
            width = f"{request.POST.get('pen_width-btn')}"
            return render(request, 'main_app/main.html', { 
                'f_setCanvasParameters' : f"onload=setDefaultPen({color},{width})",
                'canvas_id' : len(CanvasModel.objects.all()),
            })
        else:
            # создаём новый холст
            color = '\'black\''
            width = '1'
            return render(request, 'main_app/main.html', { 
                'f_setCanvasParameters' : f"onload=setDefaultPen({color},{width})",
                'canvas_id' : 0,
            })
    
    else:
        if request.POST.get('save_canvas_btn') == 'pushed':
            # сохранение холста
            canvas = CanvasModel.objects.get(id=canvas_id)
            canvas.pen_color = request.POST.get('pen_color-btn')
            canvas.pen_width = int(request.POST.get('pen_width-btn'))
            canvas.save()
            color = f"\'{request.POST.get('pen_color-btn')}\'"
            width = f"{request.POST.get('pen_width-btn')}"
            return render(request, 'main_app/main.html', { 
                'f_setCanvasParameters' : f"onload=setDefaultPen({color},{width})",
                 'canvas_id' : canvas_id,
            })
        else:
            # загрузка сохранённого холста
            canvas = CanvasModel.objects.get(id=canvas_id)
            color = f'\'{canvas.pen_color}\''
            width = f'{canvas.pen_width}'
            return render(request, 'main_app/main.html', { 
                'f_setCanvasParameters' : f"onload=setDefaultPen({color},{width})",
                 'canvas_id' : canvas_id,
            })


def delete_canvas(request, canvas_id):
    # удаление холста
    CanvasModel.objects.get(id=canvas_id).delete()  
    return render(request, 'main_app/start.html', { 
        'canvas_list' : CanvasModel.objects.all()
    })