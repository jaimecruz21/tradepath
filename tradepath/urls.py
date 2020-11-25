"""tradepath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url, include
# from rest_framework import routers, serializers, viewsets
from django.contrib import admin
#
# from . import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.index, name='index'),
# ]
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from tradepath import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER


urlpatterns = [

    url(r'^$', views.api_root),

    # Authentication
    url(r'auth/token', obtain_jwt_token, name='obtain_jwt_token'),
    url(r'auth/verify', verify_jwt_token, name='verify_jwt_token'),
    url(r'auth/me', views.AuthenticatedUserDetailAPIView.as_view(), name='authenticated-user-detail'),

    url(r'^organizations/$', views.OrganizationList.as_view(), name='organizations-list'),
    url(r'^organizations/(?P<pk>[0-9]+)$', views.OrganizationDetail.as_view(), name='organization-detail'),

    url(r'^contacts/$', views.ContactList.as_view(), name='contacts-list'),
    url(r'^contacts/(?P<pk>[0-9]+)$', views.ContactDetail.as_view(), name='contact-detail'),

    url(r'^subscriptions/$', views.SubscriptionList.as_view(), name='subscriptions-list'),
    url(r'^subscriptions/(?P<pk>[0-9]+)$', views.SubscriptionDetail.as_view(), name='subscription-detail'),

    url(r'^portfolios/$', views.PortfolioList.as_view(), name='portfolios-list'),
    url(r'^portfolios/(?P<pk>[0-9]+)$', views.PortfolioDetail.as_view(), name='portfolio-detail'),

    url(r'^issuers/$', views.IssuerList.as_view(), name='issuers-list'),
    url(r'^issuers/(?P<pk>[0-9]+)$', views.IssuerDetail.as_view(), name='issuer-detail'),

    url(r'^investments/$', views.InvestmentList.as_view(), name='investments-list'),
    url(r'^investments/(?P<pk>[0-9]+)$', views.InvestmentDetail.as_view(), name='investment-detail'),

    url(r'^trades/$', views.TradeList.as_view(), name='trades-list'),
    url(r'^trades/(?P<pk>[0-9]+)$', views.TradeDetail.as_view(), name='trade-detail'),

    url(r'^allocations/$', views.AllocationList.as_view(), name='allocations-list'),
    url(r'^allocations/(?P<pk>[0-9]+)$', views.AllocationDetail.as_view(), name='allocation-detail'),
    url(r'^allocations/(?P<pk>[0-9]+)/paths$', views.AllocationPathsList.as_view(), name='allocation-path-list'),

    url(r'^conditions/$', views.ConditionList.as_view(), name='conditions-list'),
    url(r'^conditions/(?P<pk>[0-9]+)$', views.ConditionDetail.as_view(), name='condition-detail'),

    url(r'^requirements/$', views.RequirementList.as_view(), name='requirements-list'),
    url(r'^requirements/(?P<pk>[0-9]+)$', views.RequirementDetail.as_view(), name='requirement-detail'),

    url(r'^requests/$', views.RequestList.as_view(), name='requests-list'),
    url(r'^requests/(?P<pk>[0-9]+)$', views.RequestDetail.as_view(), name='request-detail'),

    url(r'^paths/$', views.PathList.as_view(), name='paths-list'),
    url(r'^paths/(?P<pk>[0-9]+)$', views.PathDetail.as_view(), name='path-detail'),

    url(r'^admin/', admin.site.urls),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
