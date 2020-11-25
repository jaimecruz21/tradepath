from url_filter.integrations.drf import DjangoFilterBackend

from urllib.parse import urlparse
from django.contrib.auth.models import User
from django.urls import Resolver404, resolve
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.response import Response

from tradepath.models import Organization, Contact, Subscription, Portfolio, Issuer, Investment, Trade, Allocation, Condition, Requirement, Request, Path
from tradepath.serializers import OrganizationSerializer, ContactSerializer, SubscriptionSerializer, PortfolioSerializer, IssuerSerializer, \
    InvestmentSerializer, TradeSerializer, AllocationSerializer, ConditionSerializer, \
    RequirementSerializer, PathSerializer, UserSerializer, RequestSerializer



def get_api_instance(instance_link, ModelClass):
    if isinstance(instance_link, int):
        instance_id = instance_link
    elif isinstance(instance_link, str):
        try:
            instance_link = urlparse(instance_link).path
            instance_id = int(resolve(instance_link).kwargs['pk'])
        except (Resolver404, ValueError):
            raise NotFound("Instance with url=%s not found" % instance_link)

    if instance_id is not None:
        try:
            instance = ModelClass.objects.get(pk=instance_id)
            return instance
        except ModelClass.DoesNotExist:
            raise NotFound("Instance with id=%s not found" % instance_id)


def update_object(obj, **kwargs):
    for k, v in kwargs.items():
        setattr(obj, k, v)
    obj.save()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('authenticated-user-detail', request=request, format=format),
        'organizations': reverse('organizations-list', request=request, format=format),
        'contacts': reverse('contacts-list', request=request, format=format),
        'subscriptions': reverse('subscriptions-list', request=request, format=format),
        'portfolios': reverse('portfolios-list', request=request, format=format),
        'issuers': reverse('issuers-list', request=request, format=format),
        'investments': reverse('investments-list', request=request, format=format),
        'trades': reverse('trades-list', request=request, format=format),
        'allocations': reverse('allocations-list', request=request, format=format),
        'conditions': reverse('conditions-list', request=request, format=format),
        'requirements': reverse('requirements-list', request=request, format=format),
        'requests': reverse('requests-list', request=request, format=format),
        'paths': reverse('paths-list', request=request, format=format),
        'allocation_paths': reverse('allocation-path-list', kwargs={'pk': 0}, request=request, format=format),
    })

#############
# Organization #
############


class OrganizationList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

#############
# Portfolio #
############


class PortfolioList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

#############
# Issuer #
############


class IssuerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Issuer.objects.all()
    serializer_class = IssuerSerializer


class IssuerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Issuer.objects.all()
    serializer_class = IssuerSerializer

#############
# Investment #
############


class InvestmentList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data


        investment = Investment.objects.create(**data)
        serializer = self.serializer_class(investment, context={'request': request})

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        try:
            investment = Investment.objects.get(pk=kwargs['pk'])
        except Investment.DoesNotExist:
            raise NotFound()

        update_object(investment, **data)
        serializer = self.serializer_class(investment, context={'request': request})

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


#############
# Trade #
############

class TradeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if 'investment' in data:
            identifier = data.pop('investment')
            investment = get_api_instance(identifier, Investment)
            data['investment'] = investment

        if 'counterparty' in data:
            identifier = data.pop('counterparty')
            counter_party = get_api_instance(identifier, Organization)
            data['counterparty'] = counter_party

        trade = Trade.objects.create(**data)
        serializer = self.serializer_class(trade, context={'request': request})

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TradeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

#############
# Allocation #
############


class AllocationList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if 'portfolio' in data:
            identifier = data.pop('portfolio')
            portfolio = get_api_instance(identifier, Portfolio)
            data['portfolio'] = portfolio

        if 'trade' in data:
            identifier = data.pop('trade')
            trade = get_api_instance(identifier, Trade)
            data['trade'] = trade

        allocation = Allocation.objects.create(**data)
        serializer = self.serializer_class(allocation, context={'request': request})

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AllocationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


#############
# Condition #
############


class ConditionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class ConditionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


###########
# Contact #
###########


class ContactList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


###########
# Subscription #
###########


class SubscriptionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer



#############
# Requirement #
############


class RequirementList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

#############
# Requirement #
############


class RequestList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

#############
# Path #
############


class PathList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get_queryset(self):
        queryset = Path.objects.all()
        condition = self.request.query_params.get('condition', None)
        if condition is not None:
            queryset = queryset.filter(requirement__condition__id=condition)
        return queryset


class PathDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Path.objects.all()
    serializer_class = PathSerializer


class AllocationPathsList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PathSerializer

    def get_queryset(self):
        try:
            allocation = Allocation.objects.filter(pk=self.kwargs['pk'])
            return Path.objects.filter(allocation=allocation)
        except Allocation.DoesNotExist:
            raise NotFound()

#############
# User #
############


class AuthenticatedUserDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
