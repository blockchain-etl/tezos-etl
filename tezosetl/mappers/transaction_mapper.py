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


class TezosTransactionMapper(object):

    def transaction_to_dict(self, transaction, block):
        transaction_dict = {
            'type': 'transaction',
            'block_hash': block.get('id'),
            'block_number': block.get('block_num'),
            'block_timestamp': block.get('timestamp'),
            'status': transaction.get('status'),
            'cpu_usage_us': transaction.get('cpu_usage_us'),
            'net_usage_words': transaction.get('net_usage_words'),
        }

        trx = transaction.get('trx')

        if isinstance(trx, dict):
            transaction_dict['deferred'] = False
            transaction_dict['hash'] = trx.get('id')
            transaction_dict['signatures'] = trx.get('signatures')
            transaction_dict['packed_context_free_data'] = trx.get('packed_context_free_data')
            transaction_dict['context_free_data'] = trx.get('context_free_data')
            transaction_dict['packed_trx'] = trx.get('packed_trx')

            trx_transaction = trx.get('transaction')

            if trx_transaction is not None:
                transaction_dict['expiration'] = trx_transaction.get('expiration')
                transaction_dict['max_net_usage_words'] = trx_transaction.get('max_net_usage_words')
                transaction_dict['max_cpu_usage_ms'] = trx_transaction.get('max_cpu_usage_ms')
                transaction_dict['delay_sec'] = trx_transaction.get('delay_sec')
                transaction_dict['transaction_extensions'] = trx_transaction.get('transaction_extensions')

                actions = trx_transaction.get('actions')
                if actions is not None and hasattr(actions, '__len__'):
                    transaction_dict['action_count'] = len(actions)

        elif isinstance(trx, str):
            transaction_dict['hash'] = trx
            transaction_dict['deferred'] = True

        return transaction_dict
