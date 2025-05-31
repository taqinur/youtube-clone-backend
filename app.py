from flask import Flask, jsonify, send_from_directory, request
import os
import json

app = Flask(__name__)

STATIC_THUMBNAILS_FOLDER = os.path.join(app.root_path, 'static', 'thumbnails')

VIDEO_DATA = []
try:
    with open(os.path.join(app.root_path, 'data', 'videos.json'), 'r') as f:
        VIDEO_DATA = json.load(f)
except FileNotFoundError:
    print("Error: videos.json not found. Please create it in the 'data' directory.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Could not decode videos.json. Check its format.")
    exit(1)


@app.route('/getvideodata', methods=['GET'])
def get_video_data():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "video_id parameter is required"}), 400

    for video in VIDEO_DATA:
        if video['id'] == video_id:
            return jsonify({
                "title": video['title'],
                "views": video['views_full'],
                "likes": video['likes'],
                "uploaded": video['uploaded_full'],
                "channel": video['channel_name'],
                "subscribers": video['subscribers']
            })
    
    return jsonify({"error": "Video not found"}), 404

@app.route('/getvideos', methods=['GET'])
def get_videos():
    home_page_videos = []
    for video in VIDEO_DATA:
        home_page_videos.append({
            "thumbnail": video['thumbnail_url'],
            "title": video['title'],
            "views": video['views_short'],
            "uploaded": video['uploaded_short'],
            "channel": video['channel_name']
        })
    return jsonify(home_page_videos)

@app.route('/static/thumbnails/<filename>')
def serve_thumbnail(filename):
    return send_from_directory(STATIC_THUMBNAILS_FOLDER, filename)


if __name__ == '__main__':
    os.makedirs(STATIC_THUMBNAILS_FOLDER, exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'data'), exist_ok=True)

    app.run(debug=True)from flask import Flask, jsonify, send_from_directory, request
import os
import json

app = Flask(__name__)

STATIC_THUMBNAILS_FOLDER = os.path.join(app.root_path, 'static', 'thumbnails')

VIDEO_DATA = []
try:
    with open(os.path.join(app.root_path, 'data', 'videos.json'), 'r') as f:
        VIDEO_DATA = json.load(f)
except FileNotFoundError:
    print("Error: videos.json not found. Please create it in the 'data' directory.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Could not decode videos.json. Check its format.")
    exit(1)


@app.route('/getvideodata', methods=['GET'])
def get_video_data():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "video_id parameter is required"}), 400

    for video in VIDEO_DATA:
        if video['id'] == video_id:
            return jsonify({
                "title": video['title'],
                "views": video['views_full'], # Use the full views number
                "likes": video['likes'],
                "uploaded": video['uploaded_full'], # Use the full uploaded string
                "channel": video['channel_name'],
                "subscribers": video['subscribers']
            })
    
    return jsonify({"error": "Video not found"}), 404

@app.route('/getvideos', methods=['GET'])
def get_videos():
    home_page_videos = []
    for video in VIDEO_DATA:
        home_page_videos.append({
            "thumbnail": video['thumbnail_url'],
            "title": video['title'],
            "views": video['views_short'],
            "uploaded": video['uploaded_short'],
            "channel": video['channel_name']
        })
    return jsonify(home_page_videos)

@app.route('/static/thumbnails/<filename>')
def serve_thumbnail(filename):
    return send_from_directory(STATIC_THUMBNAILS_FOLDER, filename)


if __name__ == '__main__':
    os.makedirs(STATIC_THUMBNAILS_FOLDER, exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'data'), exist_ok=True)

    app.run(debug=True)