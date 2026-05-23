from django.shortcuts import render
from .models import Rewiev


def rewiev_list(request):
    rewievs = Rewiev.objects.all()
    
    context = {
        'rewiev_list': rewievs
    }

    return render(request, template_name="lesson/index.html", context=context)