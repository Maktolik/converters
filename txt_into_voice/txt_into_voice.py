from transformers import BarkModel, AutoProcessor
import torch
import scipy


def text_into_audio(bark_model='suno/bark', voice_preset='v2/ru_speaker_3'):
    model = BarkModel.from_pretrained(bark_model)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = model.to(device)
    processor = AutoProcessor.from_pretrained(bark_model)

    text = ('Дорогие друзья, выбранный нами инновационный путь '
            'представляет собой интересный эксперимент проверки '
            'ключевых компонентов планируемого обновления.')

    inputs = processor(text, voice_preset=voice_preset).to(device)
    audio_arr = model.generate(**inputs)
    audio_arr = audio_arr.cpu().numpy().squeeze()

    sample_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(f"{voice_preset.split('/')[1]}.wav", rate=sample_rate, data=audio_arr)

def main():
    text_into_audio()

if __name__ =='__main__':
    main()