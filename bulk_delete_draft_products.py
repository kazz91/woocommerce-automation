#Adicionando Recorrencia (subscription) aos produtos usando o plugin 'WooCommerce Subscriptions'

#instalar woocommerce
!pip install woocommerce

from woocommerce import API

print("Insira o percentual do Programe e Economize para o produto: (somente número)")
print()
porcentagem = int(input())
print()

#Using the API method from Woocommerce librarie THOMA,S COELHO
wcapi = API(
    url = 'sua_url',
    consumer_key='sua_consumer_key',
    consumer_secret='sua_consumer_secret',
    timeout=400,
    version="wc/v3",
    )

data = {
        "meta_data": [
        {
            "id": 268862,
            "key": "video_position",
            "value": "1"
        },
        {
            "id": 268863,
            "key": "_coupon_title",
            "value": []
        },
        {
            "id": 268864,
            "key": "send_coupons_on_renewals",
            "value": "no"
        },
        {
            "id": 268865,
            "key": "custom_badges_text",
            "value": ""
        },
        {
            "id": 268866,
            "key": "_is_new",
            "value": "0"
        },
        {
            "id": 268867,
            "key": "mf_pbt_product_ids",
            "value": "0"
        },
        {
            "id": 165898,
            "key": "_wcsatt_schemes",
            "value": [
                {
                    "subscription_period_interval": "1",
                    "subscription_period": "week",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "0",
                    "subscription_price": ""
                },
                {
                    "subscription_period_interval": "2",
                    "subscription_period": "week",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "1",
                    "subscription_price": ""
                },
                {
                    "subscription_period_interval": "3",
                    "subscription_period": "week",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "2",
                    "subscription_price": ""
                },
                {
                    "subscription_period_interval": "1",
                    "subscription_period": "month",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "3",
                    "subscription_price": ""
                },
                {
                    "subscription_period_interval": "6",
                    "subscription_period": "week",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "4",
                    "subscription_price": ""
                },
                {
                    "subscription_period_interval": "2",
                    "subscription_period": "month",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "5",
                    "subscription_price": ""
                },
                {
                    "subscription_period_interval": "3",
                    "subscription_period": "month",
                    "subscription_length": "0",
                    "subscription_payment_sync_date": 0,
                    "subscription_payment_sync_date_month": "0",
                    "subscription_payment_sync_date_day": "1",
                    "subscription_pricing_method": "inherit",
                    "subscription_regular_price": "",
                    "subscription_sale_price": "",
                    "subscription_discount": porcentagem,
                    "position": "6",
                    "subscription_price": ""
                }
            ]
        },
        {
            "id": 165899,
            "key": "_subscription_one_time_shipping",
            "value": "no"
        },
        {
            "id": 165900,
            "key": "_wcsatt_default_status",
            "value": "one-time"
        },
        {
            "id": 165901,
            "key": "_wcsatt_force_subscription",
            "value": "no"
        },
        {
            "id": 165902,
            "key": "_wcsatt_layout",
            "value": "grouped"
        },
        {
            "key": "_satt_data",
            "value": {
                "subscription_schemes": {
                    "1_week": {},
                    "2_week": {},
                    "3_week": {},
                    "1_month": {},
                    "6_week": {},
                    "2_month": {},
                    "3_month": {}
                },
                "has_forced_subscription": "no",
                "active_subscription_scheme_key": "",
            }
        }
    ]
}


ids = []



print("Insira a ID do produto a ser atualizado:")
print("(OBS: Se for um produto com variações, indique somente o ID do produto pai)")
print()
idinputada = str(input())
print()


xis= idinputada.strip()
ze = 'products/'+xis
atualizar = wcapi.put(ze, data).json()
print('O produto de ID',xis,'foi atualizado com o Programe e Economize com',porcentagem,'% off!')
print()    
