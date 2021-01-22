#x = win32com.client.Dispatch("AppRobotic.API")
import webbrowser
import os
import mouse
#import Tools.scripts.google

 
# specify URL
url = "https://www.google.com"

# open with default browser
webbrowser.open_new(url) 
# open with Safari, if installed
#webbrowser.get('safari').open_new(url) 
# open with Firefox, if installed
webbrowser.get('firefox').open_new_tab(url) 
# open with Chrome, if installed
#webbrowser.get(using='google-chrome').open_new(url)
 
# wait a bit for page to open
#x.Wait(3000)
# use UI Item Explorer to find the X,Y coordinates of Search box
#x.MoveCursor(438, 435)
# click inside Search box
#x.MouseLeftClick
 
#x.Type("AppRobotic")
#x.Type("{ENTER}")