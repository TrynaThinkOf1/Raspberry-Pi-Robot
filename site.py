from flask import Flask, render_template, request, redirect

command = ""

errors = []
updates = []

app_update = ""

site = Flask(__name__)

#PLACE ON SITE TO CONTROL WITH KEYS
@site.route("/")
def index():
    return render_template('index.html')

@site.route('/send_command', methods=['GET'])
def send_command():
    global command
    command = request.args.get('command')
    return redirect("/", code=302)

@site.route('/rec_cmd', methods=['GET'])
def rec_cmd():
    global command
    temp = command
    command = ""
    return temp

@site.route("/report_error", methods=['GET'])
def report_error():
        global errors
        error = request.args.get('error')
        errors.append(error)
        return redirect("/", code=302)

@site.route("/see_errors")
def see_errors():
        return errors

@site.route("/update", methods=['GET'])
def update_dashboard():
    global updates
    global app_update
    update = request.args.get('update')
    updates.append(update)
    app_update = update
    return redirect("/", code=302)

@site.route("/see_updates")
def update():
    return updates

@site.route("/see_app_update")
def see_app_update():
    return app_update

if __name__ == '__main__':
    site.run(host="0.0.0.0", debug=True)
