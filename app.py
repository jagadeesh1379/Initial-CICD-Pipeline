from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Congratulations..!! Hello! CI/CD Pipeline with Jenkins, Docker & Git 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
