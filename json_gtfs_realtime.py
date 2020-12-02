#!/usr/bin/env python
from google.protobuf import json_format
import sys, urllib.request, urllib.error, urllib.parse
import gtfs_realtime_pb2
import json

def main():
    json_rt = json.load(urllib.request.urlopen(sys.argv[1]))
    gtfs_realtime = gtfs_realtime_pb2.FeedMessage()
    json_format.ParseDict(json_rt, gtfs_realtime)
    with open(sys.argv[2], 'wb') as f:
        f.write(gtfs_realtime.SerializeToString())
    return

if __name__ == '__main__':
    main()
