from flask import Flask, Response

app = Flask(__name__)

def generate_html(size_in_bytes):
    # isi HTML dummy sesuai ukuran
    content = "<html><body>" + ("A" * (size_in_bytes - 20)) + "</body></html>"
    return content

@app.route("/10kb")
def serve_10kb():
    return Response(generate_html(10 * 1024), mimetype="text/html")

@app.route("/100kb")
def serve_100kb():
    return Response(generate_html(100 * 1024), mimetype="text/html")

@app.route("/1mb")
def serve_1mb():
    return Response(generate_html(1 * 1024 * 1024), mimetype="text/html")

@app.route("/5mb")
def serve_5mb():
    return Response(generate_html(5 * 1024 * 1024), mimetype="text/html")

@app.route("/10mb")
def serve_10mb():
    return Response(generate_html(10 * 1024 * 1024), mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
