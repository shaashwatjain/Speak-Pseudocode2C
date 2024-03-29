import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
#load model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")