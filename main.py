from flask import Response, Flask, jsonify, json, request

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

    for i in data['books']:
        a = i['isbn']
        if a == isbn:
            return jsonify(i)

        else:
            message={'status': 404,'message': 'Not Found book wiht isbn = '+ isbn}
            resp = jsonify(message)
            resp.status_code =404
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


    if len(result_list) > 0:
        response = {'authors': result_list}
    else:
        response = {'message': 'Not Found book with this expression = ' + expression}

    return jsonify(response)



@app.route('/ibns/<isbn>', methods=['PUT'])
def edit_publisher(isbn=None):
    print(request.args)
    if "publisher" in request.args:
        pub = request.args['publisher']
        succes_change = []
        for i in data['books']:
            a = i['isbn']
            if a == isbn:
                i['publisher'] = pub

                succes_change.append(isbn)
        if len(succes_change) > 0:
            message = {'message': 'Succes!' }
            response_put ='Succes!'
            return response_put
        else:
            message = {'message': 'Not Found book with isbn = ' + str(isbn)}
            response_put = 'Not Found book with isbn = ' + str(isbn)
            return response_put
