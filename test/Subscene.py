import os
import sys
import unittest
import tempfile

cwd = os.getcwd()
sys.path = sys.path + [os.path.join(cwd, 'mock'),
                       os.path.join(cwd, '..', 'script.xbmc.subtitles', 'resources', 'lib', 'services', 'Subscene'),
                       os.path.join(cwd, '..', 'script.xbmc.subtitles', 'resources', 'lib')]
import service

# Test goes here
class TestSubscene(unittest.TestCase):

    def test_revolution_s01e14(self):
        tmpdir = tempfile.mkdtemp(dir=tempfile.gettempdir())

        title = "Revolution.2012.S01E14.720p.HDTV.X264-DIMENSION.mkv"
        show = "Revolution 2012"
        s = "1"
        ep = "14"

        print "Using " + tmpdir + " for downloading"

        x=service.search_subtitles(tmpdir, title, show, "", s, ep, "", "", "English", "", "", "")
        for s in x[0]:
            print s["filename"]

        self.assertNotEqual(x, ([], '', ''))
        z = service.download_subtitles(x[0], 0, "", tmpdir, "", "")
        self.assertNotEqual(z, ([], '', ''))

    def test_nikita_s03e19(self):
        tmpdir = tempfile.mkdtemp(dir=tempfile.gettempdir())

        title = "Nikita.S03E19.720p.HDTV.X264-DIMENSION.mkv"
        show = "Nikita"
        s = "3"
        ep = "19"

        print "Using " + tmpdir + " for downloading"

        x=service.search_subtitles(tmpdir, title, show, "", s, ep, "", "", "English", "", "", "")
        for s in x[0]:
            print s["filename"]
        self.assertNotEqual(x, ([], '', ''))
        z = service.download_subtitles(x[0], 0, "", tmpdir, "", "")
        self.assertNotEqual(z, ([], '', ''))

    def test_homeland_s02e01(self):
        tmpdir = tempfile.mkdtemp(dir=tempfile.gettempdir())

        title = "Homeland.S02E01"
        show = "Homeland"
        s = "2"
        ep = "1"

        print "Using " + tmpdir + " for downloading"

        x=service.search_subtitles(tmpdir, title, show, "", s, ep, "", "", "English", "", "", "")
        for s in x[0]:
            print s["filename"]
        self.assertNotEqual(x, ([], '', ''))
        z = service.download_subtitles(x[0], 0, "", tmpdir, "", "")
        self.assertNotEqual(z, ([], '', ''))

        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            suite = unittest.TestSuite()
            suite.addTest(TestSubscene(sys.argv[1]))
            unittest.TextTestRunner(verbosity=2).run(suite)
        except ValueError as ex:
            unittest.main()
    else:
        unittest.main()


