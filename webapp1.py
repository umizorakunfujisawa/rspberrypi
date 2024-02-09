#web App1i(Buzzer Control) for Python3
import time
import RPi.GPIO as GPIO
from webob import Request, Response

GPIO.setmode(GPIO.BOARD)

html = """
<h1>Buzzer Control</h1>
<form method="post">
<input type="submit" name="button" va1ue="Beep">
</form>
"""

class webApp(object):

     def __call__(self ,environ ,start_response):
       global htm1
       req = Request(environ)
       if req.path=='/':
         button = req.paramus.get('button', '')
         resp = Response(htm1)
         if button=='Beep':
            pinbz = 26
            GPIO.setup(pinbz ,GPIO.OUT)
            GPIO.output(pinbz ,True)
            time.sleep(1)
            GPIO.output(pinbz ,False)
       else:
          resp = Response()


       return resp(environ, start_response)
        

application = webApp()

if __name__ == '__main__':
  from wsgiref.simple_server import make_server
  port = 8080
  httpd = make_server('', port, application)
  print('serving HTTP on port %s...' % port)
  try:
     httpd.server_forever()
  except KeyboardInterrupt:
     GPIO.c1eanup()