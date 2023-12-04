from flask import Response, Flask, jsonify, json

app = Flask(__name__)


with open('books.json') as json_data:
  result = []
  data = json.load(json_data)
  for book in data['books']:
    result.append(book['isbn'])



@app.route("/")
def hello():
    return "<h1>Hello world!!</h1>"

@app.route("/ibns", methods = ['GET'])
def ibns_list():
    json_table=json.dumps(result)
    return json_table


@app.route("/ibns/<isbn>", methods = ['GET'])
def books_inf(isbn = None):
    result_list =[]
    for i in data['books']:
        a = i['isbn']
        if a == isbn:
            result_list.append(i)
    if len(result_list)> 0:
        return json.dumps(result_list)
    else:
        message={'status': 404,'message': 'Not Found book wiht isbn = '+ isbn}
        resp = jsonify(message)
        resp.status_cod =404
        return resp


@app.route("/authors/<expression>", methods = ['GET'])
def author_list(expression = None):
    result_list =[]
    for i in range(0, len(data['books'])):
        a = data['books'][i]['title']
        if expression in a:
            result_list.append(data['books'][i]['author'])
        else:
            pass

    result_total = json.dumps(result_list)
    if len(result_list)> 0:
        return result_total
    else:
        message={'Not Found book wiht this expression = '+ expression}

        return message



@app.route('/isbns/<isbn>/publisher=<xyz>', methods=['PUT'])
def edit_publisher(isbn =None, xyz =None):
    succes_change = []
    for i in data['books']:
        a = i['isbn']
        if a == isbn:
            i['published'] = xyz

            succes_change.append(isbn)
    if len(succes_change) > 0:
        message = {'message': 'Succes! = ' + str(isbn)}
        return message

    else:
        message = {'message': 'Not Found book wiht isbn = ' + str(isbn)}
        return message
