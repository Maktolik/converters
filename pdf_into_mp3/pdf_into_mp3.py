from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_into_mp3(file_path='text.pdf', language = 'en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        print('+++ ИДЕТ КОНВЕРТАЦИЯ +++')
        my_audio.save(f'{file_name}.mp3')
        print(f'+++ {file_name}.mp3 was saved!')

    else:
        return f'No File in {file_path}'


def main():
    file_path = input('Введите абсолютный путь файла pdf:')
    language = input('Введите язык для mp3 ("en" или "ru"):')
    pdf_into_mp3(file_path=file_path, language=language)


if __name__ == '__main__':
    main()