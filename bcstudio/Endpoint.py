import json

from flask import Flask
from flask import Response
from flask import request

from bcstudio.git.CmdComposer import GitCmd
from restful_utils import ret

app = Flask(__name__)
cmd = GitCmd('/opt/git/')


@app.route('/git', methods=['GET'])
def get_repo_list():
    return Response(json.dumps(cmd.list_git_repos()), mimetype='application/json')


@app.route('/git', methods=['POST'])
def create_repo():
    req = request.get_json()
    cmd.add_git_repo(req['name'])
    return Response(ret.gen_ret_ok(message='git clone %s' % cmd.get_git_clone_path()), mimetype='application/json')


@app.route('/git/<name>', methods=['DELETE'])
def delete_repo(name):
    cmd.del_git_repo(name)
    return Response(ret.gen_ret_ok(), mimetype='application/json')


@app.route('/git/<name>')
def get_repo_detail(name):
    return '%s placeholder!' % name


# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('templates/template.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
