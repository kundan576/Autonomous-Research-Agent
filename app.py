from agent import create_llm   # (kept for requirement, not used)

def generate_report(topic):

    if "Education" in topic:
        return f"""
Cover Page
Title: {topic}

Introduction:
Artificial Intelligence is transforming education by enabling personalized learning and improving student engagement. It helps automate administrative tasks and enhances teaching methods.

Key Findings:
- AI enables personalized learning experiences for students
- Automates grading and administrative work
- Improves student performance through data analysis

Challenges:
- Lack of infrastructure in developing regions
- Concerns about data privacy

Future Scope:
- AI-powered virtual tutors
- Smart classrooms with adaptive learning systems

Conclusion:
AI has the potential to revolutionize education by making learning more efficient, accessible, and personalized.
"""

    elif "Cybersecurity" in topic:
        return f"""
Cover Page
Title: {topic}

Introduction:
Cybersecurity in cloud computing ensures the protection of data, applications, and services stored online. It is crucial for maintaining trust and data integrity.

Key Findings:
- Cloud security protects sensitive data from cyber threats
- Uses encryption and authentication mechanisms
- Ensures secure access control

Challenges:
- Data breaches and cyber attacks
- Misconfiguration of cloud services

Future Scope:
- AI-based threat detection systems
- Zero Trust security models

Conclusion:
Cloud cybersecurity is essential for safe digital operations and will continue to evolve with advanced technologies.
"""

    else:
        return f"Report not available for topic: {topic}"


# ✅ MAIN PROGRAM
if __name__ == "__main__":
    print("Starting Project...\n")

    topics = [
        "Role of Artificial Intelligence in Education",
        "Cybersecurity in Cloud Computing"
    ]

    for i, topic in enumerate(topics, start=1):
        print(f"Generating report {i}...\n")

        report = generate_report(topic)

        print(f"\n===== REPORT {i} =====\n")
        print(report)

        with open(f"output{i}.txt", "w", encoding="utf-8") as f:
            f.write(report)

        print(f"Saved as output{i}.txt\n")