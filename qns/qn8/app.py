from flask import Flask

app = Flask(__name__)

@app.get("/clear")
def clear():
    with open("qn8/log.txt","w") as f:
        pass
    return "logs cleared successfully"



if __name__ == "__main__":
    app.run(debug=True)