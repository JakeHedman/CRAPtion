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
echo export PATH=$PATH:~/CRAPtion >> .bash_profile
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
