from typing import Any
from flask import Flask,jsonify,request
import json,uuid

app = Flask(__name__)

# to get access to all books in json format
@app.route("/books",methods=['GET'])
def get_books():
    with open('data.json') as f:
        return json.loads(f.read())
    
@app.route("/books/<int:bookid>" ,methods=['GET'])
def get_onebook(bookid):
    with open('data.json') as f:
        books = json.loads(f.read())
    for i in books:
        if i["id"]== bookid:
            return jsonify(i)
    else:
        return jsonify({"message":"Book not found"}) ,404
    
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,uuid.UUID):
          return str(obj)
        return super().default(obj)


@app.route('/books',methods=["Post"])
def create_book():
    with open('data.json') as f:
        current_books = json.loads(f.read()) 
    
    current_books.append({"id":uuid.uuid4(),"title":data["title"]})
    with open('data.json','w') as f:
        json.dump(current_books,f,cls=UUIDEncoder)
    return jsonify({"message":"successfully added"}),201

@app.route('/books/<uuid:bookid>',methods=["Put"])
def update_book(bookid):
    with open('data.json') as f:
        current_books = json.loads(f.read())
    data= request.get_json() 
    for i in current_books:
       if i["id"]== bookid:
         i["title"]=data["title"]

    with open('data.json','w') as f:
        json.dump(current_books,f,cls=UUIDEncoder)
    return jsonify({"message":"book successfully updated"}),201 

@app.route("/books",methods=['DELETE'])
def delete_book():
    with open('data.json') as f:
        current_books = json.loads(f.read())
    data= request.get_json()
    for i in current_books:
      if i["title"]== data["title"] :
        current_books.remove(i)

    with open('data.json','w') as f:
        json.dump(current_books,f,cls=UUIDEncoder)

    return jsonify({"message":"book successfully deleted"}),201




if __name__=="__main__":
    app.run(debug=False,host="172.25.110.97")