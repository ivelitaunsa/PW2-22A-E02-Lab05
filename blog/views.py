from django.shortcuts import render

# Create your views here.
#nueva funcion
def post_list(request):
    return render(request, 'blog/post_list.html', {})