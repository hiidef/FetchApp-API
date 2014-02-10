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
    
    def test_00_account(self):
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
            PP.pprint(account_data)
            
    '''def test_01_items(self):
        items =  self.fa.items()
        self.assertTrue(isinstance(items, list))
        if config.DEBUG: 
            PP.pprint("FetchApp.items(...)")
            PP.pprint(items)'''
            
    '''def test_02_item(self):
        # Create
        sku = str(uuid4())
        name = str(uuid4())
        price = "%s.%s" % (random.randint(10,99),random.randint(10,99))
        item = self.fa.item_create(
            sku,
            name,
            price)
        self.assertTrue("sku" in item)
        if config.DEBUG: 
            PP.pprint("FetchApp.item_create(...)")
            PP.pprint(item)
        # List files
        files = self.fa.item_list_files(item["sku"])
        self.assertTrue(isinstance(files, list))
        if config.DEBUG: 
            PP.pprint("FetchApp.item_list_files(...)")
            PP.pprint(files)
        # List downloads
        downloads = self.fa.item_list_downloads(item["sku"])
        self.assertTrue(isinstance(downloads, list))
        if config.DEBUG: 
            PP.pprint("FetchApp.item_list_downloads(...)")
            PP.pprint(downloads)
        # Details
        item_details = self.fa.item_details(item["sku"])
        self.assertTrue("sku" in item_details)
        if config.DEBUG: 
            PP.pprint("FetchApp.item_details(...)")
            PP.pprint(item_details)
        # Update
        new_sku = str(uuid4())
        new_name = str(uuid4())
        new_price = "%s.%s" % (random.randint(10,99),random.randint(10,99))
        item = self.fa.item_update(
            item_details["sku"],
            new_sku=new_sku,
            name=new_name,
            price=new_price)
        item_details = self.fa.item_details(new_sku)
        self.assertEqual(item_details["sku"], new_sku)
        self.assertEqual(item_details["name"], new_name)
        self.assertEqual(item_details["price"], float(new_price))
        if config.DEBUG: 
            PP.pprint("FetchApp.item_update(...)")
            PP.pprint(item_details)
        response = self.fa.item_delete(item["sku"])
        self.assertTrue(response)'''

    '''def test_03_orders(self):
        orders = self.fa.orders()
        self.assertTrue(isinstance(orders, list))         
        if config.DEBUG: 
            PP.pprint("FetchApp.orders(...)")
            PP.pprint(orders)'''
                   
    '''def test_04_order(self):
        # Create an item to order.
        items =  self.fa.items()
        self.assertTrue(len(items) > 0)
        for item in items:
            if len(item["files"]) > 0:
                break
        # Order the item.
        order_id = str(uuid4())
        title = str(uuid4())
        first_name = str(uuid4())
        last_name = str(uuid4())
        email = config.TEST_EMAIL
        skus = [item["sku"]]
        expiration_date = datetime.fromtimestamp(time.time() + 24 * 60 * 60)
        send_email = True
        download_limit = 5
        ignore_items = True
        order = self.fa.order_create(
            order_id,
            title,
            first_name,
            last_name,
            email,
            skus,
            expiration_date=expiration_date,
            send_email=send_email,
            download_limit=download_limit,
            ignore_items=ignore_items)
        self.assertTrue("id" in order) 
        if config.DEBUG: 
            PP.pprint("FetchApp.order_create(...)")
            PP.pprint(order)
        # Update the order
        new_title = str(uuid4())
        new_first_name = str(uuid4())
        new_last_name = str(uuid4())
        new_email = config.TEST_EMAIL
        new_skus = [item["sku"]]
        new_expiration_date = datetime.fromtimestamp(time.time() + 24 * 60 * 60)
        new_send_email = True
        new_download_limit = 5
        new_ignore_items = True
        new_order = self.fa.order_update(
            order_id=order["id"],
            title=new_title,
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            skus=new_skus,
            expiration_date=new_expiration_date,
            send_email=new_send_email,
            download_limit=new_download_limit,
            ignore_items=new_ignore_items)
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
        self.assertEqual(order_details["title"], new_title)
        self.assertEqual(order_details["first_name"], new_first_name)
        self.assertEqual(order_details["last_name"], new_last_name)
        self.assertEqual(order_details["email"], new_email)
        # Send order email
        response = self.fa.order_send_email(order["id"])
        self.assertTrue(response)        
        # Expire the order
        response = self.fa.order_expire(order["id"])
        self.assertTrue(response)
        # Delete the order
        response = self.fa.order_delete(order["id"])
        self.assertTrue(response)'''
        
    '''def test_05_uploads(self):
        uploads = self.fa.uploads()
        self.assertTrue(isinstance(uploads, list))
        if config.DEBUG: 
            PP.pprint("FetchApp.uploads(...)")
            PP.pprint(uploads)'''

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

