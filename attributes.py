import dpkt
import datetime
import socket
import numpy as np

def mac_addr(address):
    """Convert a MAC address to a readable/printable string
       Args:
           address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
       Returns:
           str: Printable/readable MAC address
    """
    return ':'.join('%02x' % ord(b) for b in address)


def ip_to_str(address):
    """Print out an IP address given a string
    Args:
        address (inet struct): inet network address
    Returns:
        str: Printable/readable IP address
    """
    return socket.inet_ntoa(address)



def print_packets(pcap):
    """Print out information about each packet in a pcap
       Args:
           pcap: dpkt pcap reader object (dpkt.pcap.Reader)
    """
    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:
        # Print out the timestamp in UTC
        print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))
        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)
        print 'Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type
        # Make sure the Ethernet frame contains an IP packet
        # EtherType (IP, ARP, PPPoE, IP6... see http://en.wikipedia.org/wiki/EtherType)
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
            continue
        # Now unpack the data within the Ethernet frame (the IP packet)
        # Pulling out src, dst, length, fragment info, TTL, and Protocol
        ip = eth.data
        # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
        # Print out the info
        print 'IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % \
              (ip_to_str(ip.src), ip_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset)

def Store_packets_info(pcap):
    """Store information about each packet in a pcap
           Args:
               pcap: dpkt pcap reader object (dpkt.pcap.Reader)
        """
    # For each packet in the pcap process the contents
    # Collect data and process , store respectively
    packets_length = []
    timestamp_set = []
    time2live = []
    slidewindow = []
    var_set = []
    percentage = []

    for timestamp, buf in pcap:
        # Print out the timestamp in UTC
        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)
        # Make sure the Ethernet frame contains an IP packet
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
            continue
        # Now unpack the data within the Ethernet frame (the IP packet)
        # Pulling out src, dst, length, fragment info, TTL, and Protocol
        ip = eth.data
        # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
        # Print out the info
        packets_length.append(ip.len+14)
        timestamp_set.append(timestamp)
        time2live.append(ip.ttl)
    # print 'packets_length'+ str(packets_length)
    # print 'time2live'+ str(time2live)
    # print 'timestamp_set'+ str(timestamp_set)
    # print len(timestamp_set)

    # process timestamp to calculate diff
    timestamp_diff = [0]
    for i in range(1,len(timestamp_set)):
        timestamp_diff.append(timestamp_set[i]-timestamp_set[i-1])
    # print 'timestamp_diff'+ str(timestamp_diff)
    # print len(timestamp_diff)

    # process to get mean value
    meanvalue = np.mean(np.array(packets_length))
    # print meanvalue

    # process to get var of whole
    narray = np.array(packets_length)
    var = np.var(narray)
    # print var

    # process to calcalate slidewindow and var accordingly
    for i in range(len(packets_length)):
        slice = np.array(packets_length)[i:i+20]
        # print slice
        slidewindow.append(np.mean(np.array(slice)))
        var_set.append(np.var(np.array(slice)))
        # print np.var(np.array(slice))
        # print np.mean(np.array(slice))
    # print slidewindow
    # print len(slidewindow)
    # print len(var_set)

    #process to get percentage of each size
    for i in packets_length:
        res = float(packets_length.count(i))/float(len(packets_length))
        percentage.append(res)
    # print len(percentage)
    # print percentage

    #     write datasets
    # format ::
    # packet_length , timestamp_diff , time2live , average len of packge , var of total ,average of slidewindow , var of sliddewindow , label

    f = open('testdata\sampledataset.txt', 'a')
    label = "COC"
    for i in range(len(packets_length)):
        f.writelines(str(packets_length[i]) +",")
        f.writelines(str(timestamp_diff[i]) + ",")
        f.writelines(str(time2live[i]) + ",")
        f.writelines(str(meanvalue) + ",")
        f.writelines(str(var) + ",")
        f.writelines(str(var_set[i]) + ",")
        f.writelines(str(slidewindow[i]) + ":")
        f.writelines("%s" % label+'\n')
        i += 1
    f.close()


def print_http_request(pcap):
    """Print out information about each packet in a pcap
           Args:
               pcap: dpkt pcap reader object (dpkt.pcap.Reader)
        """
    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:
        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)
        # Make sure the Ethernet data contains an IP packet
        if not isinstance(eth.data, dpkt.ip.IP):
            print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
            continue
        # Now grab the data within the Ethernet frame (the IP packet)
        ip = eth.data
        # Check for TCP in the transport layer
        if isinstance(ip.data, dpkt.tcp.TCP):
            # Set the TCP data
            tcp = ip.data
            # Now see if we can parse the contents as a HTTP request
            try:
                request = dpkt.http.Request(tcp.data)
                if tcp.dport == 80 and len(tcp.data) > 0:
                    http = dpkt.http.Request(tcp.data)
                    print http.uri
                    print http.method
                    print http.headers
                    print http.body
            except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                continue
            # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
            # Print out the info
            print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))
            print 'Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type
            print 'IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)' % \
                  (ip_to_str(ip.src), ip_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments,
                   fragment_offset)
            print 'HTTP request: %s\n' % repr(request).decode(encoding='utf-8')

def Go():
    """Open up a test pcap file and print out the packets"""
    with open('testsource/COC300s.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        Store_packets_info(pcap)
        # print_http_request(pcap)


if __name__ == '__main__':
    Go()