from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request, *arg, **kwargs):
    return about_view(request, *arg, **kwargs)

def about_view(request, *args, **kwargs):
    querysets = PageVisits.objects.all()
    page_visits = PageVisits.objects.filter(path=request.path)
    PageVisits.objects.create(path=request.path)
    try:
        percent = (page_visits.count()*100)//querysets.count()
    except:
        percent=0

    context_dict = {
        'my_title': 'my_page',
        'Total_vistis': querysets.count(),
        'page_visits': page_visits.count(),
        'percent': percent,
        'querysets':querysets
    }

    return render(request, 'home.html', context_dict)
