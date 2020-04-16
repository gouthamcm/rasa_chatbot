# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

#from typing import Any, Text, Dict, List

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

#from __future__ import unicode_literals
#from rasa_core_sdk import Action
#from rasa_sdk.action import Action
#from rasa_core_sdk.events import SlotSet
#
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
#class ActionCustom(Action):
#    def name(self):
#        return "action_custom"
    
#    def run(self,dispatcher,tracker,domain):
#        dispatcher.utter_template("utter_message",tracker)
#        return []
#class ActionDefaultFallback(Action):

#   def name(self):
#      return "action_default_fallback"

#   def run(self, dispatcher, tracker, domain):
#      dispatcher.utter_message("Sorry I couldn't understand you. For information regarding COVID19, please visit https://www.who.int/")
