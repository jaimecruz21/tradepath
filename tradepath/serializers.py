from django.contrib.auth.models import User
from rest_framework import serializers
from tradepath.models import Organization, Contact, Subscription,  Portfolio, Issuer, Investment, Trade, Allocation, Condition, Requirement, Request, Path


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Organization
        fields = '__all__'


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Contact
        fields = '__all__'


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Contact
        fields = '__all__'


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Portfolio
        fields = '__all__'


class IssuerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Issuer
        fields = '__all__'


class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Investment
        fields = '__all__'


class SimpleTradeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Trade
        fields = ('id', 'trade_date', 'action', 'investment', 'market', 'status', 'price', 'quantity', 'created_on', 'updated_on', 'venue', 'venue_trade_id', 'counterparty') # 'allocations',


class AllocationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    trade = SimpleTradeSerializer(many=False, read_only=True)
    portfolio = PortfolioSerializer(many=False, read_only=True)

    class Meta:
        model = Allocation
        depth = 2
        fields = ('url', 'id', 'quantity', 'coinvest', 'settle_date', 'status', 'venue_allocation_id', 'created_on', 'updated_on', 'trade', 'portfolio')


class TradeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    investment = InvestmentSerializer(many=False, read_only=True)
    counterparty = OrganizationSerializer(many=False, read_only=True)
    allocations = AllocationSerializer(many=True, read_only=True)

    class Meta:
        depth = 5
        model = Trade
        fields = ('id', 'allocations', 'trade_date', 'action', 'investment', 'market', 'status', 'price', 'venue', 'venue_trade_id', 'quantity', 'created_on', 'updated_on', 'counterparty') # 'allocations',


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Condition
        fields = '__all__'


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    portfolio = PortfolioSerializer(many=False, read_only=True)
    condition = ConditionSerializer(many=False, read_only=True)

    class Meta:
        depth = 5
        model = Requirement
        fields = '__all__'

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        depth = 5
        model = Request
        fields = '__all__'


class PathSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    allocation = AllocationSerializer(many=False, read_only=True)
    requirement = RequirementSerializer(many=False, read_only=True)

    class Meta:
        depth = 5
        model = Path
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    email = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        exclude = ('user_permissions', 'password', 'groups',)
