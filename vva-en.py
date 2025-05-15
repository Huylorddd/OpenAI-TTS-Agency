import speech_recognition
from openai import OpenAI
from gtts import gTTS
import pygame


client = OpenAI(
    api_key=" API KEY "  #<<<< INSERT YOUR API KEY HERE. 
)

robot_ear = speech_recognition.Recognizer()
robot_brain = ""
pygame.mixer.init()

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I am hearing...")
        audio = robot_ear.listen(mic)
        print("Robot: ...")

    try:
        prompt = robot_ear.recognize_google(audio, language="en-US")
    except:
        prompt = "I can't hear what you've said. Please try again."
        continue

    print("You: " + prompt)


    try:
        completion = client.chat.completions.create( 
            model="gpt-4.1-nano",  # <<<< change your favourite model on openAI.
            messages=[
                {"role": "system", "content": "Like a supportive assistant, help me solve problem in fast and efficient"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        robot_brain = completion.choices[0].message.content

    except:
        robot_brain = "I can't hear what you've said. Please try again."

    print("Robot: " + robot_brain)

  ##### FREE TTS: Google translate voice.
    #tts = gTTS(text=robot_brain, lang='en')
    #tts.save("voice.mp3")

  ###### PAID TTS: OpenAI gen voice.
    audio_response = client.audio.speech.create(
      model="tts-1",
      voice="nova", #shimmer, echo, alloy (types of voice)
      input=robot_brain
    )
    with open("voice.mp3", "wb") as file:
      file.write(audio_response.content)
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    
    
