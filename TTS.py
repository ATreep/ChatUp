from aip import AipSpeech
from pydub import AudioSegment
from pydub.playback import play
import io
from baidu_api import APP_ID, API_KEY, SECRET_KEY

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def play_sound(text: str):

    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        })

    voice = AudioSegment.from_file(io.BytesIO(result), format="mp3")
    play(voice)
