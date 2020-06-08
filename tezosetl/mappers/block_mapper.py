# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
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


class TezosBlockMapper(object):

    def block_to_dict(self, block):
        if block.get('transactions') is not None:
            transaction_count = len(block.get('transactions'))
        else:
            transaction_count = 0

        return {
            'type': 'block',
            'hash': block.get('id'),
            'number': block.get('block_num'),
            'ref_block_prefix': block.get('ref_block_prefix'),
            'previous': block.get('previous'),
            'action_mroot': block.get('action_mroot'),
            'transaction_mroot': block.get('transaction_mroot'),
            'new_producers': block.get('new_producers'),
            'header_extensions': block.get('header_extensions'),
            'block_extensions': block.get('block_extensions'),
            'timestamp': block.get('timestamp'),
            'producer': block.get('producer'),
            'transaction_count': transaction_count
        }
