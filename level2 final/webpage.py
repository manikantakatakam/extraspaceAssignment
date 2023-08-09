from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

  if request.method == 'POST':
     raw_json = request.form['json']
     
     try:
        json_data = json.loads(raw_json)
     except ValueError:
        return "Invalid JSON", 400
        
     formatted_json = json.dumps(json_data)

     return f'''
        <h1>Submitted JSON:</h1>
           <pre>{formatted_json}</pre>
     '''
     
  return '''
     <form method="POST">
        <textarea name="json"></textarea> 
        <input type="submit">
     </form>
  '''

if __name__ == '__main__':
  app.run()
