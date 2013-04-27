import sys
import zipfile
import re

sys.modules["__main__"].__language__ = "en"
sys.modules["__main__"].__scriptname__ = "script.xbmc.subtitles"
sys.modules["__main__"].__cwd__ = "/tmp/"

LOGDEBUG=1

def log(msg, level=None):
    print msg

def executebuiltin(s):
    print "executebuiltin called, " + s

    m = re.search('XBMC.Extract\(([^,]*),([^\)]*)', s)
    if m:
        with zipfile.ZipFile(m.group(1), 'r') as z:
            z.extractall(m.group(2))
          
