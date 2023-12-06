"""vms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vendor import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/',views.Createvendor),
    path('api/vendorslist/',views.Listall),
    path('api/vendors/<int:pk>',views.Retrieve),
    path('api/vendorsupdate/<str:vendor_code>',views.Updatevendor),
    path('api/vendorsdelete/<str:vendor_code>',views.Deletevendor),
    path('api/vendorspurchase/',views.CreatePO),
    path('api/vendorspurchaselist/',views.ListPO),
    path('api/vendorsRetrivepo/<int:po_number>',views.RetrievePO),
    path('api/vendorsupdatepo/<int:po_number>',views.UpdatePO),
    path('api/vendorsdeletepo/<int:po_number>',views.DeletePO),
    path('api/vendorsperform/<int:pk>',views.Retrievevendorprfm),


    

]
