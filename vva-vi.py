import speech_recognition
from openai import OpenAI
from gtts import gTTS
import pygame


client = OpenAI(
    api_key=" API KEY "  #<<<< NHẬP API KEY TẠI ĐÂY. 
)

robot_ear = speech_recognition.Recognizer()
robot_brain = ""
pygame.mixer.init()

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi đang nghe...")
        audio = robot_ear.listen(mic)
        print("Robot: ...")

    try:
        prompt = robot_ear.recognize_google(audio, language="vi-VN")
    except:
        prompt = "Tôi không nghe bạn nói. Vui lòng thử lại xem."
        continue

    print("You: " + prompt)


    try:
        completion = client.chat.completions.create( 
            model="gpt-4.1-nano",  # <<<< đổi model AI theo nhu cầu trên trang chủ openAI.
            messages=[
                {"role": "system", "content": "Như một người trợ lí tận tâm, hãy đưa ra giải pháp nhanh và hiệu quả"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
            #max_tokens=100  <<<< điều chỉnh giá trị này để giới hạn token sử dụng, nhớ thêm dấu phẩy ở dòng trước. (token càng ít đoạn chat sẽ ít hoặc bị ngắt giữ chừng)
        )
        robot_brain = completion.choices[0].message.content

    except:
        robot_brain = "Tôi không nghe bạn nói. Vui lòng thử lại xem."

    print("Robot: " + robot_brain)

  ##### Miễn phí TTS: Giọng Google.
    #tts = gTTS(text=robot_brain, lang='vi')
    #tts.save("voice.mp3")

  ###### Trả phíphí TTS: Giọng gen AI của openAI.
    audio_response = client.audio.speech.create(
      model="tts-1",
      voice="nova", #shimmer, echo, alloy (các loại giọng khác nhau)
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
    
    
