# MIT License
#
# Copyright (c) Vasiliy Bondarenko vabondarenko@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json


class TezosActionMapper(object):

    def action_to_dict(self, action, transaction_dict):
        data = None
        if isinstance(action.get('data'), dict):
            data = dict_to_kv_list(action.get('data'))

        hex_data = None
        if isinstance(action.get('hex_data'), str):
            hex_data = action.get('hex_data')
        if hex_data is None and isinstance(action.get('data'), str):
            hex_data = action.get('data')

        result = {
            'type': 'action',
            'account': action.get('account'),
            'name': action.get('name'),
            'authorization': action.get('authorization'),
            'data': data,
            'hex_data': hex_data,
            'transaction_hash': transaction_dict.get('hash'),
            'block_hash': transaction_dict.get('block_hash'),
            'block_number': transaction_dict.get('block_number'),
            'block_timestamp': transaction_dict.get('block_timestamp'),
        }

        return result


def dict_to_kv_list(d):
    result = []
    for key, value in d.items():
        result.append({'key': to_str(key), 'value': to_str(value)})

    return result


def to_str(val):
    if val is None:
        val_str = None
    elif isinstance(val, str):
        val_str = val
    else:
        val_str = json.dumps(val)
    return val_str
