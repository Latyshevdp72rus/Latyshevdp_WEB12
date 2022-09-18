from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_site(request):
    return redirect('stand_list_view', permanent=True)
