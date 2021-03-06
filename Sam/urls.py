from .views import   CustomerApi, CustomerEditApi, EmployeeApi, EmployeeEditApi, GroupApi, GroupEditApi, ItemApi, ItemEditApi, JobApi, JobEditApi, LedgerApi, LedgerEditApi, LoginApi, LogoutApi, RegisterApi, SupplierApi, SupplierEditApi, UserApi
from django.urls import path
from Sam import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
   path('register', RegisterApi.as_view()),
    path('login', LoginApi.as_view()),
    path('user', UserApi.as_view()),
    path('logout', LogoutApi.as_view()),
    path('item', ItemApi.as_view()),
    path('itemedits/<int:id>', ItemEditApi.as_view()),
    path('groups', GroupApi.as_view()),
    path('groupedits/<int:id>', GroupEditApi.as_view()),
    path('job', JobApi.as_view()),
    path('jobedits/<int:id>', JobEditApi.as_view()),
    path('suppl', SupplierApi.as_view()),
    path('supplieredits/<int:id>', SupplierEditApi.as_view()),
    path('emp', EmployeeApi.as_view()),
    path('empedits/<int:id>', EmployeeEditApi.as_view()),
    path('cust', CustomerApi.as_view()),
    path('custedits/<int:id>', CustomerEditApi.as_view()),
    path('ledg', LedgerApi.as_view()),
    path('ledgedits/<int:id>', LedgerEditApi.as_view()),
    






    path('items', views.items),
    path('itemshow',views.itemshow), 
    path('ItemEdit/<int:id>',views.ItemEdit, name="edit-item"),
    path('ItemView/<int:id>',views.itemView, name="view-item"),
    path('ItemDelete/<int:id>',views.ItemDelete, name="delete-item"),
    path('customer', views.CustomerAdd),
    path('customerview' ,views.CustomerView),
    path('customerEdit/<int:id>',views.customerEdit, name="edit-customer"),
    path('customView/<int:id>',views.customView, name="view-customer"),
    path('customerDelete/<int:id>',views.customerDelete, name="delete-customer"),
    path('supplier' ,views.SupplierAdd),
    path('suppliershow',views.suppliershow), 
    path('supplierEdit/<int:id>',views.supplierEdit, name="edit-supplier"),
    path('supplierView/<int:id>',views.supplierView, name="view-supplier"),
    path('supplierDelete/<int:id>',views.supplierDelete, name="delete-supplier"),
    path('jobadd', views.jobadd),
    path('jobshow',views.jobshow),
    path('JobEdit/<int:id>',views.JobEdit, name="edit-job"),
    path('JobView/<int:id>',views.JobView, name="view-job"), 
    path('JobDelete/<int:id>',views.JobDelete, name="delete-job"),
    path('group', views.group),
    path('groupshow',views.groupshow), 
    path('groupEdit/<int:id>',views.groupEdit, name="edit-group"),
    path('groupView/<int:id>',views.groupView, name="view-group"), 
    path('groupDelete/<int:id>',views.groupDelete, name="delete-group"),
    path('ledger', views.ledger),
    path('ledgershow',views.ledgershow), 
    path('ledgerEdit/<int:id>',views.ledgerEdit, name="edit-ledger"),
    path('ledgerView/<int:id>',views.ledgerView, name="view-ledger"), 
    path('ledgerDelete/<int:id>',views.ledgerDelete, name="delete-ledger"),
    path('EmployeeAdd', views.EmployeeAdd),
    path('employeeshow',views.employeeshow), 
    path('employeeEdit/<int:id>',views.employeeEdit, name="edit-employee"),
    path('emploView/<int:id>',views.emploView, name="view-employee"),
    path('employeeDelete/<int:id>',views.employeeDelete, name="delete-employee"),
    path('buttons',views.buttons),
    
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

