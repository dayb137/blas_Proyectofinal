from django.shortcuts import render


def inicio(request):
    return render(request,'inicio/inicio.html')

# ACERCA DE MI
def aboutme(request):
    return render(request, "inicio/aboutme.html")

