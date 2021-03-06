from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate, logout as django_logout


from OpenML.accounts.forms import AuthenticationForm, RegistrationForm


# Create your views here.
#
def login(request):
    """
    Log in view
    """

    if request.user.is_authenticated():
        return redirect('/home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/home')
    else:
        form = AuthenticationForm()
        return render(request,'registration/login.html',{'form': form})


def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, '/home',)
    else:
        form = RegistrationForm()
        return render(request,'registration/register.html',{'form': form})

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/home')


@login_required
def home(request):
    return render(request, 'index.html')







