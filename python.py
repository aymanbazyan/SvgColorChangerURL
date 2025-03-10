from flask import Flask, request, Response, abort
import os
import re

app = Flask(__name__)
SVG_DIR = "svgs"  # Folder where your SVG files are stored

@app.route('/svgs/<path:filename>')
def serve_svg(filename):
    # Get the query parameters for color replacement
    old_color = request.args.get('old')
    new_color = request.args.get('new')
    if not old_color or not new_color:
        abort(400, "Missing 'old' or 'new' query parameter.")

    # Basic check to prevent directory traversal
    if ".." in filename or filename.startswith("/"):
        abort(400, "Invalid file name.")

    file_path = os.path.join(SVG_DIR, filename)
    if not os.path.exists(file_path):
        abort(404, "SVG file not found.")

    try:
        with open(file_path, 'r') as file:
            svg_content = file.read()
    except Exception as e:
        abort(500, f"Error reading SVG file: {e}")

    # Replace all occurrences of the old color with the new color.
    # re.escape is used in case the color contains special regex characters.
    replaced_svg = re.sub(re.escape(old_color), new_color, svg_content)
    
    return Response(replaced_svg, mimetype="image/svg+xml")

if __name__ == '__main__':
    app.run(debug=True)
