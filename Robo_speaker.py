import gtts
import playsound
print("This is a robo speaker created by Pranjal Thakre")
text = input("Enter something (or type 'exit' to stop): ")
sound = gtts.gTTS(text, lang="hi")
sound.save("robo_speaker.mp3")
playsound.playsound("robo_speaker.mp3")
