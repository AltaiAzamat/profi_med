from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# Create your views here.
def new(request):
    error= ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'форма была не верной'

    form = ArticlesForm()
    data = {
        "form":form,
        'error': error,
    }
    return render(request, 'zapis.html', data)

