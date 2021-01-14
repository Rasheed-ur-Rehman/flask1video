from flask import Flask
rasheed=Flask(__name__)

@rasheed.route('/')
def hello():
    return '<body> <h1>Rasheed ur Rehman</h1> </body>'
if __name__=='__main__':

    rasheed.run(debug=True)


#sel FLASK_ENV=DEVELOPMENT
