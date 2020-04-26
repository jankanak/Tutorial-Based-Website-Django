
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name="main"

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_request,name="logout"),
    path('login/',views.login_request,name="login"),
    path("<single_slug>",views.single_slug,name="single_slug")
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

