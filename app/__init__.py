import os, urllib.parse , urllib.request ,render_template
from app.youtube import youtube_bp
Gemini_api_Key = "Gemini_API_Key";

def home():
  return render_templete (" index.html")

def create_app():
  
  app = Flask(_name_)

app.register_blueprint(youtube_bp, url_prefix="/youtube")

@app.route("/html")
def html():

    return render_templete("index.html")

return app;
