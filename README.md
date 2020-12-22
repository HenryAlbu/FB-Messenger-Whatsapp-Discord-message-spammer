# Shrek word-by-word script sender

![Original Image](https://i.imgur.com/7HVvmhC.jpg)
# Prerequisites
Make sure you have selenium installed

``pip install selenium``

Make sure you have the correct ``chromedriver.exe``, The one included in this project is for Chrome 81. If you have a
newer version of Chrome you can download the newest driver here https://chromedriver.chromium.org/

# Variables

#### Facebook Messenger (auto_shrek_messenger.py)
```
facebookEmail = "YOUR FACEBOOK EMAIL"
facebookPassword = "YOUR FACEBOOK PASSWORD"
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1;
```

#### Whatsapp (auto_shrek_whatsapp.py)
```
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1;
```

When presented with the WhatsApp login screen, scan the QR code with your phone so that the 
script can proceed.

---
*Note: friendName should match the exact name of the user. In the image above, friendName would be "Example1". This applies to both Whatsapp and Messenger scripts*

# Shrek Text

If you want to send something other than the Shrek movie script, just change the text in ***script.txt***

# Troubleshooting

``insertMessage = driver.find_element_by_class_name('_1mj')``

This line is responsible for finding the textbox on messenger. It does this by
passing the class name of the textbox. This class name might change in future Facebook updates.
To fix it simply "inspect element" on the text box and replace "_1mj" with the current class name.

![Inspect Element](https://i.imgur.com/jzSprwy.png)
