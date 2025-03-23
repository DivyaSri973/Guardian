from app.classifier import is_offensive
from app.config import SLACK_BOT_TOKEN
from slack_bolt import App
from slack_sdk.errors import SlackApiError

app = App(token=SLACK_BOT_TOKEN)

@app.event("message")
def handle_message(event, client, logger):
    print("✅ Message event triggered")
    print(f"Full event: {event}")
    text = event.get("text", "")
    sender = event.get("user")
    channel = event.get("channel")

    if 'bot_id' in event:
        return

    if is_offensive(text):
        members = client.conversations_members(channel=channel)["members"]
        bot_id = client.auth_test()["user_id"]
        receiver = next((u for u in members if u != sender and u != bot_id), None)

        if receiver:
            try:
                client.chat_postMessage(
                    channel=receiver,
                    text="⚠️ A recent message might be inappropriate.",
                    blocks=[
                        {
                            "type": "section",
                            "text": {"type": "mrkdwn", "text": "*Do you want to report this to HR?*"}
                        },
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {"type": "plain_text", "text": "Report"},
                                    "style": "danger",
                                    "action_id": "report_btn"
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
                logger.error(f"Slack API error: {e}")

@app.action("report_btn")
def report_action(ack, body, client):
    ack()
    user = body["user"]["id"]
    client.chat_postMessage(channel=user, text="✅ Report sent to HR.")

@app.action("dismiss_btn")
def dismiss_action(ack, body, client):
    ack()
    user = body["user"]["id"]
    client.chat_postMessage(channel=user, text="👍 Okay, no action taken.")
