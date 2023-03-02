# Code for handling API requests in Nimbus

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    # TODO: Add code to handle file upload
    return jsonify({"message": "File uploaded successfully"})

@app.route("/download", methods=["GET"])
def download_file():
    # TODO: Add code to handle file download
    return jsonify({"message": "File downloaded successfully"})

@app.route("/delete", methods=["DELETE"])
def delete_file():
    # TODO: Add code to handle file deletion
    return jsonify({"message": "File deleted successfully"})

@app.route("/info", methods=["GET"])
def get_file_info():
    # TODO: Add code to get file info
    return jsonify({"message": "File info retrieved successfully"})

if __name__ == "__main__":
    app.run(port=8000, debug=True)

