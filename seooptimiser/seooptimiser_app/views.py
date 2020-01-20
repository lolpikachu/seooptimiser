from django.http import HttpResponse
from django.shortcuts import render, redirect
from seooptimiser_app.functions import seooptimiser
from .forms import LinksForm
   
def index(request): 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # link = request.POST['link']
        
        # create a form instance and populate it with data from the request:
        form = LinksForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            link = request.POST['link']
            keyword = request.POST['keyword']
            output = seooptimiser(link, keyword)
            print(output)
            # output =  colors(link, keyword)
        # return HttpResponse(output, content_type='text/plain')
        return render(request, 'seoapp/output.html', {'output': output})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LinksForm()

    return render(request, 'seoapp/index.html', {'form': form})