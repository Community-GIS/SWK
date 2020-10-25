from django.shortcuts import render,redirect
from django.template import loader
from .forms import TracksheetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.form

def user_login(request):
    # context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to index page.
                    # messages.info(request,"login sucessfully")
                    return render(request,"mainPage.html")
                else:
                    # Return a 'disabled account' error message
                    messages.info(request,"You're account is disabled")
                    return HttpResponseRedirect("You're account is disabled.")
        else:
                # Return an 'invalid login' error message.
                print ("invalid login details " + username + " " + password)
                messages.info(request,"Invalid login details"+ username + " " + password)
                return render(request,'adminlogin.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'adminlogin.html')



def HomePage(request):
    # template = 'HomePage.html'
   return render(request,"HomePage.html")

def TracksheetPage(request):
    form = TracksheetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request,"Daily Entry is saved.")
        return render(request,'mainPage.html')
        
    context= {
        'form': form,
        'test': 'test',
    }

    return render(request,'TracksheetForm.html',context)

# def MultipleForms(request):


#     return render(request,'sample.html')

# def form1(request):


#     return render(request,'form1.html')
# def form2(request):


#     return render(request,'form2.html')

# def user_login(request):
#     # context = RequestContext(request)
#     if request.method == 'POST':
#           username = request.POST['username']
#           password = request.POST['password']
#           user = authenticate(username=username, password=password)
#           if user is not None:
#               if user.is_active:
#                   login(request, user)
#                   # Redirect to index page.
#                   return HttpResponseRedirect("trackform/")
#               else:
#                   # Return a 'disabled account' error message
#                   return HttpResponse("You're account is disabled.")
#           else:
#               # Return an 'invalid login' error message.
#               print ("invalid login details " + username + " " + password)
#               return render(request,'adminlogin.html')
#     else:
#         # the login is a  GET request, so just show the user the login form.
#         return render(request,'adminlogin.html')


# def HomePage(request):
#     # template = 'HomePage.html'
#    return render(request,"HomePage.html")

def MapPage(request):
    return render(request,"map_fromFGIS.html")

# def TracksheetPage(request):
#     form = TracksheetForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context= {
#         'form': form,
#         'test': 'test',
#     }

#     return render(request,'TracksheetForm.html',context)

def AboutUs(request):
    return render(request,"aboutus.html")

        