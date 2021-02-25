from pydub.utils import mediainfo
info = mediainfo("../sample_audio/untitled.wav")
print(info['sample_rate'])
