import webapp2
import string

form = '''
<form method="post" action="/Coded">
    <input type="textarea" name="code" value="">
    <input type="submit">
</form>
'''

message = "Hello, everyone! What are your names?"



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

class Coded(webapp2.RequestHandler):
    def post(self):
        code = slef.request.get("code")
        
    def shift(char):
    # This is the 13 character shift for each character
        ascii = ord(char) + 13
        if  ascii > 122:
            char = chr((97 + (ascii - 123)))
            return char
        
        return chr((ord(char) + 13))

    def convert(text):
    # This is the method that converts the message
        code = []
        for char in text:
            cap = False
        
            if char in string.uppercase:
                cap = True
                new_char = shift(char.lower())
                code.append(chr(ord(new_char) - 32))
            elif char in string.lowercase:
                code.append(shift(char))
            else:
                code.append(char)

        return ''.join(code)
    
app = webapp2.WSGIApplication([
    ('/', Mainpage),
    ('/coded', Coded),
    ], debug = True)

print convert(message)
