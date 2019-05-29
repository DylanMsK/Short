from django.shortcuts import render

# Create your views here.
def redirect_url(request, subUrl):
    context = {
        'subUrl': subUrl,
    }
    return render(request, 'subs/redirect_url.html', context)
