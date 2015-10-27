import webapp2
import validate

form = '''
<html>
    <head>
        <title>Sign Up</title>
        <style type="text/css">
            .label {text-align:right}
            .error {color: red}
        </style>
    <head>

    <h1>Signup</h1>
    <form method="post" action="/success">
        <table>
            <tr>
                <td class="label">
                    Username
                </td>
                <td>
                    <input name="username" value="%(name)s">
                <td>
                <td class="error">
                    %(invalid_name)s
                </td>
            </tr>
            <tr>
                <td class="label">
                    Password
                </td>
                <td>
                    <input type="password" name="password" value="%(password)s">
                </td>
                <td class="error">
                    %(invalid_password)s
                </td>
            <tr>
                <td class="label">
                    Verify Password
                </td>
                <td>
                    <input type="password" name="verify" value="%(verify)s">
                </td>
                <td class="error">
                    %(no_match)s
                </td>
            <tr>
                <td class="label">
                    Email(optional)
                </td>
                <td>
                    <input name="email" value="%(email)s">
                </td>
                <td class="error">
                    %(invalid_email)s
                </td>
        </table>
        <input type="submit">

        </form>
'''

form2 = '''
<html>
  <head>
    <title>Unit 2 Signup</title>
  </head>

  <body>
    <h2>Welcome, %(name)s</h2>
  </body>
</html>
'''

class MainPage(webapp2.RequestHandler):
    def write_form(self, name='',
                    invalid_name='',
                    password='',
                    invalid_password='',
                    verify='',
                    no_match='',
                    email='',
                    invalid_email=''):
        self.response.out.write(form % {"name": name,
                                        "invalid_name": invalid_name,
                                        "password": password,
                                        "invalid_password": invalid_password,
                                        "verify": verify,
                                        "no_match": no_match,
                                        "email": email,
                                        "invalid_email": invalid_email})
    def get(self):
        self.write_form()

    def post(self):
        mail = self.request.get("email")
        user_name = valid_name(self.request.get("name"))
        user_password = valid_passwd(self.request.get("password"))
        user_verify = valid_passwd(self.request.get("verify"))
        user_email = valid_email(mail)
        match = (user_password == user_verify)
'''
        valid_user = [user_name, user_password,no_match]

        if user_name == '':
            invalid_name = "Your username is invalid"

        if user_password == '':
            invalid_password = "Your password is invalid"

        if match(user_password, user_verify) == False:
            no_match = "Your varification does not match your password"

        if mail and user_email == '':
            user_email = "Your email is invalid"

        for x in valid_user:
            if x != '':
                self.write_form()


        self.redirect('/success', username)

'''
        self.response.out.write(self.request)

class SuccessHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(form2 % name)

    def post(self):
        name = self.response.get("user_name")


app = webapp2.WSGIApplication([('/', MainPage),
                                ('/success', SuccessHandler),
                                ], debug=True)
