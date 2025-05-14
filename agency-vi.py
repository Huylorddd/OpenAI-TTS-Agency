import speech_recognition
from openai import OpenAI
from gtts import gTTS
import pygame


client = OpenAI(
    api_key=" OPENAI KEY "    <<---- Insert your key here.
)

robot_ear = speech_recognition.Recognizer()
robot_brain = ""
pygame.mixer.init()

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi đang lắng nghe...")
        audio = robot_ear.listen(mic)
        print("Robot: ...")

    try:
        prompt = robot_ear.recognize_google(audio, language="vi-VN")
    except:
        prompt = "Tôi không nghe thấy gì. Vui lòng thử lại."

    print("You: " + prompt)


    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "Như một giáo viên cấp 2, bạn cần câu trả lời ngắn gọn, súc tích."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        robot_brain = completion.choices[0].message.content

    except:
        robot_brain = "Tôi không thể trả lời câu hỏi của bạn. Vui lòng thử lại sau."

    print("Robot: " + robot_brain)

  ##### FREE CHOICE: Google translate voice.
    #tts = gTTS(text=robot_brain, lang='vi')
    #tts.save("voice.mp3")

  ###### PAID CHOICE: OpenAI gen voice.
    audio_response = client.audio.speech.create{
      model="tts-1",
      voice="nova", #shimmer, echo, alloy
      input=robot_brain
    }
    with open("voice.mp3", "wb") as file:
      file.write(audio_response.content)

    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


