#!/usr/bin/env python 
import webapp2

MAIN_PAGE_HTML = """\
<!doctype html>
<html>
  <body>
    under construction
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
