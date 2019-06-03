from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from .models import Sub
from .forms import SubForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            sub_url = request.POST.get('new')
            new = Sub.objects.filter(new=sub_url).first()
            if new:
                new.delete
            form.save()
            context = {
                'flag': True
            }
            return render(request, 'subs/done.html', context)
            # return redirect('subs:index')
    else:
        form = SubForm()
        context = {
            'form': form,
        }
        return render(request, 'subs/index.html', context)

def done(request):
    return redirect('subs:index')


def redirect_url(request, subUrl):
    url = get_object_or_404(Sub, new=subUrl)
    origin_url = url.origin
    return redirect(origin_url)


def page_not_found(request):
    response = render(request, 'subs/404.html', {})
    response.status_code = 404
    return response