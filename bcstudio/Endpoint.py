from flask import Flask
from flask import request
from bcstudio.git.CmdComposer import GitCmd
import json

app = Flask(__name__)
cmd = GitCmd('/opt/git/')


@app.route('/git', methods=['GET'])
def get_repo_list():
    return json.dumps(cmd.list_git_repos())

@app.route('/git', methods=['POST'])
def create_repo():
    req = request.get_json()
    cmd.add_git_repo(req['name'])
    return 'create ok'


@app.route('/git/<name>')
def get_repo_detail(name):
    return '%s placeholder!' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
