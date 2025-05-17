# OpenAI Virtual Voice Assistant 🔊
My template about OpenAI Agency with Text to speech based on gTTS/OpenAI-TTS.

![image](https://github.com/user-attachments/assets/c1710208-d6b3-4add-bcf1-24cc749222cb)


## INSTRUCTION 
Welcome to my repository, there are 2 python scripts that was written in en-US and vi-VN.
 > These scripts are the same except for the language, choose whichever is more convenient for you.

## REQUIREMENT 🛠️
 **╰┈➤ Windows 10/11, MacOS, LinuxOS.**

 **╰┈➤ Visual Code Studio (or equivalent IDE).**

 **╰┈➤ Python & PIP packages.**

## INSTALLATION STEPS ⭐
### STEP 1: Visual Code Studio 💻
  1. Download VS Code from the main page. src: https://code.visualstudio.com/
  2. Open the downloaded file and complete the setup to start installing.
  3. Choose **Extension** on the left and install 4 extensions that marked.
     
     ![image](https://github.com/user-attachments/assets/4d321ed2-61f0-4d17-bb27-79c4d56c8522)

  4. Choose **File icon** -> **File** on top -> Open Folder. Make sure you've created an empty folder for this. -> Click **'Open Folder'**.
     
     ![image](https://github.com/user-attachments/assets/7605dfeb-7d10-40ea-96b3-b68570a2ef6d)

  5. After having a brand new folder, we need to setting a bit with preferences. **File -> Preferences -> Settings**.

     ![image](https://github.com/user-attachments/assets/c81d7a8d-7420-49f9-bc83-3b2d45f9c87e)

  6. Some changes in the settings that you need to follow up:
     > Use **settings search** for the belows.
     
     ➤ Auto Save & Font Size
     
      ![image](https://github.com/user-attachments/assets/ed71a4ae-3b76-40dd-94c6-ed9d8641a3ce)

     ➤ Code-runner: in Terminal
     
      ![image](https://github.com/user-attachments/assets/cdd8c2a1-ba74-43ab-8d25-eaab1fa3ec74)

     ➤ Code-runner: Save files
     
      ![image](https://github.com/user-attachments/assets/abef777d-456b-45b5-9a7c-92ea925aa2ce)




### STEP 2: Python and PIP packages 🐍
  1. Download **Python** directly from the mainpage. src: https://www.python.org/downloads/
  2. Open the downloaded file and complete the setup to start installing.
  3. Insert the **download path** to environtment on your desktop :
     
     ➤ Find 'environment' in the **Start**

      ![image](https://github.com/user-attachments/assets/1f597da8-b738-45ac-969a-f0fe2ea6ae33)

     ➤ Click on **Environment Variables** -> Choose **PATH** below the **System variables** section -> **Edit..**
          
      ![image](https://github.com/user-attachments/assets/42059b06-7344-4699-bafa-1ddb378a1163)

     ➤ Choose **New** -> Then add 2 paths like the image below -> Remember to change to **your profile** in the **green section** that i've marked.

      ![image](https://github.com/user-attachments/assets/9a8ea0f8-3b67-47fc-8723-08fe12d3e603)

     
  4. Open **Terminal/Command Prompt** in your computer and run this command to install **PIP**:
     
         curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py.

  6. Run the **downloaded file**:
     
         python get-pip.py

  8. **Reboot** your computer.


### STEP 3: Install Virtual Voice Assistant 🤖
  1. Install **'agency.py'** (en-US/vi-VN based on your convenient) to prepared folder that we've made before or copy/paste to your **py file**.
  2. In the code, we need to check & adjust a little bit:

     **➤ API KEY:** This key is provided by openAI to run the fully functional API. Otherwise, nothing happens.
     
      ![image](https://github.com/user-attachments/assets/2c4d61b9-2f95-41b9-8dc1-bbd0d51374de)

     **➤ MODELS & SYSTEM.CONTENT:**
     
       **Models:** choose the model that's suitable for your tasks. **Higher price the more different**. Checkout: https://openai.com/api/pricing
         
        > for example: if you want to use 'GPT-4.1' model -> model="gpt-4.1"
     
       **System.content:** adjust this field to change personality & performance for your assistant.
     
        > for example: if you want your assistant girly -> "as a helpful and cute girl, help me come up with quick and effective solutions"

      ![image](https://github.com/user-attachments/assets/ee1b7af3-a962-4746-8720-bdcb3268d227)

     **➤ VOICES:** options for your assitant's voice. Need to set your "#" like the image below if you want to use OpenAI gen voice and vice versa.

        -**FREE TEXT-TO-SPEECH:** this choice is using **Google Translate** voice, fast and no cost.

        -**COST TEXT-TO-SPEECH:** using **OpenAI** gen voice, natural and smooth talk. You can also change the model and type of voice if you want to.
    

      ![image](https://github.com/user-attachments/assets/95f59554-c7bc-493e-b4ef-9fa4c62e8d13)

     ## ATTENTION ⚠️
     If you're using **gpt-4.1-nano** or the older versions, the assistant is **dumber** and **too much mechanical**, the voice **cracks often** than the new one.

     ## GET OPENAI API KEY 🔑
     1. Go to mainpage OpenAI and login/sign up your account. src: https://openai.com/api/
    
        ![image](https://github.com/user-attachments/assets/ec93ab29-31c5-4626-9a74-669a3b1cbeec)

     2. Create a **project** for your purpose
    
        ![image](https://github.com/user-attachments/assets/ff514af3-c2cd-4049-bc79-aa8644adfe44)
        
     3. Create **a or more**(if you want to) new **secret/api keys**

        ![image](https://github.com/user-attachments/assets/1fefef63-2d8a-47bd-b568-a8eb064b660d)

     4. A table will show and you need to fill the name field and choose your project that we've just created.
    
        ![image](https://github.com/user-attachments/assets/3a36fca1-d850-404d-9f16-25664c22890a)

     5. The **API key** will appear and you can copy/paste it to your "**API KEY**" in your code
    
        ![image](https://github.com/user-attachments/assets/34e27839-c527-475e-9915-fed8650822a1)

     ## ATTENTION ⚠️
     You need to **save** your **API key** at safe place and don't let anyone know that as they'll use yours without paying.
     If someone already knows, you can **revoke** your **API key** and create a **new one**.

       ![image](https://github.com/user-attachments/assets/5f506f47-a1b2-4071-9a8b-6b30e3d5add7)

     ## PAYING TO USE 💵
     Since the models we're using belong to **OpenAI**, so you need to have balance in your account to keep using the API.
     Don't worry! You can choose the model that suits your budget.

       ![image](https://github.com/user-attachments/assets/415b2857-0a36-4e27-9f1c-58ed56b86272)


     ### Add payment method and balance to your account
       1. Move to **Billing** section -> choose **Add payment method** and add your payment.
       2. Add your amount of balance.
        > between 5$ and 95$. You can enable auto-recharge for automatically paying when your balance goes empty.
    
        ![image](https://github.com/user-attachments/assets/61e3b35a-87c0-493d-8711-b239bffd7df5)

        ![image](https://github.com/user-attachments/assets/e203a60d-7ddd-4158-8516-4a90349f3644)


### Check how much balance you have used for API

**Token:** unit of measure for the amount payable.
At the **Usage** section, there are 2 things you have to pay attention.

╰┈➤ **Total Spend:** This field shows you how much **money** you've used for **API calls**.

   > The price it costs based on which model you're using. 

╰┈➤ **Chat Completion:** This field shows how many **requests** you've called.

   > Each **request** has different **tokens**. The newer model the more tokens it uses.

 ![image](https://github.com/user-attachments/assets/2362cc7f-2369-45cf-aff5-8b5ad9b26d4f)

## HOW TO USE THE VIRTUAL VOICE ASSISTANT 🚀

### METHOD 1: RUN IN IDE

Open your script on your IDE (VS Code for example) and run the code.

![image](https://github.com/user-attachments/assets/1822223b-6af0-4dab-be00-bd279993a730)

### METHOD 2: RUN IN TERMINAL

Locate the path of your script and run the code.

 > for example: **python code-storage/ai/vva-en.py**

    python path/to/your/script.py

# GIVE A ⭐ IF YOU FIND THIS HELPFUL
☕ **Buy me a coffee: https://bit.ly/4kjY1TJ**

☀️ **Have a nice day.**






     



