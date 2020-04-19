from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from django.urls import path

from temp_monitor.views import AddTemperatureView, TemperatureTableView, person_list

from main.views import IndexPageView, ChangeLanguageView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', login_required(IndexPageView.as_view(), login_url='/accounts/log-in/'), name='index'),
    path('', login_required(person_list, login_url='/accounts/log-in/'), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),

    path('add_temp/', AddTemperatureView.as_view(), name='add_temp'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
