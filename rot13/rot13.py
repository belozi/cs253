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
    <form method="post">
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
        self.response.out.write(form % {"code": cgi.escape(code, quote = True)})

    def get(self):
        self.write_form()

    def post(self):
        code = halp.convert(self.request.get("text"))
        self.write_form(code)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug = True)
