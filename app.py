from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Git-SSH-TEST_BUILD1-UPDATE_WEBHOOK-URL! Docker! Jenkins! GKE! CICD1!'
