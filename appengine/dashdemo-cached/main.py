import webapp2
import bqclient
import httplib2
import logging
import os
from django.utils import simplejson as json
from google.appengine.ext.webapp.template import render
from oauth2client.appengine import oauth2decorator_from_clientsecrets
from google.appengine.api.memcache import Client

# CLIENT_SECRETS, name of a file containing
# the OAuth 2.0 information for this application,
# including client_id and client_secret, which are found
# on the API Access tab on the Google APIs Console # 
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Project ID for a project where you and your users
#   are viewing members.  This is where the bill will be sent.
#   During the limited availability preview, there is no bill.
# Replace this value with the Client ID value from your project,
#   the same numeric value you used in client_secrets.json  
BILLING_PROJECT_ID = "475473128136"
DATA_PROJECT_ID = "publicdata"
DATASET = "samples"
TABLE = "natality"
QUERY = """
select state, SUM(gestation_weeks) / COUNT(gestation_weeks) as weeks 
from publicdata:samples.natality 
where year > 1990 and year < 2005 and IS_EXPLICITLY_DEFINED(gestation_weeks) 
group by state order by weeks
"""
decorator = oauth2decorator_from_clientsecrets(CLIENT_SECRETS,
    'https://www.googleapis.com/auth/bigquery')

mem = Client()

class InfoHandler(webapp2.RequestHandler):
    @decorator.oauth_aware
    def get(self):
        self.response.out.write(decorator.authorize_url())

class MainHandler(webapp2.RequestHandler):
    def _bq4geo(self, bqdata):
        """geodata output for region maps must be in the format region, value.
           Assume the BigQuery query output is in this format and get names from schema.
        """
        columnNameGeo = bqdata["schema"]["fields"][0]["name"]
        columnNameVal = bqdata["schema"]["fields"][1]["name"]
        #logging.info("Column Names=%s, %s" % (columnNameGeo, columnNameVal))
        geodata = [];
        geodata.append((columnNameGeo,columnNameVal))
        logging.info(geodata)
        for row in bqdata["rows"]:
            geodata.append(("US-"+row["f"][0]["v"],row["f"][1]["v"]))
        Wlogging.info("FINAL GEODATA---")
        #logging.info(geodata)
        return json.dumps(geodata, ensure_ascii=True)
        
    @decorator.oauth_required
    def _bq2geo(self ):
        """geodata output for region maps must be in the format region, value.
           Assume the BigQuery query output is in this format and get names from schema.
        """
        http = decorator.http()
        bq = bqclient.BigQueryClient(http, decorator)
        bqdata = bq.Query(QUERY, BILLING_PROJECT_ID)
        #logging.info(bqdata)
        columnNameGeo = bqdata["schema"]["fields"][0]["name"]
        columnNameVal = bqdata["schema"]["fields"][1]["name"]
        #logging.info("Column Names=%s, %s" % (columnNameGeo, columnNameVal))
        geodata = {}
        geodata["rows"] = [];
        logging.info(geodata)
        for row in bqdata["rows"]:
            newrow = ({"c":[]})
            newrow["c"].append({"v": "US-"+row["f"][0]["v"]})
            newrow["c"].append({"v":row["f"][1]["v"]})
            geodata["rows"].append(newrow)
        geodata["cols"] = ({"id":columnNameGeo,"label":columnNameGeo,"type":"string"}, 
                           {"id":columnNameVal, "label":columnNameVal, "type":"number"})
        logging.info("FINAL GEODATA---")
        logging.info(geodata)
        return json.dumps(geodata, ensure_ascii=True)
        
    def get(self):
        data = mem.get('natality')
        if not(data):    
            values = self._bq2geo()
            data = { 'data': values,
                     'query': QUERY }
            mem.set('natality', data)
        template = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(render(template, data))

application = webapp2.WSGIApplication([
   ('/', MainHandler),
   ('/info', InfoHandler),
   (decorator.callback_path, decorator.callback_handler()),
], debug=True)
