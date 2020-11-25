from django.core.management import BaseCommand
from tradepath.models import Organization, Portfolio, Issuer, Investment, Trade, Allocation, Condition, Requirement, Path

def save_items(obj):
    for key in obj:
        key.save()
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
        o = [
            Organization(name='Barclays', external_id=1, is_counterparty=True, is_agent=True),
            Organization(name='Jefferies', external_id=2, is_counterparty=True, is_agent=True),
            Organization(name='GS', external_id=3, is_counterparty=True, is_agent=True),
            Organization(name='BofA', external_id=4, is_counterparty=True, is_agent=True),
            Organization(name='UBS', external_id=5, is_counterparty=True, is_agent=True),
            Organization(name='CS', external_id=6, is_counterparty=True, is_agent=True),
            Organization(name='BAML', external_id=7, is_counterparty=True, is_agent=True),
            Organization(name='FS', external_id=8, is_counterparty=True, is_agent=True),
            Organization(name='Citi', external_id=9, is_counterparty=True, is_agent=True),
            Organization(name='JPM', external_id=10, is_counterparty=True, is_agent=True),
        ]
        save_items(o)

        print('\nCreating Portfolios')
        p = [
            Portfolio(name='Fifth Street Finance Corp.', short_name='FSC', external_id=1),
            Portfolio(name='Fifth Street Senior Floating Rate Corp.', short_name='FSFR', external_id=2),
            Portfolio(name='Fifth Street Opportunities Fund, L.P.', short_name='FSOF', external_id=3),
            Portfolio(name='FS Senior Funding Ltd.', short_name='FSSF', external_id=4),
            Portfolio(name='FS Senior Funding II LLC', short_name='FSSF II', external_id=5),
            Portfolio(name='FSFR Glick JV Funding LLC', short_name='Glick', external_id=6),
            Portfolio(name='Fifth Street Senior Loan Fund I, LLC', short_name='SLF I', external_id=7),
            Portfolio(name='Fifth Street SLF II, Ltd.', short_name='SLF II', external_id=8),
            Portfolio(name='SLF JV II Funding LLC', short_name='SLF JV II', external_id=9),
            Portfolio(name='SLF JV I Funding LLC', short_name='SLF JV I', external_id=10),
            Portfolio(name='Fifth Street Funding II, LLC', short_name='FSF II', external_id=11),
            Portfolio(name='Fifth Street Funding, LLC', short_name='FSF', external_id=12),
        ]
        save_items(p)

        print('\nCreating Issuers')
        i = [
            Issuer(name='Accudyne', external_id=1),
            Issuer(name='BMC Software', external_id=2),
            Issuer(name='CCC Information (Cypress Intermediate)', external_id=3),
            Issuer(name='DTZ', external_id=4),
            Issuer(name='Idera', external_id=5),
            Issuer(name='iHeartcommunications', external_id=6),
            Issuer(name='Internet Brands (Micro Holding)', external_id=7),
            Issuer(name='Nature\'s Bounty (Alphabet Holding Company)', external_id=8),
            Issuer(name='PSI Services Inc', external_id=9),
            Issuer(name='Scientific Games', external_id=10),
            Issuer(name='Staples', external_id=11),
            Issuer(name='TIBCO', external_id=12),
            Issuer(name='United Site Services', external_id=13),
            Issuer(name='Veritas', external_id=14),
        ]
        save_items(i)

        print('\nCreating Investments')
        inv = [
            Investment(name='TLB', spread=0.0375, base=0.01, external_id=11, issuer=Issuer.objects.get(external_id=1)),
            Investment(name='TLB', spread=0.04, base=0.01, external_id=14, issuer=Issuer.objects.get(external_id=2)),
            Investment(name='2nd Lien', spread=0.0675, base=0.01, external_id=2, issuer=Issuer.objects.get(external_id=3)),
            Investment(name='1st Lien TL', spread=0.0325, base=0.01, external_id=15, issuer=Issuer.objects.get(external_id=4)),
            Investment(name='TLB', spread=0.05, base=0.01, external_id=3, issuer=Issuer.objects.get(external_id=5)),
            Investment(name='DDTL', spread=0.05, base=0.01, external_id=4, issuer=Issuer.objects.get(external_id=5)),
            Investment(name='TLD', spread=0.0675, base=0.01, external_id=1, issuer=Issuer.objects.get(external_id=6)),
            Investment(name='1st Lien TL', spread=0.0375, base=0, external_id=10, issuer=Issuer.objects.get(external_id=7)),
            Investment(name='1st Lien TL', spread=0.035, base=0, external_id=8, issuer=Issuer.objects.get(external_id=8)),
            Investment(name='1L TL', spread=0.05, base=0.0123611, external_id=12, issuer=Issuer.objects.get(external_id=9)),
            Investment(name='1L TL (Add On)', spread=0.05, base=0.0123611, external_id=13, issuer=Issuer.objects.get(external_id=9)),
            Investment(name='TLB - 4', spread=0.0325, base=0, external_id=5, issuer=Issuer.objects.get(external_id=10)),
            Investment(name='1st Lien TL', spread=0.04, base=0.01, external_id=7, issuer=Issuer.objects.get(external_id=11)),
            Investment(name='TLB', spread=0.045, base=0.01, external_id=16, issuer=Issuer.objects.get(external_id=12)),
            Investment(name='1st Lien TL', spread=0.0375, base=0.01, external_id=9, issuer=Issuer.objects.get(external_id=13)),
            Investment(name='TLB-1', spread=0.045, base=0.01, external_id=6, issuer=Issuer.objects.get(external_id=14)),
        ]
        save_items(inv)

        print('\nCreating Conditions')
        conditions = [
        	Condition(name='ClearPar Allocation', condition='DEFAULT', sort_order=100),
        	Condition(name='Trader Approval', condition='DEFAULT', sort_order=200),
        	Condition(name='Co-Invest Approval', condition='COINVEST', sort_order=300),
        	Condition(name='Joint Venture / Leverage Approval', condition='DEFAULT', sort_order=400),
        	Condition(name='PM Approval', condition='DEFAULT', sort_order=500),
        	Condition(name='Execute Trade Confirm', condition='DEFAULT', sort_order=600),
        	Condition(name='Execute Assignment Agreement', condition='DEFAULT', sort_order=700),
        	Condition(name='Cash Availability Confirmation', condition='BUY', sort_order=800),
        	Condition(name='Set SDC', condition='DEFAULT', sort_order=900),
        	Condition(name='Execute Funding Memo', condition='DEFAULT', sort_order=1000),
        	Condition(name='Distribute Wire Memo', condition='BUY', sort_order=1100),
        	Condition(name='Distribute ECD', condition='DEFAULT', sort_order=1200),
        ]
        save_items(conditions)

        print('\nCreating Requirements')
        requirements = [
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='SLF II')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='FSC')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='FSF II')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=400), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='SLF JV I')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=400), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='SLF JV II')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='FSFR')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='FSSF')),
            Requirement(condition=Condition.objects.get(sort_order=100), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=200), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=300), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=500), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=600), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=700), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=800), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=900), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=1000), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=1100), portfolio=Portfolio.objects.get(short_name='FSSF II')),
            Requirement(condition=Condition.objects.get(sort_order=1200), portfolio=Portfolio.objects.get(short_name='FSSF II')),
        ]
        save_items(requirements)

        print('\nCreating Trades')
        trades = [
            Trade(external_id=1, investment=Investment.objects.get(external_id=1), counterparty=Organization.objects.get(external_id=3), trade_date='2017-03-10', venue='CLEARPAR', venue_trade_id=2478536, action='BUY', market='SECONDARY', status='ACTIVE', price=0.89, amount=4000000),
            Trade(external_id=2, investment=Investment.objects.get(external_id=1), counterparty=Organization.objects.get(external_id=1), trade_date='2017-03-15', venue='CLEARPAR', venue_trade_id=2484462, action='SELL', market='SECONDARY', status='ACTIVE', price=0.8875, amount=4000000),
            Trade(external_id=3, investment=Investment.objects.get(external_id=2), counterparty=Organization.objects.get(external_id=2), trade_date='2017-05-03', venue='CLEARPAR', venue_trade_id=2542478, action='BUY', market='SECONDARY', status='ACTIVE', price=1.025, amount=2500000),
            Trade(external_id=4, investment=Investment.objects.get(external_id=16), counterparty=Organization.objects.get(external_id=10), trade_date='2017-06-02', venue='CLEARPAR', venue_trade_id=2573981, action='BUY', market='SECONDARY', status='ACTIVE', price=1.01625, amount=0),
            Trade(external_id=5, investment=Investment.objects.get(external_id=3), counterparty=Organization.objects.get(external_id=2), trade_date='2017-06-28', venue='CLEARPAR', venue_trade_id=2600593, action='BUY', market='SECONDARY', status='ACTIVE', price=1.0025, amount=4227272.73),
            Trade(external_id=6, investment=Investment.objects.get(external_id=4), counterparty=Organization.objects.get(external_id=2), trade_date='2017-06-28', venue='CLEARPAR', venue_trade_id=2600593, action='BUY', market='SECONDARY', status='ACTIVE', price=1.0025, amount=772727.27),
            Trade(external_id=7, investment=Investment.objects.get(external_id=5), counterparty=Organization.objects.get(external_id=4), trade_date='2017-07-31', venue='CLEARPAR', venue_trade_id=2657778, action='BUY', market='SECONDARY', status='ACTIVE', price=0.995, amount=18000000),
            Trade(external_id=8, investment=Investment.objects.get(external_id=6), counterparty=Organization.objects.get(external_id=4), trade_date='2017-08-08', venue='CLEARPAR', venue_trade_id=2657360, action='BUY', market='SECONDARY', status='ACTIVE', price=1.015, amount=7000000),
            Trade(external_id=9, investment=Investment.objects.get(external_id=9), counterparty=Organization.objects.get(external_id=7), trade_date='2017-08-10', venue='CLEARPAR', venue_trade_id=2666599, action='BUY', market='PRIMARY', status='ACTIVE', price=1, amount=500000),
            Trade(external_id=10, investment=Investment.objects.get(external_id=7), counterparty=Organization.objects.get(external_id=5), trade_date='2017-08-15', venue='OFFLINE', venue_trade_id='', action='BUY', market='PRIMARY', status='ACTIVE', price=0.9975, amount=20000000),
            Trade(external_id=11, investment=Investment.objects.get(external_id=8), counterparty=Organization.objects.get(external_id=6), trade_date='2017-08-15', venue='CLEARPAR', venue_trade_id=2649951, action='BUY', market='PRIMARY', status='ACTIVE', price=0.995, amount=5000000),
            Trade(external_id=12, investment=Investment.objects.get(external_id=10), counterparty=Organization.objects.get(external_id=6), trade_date='2017-08-17', venue='CLEARPAR', venue_trade_id=2651134, action='BUY', market='PRIMARY', status='ACTIVE', price=0.995, amount=6000000),
            Trade(external_id=13, investment=Investment.objects.get(external_id=11), counterparty=Organization.objects.get(external_id=2), trade_date='2017-08-24', venue='CLEARPAR', venue_trade_id=2656812, action='BUY', market='SECONDARY', status='ACTIVE', price=1.0025, amount=4915254.24),
            Trade(external_id=14, investment=Investment.objects.get(external_id=11), counterparty=Organization.objects.get(external_id=6), trade_date='2017-08-28', venue='CLEARPAR', venue_trade_id=2657435, action='BUY', market='SECONDARY', status='ACTIVE', price=1.00375, amount=5000000),
            Trade(external_id=15, investment=Investment.objects.get(external_id=6), counterparty=Organization.objects.get(external_id=7), trade_date='2017-08-28', venue='CLEARPAR', venue_trade_id=2657366, action='BUY', market='SECONDARY', status='ACTIVE', price=1.00875, amount=3000000),
            Trade(external_id=16, investment=Investment.objects.get(external_id=12), counterparty=Organization.objects.get(external_id=8), trade_date='2017-09-05', venue='OFFLINE', venue_trade_id='', action='BUY', market='SECONDARY', status='ACTIVE', price=0.9856, amount=6483750),
            Trade(external_id=17, investment=Investment.objects.get(external_id=13), counterparty=Organization.objects.get(external_id=8), trade_date='2017-09-05', venue='OFFLINE', venue_trade_id='', action='BUY', market='SECONDARY', status='ACTIVE', price=0.9856, amount=270155.92),
            Trade(external_id=18, investment=Investment.objects.get(external_id=12), counterparty=Organization.objects.get(external_id=8), trade_date='2017-09-05', venue='OFFLINE', venue_trade_id='', action='SELL', market='SECONDARY', status='ACTIVE', price=0.9856, amount=6483750),
            Trade(external_id=19, investment=Investment.objects.get(external_id=13), counterparty=Organization.objects.get(external_id=8), trade_date='2017-09-05', venue='OFFLINE', venue_trade_id='', action='SELL', market='SECONDARY', status='ACTIVE', price=0.9856, amount=270155.92),
            Trade(external_id=20, investment=Investment.objects.get(external_id=11), counterparty=Organization.objects.get(external_id=6), trade_date='2017-09-06', venue='CLEARPAR', venue_trade_id=2663082, action='BUY', market='SECONDARY', status='ACTIVE', price=1.00125, amount=5000000),
            Trade(external_id=21, investment=Investment.objects.get(external_id=9), counterparty=Organization.objects.get(external_id=7), trade_date='2017-09-07', venue='CLEARPAR', venue_trade_id=2669046, action='SELL', market='PRIMARY', status='ACTIVE', price=1.01, amount=500000),
            Trade(external_id=22, investment=Investment.objects.get(external_id=14), counterparty=Organization.objects.get(external_id=6), trade_date='2017-09-11', venue='CLEARPAR', venue_trade_id=2666397, action='BUY', market='SECONDARY', status='ACTIVE', price=1.00625, amount=3000000),
            Trade(external_id=23, investment=Investment.objects.get(external_id=6), counterparty=Organization.objects.get(external_id=9), trade_date='2017-09-11', venue='CLEARPAR', venue_trade_id=2665835, action='BUY', market='SECONDARY', status='ACTIVE', price=1.01, amount=3000000),
            Trade(external_id=24, investment=Investment.objects.get(external_id=7), counterparty=Organization.objects.get(external_id=5), trade_date='2017-09-11', venue='CLEARPAR', venue_trade_id=2665524, action='BUY', market='SECONDARY', status='ACTIVE', price=0.9975, amount=3000000),
            Trade(external_id=25, investment=Investment.objects.get(external_id=6), counterparty=Organization.objects.get(external_id=9), trade_date='2017-09-12', venue='CLEARPAR', venue_trade_id=2666627, action='BUY', market='SECONDARY', status='ACTIVE', price=1.0125, amount=3000000),
            Trade(external_id=26, investment=Investment.objects.get(external_id=15), counterparty=Organization.objects.get(external_id=5), trade_date='2017-09-12', venue='CLEARPAR', venue_trade_id=2666879, action='BUY', market='SECONDARY', status='ACTIVE', price=1.00375, amount=5000000),
            Trade(external_id=27, investment=Investment.objects.get(external_id=14), counterparty=Organization.objects.get(external_id=6), trade_date='2017-09-14', venue='CLEARPAR', venue_trade_id=2669920, action='BUY', market='SECONDARY', status='ACTIVE', price=1.0075, amount=2000000),
            Trade(external_id=28, investment=Investment.objects.get(external_id=11), counterparty=Organization.objects.get(external_id=6), trade_date='2017-09-15', venue='CLEARPAR', venue_trade_id='', action='BUY', market='SECONDARY', status='ACTIVE', price=1.00375, amount=5000000),
            Trade(external_id=29, investment=Investment.objects.get(external_id=6), counterparty=Organization.objects.get(external_id=7), trade_date='2017-09-15', venue='CLEARPAR', venue_trade_id='', action='BUY', market='SECONDARY', status='ACTIVE', price=1.01375, amount=3000000),
            Trade(external_id=30, investment=Investment.objects.get(external_id=15), counterparty=Organization.objects.get(external_id=5), trade_date='2017-09-15', venue='CLEARPAR', venue_trade_id='', action='BUY', market='SECONDARY', status='ACTIVE', price=1.005, amount=5000000),
        ]
        save_items(trades)

        print('\nCreating Allocation')
        allocations = [
            Allocation(portfolio=Portfolio.objects.get(external_id=8), trade=Trade.objects.get(external_id=2), amount=4000000, status='PENDING', venue_allocation_id='001', external_id=1, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=3), amount=2500000, status='PENDING', venue_allocation_id='001', external_id=2, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=8), trade=Trade.objects.get(external_id=1), amount=4000000, status='PENDING', venue_allocation_id='001', external_id=3, settle_date='2017-07-17'),
            Allocation(portfolio=Portfolio.objects.get(external_id=11), trade=Trade.objects.get(external_id=5), amount=4227272.73, status='PENDING', venue_allocation_id='001', external_id=4, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=11), trade=Trade.objects.get(external_id=6), amount=772727.27, status='PENDING', venue_allocation_id='001', external_id=5, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=7), amount=11368421.05, status='PENDING', venue_allocation_id='001', external_id=6, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=9), trade=Trade.objects.get(external_id=7), amount=6631578.95, status='PENDING', venue_allocation_id='002', external_id=7, settle_date='2017-09-15'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=8), amount=5000000, status='PENDING', venue_allocation_id='001', external_id=8, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=2), trade=Trade.objects.get(external_id=8), amount=2000000, status='PENDING', venue_allocation_id='002', external_id=9, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=10), amount=10000000, status='PENDING', venue_allocation_id='', external_id=10, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=10), amount=3000000, status='PENDING', venue_allocation_id='', external_id=11, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=5), trade=Trade.objects.get(external_id=10), amount=7000000, status='PENDING', venue_allocation_id='', external_id=12, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=11), amount=5000000, status='PENDING', venue_allocation_id='001', external_id=13, settle_date='2017-09-05'),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=9), amount=500000, status='PENDING', venue_allocation_id='001', external_id=14, settle_date='2017-09-15'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=12), amount=6000000, status='PENDING', venue_allocation_id='001', external_id=15, settle_date='2017-09-19'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=13), amount=4915254.24, status='PENDING', venue_allocation_id='001', external_id=16, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=14), amount=5000000, status='PENDING', venue_allocation_id='001', external_id=17, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=15), amount=3000000, status='PENDING', venue_allocation_id='001', external_id=18, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=2), trade=Trade.objects.get(external_id=16), amount=6483750, status='PENDING', venue_allocation_id='', external_id=19, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=2), trade=Trade.objects.get(external_id=17), amount=270155.92, status='PENDING', venue_allocation_id='', external_id=20, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=18), amount=6483750, status='PENDING', venue_allocation_id='', external_id=21, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=19), amount=270155.92, status='PENDING', venue_allocation_id='', external_id=22, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=20), amount=5000000, status='PENDING', venue_allocation_id='001', external_id=23, settle_date='2017-09-12'),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=21), amount=500000, status='PENDING', venue_allocation_id='001', external_id=24, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=22), amount=3000000, status='PENDING', venue_allocation_id='001', external_id=25, settle_date='2017-09-15'),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=23), amount=3000000, status='PENDING', venue_allocation_id='001', external_id=26, settle_date='2017-09-15'),
            Allocation(portfolio=Portfolio.objects.get(external_id=4), trade=Trade.objects.get(external_id=24), amount=3000000, status='PENDING', venue_allocation_id='001', external_id=27, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=25), amount=3000000, status='PENDING', venue_allocation_id='001', external_id=28, settle_date='2017-09-15'),
            Allocation(portfolio=Portfolio.objects.get(external_id=2), trade=Trade.objects.get(external_id=26), amount=5000000, status='PENDING', venue_allocation_id='002', external_id=29, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=27), amount=2000000, status='PENDING', venue_allocation_id='001', external_id=30, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=5), trade=Trade.objects.get(external_id=28), amount=5000000, status='PENDING', venue_allocation_id='', external_id=31, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=29), amount=3000000, status='PENDING', venue_allocation_id='', external_id=32, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=1), trade=Trade.objects.get(external_id=30), amount=5000000, status='PENDING', venue_allocation_id='', external_id=33, ),
            Allocation(portfolio=Portfolio.objects.get(external_id=10), trade=Trade.objects.get(external_id=4), amount=0, status='PENDING', venue_allocation_id='001', external_id=34, settle_date='2017-08-21'),
        ]
        save_items(allocations)
