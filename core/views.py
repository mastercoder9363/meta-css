from django.shortcuts import render


def qiymat(request):
    return render(request, 'index.html')
def jeepp(request):
    return render(request, 'jeep.html')
def masha(request):
    return render(request, 'ayiqmasha.html')
