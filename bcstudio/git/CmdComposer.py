import os


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

    def del_git_repo(self, name):
        if name not in self.list_git_repos():
            raise ValueError('Repository is not found')

        os.rmdir(self.__get_repo_path(name))


if __name__ == '__main__':
    g = GitCmd('/opt/git/')
    g.list_git_repos()
    g.add_git_repo('AAA')
    g.del_git_repo('AAA')
    pass
