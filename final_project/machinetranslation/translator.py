import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    frenchText = language_translator.translate(
        text = englishText,
        source = en,
        target = fr
    ).get_result()
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text = englishText,
        source = fr,
        target = en
    ).get_result()
    return englishText