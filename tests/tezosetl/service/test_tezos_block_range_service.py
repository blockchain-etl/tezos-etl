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

import pytest
from dateutil.parser import parse

from tezosetl.service.tezos_block_range_service import TezosBlockRangeService
from blockchainetl_common.graph.graph_operations import OutOfBoundsError
from tests.tezosetl.helpers import get_tezos_rpc
from tests.helpers import skip_if_slow_tests_disabled


@pytest.mark.parametrize("date,expected_start_block,expected_end_block", [
    skip_if_slow_tests_disabled(['2018-06-30', 0, 377]),
    skip_if_slow_tests_disabled(['2020-01-01', 760512, 761937]),
])
def test_get_block_range_for_date(date, expected_start_block, expected_end_block):
    tezos_block_range_service = get_new_tezos_block_range_service()
    parsed_date = parse(date)
    blocks = tezos_block_range_service.get_block_range_for_date(parsed_date)
    assert (expected_start_block, expected_end_block) == blocks


@pytest.mark.parametrize("date", [
    skip_if_slow_tests_disabled(['2030-01-01'])
])
def test_get_block_range_for_date_fail(date):
    tezos_service = get_new_tezos_block_range_service()
    parsed_date = parse(date)
    with pytest.raises(OutOfBoundsError):
        tezos_service.get_block_range_for_date(parsed_date)


def get_new_tezos_block_range_service():
    rpc = get_tezos_rpc("online")
    return TezosBlockRangeService(rpc)
