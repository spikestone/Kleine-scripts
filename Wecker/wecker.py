import schedule
import time
from playsound import playsound

def job():
    # Ersetze 'dein_mp3_file.mp3' durch den vollständigen Pfad zu deiner MP3-Datei
    playsound('Waky.mp3')

# Stelle die gewünschte Zeit ein (HH:MM)
schedule.every().day.at("06:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
