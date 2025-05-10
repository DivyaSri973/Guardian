import yagmail
from app.config import EMAIL_USER, EMAIL_PASS, HR_EMAIL

def report_message(sender_name, message, reasons):
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)

        # Set subject based on reason
        if "Offensive Language" in reasons and "Sexist Language" in reasons:
            subject = "🚨 Offensive and Sexist Message Flagged for Review"
        elif "Offensive Language" in reasons:
            subject = "🚨 Offensive Message Flagged for Review"
        elif "Sexist Language" in reasons:
            subject = "🚨 Sexist Message Flagged for Review"
        else:
            subject = "🚨 Inappropriate Message Flagged"

        reason_text = ", ".join(reasons)
        body = f"""
Dear HR Team,

A team member has reported a potentially inappropriate message that may violate company policies.

🚨 **Reported Details**
---------------------------------------------------------------------
👤 Sender: {sender_name}
🔍 Reason(s): {reason_text}

💬 Message:
'''{message}'''

📌 This report was submitted anonymously to ensure a safe and respectful environment.

Best regards,  
Guardian (Slack Bot)
"""
        yag.send(to=HR_EMAIL, subject=subject, contents=[body])
        print("\u2705 Email sent to HR")
    except Exception as e:
        print(f"\u274c Email error: {e}")