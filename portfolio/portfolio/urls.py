
from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls'), name='home'),
    path('employee/', include('employee.urls')),
    path('contactus/', include('contact.urls')),
    path('pricing/', include('pricing.urls')),
    path('blog/', include('blog.urls')),
   
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
