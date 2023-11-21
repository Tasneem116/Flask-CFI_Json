from flask import Flask,jsonify,request

app = Flask(__name__)

books = [{"id":1,"title":"Book 1"},
         {"id":2,"title":"Book 2"},
         {"id":3,"title":"Book 3"},
         {"id":4,"title":"Book 4"}
         ]

@app.route("/books",methods=['GET'])
def get_books():
    return books

 
@app.route("/books/<int:bookid>",methods=['GET'])
def get_book(bookid):
    for i in books:
       if i["id"] == bookid:
            return jsonify(i)
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route('/books',methods=['POST'])
def create_book():
    data = request.get_json()
    books.append({"id":len(books)+1, "title":data["title"]})
    return jsonify({"message": "Book succesfully added"}), 201


if __name__== "__main__":
    app.run(debug=False,host="172.30.52.191")