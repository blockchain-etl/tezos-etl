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


from datetime import datetime, timezone

from tezosetl.service.tezos_block_timestamp_graph import BlockTimestampGraph
from blockchainetl_common.graph.graph_operations import GraphOperations, OutOfBoundsError


class TezosBlockRangeService(object):
    def __init__(self, tezos_rpc):
        graph = BlockTimestampGraph(tezos_rpc)
        self._graph_operations = GraphOperations(graph, max_not_monotonic_points=5, prefetch_size=0)

    def get_block_range_for_date(self, date):
        start_datetime = datetime.combine(date, datetime.min.time().replace(tzinfo=timezone.utc))
        end_datetime = datetime.combine(date, datetime.max.time().replace(tzinfo=timezone.utc))
        return self.get_block_range_for_timestamps(start_datetime.timestamp(), end_datetime.timestamp())

    def get_block_range_for_timestamps(self, start_timestamp, end_timestamp):
        start_timestamp = start_timestamp
        end_timestamp = end_timestamp
        if start_timestamp > end_timestamp:
            raise ValueError('start_timestamp must be greater or equal to end_timestamp')

        try:
            start_block_bounds = self._graph_operations.get_bounds_for_y_coordinate(start_timestamp)
        except OutOfBoundsError:
            start_block_bounds = (0, 0)

        try:
            end_block_bounds = self._graph_operations.get_bounds_for_y_coordinate(end_timestamp)
        except OutOfBoundsError as e:
            raise OutOfBoundsError('The existing blocks do not completely cover the given time range') from e

        if start_block_bounds == end_block_bounds and start_block_bounds[0] != start_block_bounds[1]:
            raise ValueError('The given timestamp range does not cover any blocks')

        start_block = start_block_bounds[1]
        end_block = end_block_bounds[0]

        return start_block, end_block


