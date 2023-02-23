import argparse
from flask import Flask, render_template, session, request
from flask_dropzone import Dropzone


# Setup Flaskapp
app = Flask(__name__)
app.secret_key = 'Dog Breed Classifier'
dropzone = Dropzone(app)
app.config.update(
    DROPZONE_ALLOWED_FILE_TYPE="image",
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
    DROPZONE_UPLOAD_ON_CLICK=True,
)

# Index page
@app.route("/")
@app.route("/index")
def index():
    session["result"] = ""
    return render_template("master.html")


# Handle query and display results
@app.route("/go", methods=["POST", "GET"])
def go():
    if request.method == "POST":
        for key, f in request.files.items():
            if key.startswith("file"):
                img_path = "static/uploads/tmp_img." + f.filename.split(".")[-1]
                f.save(img_path)
                # session["result"] = dog_app.run(img_path)
                session["img_path"] = img_path
                break

    return render_template("go.html", result=session["result"], img=session["img_path"])


def main():
    app.run(host="0.0.0.0", port=3001, debug=True, use_reloader=False)


if __name__ == "__main__":
    main()