
from django.contrib import admin
from django.urls import path, include
import first_app.views # from first_app import views 와 같음
import app_portfolio.views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_app.views.home, name='home'), #위의 경우에는 두번째 인자를 views.home 으로 줌
    path('blog/', include('first_app.urls')),
    path('portfolio/', include('app_portfolio.urls')),
    
    path('account/', include('app_account.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
