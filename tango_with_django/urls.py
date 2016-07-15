from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user=None):
        return '/rango/'

urlpatterns = [
    # Examples:
    # url(r'^$', 'tango_with_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'accounts/', include('registration.backends.simple.urls')),
]
