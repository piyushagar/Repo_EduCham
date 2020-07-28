from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic.edit import DeleteView 
import json
from django.http import Http404
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from student.forms import CommentForm
from .filters import ProductFilter
from .models import * 
from teacher.models import * 
from .forms import SignupForm
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import F 
from django.core.mail import send_mail
from six.moves import urllib
from django.contrib.sites.shortcuts import get_current_site
from urllib.parse import urljoin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    school= Cschool.objects.all()
    products = Product.objects.all()
    customize= Customize.objects.all()
    NEW_DOMAIN = Domain.objects.filter(tenant=request.tenant.id, is_primary=False)
    if request.META['HTTP_HOST'] != NEW_DOMAIN:
        full_address = get_object_or_404(Domain,tenant=request.tenant.id, is_primary=True)
        
    context = {'school': school, 'products': products, 'customize':customize, 'NEW_DOMAIN': NEW_DOMAIN, 'full_address': full_address}
    # NEW_DOMAIN = Domain.objects.filter(tenant=request.tenant.id, is_primary=False)
    # if request.META['HTTP_HOST'] != NEW_DOMAIN:
    #     full_address = get_object_or_404(Domain,tenant=request.tenant.id, is_primary=True)
    #     break
    #     return HttpResponseRedirect("http://"+urllib.parse.quote(str(full_address))+":8000/")
    return render(request, 'index.html', context)

def course(request):
    customize= Customize.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        leason = Leason.objects.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        leason = Leason.objects.all()
    products = Product.objects.all()
    school= Cschool.objects.all()
    context = {'products':products, 'leason':leason, 'school': school, 'customize': customize}
    return render(request, 'student/store.html', context)

def course_detail(request, id=None):
    customize = Customize.objects.all()
    context = {}
    try:
        products = Product.objects.get(id=id)
    except:
        raise Http404
    school= Cschool.objects.all()
    
    author= Author.objects.all()
    faq= Faq.objects.all()

    context = {'products': products, 'school': school, 'author': author, 'faq':faq, 'customize': customize}
    return render(request, 'student/product_detail.html', context)

def leason_list(request):
    customize= Customize.objects.all() 
    leason = Leason.objects.all()
    school= Cschool.objects.all()
   
    context = {'leason':leason, 'school': school, 'customize': customize}
    return render(request, 'student/leason_list.html', context)


def leason_detail(request, id):
    template_name = "student/leason_detail.html"
    
    school= Cschool.objects.all()
    customize= Customize.objects.all()
    leason = get_object_or_404(Leason, id=id)
    comments = Comment.objects.filter(leason=leason).order_by("-id")
    
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
        	
        	content = request.POST.get('content')
        	comment = Comment.objects.create(leason=leason, user=request.user, content=content)    
        	comment.save
        	 
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "leason": leason,
            'school': school,
            'customize': customize,
            "comments": comments,
            # "new_comment": new_comment,
            "comment_form": comment_form,
            
        },
    )

def cart(request):
    customize= Customize.objects.all()
    if request.user.is_authenticated:	
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    school= Cschool.objects.all()
    NEW_DOMAIN = Domain.objects.filter(tenant=request.tenant.id, is_primary=False)
    if request.META['HTTP_HOST'] != NEW_DOMAIN:
        full_address = get_object_or_404(Domain,tenant=request.tenant.id, is_primary=True)

    context = {'items':items, 'order':order, 'school': school, 'customize': customize, 'NEW_DOMAIN': NEW_DOMAIN, 'full_address': full_address}
    return render(request, 'student/cart.html', context)

def checkout(request):
    customize= Customize.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    school= Cschool.objects.all()
    context = {'items':items, 'order':order, 'school': school, 'customize': customize}
    return render(request, 'student/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	return JsonResponse('Item was added', safe=False)

def course_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    school= Cschool.objects.all()
    customize = Customize.objects.all()
    return render(request, 'student/course_list.html', {'filter': f, 'school':school, 'customize': customize})
 	 	


#######################accounts#######################################
class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ['domain', 'is_primary', 'tenant']
    
@user_passes_test(lambda u: u.is_superuser)
def create_view(request,pk): 
	school= Cschool.objects.all()
	tenant= get_object_or_404(Client, pk=pk, id=request.tenant.id)
	form = DomainForm(request.POST or None)
	if form.is_valid(): 
		form.save()
		return redirect("http://"+request.POST.get("domain") +":8000/")

	subdomain=Domain.objects.filter(tenant=request.tenant.id, is_primary=False)
	context = {'form': form, 'subdomain': subdomain, 'school':school}
	return render(request, "domain_form.html", context) 

# def myView(request):
# 	NEW_DOMAIN = Domain.objects.filter(tenant=request.tenant.id, is_primary=False)

# 	if request.META['HTTP_HOST'] != NEW_DOMAIN:
# 		full_address = get_object_or_404(Domain,tenant=request.tenant.id, is_primary=True)
# 		return HttpResponseRedirect("http://"+urllib.parse.quote(str(full_address))+":8000/")

def myView(request):
    NEW_DOMAIN = Domain.objects.filter(tenant=request.tenant.id, is_primary=False)
    if request.META['HTTP_HOST'] != NEW_DOMAIN:
        full_address = get_object_or_404(Domain,tenant=request.tenant.id, is_primary=True)
        
    return render(request, 'tabdeel.html', {'NEW_DOMAIN': NEW_DOMAIN, 'full_address': full_address})


@user_passes_test(lambda u: u.is_superuser)
def delete_view(request, pk):

  subdomain=Domain.objects.filter(tenant=request.tenant.id)
  context ={} 
  school= Cschool.objects.all()
  obj = get_object_or_404(Domain, pk=pk) 
  obj.visit_num = F('visit_num') + 1
  obj.save()

  if request.method =="POST": 
    # delete object 
    obj.delete() 
    # after deleting redirect to 
    # home page 
    return render(request, "delete_view.html", {'subdomain': subdomain}, {'obj': obj}) 

  ###########Admin#####################################
class ProductForm(ModelForm):
	class Meta:
	    model = Product
	    fields = ['name', 'price', 'digital', 'image', 'subtitle', 'author', 'discription']

def product_create(request, template_name='myadmin/project_form.html'):
    form = ProductForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Course has been create.')
        return redirect('/admin/leason/new')
        products = Product.objects.all()
    return render(request, template_name, {'form':form})


def product_update(request, pk, template_name='myadmin/school/project_create_form.html'):
    product= get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course Updated Successfully.')
        return redirect('/admin/home')
    return render(request, template_name, {'form':form})



def product_delete(request, pk, template_name='myadmin/project_confirm_delete.html'):
    product= get_object_or_404(Product, pk=pk)    
    if request.method=='POST':
        product.delete()
        messages.success(request, 'Course Deleted Successfully.')
        return redirect('/admin/home')
    return render(request, template_name, {'object':product})



def product_home(request):
    
    product = Product.objects.all()
    context = {'product':product}
    
    return render(request, 'myadmin/home.html', context)



# def productdetail(request, pk):
#     product = Product.objects.all()
#     project = Project.objects.get(pk=pk)
#     context = {'project': project, 'projects':projects}

#     return render(request, 'project/projectdetail.html', context)



########### leason################################


class LeasonForm(ModelForm):
	class Meta:
	    model = Leason
	    fields = ['title', 'slug', 'label', 'button', 'video', 'product', 'content']

def leason_create(request, template_name='myadmin/leason/leason_form.html'):
    form = LeasonForm(request.POST, request.FILES or None)
    if request.method == "POST":
    	send_mail(
    'new contact',
    'hii',
    'nabeelahmddd@gmail.com',
    ['nabeelahmed0111@gmail.com'],
    fail_silently=False,
)
    if form.is_valid():
        form.save()
        messages.success(request, 'Leason has been create.')
        return redirect('/admin/leason/home')
    return render(request, template_name, {'form':form})


def leason_update(request, pk, template_name='myadmin/leason/leason_form.html'):
    leason= get_object_or_404(Leason, pk=pk)
    form = LeasonForm(request.POST, request.FILES or None, instance=leason)
    if form.is_valid():
        form.save()
        messages.success(request, 'Leason Updated Successfully.')
        return redirect('/admin/leason/home')
    return render(request, template_name, {'form':form})



def leason_delete(request, pk, template_name='myadmin/leason/leason_confirm_delete.html'):
    leason= get_object_or_404(Leason, pk=pk)    
    if request.method=='POST':
        leason.delete()
        messages.success(request, 'Course Deleted Successfully.')
        return redirect('/admin/leason/home')
    return render(request, template_name, {'object':leason})



def leason_home(request):
    
    leason = Leason.objects.all()
    context = {'leason':leason}
    
    return render(request, 'myadmin/leason/home.html', context)

def school(request):
    school= Cschool.objects.all() 
    context = {'school': school}
    return render(request, 'myadmin/school/school.html', context)

class SchoolForm(ModelForm):
    class Meta:
        model = Cschool
        fields = ['name', 'title', 'subtitle', 'owner', 'img']

def school_create(request, template_name='myadmin/school/school_form.html'):
    form = SchoolForm(request.POST, request.FILES or None)
    if request.method == "POST":
        send_mail(
    'new contact',
    'hii',
    'nabeelahmddd@gmail.com',
    ['nabeelahmed0111@gmail.com'],
    fail_silently=False,
)
    if form.is_valid():
        form.save()
        messages.success(request, 'School has been create.')
        return redirect('/admin/leason/home')
    return render(request, template_name, {'form':form})

class CustomizeForm(ModelForm):
    class Meta:
        model = Customize
        fields = ['navbar', 'footer', 'homepageimage', 'logo', 'favicon']

def customize_update(request, pk, template_name='myadmin//customize_form.html'):
    customize= get_object_or_404(Customize, pk=pk)
    form = CustomizeForm(request.POST, request.FILES or None, instance=customize)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course Updated Successfully.')
        return redirect('/admin/leason/home')
    return render(request, template_name, {'form':form})


def order(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, 'order.html', context)