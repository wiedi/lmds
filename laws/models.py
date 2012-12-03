from django.db import models
import base64

default_length = 250

"""
def instance_id_from_mac(mac):
    bar = 0x424152 # "bar"
    return 'i-' + hex(bar ^ int(''.join(mac.split(':')[3:]), 16))[2:]
"""


class Instance(models.Model):
    hostname   = models.CharField(max_length=default_length)
    mac_addr   = models.CharField(max_length=18)
    ipv4       = models.CharField(max_length=18)
    _user_data = models.TextField(db_column='user_data', blank=True)
    
    def set_user_data(self, user_data):
        self._user_data = base64.encodestring(user_data)

    def get_user_data(self):
        return base64.decodestring(self._user_data)

    user_data = property(get_user_data, set_user_data)
    
    def instance_id(self):
        return 'i-' + ''.join(self.mac_addr.split(':')[3:])