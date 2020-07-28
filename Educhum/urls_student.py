from django.contrib import admin
from django.urls import path, include
from student import views
from django.conf.urls.static import static
from Educhum import settings
from django.conf.urls import url
from django.contrib.auth.views import *
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('course/', views.course_list),
	path('cart/', views.cart, name="cart"),
	path('product/<int:id>', views.course_detail),
	path('product/leason/', views.leason_list),
	path("leason/<int:id>", views.leason_detail, name="leason_detail"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('accounts/', include('registration.backends.default.urls')),
    path('new/<int:pk>', views.create_view, name='domain_new'),
    path('delete/<int:pk>', views.delete_view, name='domain_delete'),

    path('neww/', views.myView, name="myView"),

    ###product
    path('admin/home', views.product_home, name='project_list'),
    # path('admin/view/<int:pk>', views.productdetail, name='productdetail'),
    path('admin/new', views.product_create, name='product_create'),
	path('admin/edit/<int:pk>', views.product_update, name='product_update'),
    path('admin/delete/<int:pk>', views.product_delete, name='product_delete'),

    ###leason
    path('admin/leason/home', views.leason_home, name='leason_list'),
    # path('admin/view/<int:pk>', views.productdetail, name='productdetail'),
    path('admin/leason/new', views.leason_create, name='leason_create'),
    path('admin/leason/edit/<int:pk>', views.leason_update, name='leason_update'),
    path('admin/leason/delete/<int:pk>', views.leason_delete, name='leason_delete'),
    path('admin/school/', views.school, name="school"),
    path('admin/school/new', views.school_create, name='school_create'),

    path('admin/customize/<int:pk>', views.customize_update, name='customize_update'),
    path('media/', views.myView),
    path('order/', views.order, name="order"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
