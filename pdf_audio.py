import PyPDF2
import pyttsx3

with open ('sample.pdf', 'rb') as book:

    full_book = ""

    reader = PyPDF2.PdfFileReader(book)
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_book += content

    audio_reader.save_to_file(full_book, "testAudio.mp3")
    audio_reader.runAndWait()