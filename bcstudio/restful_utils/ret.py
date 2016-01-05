import json

ret_stat_ok = {
    'status': 'ok'
}

ret_stat_err = {
    'status': 'err'
}


def gen_ret_ok(message='Request have been handled successfully'):
    ret = ret_stat_ok
    ret.update({'message': message})
    return json.dumps(ret)


def gen_ret_err(message='Internal Error'):
    ret = ret_stat_err
    ret.update({'message': message})
    return json.dumps(ret)
