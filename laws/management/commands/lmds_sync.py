from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import sqlite3
import urllib
import csv

class Command(BaseCommand):
    args = ''
    help = 'called by limed. syncs local db with limeade.'
    
    def handle(self, *args, **options):
        
        url = settings.LIMEADE_MASTER + '/cloud/api/lmds_sync/' + settings.LIMEADE_ZONE
        try:
            f = open(urllib.urlretrieve(url)[0])
        except:
            raise CommandError('Failed to communicate with limeade. Aborting sync...')
            
        con = sqlite3.connect(settings.DATABASES['default']['NAME'], isolation_level = 'EXCLUSIVE')
        
        con.execute('begin transaction;')
        con.execute('delete from laws_instance;')
        con.executemany(u"insert into laws_instance (id, hostname, mac_addr, ipv4, user_data) values (?, ?, ?, ?, ?)", csv.reader(f))
        
        con.commit()
        f.close()