from django.urls import path

from  reminder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# path('admin/', admin.site.urls),
	path('',views.home_page),
	path('logout/',views.logout_view),
	path('signup/',views.signup),
	path('login/', views.signin),

	path('main/',views.main),
	path('dashboard/', views.dashboard),

	path('checklist/<int:check_id>',views.checklist_view),

	path('delete/<int:id>/',views.delete_checklist),

	path('checklist/<int:pk>/edit/', views.edit_checklist),

	path('checklist/new/', views.new,),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)