from flask import Flask
import os

app = Flask(__name__)
# adding comment to test cloud build trigger
# adding another comment to test cloud build trigger
# adding another comment to test cloud build trigger
@app.route("/")
def wish():
    message = "Happy birthday {name}"
    return message.format(name=os.getenv("NAME", "John"))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)