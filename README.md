# Shrek word-by-word script sender

![Original Image](https://i.imgur.com/7HVvmhC.jpg)
# Prerequisites
Make sure you have selenium installed

``pip install selenium``

Make sure you have the correct ``chromedriver.exe``, The one included in this project is for Chrome 81. If you have a
newer version of Chrome you can download the newest driver here:
https://chromedriver.chromium.org/

# Variables

#### 
```
email = "YOUR EMAIL"
password = "YOUR PASSWORD"
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1;
```
*Note: friendName should match the exact name of the user. In the image above, friendName would be "Example1". This applies to both Whatsapp/Messenger and Discord scripts*


#### Whatsapp (auto_shrek_whatsapp.py)
When presented with the WhatsApp login screen, scan the QR code with your phone so that the 
script can proceed.

#### Discord (auto_shrek_discord.py)
Currently can only send DMs.


# Shrek Text

If you want to send something other than the Shrek movie script, just change the text in ***script.txt***

