import sys
import unittest
from datetime import datetime
import time
from uuid import uuid4
import random
from .client import FetchApp
from .client import FetchAppAuthenticationException
from .client import FetchAppInvalidOrderTypeException
import pprint
try:
    import config
except Exception, e:
    print """

Could not find config.py. Please add a module to your path with
strings FETCHAPP_KEY and FETCHAPP_TOKEN

See: See http://YOUR_STORE_NAME.fetchapp.com/admin/settings/payments

"""
    raise e

PP = pprint.PrettyPrinter(indent=4)


class FetchAppTest(unittest.TestCase):

    def setUp(self):
        self.fa = FetchApp(config.FETCHAPP_KEY, config.FETCHAPP_TOKEN)
        pass

    def tearDown(self):
        pass

    '''def test_00_account(self):
        name = str(uuid4())
        first_name = str(uuid4())
        last_name = str(uuid4())
        email = config.TEST_EMAIL
        url = str(uuid4())[0:12].replace("-", "")
        account = self.fa.account_create(
            name,
            first_name,
            last_name,
            email,
            url
        )
        self.assertTrue("api_key" in account)
        if config.DEBUG:
            PP.pprint("FetchApp.account_create(...)")
            PP.pprint(account)
        fa = FetchApp(account["api_key"], account["api_token"])
        account_data = fa.account()
        self.assertTrue("email" in account_data)
        if config.DEBUG:
            PP.pprint("FetchApp.account(...)")
            PP.pprint(account_data)'''

    '''def test_01_products(self):
        products =  self.fa.products()
        self.assertTrue(isinstance(products, list))
        if config.DEBUG:
            PP.pprint("FetchApp.products(...)")
            PP.pprint(products)'''

    '''def test_02_products(self):
        # Create
        sku = str(uuid4())
        name = str(uuid4())
        price = "%s.%s" % (random.randint(10,99),random.randint(10,99))
        description = str(uuid4())
        product = self.fa.product_create(
            sku,
            name,
            price,
            description)
        self.assertTrue("sku" in product)
        if config.DEBUG:
            PP.pprint("FetchApp.product_create(...)")
            PP.pprint(product)
        # List files
        files = self.fa.product_list_files(product["sku"])
        self.assertTrue(isinstance(files, list))
        if config.DEBUG:
            PP.pprint("FetchApp.product_list_files(...)")
            PP.pprint(files)
        # List downloads
        downloads = self.fa.product_list_downloads(product["sku"])
        self.assertTrue(isinstance(downloads, list))
        if config.DEBUG:
            PP.pprint("FetchApp.product_list_downloads(...)")
            PP.pprint(downloads)
        # Details
        product_details = self.fa.product_details(product["sku"])
        self.assertTrue("sku" in product_details)
        if config.DEBUG:
            PP.pprint("FetchApp.product_details(...)")
            PP.pprint(product_details)
        # Update
        new_sku = str(uuid4())
        new_name = str(uuid4())
        new_price = "%s.%s" % (random.randint(10,99),random.randint(10,99))
        new_description = str(uuid4())
        product = self.fa.product_update(
            product_details["sku"],
            new_sku=new_sku,
            name=new_name,
            price=new_price,
            description=new_description)
        product_details = self.fa.product_details(new_sku)
        product_stats = self.fa.product_stats(new_sku)
        self.assertEqual(product_details["sku"], new_sku)
        self.assertEqual(product_details["name"], new_name)
        self.assertEqual(product_details["price"], float(new_price))
        self.assertEqual(product_details["description"], new_description)
        if config.DEBUG:
            PP.pprint("FetchApp.product_update(...)")
            PP.pprint(product_details)
            PP.pprint(product_stats)
        response = self.fa.product_delete(product["sku"])
        self.assertTrue(response)'''

    '''def test_03_orders(self):
        orders = self.fa.orders()
        self.assertTrue(isinstance(orders, list))
        if config.DEBUG:
            PP.pprint("FetchApp.orders(...)")
            PP.pprint(orders)'''

    def test_04_order(self):
        # Create products to order.
        products =  self.fa.products()
        self.assertTrue(len(products) > 0)
        skus = []
        for product in products:
            if product["files_count"] > 0:
                skus.append(product["sku"])
                if len(skus) == 2:
                    break
        # Order the products.
        order_id = str(uuid4())
        first_name = str(uuid4())
        last_name = str(uuid4())
        custom_fields = []
        TEST_NUM_FIELDS = 2
        for i in range(1, TEST_NUM_FIELDS+1):
            custom_fields.append(str(uuid4()))
        email = config.TEST_EMAIL
        expiration_date = datetime.fromtimestamp(time.time() + 24 * 60 * 60)
        send_email = True
        download_limit = 5
        ignore_products = True
        order = self.fa.order_create(
            order_id,
            first_name,
            last_name,
            email,
            custom_fields,
            skus,
            expiration_date=expiration_date,
            send_email=send_email,
            download_limit=download_limit,
            ignore_products=ignore_products)
        self.assertTrue("id" in order)
        if config.DEBUG:
            PP.pprint("FetchApp.order_create(...)")
            PP.pprint(order)
        # Update the order
        new_title = str(uuid4())
        new_first_name = str(uuid4())
        new_last_name = str(uuid4())
        new_email = config.TEST_EMAIL
        new_custom_fields = []
        TEST_NUM_FIELDS = 3
        for i in range(1, TEST_NUM_FIELDS+1):
            new_custom_fields.append(str(uuid4()))
        new_skus = skus
        new_expiration_date = datetime.fromtimestamp(time.time() + 24 * 60 * 60)
        new_send_email = True
        new_download_limit = 5
        new_ignore_products = True
        new_order = self.fa.order_update(
            order_id=order["id"],
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            custom_fields=new_custom_fields,
            skus=new_skus,
            expiration_date=new_expiration_date,
            send_email=new_send_email,
            download_limit=new_download_limit,
            ignore_products=new_ignore_products)
        self.assertTrue("id" in new_order)
        if config.DEBUG:
            PP.pprint("FetchApp.order_update(...)")
            PP.pprint(new_order)
        # Get order details
        order_details = self.fa.order_details(order["id"])
        self.assertTrue("id" in order_details)
        if config.DEBUG:
            PP.pprint("FetchApp.order_details(...)")
            PP.pprint(order_details)
        # Check updates
        self.assertEqual(order_details["first_name"], new_first_name)
        self.assertEqual(order_details["last_name"], new_last_name)
        self.assertEqual(order_details["email"], new_email)
        # Send order email
        response = self.fa.order_send_email(order["id"])
        self.assertTrue(response)
        # List order downloads
        downloads = self.fa.order_downloads(order["id"])
        # List order stats
        stats = self.fa.order_stats(order["id"])
        if config.DEBUG:
            PP.pprint("FetchApp.order_downloads(...)")
            PP.pprint(downloads)
            PP.pprint("FetchApp.order_stats(...)")
            PP.pprint(stats)
        # List order items
        items = self.fa.order_list_items(new_order["id"])
        single_item = self.fa.order_item_details(new_order["id"], new_skus[0])
        if config.DEBUG:
            PP.pprint("FetchApp.order_list_items(...)")
            PP.pprint(items)
            PP.pprint("FetchApp.order_item_details(...)")
            PP.pprint(single_item)
        # List order item files
        #throw exception -> bad = self.fa.order_item_files(new_order["id"], None)
        files = self.fa.order_item_files(new_order["id"], new_skus[0])
        # List order item downloads
        downloads = self.fa.order_item_downloads(new_order["id"], new_skus[0])
        if config.DEBUG:
            PP.pprint("FetchApp.order_item_files(...)")
            PP.pprint(files)
            PP.pprint("FetchApp.order_item_downloads(...)")
            PP.pprint(downloads)
        # Expire one item
        #response = self.fa.order_item_expire(order["id"], new_skus[0])
        #self.assertTrue(response)
        # Expire the order
        response = self.fa.order_expire(order["id"])
        self.assertTrue(response)
        # Delete the order
        response = self.fa.order_delete(order["id"])
        self.assertTrue(response)

    '''def test_05_files(self):
        files = self.fa.files()
        self.assertTrue(isinstance(files, list))
        if config.DEBUG:
            PP.pprint("FetchApp.files(...)")
            PP.pprint(files)'''

    '''def test_06_downloads(self):
        downloads = self.fa.downloads()
        self.assertTrue(isinstance(downloads, list))
        if config.DEBUG:
            PP.pprint("FetchApp.downloads(...)")
            PP.pprint(downloads)'''

    '''def test_07_new_token(self):
        token = self.fa.new_token()
        if config.DEBUG:
            PP.pprint("FetchApp.token(...)")
            PP.pprint(token)'''
