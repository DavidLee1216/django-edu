#_*_ encoding:utf-8 _*_

"""MxOnline URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
import xadmin
from django.views.static import serve
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from users.views import IndexView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"), #process static file
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    #organization url setting
    url(r'^org/', include('organization.urls', namespace="org")),
    #the process function that configure the upload file's access
    url(r'^media/(?P<path>.*)', serve, {"document_root":MEDIA_ROOT}),

    # Production mode
    # url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    # courses relative url setting
    url(r'^course/', include('courses.urls', namespace="course")),
    # teacher relative url setting
    url(r'^teacher/', include('courses.urls', namespace="teacher")),
    # user relative url setting
    url(r'^users/', include('users.urls', namespace="users")),
    #contact us app url
    url(r'^contact/', include('contactus.urls')),

    #ueditor related url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^cart_payment/',include('cart_payment.urls', namespace="cart_payment" )),
    url(r'^aboutus', TemplateView.as_view(template_name='about_us.html'),name='aboutus'),
    url(r'^howitworks', TemplateView.as_view(template_name='how_it_works.html'),name='howitworks'),
    url(r'^terms', TemplateView.as_view(template_name='terms_service.html'),name='terms'),
    url(r'^privacy', TemplateView.as_view(template_name='privacy_policy.html'),name='privacy')

]
#404 page set up
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
# urlpatterns += staticfiles_urlpatterns()