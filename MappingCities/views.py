from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, render

import ImportNodes
from MappingCities.forms import HomeForm
from MappingCities.models import Post


def home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        args = {
            'form': form, 'posts': posts
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form}
        return render(request, self.template_name, args)
    html ='<form action="/output/" method="post"> {% csrf_token %}<label for="your_name">Your name: </label> <input id="your_name" type="text" name="your_name" > <input type="submit" value="OK"> </form>'
    return HttpResponse(html)
def output(request):
    now = ImportNodes.get_roads("Norwich")
    listroads = []
    for i in now:
        listroads.append(i.name)
    html = "<html><body> %s.</body></html>" % listroads
    return HttpResponse(html)