from django.contrib import admin
from .models import *

admin.site.register(Issuer)
admin.site.register(Investment)
admin.site.register(Trade)
admin.site.register(Allocation)
admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(Condition)
admin.site.register(Request)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_filter = ('parent_portfolio', 'portfolio_type',)

@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_filter = ('status', 'requirement__approval_subscription',  'requirement__notification_subscription',)

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_filter = ('condition__condition_type', 'portfolio__parent_portfolio', 'approval_subscription', 'notification_subscription')
