import pyaudio
from aip import AipSpeech
import keyboard
from baidu_api import APP_ID, API_KEY, SECRET_KEY

is_finished_speech = False


def hot_call():
    global is_finished_speech
    is_finished_speech = True


keyboard.add_hotkey('f5', hot_call)


def baidu_speech_to_text():
    global is_finished_speech
    is_finished_speech = False
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("请说话（按 F5 停止识别）...")
    frames = []
    for i in range(0, int(RATE / CHUNK * 20)):
        if is_finished_speech:
            break
        data = stream.read(CHUNK)
        frames.append(data)

    print("正在识别中...")

    stream.stop_stream()
    stream.close()
    p.terminate()

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    speech_data = b''.join(frames)

    result = client.asr(speech_data, 'wav', 16000, {
        'dev_pid': 1536,
    })

    if 'result' in result:
        return result['result'][0]
    else:
        return ""
