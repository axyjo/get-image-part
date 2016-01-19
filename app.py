import io
import time
import random
import os

from flask import Flask, request, Response

from PIL import Image
from gevent import monkey; monkey.patch_all()
N = 20
app = Flask(__name__)

@app.route('/image')
def image():
  n = int(random.uniform(0,N))
  img = int(request.args.get("img"))
  fn = os.path.join(os.path.dirname(__file__), "images/"+str(img)+".jpg")
  im = Image.open(fn)
  dim = im.size
  c = im.crop((int(n*dim[0]/N), 0, int((n+1)*dim[0]/N), dim[1]))
  c = c.convert("RGBA")
  bio = io.BytesIO()
  c.save(bio, 'PNG')
 
  resp = Response(bio.getvalue())
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Content-Type'] = 'image/png'
  resp.headers['X-Ece459-Fragment'] = str(n)

  return resp


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

