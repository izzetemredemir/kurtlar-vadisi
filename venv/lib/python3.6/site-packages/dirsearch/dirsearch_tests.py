import os, unittest, uuid
from .dirsearch import dirsearch


class test_dirsearch(unittest.TestCase):
    def setUp(self):
        super(test_dirsearch, self).setUp()
        self.thispath = os.path.split(os.path.realpath(__file__))[0]
        self.testdir = os.path.join(self.thispath, 'temp', str(uuid.uuid4()).replace('-', ''))

        # create some tests files
        rel_paths = ['f1.test', 'dir1/f2.test', 'dir1/f1.test', 'dir1/dir/2f1.test', 'dir1/dir2/f1.test', 'dir1/dir3/f1.test']
        for rel_path in rel_paths:
            abs_path = os.path.join(self.testdir, rel_path)
            abs_dir = os.path.split(abs_path)[0]
            if not os.path.isdir(abs_dir):
                os.makedirs(abs_dir)
            open(abs_path, 'w')

    def tearDown(self):
        # remove test directory
        if os.path.exists(self.testdir):
            import shutil
            shutil.rmtree(self.testdir, ignore_errors=False)

    def test_search_default(self):

        # search
        path_list = dirsearch(self.testdir)

        # validate
        self.assertEqual(len(path_list), 6)

    def test_search_empty_resut(self):

        # search
        path_list = dirsearch(self.testdir, extension='*.no-such-ext')

        # validate
        self.assertEqual(len(path_list), 0)

    def test_search_non_recursive(self):

        # search
        path_list = dirsearch(self.testdir, extension='*.test', recursive=False)

        # validate
        self.assertEqual(len(path_list), 1)

    def test_search_recursive(self):

        # search
        path_list = dirsearch(self.testdir, extension='*.test', recursive=True)

        # validate
        self.assertEqual(len(path_list), 6)
