#!/usr/bin/python

## Example topology for containernet
## Created by Jorge Lopez 

"""
This is a simple example of a Containernet custom topology.
"""
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
import sys
setLogLevel('info')

net = Containernet()
info('*** Adding controller\n')
c0 = RemoteController( 'c0' )
net.addController(c0)
info('*** Adding docker containers\n')
h1 = net.addDocker('h1', ip='10.0.0.251', mac='9a:d8:73:d8:90:6a', dimage="mysql:5.7", environment={"MYSQL_DATABASE": "exampledb", "MYSQL_USER": "exampleuser", "MYSQL_PASSWORD": "examplepass", "MYSQL_RANDOM_ROOT_PASSWORD": "1" })
h2 = net.addDocker('h2', ip='10.0.0.252', mac='9a:d8:73:d8:90:6b', dimage="wordpress:latest", ports=[8080], port_bindings={80:8080}, publish_all_ports=True, environment={"WORDPRESS_DB_HOST": "10.0.0.251", "WORDPRESS_DB_USER": "exampleuser", "WORDPRESS_DB_PASSWORD": "examplepass", "WORDPRESS_DB_NAME": "exampledb"})
h3 = net.addDocker('h3', ip='10.0.0.253', mac='9a:d8:73:d8:90:6c', dimage="lab-api", ports=[8888], port_bindings={5000:8888}, publish_all_ports=True)
h4 = net.addDocker('h4', ip='10.0.0.254', mac='9a:d8:73:d8:90:6d', dimage="lab-web", ports=[8081], port_bindings={80:8081}, publish_all_ports=True)
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
info('*** Creating links\n')
net.addLink( h1, s1, 1, 1 )
net.addLink( h2, s2, 1, 1 )
net.addLink( h3, s3, 1, 1 )
net.addLink( h4, s4, 1, 1 )
net.addLink( s1, s2, 2, 2 )
net.addLink( s1, s3, 3, 2 )
net.addLink( s2, s3, 3, 3 )
net.addLink( s2, s4, 4, 2 )
net.addLink( s3, s4, 4, 3 )
info('*** Starting network\n')
net.start()
info('*** Running CLI\n')
CLI(net)
net.stop()
