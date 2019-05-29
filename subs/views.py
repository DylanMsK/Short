from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'subs/test.html')


def redirect_url(request, subUrl):
    context = {
        'url_name': subUrl,
    }
    return render(request, 'subs/index.html', context)
