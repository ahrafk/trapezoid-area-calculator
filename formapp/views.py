import openpyxl
from django.shortcuts import render
from django.http import HttpResponse
from .models import TrapezoidCalculation

def home(request):
    area = None
    error = None

    if request.method == 'POST':
        try:
            base1 = float(request.POST.get('base1'))
            base2 = float(request.POST.get('base2'))
            height = float(request.POST.get('height'))

            if base1 <= 0 or base2 <= 0 or height <= 0:
                error = "All values must be greater than 0."
            else:
                area = round(0.5 * (base1 + base2) * height, 2)
                
                TrapezoidCalculation.objects.create(
                    base1=base1,
                    base2=base2,
                    height=height,
                    area=area
                )

        except (TypeError, ValueError):
            error = "Please enter valid numeric values."

    return render(request, 'formapp/home.html', {
        'area': area,
        'error': error
    })

def download_excel(request):
    try:
        base1 = float(request.GET.get('base1'))
        base2 = float(request.GET.get('base2'))
        height = float(request.GET.get('height'))
        area = 0.5 * (base1 + base2) * height
        area = round(area, 2)
    except (TypeError, ValueError):
        return HttpResponse("Invalid inputs.", status=400)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Trapezoid Area"

    
    ws.append(['Base 1', 'Base 2', 'Height', 'Area'])

    ws.append([base1, base2, height, area])


    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=trapezoid_area.xlsx'
    wb.save(response)
    return response

def history(request):
    records = TrapezoidCalculation.objects.all().order_by('-created_at')
    return render(request, 'formapp/history.html', {'records': records})