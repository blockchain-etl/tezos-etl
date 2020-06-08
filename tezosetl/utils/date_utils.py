from datetime import datetime


def convert_timestr_to_timestamp(timestr):
    d = datetime.strptime(timestr, '%Y-%m-%dT%H:%M:%SZ')
    return int(d.timestamp())
