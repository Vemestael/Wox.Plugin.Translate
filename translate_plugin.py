from wox import Wox

import pyperclip
from googletrans import Translator
from googletrans.constants import LANGUAGES


class TranslatePlugin(Wox):
    def query(self, query):
        result = self.translate(query)
        results = [{
            "Title": "Translate: {}".format(result),
            "SubTitle": "Press ENTER to copy in Clipboard",
            "IcoPath": "Images/app.ico",
            "JsonRPCAction": {
                'method': 'take_action',
                'parameters': [result],
                'dontHideAfterAction': True
            }
        }]
        return results

    def translate(self, query):
        trans = Translator()
        string = query[:6].split(' ')
        src = None
        dest = None
        if (len(string[0]) == 2 and len(string[1]) == 2):
            if (LANGUAGES.get(string[1]) != None):
                dest = string[1]

        if (len(string[0]) == 2):
            if (LANGUAGES.get(string[0]) != None):
                src = string[0]

        if (src != None and dest != None):
            return trans.translate(query[6:], src = src, dest = dest).text
        elif (src != None):
            return trans.translate(query[3:], src = src).text
        else:
            return trans.translate(query).text

    def take_action(self, arg):
        pyperclip.copy(arg)