from django.shortcuts import render, redirect, get_object_or_404
from .models import Sub
from .forms import SubForm

# Create your views here.
base_url = 'http://127.0.0.1:8000/'

def index(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subs:index')
    else:
        form = SubForm()
        context = {
            'form': form,
        }
        return render(request, 'subs/index.html', context)

def redirect_url(request, subUrl):
    url = get_object_or_404(Sub, new=subUrl)
    origin_url = url.origin
    return redirect(origin_url)
