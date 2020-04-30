# Shrek word-by-word script sender
This is a annoying script that sends someone on your Facebook Messenger the Shrek movie word by word.

![Original Image](https://i.imgur.com/7HVvmhC.jpg)
# Prerequisites
Make sure you have selenium installed

``pip install selenium``

Make sure you have the correct ``chromedriver.exe``, The one included in this project is for Chrome 81. If you have a
newer version of Chrome you can download the newest driver here https://chromedriver.chromium.org/

# Variables

```
facebookEmail = "YOUR FACEBOOK EMAIL"
facebookPassword = "YOUR FACEBOOK PASSWORD"
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1;
```
Note: friendName should match the exact name of the user. In the image above, friendName would be "Example1"

# Shrek Text

If you want to send something other than the Shrek movie script, just change the text in ***script.txt***

# Troubleshooting

``insertMessage = driver.find_element_by_class_name('_1mj')``

This line is responsible for finding the textbox on messenger. It does this by
passing the class name of the textbox. This class name might change in future Facebook updates.
To fix it simply "inspect element" on the text box and replace "_1mj" with the current class name.

![Inspect Element](https://i.imgur.com/jzSprwy.png)

