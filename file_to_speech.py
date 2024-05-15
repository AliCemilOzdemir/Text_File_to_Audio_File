"""
NAME
    file_to_speech

DESCRIPTION
    This module allows converting text files to audio files.

FUNCTIONS
    filetospeech(file_path,lang_input="tr",isSlow=False)
        create an audio file in lang_input at the current directory,which is the transformed form of the text file whose file path is file_path.
"""

from gtts import gTTS
def filetospeech(file_path,lang_input="tr",isSlow=False) :
    """filetospeech(file_path,lang_input="tr",isSlow=False)
    file_path : file path that you want to save folder in it
    lang_input : language abbreviation that you want folder to be saved in that language
    isSlow : True if you want it to be slow ,False if you want it to be Normal"""

    with open(file_path,mode = "r",encoding="utf-8") as file :
        metin = str(file.read())
    
    try :    
        print(metin)
        kayit = gTTS(text=metin,lang=lang_input,slow=isSlow)
        dosya_adi = metin[:5]+".mp3"
        kayit.save(dosya_adi)
        print("voice file is recorded : ",dosya_adi)

    except :
        print("voice file couldn't recorded")