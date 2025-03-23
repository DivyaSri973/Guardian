from app.classifier import is_offensive, is_sexist
from app.config import SLACK_BOT_TOKEN
from slack_bolt import App
from slack_sdk.errors import SlackApiError
from app.utils import report_message

app = App(token=SLACK_BOT_TOKEN)

@app.event("message")
def handle_message(event, client, logger):
    print("\u2705 Message event triggered")
    text = event.get("text", "")
    sender = event.get("user")
    channel = event.get("channel")

    if 'bot_id' in event:
        return

    reasons = []
    if is_offensive(text):
        reasons.append("Offensive Language")
    if is_sexist(text):
        reasons.append("Sexist Language")

    if reasons:
        members = client.conversations_members(channel=channel)["members"]
        bot_id = client.auth_test()["user_id"]
        sender_info = client.users_info(user=sender)
        sender_name = sender_info["user"]["real_name"]
        sender_mention = f"<@{sender}>"
        receivers = [u for u in members if u != sender and u != bot_id]
        reason_text = ", ".join(reasons)
        print(reason_text)

        for receiver in receivers:
            try:
                client.chat_postMessage(
                    channel=receiver,
                    text=f"\u26a0\ufe0f Message from {sender_name} may be inappropriate.",
                    blocks=[
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"\ud83d\udea8 *{reason_text} message detected from {sender_mention}:*\n\n```{text}```\n\nDo you want to report this to HR?"
                            }
                        },
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {"type": "plain_text", "text": "Report to HR"},
                                    "style": "danger",
                                    "action_id": "report_btn",
                                    "value": f"{sender_name}|{text}|{reason_text}|{receiver}"
                                },
                                {
                                    "type": "button",
                                    "text": {"type": "plain_text", "text": "Dismiss"},
                                    "style": "primary",
                                    "action_id": "dismiss_btn"
                                }
                            ]
                        }
                    ]
                )
            except SlackApiError as e:
                logger.error(f"Slack API error for {receiver}: {e}")

@app.action("report_btn")
def report_action(ack, body, client):
    # print("\ud83d\udd34 Report action triggered")
    ack()
    user = body["user"]["id"]
    value = body["actions"][0]["value"]
    sender_name, message, reasons, _ = value.split("|", 3)
    report_message(sender_name, message, reasons.split(", "))
    client.chat_postMessage(channel=user, text="✅ Report sent to HR.")

@app.action("dismiss_btn")
def dismiss_action(ack, body, client):
    ack()
    user = body["user"]["id"]
    client.chat_postMessage(channel=user, text="👍 Okay, no action taken.")

@app.event({"type": "message"})
def catch_all_messages(event, logger):
    logger.info("\ud83d\df29\ufe0f CATCH-ALL: Received message event")
    logger.info(event)
    # print("\ud83d\df29\ufe0f CATCH-ALL: Event triggered")
    print(event)