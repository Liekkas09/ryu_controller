'''
ports and ips
'''

s1_all_ip =['121.0.0.1', '121.0.0.2', '121.0.0.3', '121.0.0.4', '121.0.0.5']


s2_all_ip =['122.0.0.1', '122.0.0.2', '122.0.0.3', '122.0.0.4', '122.0.0.5']
s3_all_ip =['123.0.0.1', '123.0.0.2', '123.0.0.3', '123.0.0.4', '123.0.0.5']


s1_ports = [21, 23, 25, 80]
s2_ports = [21, 22, 23, 25]#, 80, 443]
s3_ports = [21, 22, 23]#, 25, 80, 443, 11, 13, 18, 19]

ext_ports = [1599, 2233]#, 15583, 8080, 8088, 9999]
k1 = s1_ports
k2 = s2_ports + ext_ports
k3 = s3_ports + ext_ports

s1_dst_ip = s2_all_ip + s3_all_ip
s2_dst_ip = s1_all_ip + s3_all_ip
s3_dst_ip = s1_all_ip + s2_all_ip
