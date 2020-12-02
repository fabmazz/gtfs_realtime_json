#!/usr/bin/env python
import sys, urllib.request, urllib.error, urllib.parse
import gtfs_realtime_pb2
import protobuf_json
import json

def main():
    gtfs_realtime = gtfs_realtime_pb2.FeedMessage()
    req = urllib.request.urlopen(sys.argv[1])
    data = req.read()
    gtfs_realtime.ParseFromString(data)
    print(json.dumps(
        protobuf_json.pb2json(gtfs_realtime), separators=(',',':'), indent=2))
    return
    
if __name__ == '__main__':
    main()
