#!/usr/bin/env python

import dpkt
import sys
import db_neo4j

def str_from_mac(mac):
  """Returns a string representing a given MAC"""
  return "%02x:%02x:%02x:%02x:%02x:%02x" % (ord(mac[0]), ord(mac[1]), ord(mac[2]), \
                                              ord(mac[3]), ord(mac[4]), ord(mac[5]))
file = open(sys.argv[1])
pcap = dpkt.pcap.Reader(file)

db = db_neo4j.db_neo4j()

n = 1
for time_stamp, buf in pcap:
  eth = dpkt.ethernet.Ethernet(buf)
  db.insert_nodes_relation({"mac": str_from_mac(eth.src)}, {"mac": str_from_mac(eth.dst)}, str(n))
  print str_from_mac(eth.src), str_from_mac(eth.dst), str(n)
  n += 1

f.close()