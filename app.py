import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world web server. Your job script runs separately."

if __name__ == '__main__':
    # Render automatically sets the PORT environment variable.
    # We bind to 0.0.0.0 to make it accessible from outside the container.
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
