from django.db import models

from .investment import Investment
from .organization import Organization
from django.db.models.signals import post_save

class Trade(models.Model):


    ACTIONS = (
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )
    MARKETS = (
        ('PRIMARY', 'Primary'),
        ('SECONDARY', 'Secondary'),
        ('DIRECT', 'Direct Origination'),
        ('OTHER', 'Other'),
    )
    STATUSES = (
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('CLOSED', 'Closed'),
        ('CANCELLED', 'Cancelled'),
    )
    VENUES = (
        ('CLEARPAR', 'ClearPar'),
        ('DIRECT', 'Direct Settlement'),
        ('OFFLINE', 'Offline'),
        ('OTHER', 'Other'),
    )
    PRICE_FACTOR = (
        ('ACTUAL', 'Actual'),
        ('PERCENT', 'Percent'),
    )
    CURRENCIES = (
        ('AED', 'UAE Dirham'),
        ('AFN', 'Afghani'),
        ('ALL', 'Lek'),
        ('AMD', 'Armenian Dram'),
        ('ANG', 'Netherlands Antillian Guilder'),
        ('AOA', 'Kwanza'),
        ('ARS', 'Argentine Peso'),
        ('AUD', 'Australian Dollar'),
        ('AWG', 'Aruban Guilder'),
        ('AZN', 'Azerbaijanian Manat'),
        ('BAM', 'Convertible Marks'),
        ('BBD', 'Barbados Dollar'),
        ('BDT', 'Taka'),
        ('BGN', 'Bulgarian Lev'),
        ('BHD', 'Bahraini Dinar'),
        ('BIF', 'Burundi Franc'),
        ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'),
        ('BND', 'Brunei Dollar'),
        ('BOB BOV', 'Boliviano Mvdol'),
        ('BRL', 'Brazilian Real'),
        ('BSD', 'Bahamian Dollar'),
        ('BWP', 'Pula'),
        ('BYR', 'Belarussian Ruble'),
        ('BZD', 'Belize Dollar'),
        ('CAD', 'Canadian Dollar'),
        ('CDF', 'Congolese Franc'),
        ('CHF', 'Swiss Franc'),
        ('CLP CLF', 'Chilean Peso Unidades de fomento'),
        ('CNY', 'Yuan Renminbi'),
        ('COP COU', 'Colombian Peso Unidad de Valor Real'),
        ('CRC', 'Costa Rican Colon'),
        ('CUP CUC', 'Cuban Peso Peso Convertible'),
        ('CVE', 'Cape Verde Escudo'),
        ('CZK', 'Czech Koruna'),
        ('DJF', 'Djibouti Franc'),
        ('DKK', 'Danish Krone'),
        ('DOP', 'Dominican Peso'),
        ('DZD', 'Algerian Dinar'),
        ('EEK', 'Kroon'),
        ('EGP', 'Egyptian Pound'),
        ('ERN', 'Nakfa'),
        ('ETB', 'Ethiopian Birr'),
        ('EUR', 'Euro'),
        ('FJD', 'Fiji Dollar'),
        ('FKP', 'Falkland Islands Pound'),
        ('GBP', 'Pound Sterling'),
        ('GEL', 'Lari'),
        ('GHS', 'Cedi'),
        ('GIP', 'Gibraltar Pound'),
        ('GMD', 'Dalasi'),
        ('GNF', 'Guinea Franc'),
        ('GTQ', 'Quetzal'),
        ('GYD', 'Guyana Dollar'),
        ('HKD', 'Hong Kong Dollar'),
        ('HNL', 'Lempira'),
        ('HRK', 'Croatian Kuna'),
        ('HTG USD', 'Gourde US Dollar'),
        ('HUF', 'Forint'),
        ('IDR', 'Rupiah'),
        ('ILS', 'New Israeli Sheqel'),
        ('INR', 'Indian Rupee'),
        ('INR BTN', 'Indian Rupee Ngultrum'),
        ('IQD', 'Iraqi Dinar'),
        ('IRR', 'Iranian Rial'),
        ('ISK', 'Iceland Krona'),
        ('JMD', 'Jamaican Dollar'),
        ('JOD', 'Jordanian Dinar'),
        ('JPY', 'Yen'),
        ('KES', 'Kenyan Shilling'),
        ('KGS', 'Som'),
        ('KHR', 'Riel'),
        ('KMF', 'Comoro Franc'),
        ('KPW', 'North Korean Won'),
        ('KRW', 'Won'),
        ('KWD', 'Kuwaiti Dinar'),
        ('KYD', 'Cayman Islands Dollar'),
        ('KZT', 'Tenge'),
        ('LAK', 'Kip'),
        ('LBP', 'Lebanese Pound'),
        ('LKR', 'Sri Lanka Rupee'),
        ('LRD', 'Liberian Dollar'),
        ('LTL', 'Lithuanian Litas'),
        ('LVL', 'Latvian Lats'),
        ('LYD', 'Libyan Dinar'),
        ('MAD', 'Moroccan Dirham'),
        ('MDL', 'Moldovan Leu'),
        ('MGA', 'Malagasy Ariary'),
        ('MKD', 'Denar'),
        ('MMK', 'Kyat'),
        ('MNT', 'Tugrik'),
        ('MOP', 'Pataca'),
        ('MRO', 'Ouguiya'),
        ('MUR', 'Mauritius Rupee'),
        ('MVR', 'Rufiyaa'),
        ('MWK', 'Kwacha'),
        ('MXN MXV', 'Mexican Peso Mexican Unidad de Inversion (UDI)'),
        ('MYR', 'Malaysian Ringgit'),
        ('MZN', 'Metical'),
        ('NGN', 'Naira'),
        ('NIO', 'Cordoba Oro'),
        ('NOK', 'Norwegian Krone'),
        ('NPR', 'Nepalese Rupee'),
        ('NZD', 'New Zealand Dollar'),
        ('OMR', 'Rial Omani'),
        ('PAB USD', 'Balboa US Dollar'),
        ('PEN', 'Nuevo Sol'),
        ('PGK', 'Kina'),
        ('PHP', 'Philippine Peso'),
        ('PKR', 'Pakistan Rupee'),
        ('PLN', 'Zloty'),
        ('PYG', 'Guarani'),
        ('QAR', 'Qatari Rial'),
        ('RON', 'New Leu'),
        ('RSD', 'Serbian Dinar'),
        ('RUB', 'Russian Ruble'),
        ('RWF', 'Rwanda Franc'),
        ('SAR', 'Saudi Riyal'),
        ('SBD', 'Solomon Islands Dollar'),
        ('SCR', 'Seychelles Rupee'),
        ('SDG', 'Sudanese Pound'),
        ('SEK', 'Swedish Krona'),
        ('SGD', 'Singapore Dollar'),
        ('SHP', 'Saint Helena Pound'),
        ('SLL', 'Leone'),
        ('SOS', 'Somali Shilling'),
        ('SRD', 'Surinam Dollar'),
        ('STD', 'Dobra'),
        ('SVC USD', 'El Salvador Colon US Dollar'),
        ('SYP', 'Syrian Pound'),
        ('SZL', 'Lilangeni'),
        ('THB', 'Baht'),
        ('TJS', 'Somoni'),
        ('TMT', 'Manat'),
        ('TND', 'Tunisian Dinar'),
        ('TOP', 'Paanga'),
        ('TRY', 'Turkish Lira'),
        ('TTD', 'Trinidad and Tobago Dollar'),
        ('TWD', 'New Taiwan Dollar'),
        ('TZS', 'Tanzanian Shilling'),
        ('UAH', 'Hryvnia'),
        ('UGX', 'Uganda Shilling'),
        ('USD', 'US Dollar'),
        ('UYU UYI', 'Peso Uruguayo Uruguay Peso en Unidades Indexadas'),
        ('UZS', 'Uzbekistan Sum'),
        ('VEF', 'Bolivar Fuerte'),
        ('VND', 'Dong'),
        ('VUV', 'Vatu'),
        ('WST', 'Tala'),
        ('XAF', 'CFA Franc BEAC'),
        ('XAG', 'Silver'),
        ('XAU', 'Gold'),
        ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'),
        ('XBB', 'European Monetary Unit (E.M.U.-6)'),
        ('XBC', 'European Unit of Account 9(E.U.A.-9)'),
        ('XBD', 'European Unit of Account 17(E.U.A.-17)'),
        ('XCD', 'East Caribbean Dollar'),
        ('XDR', 'SDR'),
        ('XFU', 'UIC-Franc'),
        ('XOF', 'CFA Franc BCEAO'),
        ('XPD', 'Palladium'),
        ('XPF', 'CFP Franc'),
        ('XPT', 'Platinum'),
        ('XTS', 'Codes specifically reserved for testing purposes'),
        ('YER', 'Yemeni Rial'),
        ('ZAR', 'Rand'),
        ('ZAR LSL', 'Rand Loti'),
        ('ZAR NAD', 'Rand Namibia Dollar'),
        ('ZMK', 'Zambian Kwacha'),
        ('ZWL', 'Zimbabwe Dollar'),
    )

    trade_date = models.DateField()
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    counterparty = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={ 'is_counterparty': True}
                                     )
    action = models.CharField(
        max_length=10,
        choices=ACTIONS,
        default='BUY',
    )
    market = models.CharField(
        max_length=10,
        choices=MARKETS,
        default='PRIMARY',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default='DRAFT',
    )
    venue = models.CharField(
        max_length=15,
        choices=VENUES,
        default='CLEARPAR',
    )
    venue_trade_id = models.CharField(max_length=50, null=True, blank=True)

    currency = models.CharField(
        max_length=15,
        choices=CURRENCIES,
        default='USD',
    )

    price = models.FloatField()
    price_factor = models.CharField(
        max_length=15,
        choices=PRICE_FACTOR,
        default=100,
    )
    quantity = models.FloatField()

    fee = models.FloatField(blank=True, null=True)
    fee_factor = models.CharField(
        max_length=15,
        choices=PRICE_FACTOR,
        default=100,
        blank=True,
        null=True
    )
    fee_quantity = models.FloatField(blank=True, null=True)

    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)

    external_id = models.CharField(max_length=50, null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    @property
    def _get_net_proceeds(self):
        "Returns the trade net proceeds."
        return self.price * self.price_factor * self.amount

    def __str__(self):
       return '[{}] {} on {}'.format(self.action, self.investment.name, self.trade_date)


def send_notifications(sender, **kwargs):
    instance = kwargs['instance']
    print('\n> Trade Saved', instance)
    # q = Requirement.objects.all().filter(portfolio=instance.portfolio)

    # Path.objects.filter(allocation=instance).delete()
    #
    # for r in q:
    #     print('\t', r.condition)
    #     if (r.condition.condition == 'DEFAULT'):
    #         Path.objects.create(allocation=instance, requirement=r)
    #         print('\t\t> Default')
    #
    #     if ((r.condition.condition == 'COINVEST') & (instance.coinvest == True)):
    #         Path.objects.create(allocation=instance, requirement=r)
    #         print('\t\t> Co-Invest')
    #
    #     if ((r.condition.condition == 'BUY') & (instance.trade.action == 'BUY')):
    #         Path.objects.create(allocation=instance, requirement=r)
    #         print('\t\t> Buy')

post_save.connect(send_notifications, sender=Trade)
