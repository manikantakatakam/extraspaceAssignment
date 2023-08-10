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
      <head>
         <style>
            .center {
               display: flex;
               justify-content: center;
               align-items: center;
               height: 100vh;
            }
            textarea {
               width: 50%;
               height: 200px;
               border: 1px solid #ccc;
               padding:.2em;
               font-family: monospace;
               font-size: 20px;
            }
         </style>
      </head>
     <form method="POST" class="center">
        <textarea name="json" rows="5" cols="50"></textarea>
        <br><br>
        <input type="submit">
     </form>
  '''

if __name__ == '__main__':
  app.run()
