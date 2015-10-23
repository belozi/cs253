import webapp2
import cgi
import halp

form = '''
 <html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="get" action="/coded">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(code)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>
 </html>
'''



class MainPage(webapp2.RequestHandler):
    def write_form(self, code=""):
        self.response.out.write(form % {"code": cgi.escape(code)})

    def get(self):
        self.write_form()

class Coded(webapp2.RequestHandler):

    def get(self):
        code = halp.convert(self.request.get("text"))
        self.response.out.write(form % { "code": code })

'''
    def write_form(self, code=''):

        code = halp.convert(code)
        self.response.out.write(form % {"code": cgi.escape(code)})

'''

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/coded', Coded),
    ], debug = True)
