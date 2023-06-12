# Jarvis - Your AI Assistant Inspired from Iron Man

![image](jarvis.png)

## Description:
Jarvis is an advanced AI assistant, inspired by the iconic Iron Man movie, designed to simplify your daily tasks and enhance your productivity. With its diverse range of capabilities, Jarvis brings the power of artificial intelligence right to your fingertips.

## Features:

- Messaging: Jarvis enables you to effortlessly send WhatsApp messages and voice messages, making communication more efficient and convenient.

- Weather Information: Stay updated on the latest weather conditions and forecasts in your area, providing you with valuable insights to plan your day effectively.

- Time Telling: With Jarvis, you can instantly inquire about the current time, ensuring you never miss an important appointment or deadline.

- Crypto Prices: Stay on top of the volatile cryptocurrency market by accessing real-time prices, allowing you to make informed decisions.

- Language Translation: Break down language barriers with Jarvis's built-in translation capabilities, facilitating seamless communication across different languages.

- Wikipedia Search: Jarvis harnesses the vast knowledge of Wikipedia to provide you with quick and accurate answers to your queries, ensuring reliable information at your fingertips.

- WhatsApp Calling: Effortlessly make WhatsApp calls using Jarvis, making it easier to connect with friends, family, or colleagues anytime, anywhere.

- Music Playback: Enjoy your favorite tunes with Jarvis's integrated YouTube music player, providing a personalized and immersive listening experience.

- News Headlines: Stay informed and up-to-date with the latest news headlines, keeping you in the know about current events and trending topics.

- Intelligent Chat: Engage in interactive conversations with Jarvis, allowing you to ask questions, seek guidance, or simply enjoy friendly banter, all powered by advanced natural language processing.

## Requirements:

- Python 3.9.8 (As there are some packages like pyttsx3 that do not support 3.10 yet).
- OpenWeatherMap API Key (To fetch the weather information in your local area).
- NewsAPI API Key (To fetch the latest headlines from your favorite news paper).
- WhatsApp to be installed on your system (For whatsapp automation such as, voice calling, voice messaging and text messaging).
- There is a voice package that you need to download, to get a voice close to Jarvis's voice. If you do not wish to install it, you can change the voice to sapi5 in the env file and proceed to use the default text to speech engine of microsoft.
- Currently only works on Windows (But soon will be available for Linux and MacOS)
- Last but not the least, You need 8GB or more RAM on your computer (For running local AI model on your computer, its not necessary as Jarvis only uses gpt3 API but incase if the request fails or something, it uses the local AI model. So its recommended).

## Commands:

**Saying ``Jarvis`` Will wake Jarvis up, he will stay awake for 300 seconds. You can say any of the following commands during that 300 seconds or you can just talk with him casually. After 300 seconds he goes back to sleep and can be waked up by saying Jarvis again.**

### WhatsApp automation:
> **Note that Jarvis should be running in background and WhatsApp should be open in the foreground in order for it to work.**

- To send WhatsApp message, you can say: \
 ``send a message to <PERSON NAME>`` \
 here it will ask you what message would you like to send to that person you specified. Once you tell the message to it, it will then begin to search the person in whatsapp, type the message and send the message.

- To call a person on WhatsApp, you can say: \
``make a call to <PERSON NAME>``  \
This will search the person again, and call them.

- To hang up an ongoing call on WhatsApp, you can say: \
``cut the call`` \
This will hang up the ongoing call.

- To send a voice message on WhatsApp, you can say: \
``send a voice message to <PERSON NAME> <MESSAGE>`` \ 
Jarvis will search the person, click on the record button and speak. Then send the message.

- To search something on wikipedia, you can say: \
``could you search something on wikipedia`` \
This will ask you what do u want to search, you can just say what you wanted to search and it will reply back with the information.

- To stop jarvis by voice command, you can say: \
``self destruct`` \
This will ask you a confirmation, if you say yes then it shuts down. saying no will cancel all the self destruct mission.

- To get the weather details, you can say: \
``whats the current weather in <CITY NAME>`` \
This will fetch the weather details such as temperature, humidity and weather description.

- To get the current time, you can say: \
``what is the time`` \
This will tell you your current local time.

- To play a music on YouTube, you can say: \
``could you play <MUSIC NAME> on youtube`` \
OR \
``play <MUSIC NAME>`` \
This will fetch the URL of the song by its name, then open up a browser window and start playing the music.

- To pause the music thats playing, you can say: \
``pause the music`` \
OR \
``could you halt the music`` \
This needs the web browser window where the song is playing on youtube to be open, it pauses the music.

- To resume the music thats paused, you can say: \
``resume the music`` \
OR \
``could you resume the music`` \
This needs the web browser window where the song is playing on youtube to be open, it resumes the music.

- To stop the music thats playing, you can say: \
``stop the music`` \
OR \
``could you stop the music`` \
This needs the web browser window where the song is playing on youtube to be open, it closes the tab.

- To translate the words or sentences, you can say: \
``could you translate <SENTENCE> into <LANGUAGE>`` \
OR \
``translate <SENTENCE> into <LANGUAGE>`` \
This translates and prints the translated sentence. TTS system can only speak in english so its currently not possible to make it say the translation. If the translation language is not found, then it just says the requested language is not found.

What ever you talk besides these commands will directly go to the AI. And then the AI in Jarvis will answer your question or have a conversation with you.

## Installing the voice package on Windows:

- Just clone or download the repository.
- Go to Voice Packages folder.
- Install the exe file.

## Configuring the env file:

- Edit the ``example.env`` file:
``# Configuration for API parameters
BATCH_SIZE=128                  # Number of examples processed in parallel during API call
TEMPERATURE=0.2                 # Controls the randomness of the generated text
TOP_K=40                        # Limits the number of tokens to consider for each step
TOP_P=0.9                       # Limits the cumulative probability of the generated text
N_KEEP=-1                       # Number of tokens to keep from the previous completion
N_PREDICT=200                   # Maximum number of tokens to generate
STOP="### Instruction:\n\n"     # Text that triggers the completion to stop
THREADS=4                       # Number of concurrent threads for generating completions
AS_LOOP=True                    # Specify if the completions should be generated token by token
INTERACTIVE=True                # Enable the detection of a stop word

# General Configuration
SPEECH_RATE=150                  # This controls the speed of talking
VOLUME=0.8                       # This adjusts the volume of Jarvis
OWNER_NAME=<YOUR NAME>               # This is used by jarvis in voice messages
OPENWEATHERMAP_APIKEY=<YOUR API KEY> # This is used by jarvis to fetch the weather data
LISTENING_DURATION=300           # This defines the awake time for jarvis
NEWSAPI_APIKEY=<YOUR API KEY> # This is used by jarvis to fetch news from newsapi
NEWS_PAPER=the-times-of-india    # This is the name of the newspaper from where you get the feeds
VOICE_ENGINE="IVONA 2 Brian - British English male voice [22kHz]" # Change this to sapi5 if you dont want to install the voice package``
- Then once you edit and save the file, rename it as .env (remove the example that was in front of .env).

## Running Jarvis:

- Install the dependencies:
``pip install -r requirements.txt``

- Run Jarvis:
``python jarvis.py``

And voila!! now you have your own jarvis!

## To-Do list:
- Fix the mic problem. (Jarvis stops hearing when its talking, you can't say stop to him or quit the program)
- Add portability (Run Jarvis on your PC, carry a portable version of him with you. Or talk to it from anywhere using API)
- Add Home Automation system (Control anything in your house using Jarvis)

## Contributions:
Any contributors who are willing to contribute to this project, are greatly appreciated.
--------------------------------------------------------------------------------------------------------
- Jarvis combines cutting-edge technologies to deliver a comprehensive and intuitive AI assistant experience. Embrace the future of productivity and let Jarvis streamline your daily routine, enabling you to focus on what truly matters.
