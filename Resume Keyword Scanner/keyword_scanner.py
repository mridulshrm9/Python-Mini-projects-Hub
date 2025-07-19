skills_needed = ["python", "sql", "etl", "cloud"]
resume_text = input("Paste your resume text:\n").lower()

for skill in skills_needed:
    if skill in resume_text:
        print(f"✅ Found: {skill}")
    else:
        print(f"❌ Missing: {skill}")
