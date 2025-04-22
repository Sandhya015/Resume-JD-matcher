from flask import Flask, request, jsonify
from flask_cors import CORS
from match_engine import get_match_score  # make sure this returns the full dict
from resume_parser import extract_text

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload_files():
    resume_file = request.files['resume']
    jd_file = request.files['jd']

    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    result = get_match_score(resume_text, jd_text)  # Now returns dict with score, report, skills

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
