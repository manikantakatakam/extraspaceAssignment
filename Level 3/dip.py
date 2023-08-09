from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

  if request.method == 'POST':
    json_data = request.form['json']
    return render_template('index.html', json=json.loads(json_data))

  return render_template('index.html')

if __name__ == '__main__':
  app.run()