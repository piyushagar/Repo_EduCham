from django.shortcuts import render
from django_tenants.utils import schema_context
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from teacher.models import Client, Domain
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from tenant_schemas.utils import tenant_context
from django.views.generic.edit import UpdateView,  CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():


            form.save()
            username = form.cleaned_data.get('username')
            
            tenant = Client(schema_name=username,
                name=username,
                )
            tenant.save()
            domain = Domain()
            domain.domain = username+'.mainsite.com' # don't add your port or www here!
            domain.tenant = tenant
            domain.is_primary = False
            domain.save()




            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user) 
            test5 = Client(schema_name=username)  # "Client" is a tenant model

            with tenant_context(test5):
                User.objects.create_superuser(username=username, password=raw_password, email='sonal@gmail.com')

            return HttpResponseRedirect('http://'+domain.domain+':8000/admin/') # you can change this ok
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(req):
    return render(req, 'home.html')

def features(req):
    return render(req, 'features.html')

def pricing(req):
    return render(req, 'pricing.html')

def examples(req):
    return render(req, 'examples.html')

def blog(req):
    return render(req, 'blog.html')

# def domain_create(request, template_name='teacher/domain_form.html'):
#     form = DomainForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, template_name, {'form':form})




 






   


