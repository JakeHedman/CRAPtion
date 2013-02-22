```
# # # # # # # # # # # # # # # # # # # # # # # # # # #
#    _____ ______  ___  ______ _   _                #
#   /  __ \| ___ \/ _ \ | ___ \ | (_)               #
#   | /  \/| |_/ / /_\ \| |_/ / |_ _  ___  _ __     #
#   | |    |    /|  _  ||  __/| __| |/ _ \| '_ \    #
#   | \__/\| |\ \| | | || |   | |_| | (_) | | | |   #
#    \____/\_| \_\_| |_/\_|    \__|_|\___/|_| |_|   #
#                                                   #
#             Not as crappy as tinygrab             #
#                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
```
Requirements
------------
* OS X
* Python 2.x

### Python packages

* configobj
* dropbox

Config
------
```
cd
git clone https://github.com/spillevink/CRAPtion.git
echo export PATH=$path:~/CRAPtion >> .bash_profile
./CRAPtion/craption
vim .craptionrc
```
Dropbox login
```
python CRAPtion/settings.py dropbox
```
Restore default settings
```
python CRAPtion/settings.py clear-conf
```
Bind hotkey
* Open automator
* Create service
* Select run shell script
* Type python /path/to/craption
* Save your service/workflow
* Open System Pref -> Keyboard settings -> Keyboard shortcuts
* Find your service in Services

Todo:
-----
 * Linux
 * FTP
 * Libnotify/Growl
 * Your mom
