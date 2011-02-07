from urllib import urlencode


VALID_ITEM_PROPERTIES = []
VALID_ORDER_PROPERTIES = []


class FetchAppAuthenticationException(Exception):
    """Raised when authentication fails."""
    pass


class FetchAppInvalidPropertyException(Exception):
    """
    Raised when an unsupported property is passed to
    the create or update item or order methods.
    """
    pass


class FetchAppInvalidOrderTypeException(Exception):
    """
    Raised when an unsupported order type is passed to
    the orders methods.
    """
    pass


class FetchApp(object):
    """
    Support for the FetchApp API.
    http://www.fetchapp.com/pages/help-api
    """

    def __init__(self, key, token):
        self.key = key
        self.token = token
    
    def account(self):
        """Information about your account."""
        
        path = "/api/account"
        xmldoc = self._call(path)
        return self._deserialize(xmldoc)

    def new_token(self):
        """Generate a new API token (this replaces your existing one)"""
        
        path = "/api/new_token"
        xmldoc = self._call(path)
        data = self._deserialize(xmldoc)
        return data["message"]
        
    def downloads(self, per_page=None, page=None):
        """List your downloads"""
        
        path = "/api/downloads"
        parameters = {}
        if per_page is not None:
            parameters["per_page"] = int(per_page)
        if page is not None:
            parameters["page"] = int(page)
        xmldoc = self._call(path, parameters=parameters)
        return self._deserialize(xmldoc)        
    
    def items(self, per_page=None, page=None, sku=None):
        """List your items"""
        
        path = "/api/items"
        if sku is not None:
            path = "%s/:%s" % (path, sku)
        parameters = {}
        if per_page is not None:
            parameters["per_page"] = int(per_page)
        if page is not None:
            parameters["page"] = int(page)
        xmldoc = self._call(path, parameters=parameters)
        return self._deserialize(xmldoc)

    def item_details(self, sku):
        """List details of a specified item"""
        
        path = "/api/items/:%s" % sku
        xmldoc = self._call(path)
        return self._deserialize(xmldoc)
    
    def item_delete(self, sku):
        """Delete a specified item"""
        
        path = "/api/items/:%s/delete" % sku
        xmldoc = self._call(path, method="delete")
        return self._deserialize(xmldoc)
    
    def item_create(self, **kwargs):
        """Create a specified item"""
        
        path = "/api/items/create"
        parameters = {}
        for key in kwargs:
            if key in VALID_ITEM_PROPERTIES:
                parameters[key] = kwargs[key]
            else:
                raise FetchAppInvalidPropertyException(key)
        xmldoc = self._call(path, parameters=parameters, method="post")
        return self._deserialize(xmldoc)
    
    def item_update(self, sku, **kwargs):
        """Update a specified item"""
        
        path = "/api/items/:%s/items" % sku
        parameters = {}
        for key in kwargs:
            if key in VALID_ITEM_PROPERTIES:
                parameters[key] = kwargs[key]
            else:
                raise FetchAppInvalidPropertyException(key)
        xmldoc = self._call(path, parameters=parameters, method="put")
        return self._deserialize(xmldoc)        
    
    def list_files(self, sku):
        """List all the files for an item."""
        
        path = "/api/items/:%s/files" % sku
        xmldoc = self._call(path)
        return self._deserialize(xmldoc)       

    def list_downloads(self, sku):
        """List all the downloads for an item"""
        
        path = "/api/items/:%s/downloads" % sku
        xmldoc = self._call(path)
        return self._deserialize(xmldoc)
    
    def orders(self, per_page=None, page=None, type=None):
        """List all your orders"""
        
        path = "/api/orders"
        parameters = {}
        if type not in [None, "current", "manual", "expired"]:
            raise FetchAppInvalidOrderTypeException(type)
        if type is None:
            if per_page is not None:
                parameters["per_page"] = int(per_page)
            if page is not None:
                parameters["page"] = int(page)
        else:
            subparameters = {}
            if per_page is not None:
                subparameters["per_page"] = int(per_page)
            if page is not None:
                subparameters["page"] = int(page)  
            parameters["filter"] = "<type>%s</type>" % urlencode(subparameters)
        xmldoc = self._call(path, parameters)
        return self._deserialize(xmldoc)        
    
    def order_details(self, order_id):
        """Details of a specified order"""
        
        path = "/api/orders/:%s" % order_id
        xmldoc = self._call(path)
        return self._deserialize(xmldoc)        
    
    def order_delete(self, order_id):
        """Delete a specified order"""
        
        path = "/api/orders/:%s/delete" % order_id
        xmldoc = self._call(path, method="delete")
        return self._deserialize(xmldoc)

    def order_expire(self, order_id):
        """Expire a specified order"""
        
        path = "/api/orders/:%s/expire" % order_id
        xmldoc = self._call(path, method="post")
        return self._deserialize(xmldoc)

    def order_send_email(self, order_id):
        """Send download email of a specified order"""
        
        path = "/api/orders/:%s/send_email" % order_id
        xmldoc = self._call(path, method="post")
        return self._deserialize(xmldoc)

    def order_create(self, **kwargs):
        """Create an order"""
        
        path = "/api/orders/create"
        parameters = {}
        for key in kwargs:
            if key in VALID_ORDER_PROPERTIES:
                parameters[key] = kwargs[key]
            else:
                raise FetchAppInvalidPropertyException(key)
        xmldoc = self._call(path, parameters=parameters, method="post")
        return self._deserialize(xmldoc)

    def order_update(self, order_id, **kwargs):
        """Update a specified order"""
        
        path = "/api/orders/:%s/update" % order_id
        parameters = {}
        for key in kwargs:
            if key in VALID_ORDER_PROPERTIES:
                parameters[key] = kwargs[key]
            else:
                raise FetchAppInvalidPropertyException(key)
        xmldoc = self._call(path, parameters=parameters, method="post")
        return self._deserialize(xmldoc)
    
    def uploads(self, per_page=None, page=None):
        """List your uploads"""
        
        path = "/api/uploads"
        parameters = {}
        if per_page is not None:
            parameters["per_page"] = int(per_page)
        if page is not None:
            parameters["page"] = int(page)
        xmldoc = self._call(path, parameters=parameters)
        return self._deserialize(xmldoc)
    
    def _deserialize(self, xmldoc):
        return None
        
    def _call(self, path, parameters=None, method="get"):
        return None