from .views import RegisterView,LoginView, UserView,LogoutView
from django.urls import path
from Sam import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('items', views.items),
    path('itemshow',views.itemshow), 
    path('ItemEdit/<int:id>',views.ItemEdit, name="edit-item"),
    path('ItemDelete/<int:id>',views.ItemDelete, name="delete-item"),
    path('customer', views.CustomerAdd),
    path('customerview' ,views.CustomerView),
     path('customerEdit/<int:id>',views.customerEdit, name="edit-customer"),
    path('customerDelete/<int:id>',views.customerDelete, name="delete-customer"),
    path('supplier' ,views.SupplierAdd),
    path('suppliershow',views.suppliershow), 
    path('supplierEdit/<int:id>',views.supplierEdit, name="edit-supplier"),
    path('supplierDelete/<int:id>',views.supplierDelete, name="delete-supplier"),
    path('jobadd', views.jobadd),
    path('jobshow',views.jobshow),
    path('JobEdit/<int:id>',views.JobEdit, name="edit-job"), 
     path('JobDelete/<int:id>',views.JobDelete, name="delete-job"),
    path('group', views.group),
    path('groupshow',views.groupshow), 
    path('groupEdit/<int:id>',views.groupEdit, name="edit-group"),
    path('groupDelete/<int:id>',views.ItemDelete, name="delete-group"),
    path('ledger', views.ledger),
    path('ledgershow',views.ledgershow), 
    path('ledgerEdit/<int:id>',views.ledgerEdit, name="edit-ledger"),
    path('ledgerDelete/<int:id>',views.ledgerDelete, name="delete-ledger"),
    path('EmployeeAdd', views.EmployeeAdd),
    path('employeeshow',views.employeeshow), 
    path('employeeEdit/<int:id>',views.employeeEdit, name="edit-employee"),
    path('employeeDelete/<int:id>',views.employeeDelete, name="delete-employee"),
    path('buttons',views.buttons)
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

