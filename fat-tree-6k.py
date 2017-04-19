#!/usr/bin/python

from mininet.net import Mininet
from mininet.term import makeTerm
from mininet.node import RemoteController
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import json
from bottle import route, run, request

net = "net_object"


def myFatTree():
    global net
    net = Mininet(topo=None,
                  link=TCLink,
                  build=False,
                  ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='172.20.5.41',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    info('*** switches protocols')
    openFlowVersions = []
    openFlowVersions.append('OpenFlow13')
    protoList = ",".join(openFlowVersions)
    switchParms = {}
    switchParms['protocols'] = protoList
    # K-ary fat tree: three-layer topology (edge, aggregation and core)
    # each pod consists of (k/2)^2 servers & 2 layers of k/2 k-port switches
    # each edge switch connects to k/2 servers & k/2 aggr. switches
    # each aggr. switch connects to k/2 edge & k/2 core switches
    # (k/2)^2 core switches: each connects to k pods

    # ------------------------CORE---------------------------------
    cs1 = net.addSwitch('cs1', cls=OVSKernelSwitch, **switchParms)
    cs2 = net.addSwitch('cs2', cls=OVSKernelSwitch, **switchParms)
    cs3 = net.addSwitch('cs3', cls=OVSKernelSwitch, **switchParms)
    cs4 = net.addSwitch('cs4', cls=OVSKernelSwitch, **switchParms)

    cs5 = net.addSwitch('cs5', cls=OVSKernelSwitch, **switchParms)
    cs6 = net.addSwitch('cs6', cls=OVSKernelSwitch, **switchParms)
    cs7 = net.addSwitch('cs7', cls=OVSKernelSwitch, **switchParms)
    cs8 = net.addSwitch('cs8', cls=OVSKernelSwitch, **switchParms)
    cs9 = net.addSwitch('cs9', cls=OVSKernelSwitch, **switchParms)

    # -----------------------------AGRE----------------------------
    # POD 1
    as11 = net.addSwitch('as11', cls=OVSKernelSwitch, **switchParms)
    as22 = net.addSwitch('as22', cls=OVSKernelSwitch, **switchParms)
    as33 = net.addSwitch('as33', cls=OVSKernelSwitch, **switchParms)
    # POD 2
    as44 = net.addSwitch('as44', cls=OVSKernelSwitch, **switchParms)
    as55 = net.addSwitch('as55', cls=OVSKernelSwitch, **switchParms)
    as66 = net.addSwitch('as66', cls=OVSKernelSwitch, **switchParms)
    # POD 3
    as77 = net.addSwitch('as77', cls=OVSKernelSwitch, **switchParms)
    as88 = net.addSwitch('as88', cls=OVSKernelSwitch, **switchParms)
    as99 = net.addSwitch('as99', cls=OVSKernelSwitch, **switchParms)
    # POD 4
    as100 = net.addSwitch('as100', cls=OVSKernelSwitch, **switchParms)
    as110 = net.addSwitch('as110', cls=OVSKernelSwitch, **switchParms)
    as120 = net.addSwitch('as120', cls=OVSKernelSwitch, **switchParms)
    # PD 5
    as130 = net.addSwitch('as130', cls=OVSKernelSwitch, **switchParms)
    as140 = net.addSwitch('as140', cls=OVSKernelSwitch, **switchParms)
    as150 = net.addSwitch('as150', cls=OVSKernelSwitch, **switchParms)
    # PD 6
    as160 = net.addSwitch('as160', cls=OVSKernelSwitch, **switchParms)
    as170 = net.addSwitch('as170', cls=OVSKernelSwitch, **switchParms)
    as180 = net.addSwitch('as180', cls=OVSKernelSwitch, **switchParms)

    # -------------------------EDGE-----------------------------------
    # POD 1
    es111 = net.addSwitch('es111', cls=OVSKernelSwitch, **switchParms)
    es222 = net.addSwitch('es222', cls=OVSKernelSwitch, **switchParms)
    es333 = net.addSwitch('es333', cls=OVSKernelSwitch, **switchParms)
    # POD 2
    es444 = net.addSwitch('es444', cls=OVSKernelSwitch, **switchParms)
    es555 = net.addSwitch('es555', cls=OVSKernelSwitch, **switchParms)
    es666 = net.addSwitch('es666', cls=OVSKernelSwitch, **switchParms)
    # POD 3
    es777 = net.addSwitch('es777', cls=OVSKernelSwitch, **switchParms)
    es888 = net.addSwitch('es888', cls=OVSKernelSwitch, **switchParms)
    es999 = net.addSwitch('es999', cls=OVSKernelSwitch, **switchParms)
    # POD 4
    es1000 = net.addSwitch('es1000', cls=OVSKernelSwitch, **switchParms)
    es1100 = net.addSwitch('es1100', cls=OVSKernelSwitch, **switchParms)
    es1200 = net.addSwitch('es1200', cls=OVSKernelSwitch, **switchParms)
    # POD 5
    es1300 = net.addSwitch('es1300', cls=OVSKernelSwitch, **switchParms)
    es1400 = net.addSwitch('es1400', cls=OVSKernelSwitch, **switchParms)
    es1500 = net.addSwitch('es1500', cls=OVSKernelSwitch, **switchParms)
    # POD 6
    es1600 = net.addSwitch('es1600', cls=OVSKernelSwitch, **switchParms)
    es1700 = net.addSwitch('es1700', cls=OVSKernelSwitch, **switchParms)
    es1800 = net.addSwitch('es1800', cls=OVSKernelSwitch, **switchParms)

    info('*** Add hosts\n')
    # POD 1
    pod1h1 = net.addHost('pod1h1', cls=Host, ip='10.0.0.1', mac='B6:29:CE:E1:DB:11', defaultRoute=None)
    pod1h2 = net.addHost('pod1h2', cls=Host, ip='10.0.0.2', mac='B6:29:CE:E1:DB:12', defaultRoute=None)
    pod1h3 = net.addHost('pod1h3', cls=Host, ip='10.0.0.3', mac='92:88:E9:9C:0D:13', defaultRoute=None)

    pod1h4 = net.addHost('pod1h4', cls=Host, ip='10.0.0.4', mac='92:88:E9:9C:0D:14', defaultRoute=None)
    pod1h5 = net.addHost('pod1h5', cls=Host, ip='10.0.0.5', mac='92:88:E9:9C:0D:15', defaultRoute=None)
    pod1h6 = net.addHost('pod1h6', cls=Host, ip='10.0.0.6', mac='92:88:E9:9C:0D:16', defaultRoute=None)

    pod1h7 = net.addHost('pod1h7', cls=Host, ip='10.0.0.7', mac='92:88:E9:9C:0D:17', defaultRoute=None)
    pod1h8 = net.addHost('pod1h8', cls=Host, ip='10.0.0.8', mac='92:88:E9:9C:0D:18', defaultRoute=None)
    pod1h9 = net.addHost('pod1h9', cls=Host, ip='10.0.0.9', mac='92:88:E9:9C:0D:19', defaultRoute=None)

    # POD 2
    pod2h1 = net.addHost('pod2h1', cls=Host, ip='10.0.0.10', mac='92:88:E9:9C:0D:21', defaultRoute=None)
    pod2h2 = net.addHost('pod2h2', cls=Host, ip='10.0.0.11', mac='92:88:E9:9C:0D:22', defaultRoute=None)
    pod2h3 = net.addHost('pod2h3', cls=Host, ip='10.0.0.12', mac='92:88:E9:9C:0D:23', defaultRoute=None)

    pod2h4 = net.addHost('pod2h4', cls=Host, ip='10.0.0.13', mac='92:88:E9:9C:0D:24', defaultRoute=None)
    pod2h5 = net.addHost('pod2h5', cls=Host, ip='10.0.0.14', mac='92:88:E9:9C:0D:25', defaultRoute=None)
    pod2h6 = net.addHost('pod2h6', cls=Host, ip='10.0.0.15', mac='92:88:E9:9C:0D:26', defaultRoute=None)

    pod2h7 = net.addHost('pod2h7', cls=Host, ip='10.0.0.16', mac='92:88:E9:9C:0D:27', defaultRoute=None)
    pod2h8 = net.addHost('pod2h8', cls=Host, ip='10.0.0.17', mac='92:88:E9:9C:0D:28', defaultRoute=None)
    pod2h9 = net.addHost('pod2h9', cls=Host, ip='10.0.0.18', mac='92:88:E9:9C:0D:29', defaultRoute=None)

    # POD 3
    pod3h1 = net.addHost('pod3h1', cls=Host, ip='10.0.0.19', mac='92:88:E9:9C:0D:31', defaultRoute=None)
    pod3h2 = net.addHost('pod3h2', cls=Host, ip='10.0.0.20', mac='92:88:E9:9C:0D:32', defaultRoute=None)
    pod3h3 = net.addHost('pod3h3', cls=Host, ip='10.0.0.21', mac='92:88:E9:9C:0D:33', defaultRoute=None)

    pod3h4 = net.addHost('pod3h4', cls=Host, ip='10.0.0.22', mac='92:88:E9:9C:0D:34', defaultRoute=None)
    pod3h5 = net.addHost('pod3h5', cls=Host, ip='10.0.0.23', mac='92:88:E9:9C:0D:35', defaultRoute=None)
    pod3h6 = net.addHost('pod3h6', cls=Host, ip='10.0.0.24', mac='92:88:E9:9C:0D:36', defaultRoute=None)

    pod3h7 = net.addHost('pod3h7', cls=Host, ip='10.0.0.25', mac='92:88:E9:9C:0D:37', defaultRoute=None)
    pod3h8 = net.addHost('pod3h8', cls=Host, ip='10.0.0.26', mac='92:88:E9:9C:0D:38', defaultRoute=None)
    pod3h9 = net.addHost('pod3h9', cls=Host, ip='10.0.0.27', mac='92:88:E9:9C:0D:39', defaultRoute=None)

    # POD 4
    pod4h1 = net.addHost('pod4h1', cls=Host, ip='10.0.0.28', mac='92:88:E9:9C:0D:41', defaultRoute=None)
    pod4h2 = net.addHost('pod4h2', cls=Host, ip='10.0.0.29', mac='92:88:E9:9C:0D:42', defaultRoute=None)
    pod4h3 = net.addHost('pod4h3', cls=Host, ip='10.0.0.30', mac='92:88:E9:9C:0D:43', defaultRoute=None)

    pod4h4 = net.addHost('pod4h4', cls=Host, ip='10.0.0.31', mac='92:88:E9:9C:0D:44', defaultRoute=None)
    pod4h5 = net.addHost('pod4h5', cls=Host, ip='10.0.0.32', mac='92:88:E9:9C:0D:45', defaultRoute=None)
    pod4h6 = net.addHost('pod4h6', cls=Host, ip='10.0.0.33', mac='92:88:E9:9C:0D:46', defaultRoute=None)

    pod4h7 = net.addHost('pod4h7', cls=Host, ip='10.0.0.34', mac='92:88:E9:9C:0D:47', defaultRoute=None)
    pod4h8 = net.addHost('pod4h8', cls=Host, ip='10.0.0.35', mac='92:88:E9:9C:0D:48', defaultRoute=None)
    pod4h9 = net.addHost('pod4h9', cls=Host, ip='10.0.0.36', mac='92:88:E9:9C:0D:49', defaultRoute=None)

    # POD 5
    pod5h1 = net.addHost('pod5h1', cls=Host, ip='10.0.0.37', mac='92:88:E9:9C:0D:51', defaultRoute=None)
    pod5h2 = net.addHost('pod5h2', cls=Host, ip='10.0.0.38', mac='92:88:E9:9C:0D:52', defaultRoute=None)
    pod5h3 = net.addHost('pod5h3', cls=Host, ip='10.0.0.39', mac='92:88:E9:9C:0D:53', defaultRoute=None)

    pod5h4 = net.addHost('pod5h4', cls=Host, ip='10.0.0.40', mac='92:88:E9:9C:0D:54', defaultRoute=None)
    pod5h5 = net.addHost('pod5h5', cls=Host, ip='10.0.0.41', mac='92:88:E9:9C:0D:55', defaultRoute=None)
    pod5h6 = net.addHost('pod5h6', cls=Host, ip='10.0.0.42', mac='92:88:E9:9C:0D:56', defaultRoute=None)

    pod5h7 = net.addHost('pod5h7', cls=Host, ip='10.0.0.43', mac='92:88:E9:9C:0D:57', defaultRoute=None)
    pod5h8 = net.addHost('pod5h8', cls=Host, ip='10.0.0.44', mac='92:88:E9:9C:0D:58', defaultRoute=None)
    pod5h9 = net.addHost('pod5h9', cls=Host, ip='10.0.0.45', mac='92:88:E9:9C:0D:59', defaultRoute=None)

    # POD 6
    pod6h1 = net.addHost('pod6h1', cls=Host, ip='10.0.0.46', mac='92:88:E9:9C:0D:61', defaultRoute=None)
    pod6h2 = net.addHost('pod6h2', cls=Host, ip='10.0.0.47', mac='92:88:E9:9C:0D:62', defaultRoute=None)
    pod6h3 = net.addHost('pod6h3', cls=Host, ip='10.0.0.48', mac='92:88:E9:9C:0D:63', defaultRoute=None)

    pod6h4 = net.addHost('pod6h4', cls=Host, ip='10.0.0.49', mac='92:88:E9:9C:0D:64', defaultRoute=None)
    pod6h5 = net.addHost('pod6h5', cls=Host, ip='10.0.0.50', mac='92:88:E9:9C:0D:65', defaultRoute=None)
    pod6h6 = net.addHost('pod6h6', cls=Host, ip='10.0.0.51', mac='92:88:E9:9C:0D:66', defaultRoute=None)

    pod6h7 = net.addHost('pod6h7', cls=Host, ip='10.0.0.52', mac='92:88:E9:9C:0D:67', defaultRoute=None)
    pod6h8 = net.addHost('pod6h8', cls=Host, ip='10.0.0.53', mac='92:88:E9:9C:0D:68', defaultRoute=None)
    pod6h9 = net.addHost('pod6h9', cls=Host, ip='10.0.0.54', mac='92:88:E9:9C:0D:69', defaultRoute=None)

    info('*** Add links\n')
# ---------------------CORE----------------------------------------
    net.addLink(cs1, as11, bw=10)
    net.addLink(cs1, as44, bw=10)
    net.addLink(cs1, as77, bw=10)
    net.addLink(cs1, as100, bw=10)
    net.addLink(cs1, as130, bw=10)
    net.addLink(cs1, as160, bw=10)

    net.addLink(cs2, as11, bw=10)
    net.addLink(cs2, as44, bw=10)
    net.addLink(cs2, as77, bw=10)
    net.addLink(cs2, as100, bw=10)
    net.addLink(cs2, as130, bw=10)
    net.addLink(cs2, as160, bw=10)

    net.addLink(cs3, as11, bw=10)
    net.addLink(cs3, as44, bw=10)
    net.addLink(cs3, as77, bw=10)
    net.addLink(cs3, as100, bw=10)
    net.addLink(cs3, as130, bw=10)
    net.addLink(cs3, as160, bw=10)
# -------------------------------------
    net.addLink(cs4, as22, bw=10)
    net.addLink(cs4, as55, bw=10)
    net.addLink(cs4, as88, bw=10)
    net.addLink(cs4, as110, bw=10)
    net.addLink(cs4, as140, bw=10)
    net.addLink(cs4, as170, bw=10)

    net.addLink(cs5, as22, bw=10)
    net.addLink(cs5, as55, bw=10)
    net.addLink(cs5, as88, bw=10)
    net.addLink(cs5, as110, bw=10)
    net.addLink(cs5, as140, bw=10)
    net.addLink(cs5, as170, bw=10)

    net.addLink(cs6, as22, bw=10)
    net.addLink(cs6, as55, bw=10)
    net.addLink(cs6, as88, bw=10)
    net.addLink(cs6, as110, bw=10)
    net.addLink(cs6, as140, bw=10)
    net.addLink(cs6, as170, bw=10)
# -------------------------------------
    net.addLink(cs7, as33, bw=10)
    net.addLink(cs7, as66, bw=10)
    net.addLink(cs7, as99, bw=10)
    net.addLink(cs7, as120, bw=10)
    net.addLink(cs7, as150, bw=10)
    net.addLink(cs7, as180, bw=10)

    net.addLink(cs8, as33, bw=10)
    net.addLink(cs8, as66, bw=10)
    net.addLink(cs8, as99, bw=10)
    net.addLink(cs8, as120, bw=10)
    net.addLink(cs8, as150, bw=10)
    net.addLink(cs8, as180, bw=10)

    net.addLink(cs9, as33, bw=10)
    net.addLink(cs9, as66, bw=10)
    net.addLink(cs9, as99, bw=10)
    net.addLink(cs9, as120, bw=10)
    net.addLink(cs9, as150, bw=10)
    net.addLink(cs9, as180, bw=10)

# ----------------------AGGREGATION------------------------------
    net.addLink(as11, es111, bw=10)
    net.addLink(as11, es222, bw=10)
    net.addLink(as11, es333, bw=10)

    net.addLink(as22, es111, bw=10)
    net.addLink(as22, es222, bw=10)
    net.addLink(as22, es333, bw=10)

    net.addLink(as33, es111, bw=10)
    net.addLink(as33, es222, bw=10)
    net.addLink(as33, es333, bw=10)
# ----------------------------------------2
    net.addLink(as44, es444, bw=10)
    net.addLink(as44, es555, bw=10)
    net.addLink(as44, es666, bw=10)

    net.addLink(as55, es444, bw=10)
    net.addLink(as55, es555, bw=11)
    net.addLink(as55, es666, bw=10)

    net.addLink(as66, es444, bw=10)
    net.addLink(as66, es555, bw=10)
    net.addLink(as66, es666, bw=10)
# -----------------------------------------------3
    net.addLink(as77, es777, bw=10)
    net.addLink(as77, es888, bw=10)
    net.addLink(as77, es999, bw=10)

    net.addLink(as88, es777, bw=10)
    net.addLink(as88, es888, bw=10)
    net.addLink(as88, es999, bw=10)

    net.addLink(as99, es777, bw=10)
    net.addLink(as99, es888, bw=10)
    net.addLink(as99, es999, bw=10)
# -------------------------------------------------4
    net.addLink(as100, es1000, bw=10)
    net.addLink(as100, es1100, bw=10)
    net.addLink(as100, es1200, bw=10)

    net.addLink(as110, es1000, bw=10)
    net.addLink(as110, es1100, bw=10)
    net.addLink(as110, es1200, bw=10)

    net.addLink(as120, es1000, bw=10)
    net.addLink(as120, es1100, bw=10)
    net.addLink(as120, es1200, bw=10)
# -------------------------------------------------5
    net.addLink(as130, es1300, bw=10)
    net.addLink(as130, es1400, bw=10)
    net.addLink(as130, es1500, bw=10)

    net.addLink(as140, es1300, bw=10)
    net.addLink(as140, es1400, bw=10)
    net.addLink(as140, es1500, bw=10)

    net.addLink(as150, es1300, bw=10)
    net.addLink(as150, es1400, bw=10)
    net.addLink(as150, es1500, bw=10)
# -------------------------------------------------6
    net.addLink(as160, es1600, bw=10)
    net.addLink(as160, es1700, bw=10)
    net.addLink(as160, es1800, bw=10)

    net.addLink(as170, es1600, bw=10)
    net.addLink(as170, es1700, bw=10)
    net.addLink(as170, es1800, bw=10)

    net.addLink(as180, es1600, bw=10)
    net.addLink(as180, es1700, bw=10)
    net.addLink(as180, es1800, bw=10)

# -------------------------EDGE------------------------------------
    net.addLink(es111, pod1h1, bw=20)
    net.addLink(es111, pod1h2, bw=20)
    net.addLink(es111, pod1h3, bw=20)

    net.addLink(es222, pod1h4, bw=20)
    net.addLink(es222, pod1h5, bw=20)
    net.addLink(es222, pod1h6, bw=20)

    net.addLink(es333, pod1h7, bw=20)
    net.addLink(es333, pod1h8, bw=20)
    net.addLink(es333, pod1h9, bw=20)
# -------------------------------------------2
    net.addLink(es444, pod2h1, bw=20)
    net.addLink(es444, pod2h2, bw=20)
    net.addLink(es444, pod2h3, bw=20)

    net.addLink(es555, pod2h4, bw=20)
    net.addLink(es555, pod2h5, bw=20)
    net.addLink(es555, pod2h6, bw=20)

    net.addLink(es666, pod2h7, bw=20)
    net.addLink(es666, pod2h8, bw=20)
    net.addLink(es666, pod2h9, bw=20)
# ---------------------------------------------3

    net.addLink(es777, pod3h1, bw=20)
    net.addLink(es777, pod3h2, bw=20)
    net.addLink(es777, pod3h3, bw=20)

    net.addLink(es888, pod3h4, bw=20)
    net.addLink(es888, pod3h5, bw=20)
    net.addLink(es888, pod3h6, bw=20)

    net.addLink(es999, pod3h7, bw=20)
    net.addLink(es999, pod3h8, bw=20)
    net.addLink(es999, pod3h9, bw=20)
# ---------------------------------------------4
    net.addLink(es1000, pod4h1, bw=20)
    net.addLink(es1000, pod4h2, bw=20)
    net.addLink(es1000, pod4h3, bw=20)

    net.addLink(es1100, pod4h4, bw=20)
    net.addLink(es1100, pod4h5, bw=20)
    net.addLink(es1100, pod4h6, bw=20)

    net.addLink(es1200, pod4h7, bw=20)
    net.addLink(es1200, pod4h8, bw=20)
    net.addLink(es1200, pod4h9, bw=20)
# ---------------------------------------------5
    net.addLink(es1300, pod5h1, bw=20)
    net.addLink(es1300, pod5h2, bw=20)
    net.addLink(es1300, pod5h3, bw=20)

    net.addLink(es1400, pod5h4, bw=20)
    net.addLink(es1400, pod5h5, bw=20)
    net.addLink(es1400, pod5h6, bw=20)

    net.addLink(es1500, pod5h7, bw=20)
    net.addLink(es1500, pod5h8, bw=20)
    net.addLink(es1500, pod5h9, bw=20)
# ---------------------------------------------6
    net.addLink(es1600, pod6h1, bw=20)
    net.addLink(es1600, pod6h2, bw=20)
    net.addLink(es1600, pod6h3, bw=20)

    net.addLink(es1700, pod6h4, bw=20)
    net.addLink(es1700, pod6h5, bw=20)
    net.addLink(es1700, pod6h6, bw=20)

    net.addLink(es1800, pod6h7, bw=20)
    net.addLink(es1800, pod6h8, bw=20)
    net.addLink(es1800, pod6h9, bw=20)
# ------------------------------------------------

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    # CORE
    net.get('cs1').start([c0])
    net.get('cs2').start([c0])
    net.get('cs3').start([c0])
    net.get('cs4').start([c0])
    net.get('cs5').start([c0])
    net.get('cs6').start([c0])
    net.get('cs7').start([c0])
    net.get('cs8').start([c0])
    net.get('cs9').start([c0])

    # AGGREGATION
    net.get('as11').start([c0])
    net.get('as22').start([c0])
    net.get('as33').start([c0])
    net.get('as44').start([c0])
    net.get('as55').start([c0])
    net.get('as66').start([c0])
    net.get('as77').start([c0])
    net.get('as88').start([c0])
    net.get('as99').start([c0])
    net.get('as100').start([c0])
    net.get('as110').start([c0])
    net.get('as120').start([c0])
    net.get('as130').start([c0])
    net.get('as140').start([c0])
    net.get('as150').start([c0])
    net.get('as160').start([c0])
    net.get('as170').start([c0])
    net.get('as180').start([c0])

    # EDGE
    net.get('es111').start([c0])
    net.get('es222').start([c0])
    net.get('es333').start([c0])
    net.get('es444').start([c0])
    net.get('es555').start([c0])
    net.get('es666').start([c0])
    net.get('es777').start([c0])
    net.get('es888').start([c0])
    net.get('es999').start([c0])
    net.get('es1000').start([c0])
    net.get('es1100').start([c0])
    net.get('es1200').start([c0])
    net.get('es1300').start([c0])
    net.get('es1400').start([c0])
    net.get('es1500').start([c0])
    net.get('es1600').start([c0])
    net.get('es1700').start([c0])
    net.get('es1800').start([c0])

    info('*** Post configure switches and hosts\n')
    run(host='172.20.5.41', port=8090)
    CLI(net)
    net.stop()

# ------------------------API---------------------------------


@route('/dissertation/api/transmission')
def executeTransmission():
    transmissionFromIp = request.query.fromIp
    transmissionToIp = request.query.toIp
    # transmissionPort_src = request.query.port_src
    transmissionPort_dst = request.query.port_dst
    transmissionRate = request.query.rate
    transmissionTime = request.query.time
    transmissionType = request.query.type
    hostClient = None
    hostServer = None
    for host in net.hosts:
        if host.IP() == transmissionFromIp:
            hostClient = host
        elif host.IP() == transmissionToIp:
            hostServer = host
    if transmissionType == 'UDP':
        # iperf Client
        hostClient.popen('iperf -c ' + transmissionToIp + ' -p' + transmissionPort_dst +
                         ' -u -t ' + transmissionTime + ' -i 1 -b ' + transmissionRate + 'm')
        # iperf Server
        # hostServer.popen('echo "-----------------TEST---------------------" >> iperf_server_' + transmissionToIp)
        hostServer.popen('iperf -s -u -i 1 -p ' + transmissionPort_dst +
                         ' >> iperf_server_' + transmissionToIp + '_' + transmissionPort_dst, shell=True)

    info(transmissionType)
    return "ok"


@route('/dissertation/api/host/add/<hostName>/<deviceId>')
def addHostOnDevice(hostName, deviceId):
    info('*** Dynamically add a container at runtime\n')
    for switch in net.switches:
        if switch.dpid == deviceId[3:]:
            ip = net.getNextIp()
            host = net.addHost(hostName)
            net.addLink(host, switch, params1={"ip": ip})
            net.pingAll()
            return "Host added to switch: " + switch.dpid + " with ip: " + ip


@route('/dissertation/api/xterm/<ipAddress>')
def makeXTerm(ipAddress):
    for host in net.hosts:
        if host.IP() == ipAddress:
            makeTerm(host)


@route('/dissertation/api/pingall')
def pingall():
    net.pingAll()


@route('/dissertation/api/switch/add/<name>')
def addSwitch(name):
    switch = net.addSwitch(name)
    switch.start([net.get('c0')])
    return "Switch added! " + switch.dpid


@route('/cli/link/add/<switchId1>/<switchId2>')
def switchAddLink(switchId1, switchId2):
    switch1 = ''
    switch2 = ''
    for switch in net.switches:
        if switch.dpid == switchId1[3:]:
            switch1 = switch
        elif switch.dpid == switchId2[3:]:
            switch2 = switch
    if not switch1 or not switch2:
        info("Not devices where found")
    net.addLink(switch1, switch2)
    return "Link added!"


@route('/dissertation/api/link/rm/<deviceId1>/<deviceId2>')
def removeLink(deviceId1, deviceId2):
    device1 = ''
    device2 = ''
    for switch in net.switches:
        if switch.dpid == deviceId1[3:]:
            device1 = switch
        elif switch.dpid == deviceId2[3:]:
            device2 = switch
    if not device1 and device2:
        for host in net.hosts:
            if host.MAC() == deviceId1[:17].lower():
                device1 = host
    else:
        for host in net.hosts:
            info(host.MAC().lower() + "==" + deviceId2[:17] + "\n")
            if host.MAC() == deviceId2[:17].lower():
                device2 = host
    info("device1: " + str(device1) + " device2: " + str(device2) + "\n")
    net.removeLink(node1=device1, node2=device2)
    return "Link removed!"


@route('/dissertation/api/host/exec/<hostIpAddress>/<command>')
def cli(hostIpAddress, command='ls'):
    for host in net.hosts:
        if host.IP() == hostIpAddress:
            return net.get(host).cmd(command)


@route('/dissertation/api/host/mac/<hostIpAddress>')
def getMacFromIpAddress(hostIpAddress):
    for host in net.hosts:
        if host.IP() == hostIpAddress:
            return host.MAC()


@route('/dissertation/api/host/info/<host>')
def hostInfo(host='host1'):
    hostname = net.get(host).name
    hostMac = net.get(host).MAC()
    hostIp = net.get(host).IP()
    hostDict = {'hostname': hostname, 'hostmac': hostMac, 'hostip': hostIp}
    return json.dumps(hostDict, ensure_ascii=False)


if __name__ == '__main__':
    setLogLevel('info')
    myFatTree()

