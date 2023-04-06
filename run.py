from flask import Flask, redirect, url_for, request
app = Flask(__name__)


def get_index(page):
    file=open(page)
    content=file.read()
    file.close()
    return content

@app.route('/')
def homepage():
    return get_index("index.html")

@app.route('/success/<name>')
def PostSuccess(name):
   return 'welcome POST %s' % name

@app.route('/success/<name>')
def GetSuccess(name):
   return 'welcome GET %s' % name

@app.route('/loginP')
def loginP():
    return get_index("loginP.html")

@app.route('/loginG')
def loginG():
    return get_index("loginG.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('PostSuccess',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('GetSuccess',name = user))

@app.route('/connect')
def connectP():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('PostSuccess',name = user))
   else:
      return get_index("loginP.html")

if __name__ == '__main__':
   app.run(debug = True)
