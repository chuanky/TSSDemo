import pyttsx3
from pydub import AudioSegment

engine = pyttsx3.init()
# set the utterance available within your system
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0') # for windows
sample = '''第一财经·新一线城市研究所公布《2020城市商业魅力排行榜》。其中，合肥和佛山第一次进入'''
sample1 = '''央行行长对法定数字货币表态 机构建议关注三条主线下核心'''

def checkUtterance():
    voices = engine.getProperty("voices")
    for voice in voices:
        print("id: {}, language: {}, name: {}".format(voice.id, voice.languages, voice.name))

def save(text, path: str):
    engine.save_to_file(text, path)
    engine.runAndWait()
    target_path = path.split('.')[0]
    convert_to_mp3(path, target_path + '.mp3')

def convert_to_mp3(path, target_path):
    sound = AudioSegment.from_file(path)
    sound.export(target_path, format="mp3")

# save(sample1, 'out/output')
save(sample, 'out/output.aiff')