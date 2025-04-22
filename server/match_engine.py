import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills_list import common_skills

def extract_skills(text):
    found_skills = []
    text = text.lower()
    for skill in common_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)
    return found_skills

def get_match_score(resume_text, jd_text):
    # Matching Score
    docs = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(docs)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    # Skill Extraction
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    # Feedback Generation
    feedback = []
    if matched_skills:
        feedback.append(f"✅ Skills you have that match the JD: {', '.join(matched_skills)}.")
    if missing_skills:
        feedback.append(f"❌ Skills missing from your resume: {', '.join(missing_skills)}.")
    if not matched_skills:
        feedback.append("⚠ Your resume doesn't seem to align well with the required skills.")
    if not missing_skills:
        feedback.append("🎯 You seem to match all key skills for this role!")

    report = "\n".join(feedback)

    return {
        "score": round(score * 100, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "report": report
    }
