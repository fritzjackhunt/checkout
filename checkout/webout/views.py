from django.shortcuts import render, redirect 
from .forms import MyForm
from colorama import init, Fore, Style

init(autoreset=True)

# Create your views here.
def home(request):
    return render(request, 'checkout/index.html')

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Console log the cleaned data
            print(Fore.MAGENTA + "Form submitted: " + str(form.cleaned_data))
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'checkout/form.html', {'form': form})

def success_view(request):
    return render(request, 'checkout/success.html')
