from django.conf.urls import patterns, url
# from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$', TemplateView.as_view(template_name='site_index.html'), name='home'),
   url(r'^account/signup/', include('account_captcha.urls')), 
   url(r'^contact/', include('contact.urls')),
   #url(r'^feedback/', include('feedback_form.urls')),
   url(r'^feedback/', include('django_basic_feedback.urls')),
 ) + urlpatterns
