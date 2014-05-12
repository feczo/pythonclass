#!/usr/bin/env python


"""Modification of the ApiCallHandler in order to add a blacklist.
"""

import logging

import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.remote_api import handler as remote_api_handler

email_blacklist = ['user1@email.com', 'user2@email.com']


class ApiCallHandler(remote_api_handler.ApiCallHandler):

  def CheckIsAdmin(self):
    user_email = users.get_current_user().email()

    if user_email in email_blacklist:
      logging.warning('User %s is denied.' % user_email)
      self.response.set_status(403)
      self.response.out.write('Usage not permitted. '
                              'Please contact your administrator')
      self.response.headers['Content-Type'] = 'text/plain'
      return False
    return remote_api_handler.ApiCallHandler.CheckIsAdmin(self)


application = webapp.WSGIApplication([('.*', ApiCallHandler)])


def main():
  # remote_api_handler.main()
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
