import os
from flask import Flask,request,jsonify render_template
from app.youtube import youtube_bp
from flask_cors import CORS
from app.gmail import{
    is_email_command,
    extract_email,create_gmail,
    generate_email_with_gemini
}

def create_app():

    app = Flask(__name__)
cors(APPS)
    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )
#home
    @app.route("/")
    def home():
        return render_template("index.html")
#html
    @app.route("/html")
    def html():
        return render_template("index.html")
#health
    @app.route("health")
    def health():
        return jonify({
            "status":"ok",
            "service": "Nova AI agent"
        })
    #Gmail AI agent
@app.route("/agent", method=["POST"])
def against();

    try:
        data=request.get_jaison(silent=true) or {}
        command = data.get("command","").strip()

    if not command:
        return jsonify({
            "success":False,
            "message":"command is required"
        }),400
        if not is_email_command(command):
            return jsonify({
                "success":False,
                "message":"Please give a gmail command"
            }),400

    recipient = extract_email(command)
    email = generate_email_with_gemini(command)

    return jsonify({
        "success" : True,
        "Type" : "email",
        "email_generated":True,
        "recipient":recipient,
        "subject": email["subjects"],
        "body": email["body"],
        "gmail_url": create_gmail_url(
            email["subjects"],
            email["body"],
        recipient
        )
    })
    
except Exception as e:

return jsonify({
    "success":false,
    "message":str(e)
}),500
return app
    

