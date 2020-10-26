import paho.mqtt.client as mqtt #import the client1
import time
import sys
import threading
import unittest
import Pub_Sub_client as pubsub
        
class TestClient(unittest.TestCase):

    def setUp(self):
        pubsub.message="check_name;1;F;check_procedure"
        pass

    def test_subscriber(self):
        t1=threading.Thread(target=pubsub.subscriber)
        t1.start()
        t1.join()
        #open and read the log file:
        time.sleep(2)
        f = open("subscribe_log.txt", "r")
        assert f.read()=="Subscription successful"
        f.close()

    def test_publisher(self):
        t2=threading.Thread(target=pubsub.publisher)
        t2.start()
        t2.join()
        f = open("publish_log.txt", "r")
        assert f.read()=="Publishing successful"
        f.close()

if __name__=='__main__':
    unittest.main()

