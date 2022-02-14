from django.shortcuts import render


def count(request):
    return render(request, 'blog/count.html')


# def about(request):
#     return HttpResponse('Это about страница')

def frands(request):
    return render(request, 'blog/frands.html')

# hello

# privet
