from django.core.management import BaseCommand
from tradepath.models import Organization, Portfolio, Issuer, Investment, Trade, Allocation, Condition, Requirement, Path

def save_items(obj):
    for key in obj:
        obj[key].save()
        print('\t', key, 'saved')



class Command(BaseCommand):
    help = "Import Default Data and Trades"


    def handle(self, *args, **options):

        Organization.objects.all().delete()
        Portfolio.objects.all().delete()
        Issuer.objects.all().delete()
        Investment.objects.all().delete()
        Trade.objects.all().delete()
        Allocation.objects.all().delete()
        Condition.objects.all().delete()
        Requirement.objects.all().delete()
        Path.objects.all().delete()

        print('\nCreating Organizations')
        o = {
            'bank_of_america': Organization(name='Bank of America', is_counterparty=True, is_agent=True),
            'citibank': Organization(name='Citibank', is_counterparty=True, is_agent=True),
            'cortland': Organization(name='Cortland', is_counterparty=False, is_agent=True)
        }
        save_items(o)

        print('\nCreating Portfolios')
        p = {
            'clf_i':  Portfolio(name='Cygnus Loan Fund I', short_name='CLF I'),
            'clf_ii':  Portfolio(name='Cygnus Loan Fund II', short_name='CLF II'),
            'clf_jv_i':  Portfolio(name='Cygnus JV I', short_name='CLF JV I'),
        }
        save_items(p)

        print('\nCreating Issuers')
        issuers = {
            'microsoft': Issuer(name='Microsoft'),
            'google': Issuer(name='Google'),
            'facebook': Issuer(name='Facebook'),
        }
        save_items(issuers)

        print('\nCreating Investments')
        investments = {
            'microsoft_tla': Investment(name='Term Loan A', base=.01, spread=.07, issuer=Issuer.objects.get(name='Microsoft')),
            'microsoft_tlb': Investment(name='Term Loan B', base=.01, spread=.07, issuer=Issuer.objects.get(name='Microsoft')),
            'google_tla': Investment(name='Term Loan A', base=.01, spread=.07, issuer=Issuer.objects.get(name='Google')),
            'google_tlb': Investment(name='Term Loan B', base=.01, spread=.07, issuer=Issuer.objects.get(name='Google')),
            'facebook_tla': Investment(name='Term Loan A', base=.01, spread=.07, issuer=Issuer.objects.get(name='Facebook')),
            'facebook_tlb': Investment(name='Term Loan B', base=.01, spread=.07, issuer=Issuer.objects.get(name='Facebook')),
        }
        save_items(investments)

        print('\nCreating Trades')
        trades = {
            'microsoft_tla_buy': Trade(
                trade_date='2017-09-07',
                investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                counterparty=Organization.objects.get(name='Citibank'),
                action='BUY',
                market='PRIMARY',
                status='DRAFT',
                price=99.5,
                amount=100000000
            ),
            'microsoft_tla_sell': Trade(
                trade_date='2017-09-08',
                investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                counterparty=Organization.objects.get(name='Bank of America'),
                action='SELL',
                market='PRIMARY',
                status='DRAFT',
                price=100.5,
                amount=100000000
            ),
            'google_tlb_buy': Trade(
                trade_date='2017-09-07',
                investment=Investment.objects.get(name='Term Loan B', issuer__name='Google'),
                counterparty=Organization.objects.get(name='Bank of America'),
                action='BUY',
                market='PRIMARY',
                status='DRAFT',
                price=99.5,
                amount=100000000
            ),
            'microsoft_tlb_sell': Trade(
                trade_date='2017-09-08',
                investment=Investment.objects.get(name='Term Loan A', issuer__name='Facebook'),
                counterparty=Organization.objects.get(name='Citibank'),
                action='SELL',
                market='PRIMARY',
                status='DRAFT',
                price=100.5,
                amount=100000000
            ),
        }
        save_items(trades)

        print('\nCreating Conditions')
        conditions = {
        	'condition_100': Condition(name='ClearPar Allocation', condition='DEFAULT', sort_order=100),
        	'condition_200': Condition(name='Trader Approval', condition='DEFAULT', sort_order=200),
        	'condition_300': Condition(name='Co-Invest Approval', condition='COINVEST', sort_order=300),
        	'condition_400': Condition(name='Joint Venture / Leverage Approval', condition='DEFAULT', sort_order=400),
        	'condition_500': Condition(name='PM Approval', condition='DEFAULT', sort_order=500),
        	'condition_600': Condition(name='Execute Trade Confirm', condition='DEFAULT', sort_order=600),
        	'condition_700': Condition(name='Execute Assignment Agreement', condition='DEFAULT', sort_order=700),
        	'condition_800': Condition(name='Cash Availability Confirmation', condition='BUY', sort_order=800),
        	'condition_900': Condition(name='Set SDC', condition='DEFAULT', sort_order=900),
        	'condition_1000': Condition(name='Execute Funding Memo', condition='DEFAULT', sort_order=1000),
        	'condition_1100': Condition(name='Distribute Wire Memo', condition='BUY', sort_order=1100),
        	'condition_1200': Condition(name='Distribute ECD', condition='DEFAULT', sort_order=1200),
        }
        save_items(conditions)

        print('\nCreating Requirements')
        requirements = {
            'clf_i_requirement_100': Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_200': Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_300': Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_500': Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_600': Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_700': Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_800': Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_900': Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_1000': Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_1100': Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_i_requirement_1200': Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='CLF I')),
            'clf_ii_requirement_100': Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_200': Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_300': Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_500': Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_600': Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_700': Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_800': Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_900': Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_1000': Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_1100': Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_ii_requirement_1200': Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='CLF II')),
            'clf_jv_i_requirement_100': Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_200': Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_300': Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_300': Requirement(condition=Condition.objects.get(sort_order=400), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_500': Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_600': Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_700': Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_800': Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_900': Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_1000': Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_1100': Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
            'clf_jv_i_requirement_1200': Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='CLF JV I')),
        }
        save_items(requirements)

        print('\nCreating Allocations')
        allocations = {
            'clf_i_microsoft_buy_5m': Allocation(trade=Trade.objects.get(
                    trade_date='2017-09-07',
                    investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                    counterparty=Organization.objects.get(name='Citibank'),
                    action='BUY',
                    market='PRIMARY',
                    status='DRAFT',
                    price=99.5,
                    amount=100000000),
                portfolio=Portfolio.objects.get(short_name='CLF I'),
                status='PENDING',
                amount=5000000),
            'clf_ii_microsoft_buy_5m': Allocation(trade=Trade.objects.get(
                    trade_date='2017-09-07',
                    investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                    counterparty=Organization.objects.get(name='Citibank'),
                    action='BUY',
                    market='PRIMARY',
                    status='DRAFT',
                    price=99.5,
                    amount=100000000),
                portfolio=Portfolio.objects.get(short_name='CLF II'),
                status='PENDING',
                amount=2500000),
            'clf_jv_i_microsoft_buy_5m': Allocation(trade=Trade.objects.get(
                    trade_date='2017-09-07',
                    investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                    counterparty=Organization.objects.get(name='Citibank'),
                    action='BUY',
                    market='PRIMARY',
                    status='DRAFT',
                    price=99.5,
                    amount=100000000),
                portfolio=Portfolio.objects.get(short_name='CLF JV I'),
                status='PENDING',
                amount=2500000),
            'clf_i_microsoft_sell_5m': Allocation(trade=Trade.objects.get(
                    trade_date='2017-09-08',
                    investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                    counterparty=Organization.objects.get(name='Bank of America'),
                    action='SELL',
                    market='PRIMARY',
                    status='DRAFT',
                    price=100.5,
                    amount=100000000),
                portfolio=Portfolio.objects.get(short_name='CLF I'),
                status='PENDING',
                amount=5000000),
            'clf_ii_microsoft_sell_5m': Allocation(trade=Trade.objects.get(
                    trade_date='2017-09-08',
                    investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                    counterparty=Organization.objects.get(name='Bank of America'),
                    action='SELL',
                    market='PRIMARY',
                    status='DRAFT',
                    price=100.5,
                    amount=100000000),
                    portfolio=Portfolio.objects.get(short_name='CLF II'),
                amount=2500000),
            'clf_jv_i_microsoft_sell_5m': Allocation(trade=Trade.objects.get(
                    trade_date='2017-09-08',
                    investment=Investment.objects.get(name='Term Loan A', issuer__name='Microsoft'),
                    counterparty=Organization.objects.get(name='Bank of America'),
                    action='SELL',
                    market='PRIMARY',
                    status='DRAFT',
                    price=100.5,
                    amount=100000000),
                portfolio=Portfolio.objects.get(short_name='CLF JV I'),
                status='PENDING',
                amount=2500000),
        }
        save_items(allocations)
