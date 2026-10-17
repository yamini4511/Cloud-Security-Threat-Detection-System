# CLOUD SECURITY PROJECT
# Multi-Cloud Threat Detection

logs = [
    {
        "cloud": "AWS",
        "user": "Ravi",
        "login_time": 10,
        "location": "India",
        "failed_attempts": 1
    },
    {
        "cloud": "Azure",
        "user": "Sita",
        "login_time": 3,
        "location": "Unknown",
        "failed_attempts": 6
    },
    {
        "cloud": "GCP",
        "user": "Krishna",
        "login_time": 14,
        "location": "India",
        "failed_attempts": 2
    }
]

high = 0
medium = 0
low = 0

print("CLOUD SECURITY DASHBOARD")
print("========================")

for log in logs:

    risk_score = 0
    reasons = []

    if log["location"] == "Unknown":
        risk_score += 30
        reasons.append("Unknown Location")

    if 2 <= log["login_time"] <= 5:
        risk_score += 30
        reasons.append("Unusual Login Time")

    if log["failed_attempts"] >= 5:
        risk_score += 40
        reasons.append("Multiple Failed Attempts")

    if risk_score >= 70:
        risk_level = "HIGH"
        high += 1

        actions = [
            "Require Identity Verification",
            "Review Login Activity",
            "Recommend Temporary Login Block"
        ]

    elif risk_score >= 40:
        risk_level = "MEDIUM"
        medium += 1

        actions = [
            "Send Security Alert",
            "Monitor User Activity"
        ]

    else:
        risk_level = "LOW"
        low += 1

        actions = [
            "No Immediate Action Required",
            "Continue Normal Monitoring"
        ]

    print("\nCloud:", log["cloud"])
    print("User:", log["user"])
    print("Risk Score:", risk_score)
    print("Risk Level:", risk_level)

    if reasons:
        print("Security Alerts:")
        for reason in reasons:
            print("-", reason)
    else:
        print("Security Alerts: None")

    print("Recommended Actions:")
    for action in actions:
        print("-", action)

    print("------------------------")

print("\nDASHBOARD SUMMARY")
print("========================")
print("Total Login Records:", len(logs))
print("High Risk Logins:", high)
print("Medium Risk Logins:", medium)
print("Low Risk Logins:", low)
print("========================")
print("SECURITY SCAN COMPLETED")
