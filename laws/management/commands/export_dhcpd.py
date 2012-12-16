from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from laws.models import *

import sys

tpl = 'host h{id} {{ hardware ethernet {mac_addr}; fixed-address {ipv4}; option host-name "{hostname}"; }}\n'

class Command(BaseCommand):
    args = '[filename]'
    help = 'write dhcpd config.'
    
    def handle(self, *args, **options):
        f = sys.stdout
        if args:
            f = open(args[0], 'wb')
        
        for i in Instance.objects.all():
            f.write(tpl.format(
                id       = i.id,
                mac_addr = i.mac_addr,
                ipv4     = i.ipv4,
                hostname = i.hostname,
            ))

            
