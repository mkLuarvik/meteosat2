from sanic import Sanic
from sanic import response as res
import time
import random


app = Sanic(__name__)

iii = 1;

@app.route("/")
async def test(req):

    global iii 
    aaa = iii;
    iii = iii + 1;
    sres = f'[{aaa}] Hello, its me !'
    #---
    r = random.randint(2, 4)
    time.sleep(r)
    #---
    return res.text(sres, status=418)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
