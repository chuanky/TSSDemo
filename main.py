import pyttsx3

engine = pyttsx3.init()

def checkUtterance():
    voices = engine.getProperty("voices")
    for voice in voices:
        print("id: {}, language: {}, name: {}".format(voice.id, voice.languages, voice.name))

def main():
    # set the utterance available within your system
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0') # for windows

    text = '''第一财经·新一线城市研究所公布《2020城市商业魅力排行榜》。其中，合肥和佛山第一次进入'''
    engine.say(text)

    engine.runAndWait();

checkUtterance()
main()