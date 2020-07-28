from django.contrib import admin
from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('examples/', views.examples, name='examples'),
    path('blog/', views.blog, name='blog'),
    path('signup/', views.signup, name='signup'),
    
    
    path('login/', LoginView.as_view(template_name='registration/signin.html'), name="login"),
	path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name="logout"),

]