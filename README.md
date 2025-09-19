NOTE: I am not a good dev and did not create a requirements text or package this properly......but will eventually.

# Lawyer-Web-Contact-Tool #
## To expedite your hunt for an attorney ##
### Looking up attorneys is daunting. Then you have to find their contact buttons to send them an email.
Hopefully this will cut down on your search and send time.

<a href="https://www.buymeacoffee.com/diatasso" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 145px !important;" ></a>

The code got a MAJOR facelift this weekend and looks "prettier". The entire program will be getting a huge facelift as well after seeing a comment in another post. Here is the new look, I need to upload the code to git. I can't figure out how to center the ascii art, I suck.

# To do:
How about a multi function option added to the menu?
**The new tool will also include physicians, but with some new features added as well. The NEW version will be called: PSRT = The Professional Search and Report tool.**

# Features coming will:
2. Look up current bar status (attorney).
3. Review lookup.
4. Report ethics violation (bar association).
5. Social media (Google, LI, Facebook) review page for that person if they have one. Because everyone deserves to be highlighted for their work.

# To run in cloud shell (note: will not open web browser, will give you the dork to copy into google)
1. pip install pipx
2. delete the following:
+ import webbrowser
+ import win32gui
+ import win32con
+ hwnd = win32gui.GetForegroundWindow()
+ win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/michaelnotadev/Lawyer-Web-Contact-Tool)
