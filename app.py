from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world! This is flask!"

@app.route('/request_count')
def request_count():
    global request_count_number
    request_count_number = request_count_number + 1

    message_to_display = "This is request number " + str(request_count_number) + " since the server was restarted"

    print (message_to_display)
    return message_to_display


#Main route
request_count_number = 0
app.run(host='0.0.0.0', port=80, debug=True)