import wikipedia
from libs.speech_recog import listen_and_transcribe
from libs.communicate import post_prompt, chatwithgpt
from libs.vocal import speak
import os
import sys, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from time import sleep
import requests
import re, pywhatkit, keyboard, pyautogui, json
from pyautogui import click
from keyboard import write
from datetime import datetime
from googletrans import Translator

load_dotenv(r".env")
speechrate = os.getenv("SPEECH_RATE")
volume = os.getenv("VOLUME")
owner_name = os.getenv("OWNER_NAME")
owm_apikey = os.getenv("OPENWEATHERMAP_APIKEY")
newsapikey = os.getenv("NEWSAPI_APIKEY")
newspaper = os.getenv("NEWS_PAPER")

def extract_coin_name(statement):
    words = statement.split()
    if words:
        return words[-1]
    else:
        return None

def get_crypto_price(coin_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    url2 = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=inr'
    response2 = requests.get(url2)
    data2 = response2.json()
    
    if coin_id in data and coin_id in data2:
        price = data[coin_id]['usd']
        price2 = data2[coin_id]['inr']
        speak(speechrate, volume, f"Sir, the current price of {coin_id} is {price:.2f} US Dollars or {price2:.2f} Rupees")
    else:
        speak(120, volume, "Sir, that seems like an invalid coin, the data is not available.")

def extract_city_name(text):
    pattern = r'in\s+(\w+)'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        city = match.group(1)
        return city
    else:
        return
    
def translate_text(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def extract_translation_request(statement):
    statement = statement.lower()
    languages = {
        "afrikaans": "af",
        "albanian": "sq",
        "amharic": "am",
        "arabic": "ar",
        "armenian": "hy",
        "azerbaijani": "az",
        "basque": "eu",
        "belarusian": "be",
        "bengali": "bn",
        "bosnian": "bs",
        "bulgarian": "bg",
        "catalan": "ca",
        "cebuano": "ceb",
        "chichewa": "ny",
        "chinese (simplified)": "zh-cn",
        "chinese (traditional)": "zh-tw",
        "corsican": "co",
        "croatian": "hr",
        "czech": "cs",
        "danish": "da",
        "dutch": "nl",
        "english": "en",
        "esperanto": "eo",
        "estonian": "et",
        "filipino": "tl",
        "finnish": "fi",
        "french": "fr",
        "frisian": "fy",
        "galician": "gl",
        "georgian": "ka",
        "german": "de",
        "greek": "el",
        "gujarati": "gu",
        "haitian creole": "ht",
        "hausa": "ha",
        "hawaiian": "haw",
        "hebrew": "iw",
        "hindi": "hi",
        "hmong": "hmn",
        "hungarian": "hu",
        "icelandic": "is",
        "igbo": "ig",
        "indonesian": "id",
        "irish": "ga",
        "italian": "it",
        "japanese": "ja",
        "javanese": "jw",
        "kannada": "kn",
        "kazakh": "kk",
        "khmer": "km",
        "korean": "ko",
        "kurdish (kurmanji)": "ku",
        "kyrgyz": "ky",
        "lao": "lo",
        "latin": "la",
        "latvian": "lv",
        "lithuanian": "lt",
        "luxembourgish": "lb",
        "macedonian": "mk",
        "malagasy": "mg",
        "malay": "ms",
        "malayalam": "ml",
        "maltese": "mt",
        "maori": "mi",
        "marathi": "mr",
        "mongolian": "mn",
        "myanmar (burmese)": "my",
        "nepali": "ne",
        "norwegian": "no",
        "odia": "or",
        "pashto": "ps",
        "persian": "fa",
        "polish": "pl",
        "portuguese": "pt",
        "punjabi": "pa",
        "romanian": "ro",
        "russian": "ru",
        "samoan": "sm",
        "scots gaelic": "gd",
        "serbian": "sr",
        "sesotho": "st",
        "shona": "sn",
        "sindhi": "sd",
        "sinhala": "si"
    }
    default_lang = 'en'
    dest_lang = default_lang
    translation_text = statement

    for lang, lang_code in languages.items():
        if lang in statement:
            dest_lang = lang_code
            translation_text = statement.replace(lang, '')
            break
    else:
        return None, None
    return translation_text.strip(), dest_lang

def get_song_name(sentence):
    # Remove unwanted words and characters
    cleaned_sentence = re.sub(r"could you play|on youtube", "", sentence, flags=re.IGNORECASE)
    # Extract the song name
    song_name = re.sub(r"\s+", "", cleaned_sentence)
    return song_name

def search_wikipedia(query):
    try:
        # Search for the query on Wikipedia
        results = wikipedia.search(query)

        if len(results) > 0:
            # Retrieve the page summary for the first result
            page = wikipedia.page(results[0])
            summary = wikipedia.summary(results[0], sentences=2)  # Modify the sentences parameter

            return summary
        else:
            return "No results found."

    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages
        options = e.options
        return f"Multiple options found: {', '.join(options)}"

    except wikipedia.exceptions.PageError:
        return "Page not found."

def getnews():
    url = f'http://newsapi.org/v2/top-headlines?sources={newspaper}&apiKey={newsapikey}'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak(speechrate, volume, 'Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(speechrate, volume, articles['title'])
        if index == len(arts)-1:
            break
        speak(speechrate, volume, 'Moving on the next news headline..')
    speak(speechrate, volume, 'These were the top headlines, Have a nice day Sir!!..')

def webcomms(userinput):
    words = userinput.split()
    if userinput.startswith("send a message") and len(words) > 3:
        name = words[-1]
        speak(speech_rate=speechrate, volume=volume, speak_sentence="Okay Sir, what message would you like to send?")
        message = listen_and_transcribe()
        try:
            click(x=383, y=117)
            sleep(0.5)
            click(x=224, y=123)
            sleep(1)
            write(name)
            sleep(0.5)
            click(x=179, y=197)
            sleep(1)
            click(x=1161, y=712)
            sleep(0.5)
            write(message)
            sleep(0.8)
            click(x=1331, y=710)
            speak(speechrate, volume, speak_sentence=f"Sir, your message has been sent to {name}.")
        except:
            speak(speech_rate=speechrate, volume=volume, speak_sentence="Sir, This number does not exist in my configuration file. ")
        
    elif "wikipedia" in userinput.lower():
        speak(speech_rate=speechrate, volume=volume, speak_sentence="Sure Sir, What would you like to search about?")
        message = listen_and_transcribe()
        searchresults = search_wikipedia(message)
        speak(speech_rate=speechrate, volume=volume, speak_sentence=searchresults)
    elif "self destruct" in userinput.lower():
        speak(speechrate, volume, speak_sentence="Do you really want me to shut down Sir?")
        message = listen_and_transcribe()
        if message.lower() == "yes":
            speak(speechrate, volume, speak_sentence="Okay Sir, Shutting down my systems.")
            sleep(1)
            speak(speechrate, volume, speak_sentence="Detaching modules..")
            sleep(1)
            speak(speechrate, volume, speak_sentence="Stopping Speech recognition and voice synthesis..")
            sleep(1)
            speak(speechrate, volume, speak_sentence="Closing programs..")
            sleep(1)
            sys.exit()
        else:
            speak(speechrate, volume, speak_sentence="I have aborted the shutdown missions.")
    elif "current weather in" in userinput.lower():
        city = extract_city_name(userinput)
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={owm_apikey}'
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        speak(speechrate, volume, speak_sentence=f"The current temperature in {city} is {temperature}, humidity is about {humidity} and the current weather description is {weather_description}")
    elif userinput.startswith("make a call") and len(words) > 3:
        name = words[-1]
        click(x=383, y=117)
        sleep(0.5)
        click(x=224, y=123)
        sleep(1)
        write(name)
        sleep(0.5)
        click(x=179, y=197)
        speak(speechrate, volume, speak_sentence="Sir, your call has been placed!")
        sleep(2)
        click(x=1246, y=72)
    elif userinput.startswith("cut the call"):
        click(x=780, y=605)
        sleep(1)
        speak(speechrate, volume, speak_sentence="Sir, your call has been cut")
    elif userinput.startswith("send a voice message"):
        words = userinput.split()
        memname = words[5]
        message = ' '.join(words[6:])
        click(x=383, y=117)
        sleep(0.5)
        click(x=224, y=123)
        sleep(1)
        write(memname)
        sleep(2)
        click(x=179, y=197)
        sleep(2)
        click(x=1331, y=710)
        sleep(1)
        speak(speechrate, volume=1.2, speak_sentence=f"Hello, this is Jarvis speaking. {owner_name} told me to tell you the following message, {message}")
        sleep(2)
        click(x=1331, y=710)
    elif userinput.startswith("what is the time"):
        timed = datetime.now().strftime("%I:%M %p")
        speak(speechrate, volume, speak_sentence=f"Sir, The current time is {timed}")
    elif userinput.startswith("could you play") or userinput.startswith("play"):
        song = get_song_name(userinput)
        query_string = urllib.parse.urlencode({"search_query": song})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        inspect = BeautifulSoup(clip.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")
        for concatMusic1 in yt_title:
            pass
        print(f"Now Playing {concatMusic1['content']} on YouTube")
        speak(speechrate, volume, speak_sentence=f"Sir, the music {song} is now playing on youtube!")
        sleep(2)
        pywhatkit.playonyt(clip2)
    elif userinput.startswith("could you halt the music") or userinput.startswith("pause the music"):
        keyboard.press_and_release("spacebar")
        speak(speechrate, volume, speak_sentence="Sir, the music has been paused")
    elif userinput.startswith("could you resume") or userinput.startswith("resume the music"):
        keyboard.press_and_release("spacebar")
        speak(speechrate, volume, speak_sentence="Sir, the music has been resumed")
    elif userinput.startswith("could you stop") or userinput.startswith("stop the music"):
        pyautogui.hotkey("ctrl", "w")
        speak(speechrate, volume, speak_sentence="Sir, the music has been stopped")
    elif userinput.startswith("could you tell some news") or userinput.startswith("get me the latest news headlines"):
        getnews()
    elif userinput.startswith("could you translate") or userinput.startswith("translate"):
        text, dest_lang = extract_translation_request(userinput)
        if text != None and dest_lang != None:
            translation = translate_text(text, dest_lang)
            print(translation)
        else:
            speak(speechrate, volume, "Sir, that language is not in my database.")
    elif userinput.startswith("could you get me the price") or userinput.startswith("get the price of") or userinput.startswith("tell me the price"):
        coin = extract_coin_name(userinput)
        get_crypto_price(str(coin).lower())
    else:
        try:
            AIresp = chatwithgpt(userinput)
        except Exception as e:
            print(f"Skipping asking the AI because of {e} Asking the local AI through the Local API")
            try:
                AIresp = post_prompt(userinput)
            except:
                print(f"Error! Cant reach the local llama API, Are you sure the API is running?")
        speak(150, volume, AIresp)