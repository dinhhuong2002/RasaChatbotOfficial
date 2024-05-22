# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# Chatbot gửi lời chào và đưa ra các lựa chọn, băt đàu phiên nói chuyện.
class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        # Gửi sự kiện bắt đầu phiên
        events = [SessionStarted()]

        # Gửi lời chào
        dispatcher.utter_message(text="Xin chào, mình là iTalk - trợ lý của bạn.")

        # Gửi các buttons lựa chọn
        buttons = [
            {"title": "Đăng ký tài khoản", "payload": "/sign_up"},
            {"title": "Đăng nhập", "payload": "/sign_in"},
            {"title": "Nạp GO", "payload": "/add_GO"}
        ]
        dispatcher.utter_message(text="Mình có thể giúp gì cho bạn?", buttons=buttons)

        # Gửi sự kiện kết thúc hành động
        events.append(ActionExecuted("action_listen"))

        return events
