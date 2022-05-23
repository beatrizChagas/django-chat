from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def homepage(request):
  return render(request, 'core/homepage.html')

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)

    if form.is_valid():
      user = form.save()

      login(request, user)

      return redirect('home')
    else:
      print(form.errors)
  else:
    form = SignUpForm()

  return render(request, 'core/signup.html', { 'form': form })
