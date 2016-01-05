import os
import shutil
import subprocess


class GitCmd:
    def __init__(self, git_dir):
        self.dir = git_dir
        os.chdir(self.dir)

    def __get_repo_path(self, name):
        return '%s/%s.git' % (self.dir, name)

    def list_git_repos(self):
        return [f for f in os.listdir(self.dir) if f.endswith('.git') and os.path.isdir(self.dir + '/' + f)]

    def add_git_repo(self, name):
        if name in self.list_git_repos():
            raise ValueError('Name duplicated!')
        os.mkdir(self.__get_repo_path(name))
        p = subprocess.Popen(['git', 'init', '--bare'], cwd=self.__get_repo_path(name))
        p.communicate()
        p.wait()

    def del_git_repo(self, name):
        if (name + '.git') not in self.list_git_repos():
            raise ValueError('Repository is not found')
        # os.rmdir(self.__get_repo_path(name))
        shutil.rmtree(self.__get_repo_path(name))

    def get_ssh_public_keys(self):
        pass

    def set_ssh_public_keys(self, keyslot):
        pass


if __name__ == '__main__':
    g = GitCmd('/home/rayer/test_git/')
    print(g.list_git_repos())

    for c in xrange(0, 200, 2):
        print(g.del_git_repo('test-git-repo-%d' % c))
