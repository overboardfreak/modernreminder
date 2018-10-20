from django.urls import path

from  reminder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# path('admin/', admin.site.urls),
	path('',views.home),
	path('logout/',views.logout_view),
	path('signup/',views.signup),
	path('login/', views.signin),
	path('main/',views.main),
	path('checklist/',views.checklist),
	path('checklist/<int:check_id>',views.my_checklist),
	path('delete/<int:id>/',views.delete),
	path('checklist/<int:pk>/edit/', views.checklist_edit),
	path('checklist/new', views.new,),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)