from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Git-SSH-TEST_BUILD! Docker! Jenkins! GKE! CICD1!'
