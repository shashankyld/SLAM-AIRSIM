# Python client example to get Lidar data from a drone
#

import setup_path 
import airsim

import sys
import math
import time
import argparse
import pprint
import numpy
import pandas as pd
import xlsxwriter
import xlwt
import random

# Makes the drone fly and get Lidar data
class LidarTest:

    def __init__(self):

        # connect to the AirSim simulator
        
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)

    def execute(self):

        print("arming the drone...")
        self.client.armDisarm(True)

        # state = self.client.getMultirotorState()
        # s = pprint.pformat(state)
        # print("state: %s" % s)

        airsim.wait_key('Press any key to takeoff')
        self.client.takeoffAsync()

        # state = self.client.getMultirotorState()
        # print("state: %s" % pprint.pformat(state))

        airsim.wait_key('Press any key to move vehicle to (0,0,-7) at 5 m/s')
        self.client.moveToPositionAsync(0, 0, -40, 5).join()
        self.client.hoverAsync().join()

        airsim.wait_key('Press any key to get Lidar scans')


        names = {}
        totallidarcollections = 1000
        for i in range(totallidarcollections):
            names[str(i)]= "lidar" + str(i+1)
            #print(names[str(i)])

        writer = pd.ExcelWriter('corridor_rough.xlsx', engine = 'xlsxwriter')
        
        for i in range(10):

            lidarData = self.client.getLidarData()
            #print(lidarData)
            #print(len(lidarData))
            points = self.parse_lidarData(lidarData)
            print('lidar', str(i+1), ' points: ', points)
            state = self.client.getMultirotorState()
            print("state: %s" % pprint.pformat(state))
            print('total lidar points in lidar range ' + str(len(points)))
            x = points[:,0]
            y = points[:,1]
            z = points[:,2]

            # indexes = [0]*270

            # for i in range(270):
            #     indexes[i] = rangerandom.randint(0, len(x))


            df = pd.DataFrame([x,y])
            
            df.to_excel(writer, sheet_name = names[str(i)])
            #writer.save()
            #writer.close()
            self.client.moveToPositionAsync(0,177*(i+1)/10, -40, 5).join()
            #self.client.hoverAsync().join()
            if i > 8:
                time.sleep(0)
            else:
                time.sleep(6)
            # print(len(points))
            # print("\tReading %d: time_stamp: %d number_of_points: %d" % (i, lidarData.time_stamp, len(points)))
            # print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
            # print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))
        
        for i in range(20):

            lidarData = self.client.getLidarData()
            #print(lidarData)
            #print(len(lidarData))
            points = self.parse_lidarData(lidarData)
            print('lidar', str(i+1), ' points: ', points)
            state = self.client.getMultirotorState()
            print("state: %s" % pprint.pformat(state))
            print('total lidar points in lidar range ' + str(len(points)))
            x = points[:,0]
            y = points[:,1]
            z = points[:,2]


            df = pd.DataFrame([x,y])
            
            df.to_excel(writer, sheet_name = names[str(i+10)])
            #writer.save()
            #writer.close()
            self.client.moveToPositionAsync(-300*(i+1)/20,177, -40, 5).join()
            #self.client.hoverAsync().join()
            if i > 18:
                time.sleep(0)
            else:
                time.sleep(6)
            # print(len(points))
            # print("\tReading %d: time_stamp: %d number_of_points: %d" % (i, lidarData.time_stamp, len(points)))
            # print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
            # print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))


        for i in range(10):

            lidarData = self.client.getLidarData()
            #print(lidarData)
            #print(len(lidarData))
            points = self.parse_lidarData(lidarData)
            print('lidar', str(i+1), ' points: ', points)
            state = self.client.getMultirotorState()
            print("state: %s" % pprint.pformat(state))
            print('total lidar points in lidar range ' + str(len(points)))
            x = points[:,0]
            y = points[:,1]
            z = points[:,2]


            df = pd.DataFrame([x,y])
            
            df.to_excel(writer, sheet_name = names[str(i+30)])
            #writer.save()
            #writer.close()
            self.client.moveToPositionAsync(-300,177-177*(i+1)/10, -40,5).join()
            #self.client.hoverAsync().join()
            if i > 8:
                time.sleep(0)
            else:
                time.sleep(5)
            # print(len(points))
            # print("\tReading %d: time_stamp: %d number_of_points: %d" % (i, lidarData.time_stamp, len(points)))
            # print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
            # print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))

        for i in range(20):

            lidarData = self.client.getLidarData()
            #print(lidarData)
            #print(len(lidarData))
            points = self.parse_lidarData(lidarData)
            print('lidar', str(i+1), ' points: ', points)
            state = self.client.getMultirotorState()
            print("state: %s" % pprint.pformat(state))
            print('total lidar points in lidar range ' + str(len(points)))
            x = points[:,0]
            y = points[:,1]
            z = points[:,2]




            df = pd.DataFrame([x,y])
            
            df.to_excel(writer, sheet_name = names[str(i+40)])
            #writer.save()
            #writer.close()
            self.client.moveToPositionAsync(-300+300*(i+1)/20,0, -40, 5).join()
            #self.client.hoverAsync().join()
            if i > 18:
                time.sleep(0)
            else:
                time.sleep(5)
            # print(len(points))
            # print("\tReading %d: time_stamp: %d number_of_points: %d" % (i, lidarData.time_stamp, len(points)))
            # print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
            # print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))

        for i in range(10):

            lidarData = self.client.getLidarData()
            #print(lidarData)
            #print(len(lidarData))
            points = self.parse_lidarData(lidarData)
            print('lidar', str(i+1), ' points: ', points)
            state = self.client.getMultirotorState()
            print("state: %s" % pprint.pformat(state))
            print('total lidar points in lidar range ' + str(len(points)))
            x = points[:,0]
            y = points[:,1]
            z = points[:,2]

            # indexes = [0]*270

            # for i in range(270):
            #     indexes[i] = rangerandom.randint(0, len(x))


            df = pd.DataFrame([x,y])
            
            df.to_excel(writer, sheet_name = names[str(i+60)])
            #writer.save()
            #writer.close()
            self.client.moveToPositionAsync(0,177*(i+1)/10, -40, 5).join()
            #self.client.hoverAsync().join()
            if i > 8:
                time.sleep(0)
            else:
                time.sleep(5)
            # print(len(points))
            # print("\tReading %d: time_stamp: %d number_of_points: %d" % (i, lidarData.time_stamp, len(points)))
            # print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
            # print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))

        writer.save()
        #writer.close()

    def parse_lidarData(self, data):

        # reshape array of floats to array of [X,Y,Z]
        points = numpy.array(data.point_cloud, dtype=numpy.dtype('f4'))
        points = numpy.reshape(points, (int(points.shape[0]/3), 3))
       
        return points

    def write_lidarData_to_disk(self, points):
        # TODO
        print("not yet implemented")

    def stop(self):

        airsim.wait_key('Press any key to reset to original state')

        self.client.armDisarm(False)
        self.client.reset()

        self.client.enableApiControl(False)
        print("Done!\n")

# main
if __name__ == "__main__":
    args = sys.argv
    args.pop(0)

    arg_parser = argparse.ArgumentParser("Lidar.py makes drone fly and gets Lidar data")

    arg_parser.add_argument('-save-to-disk', type=bool, help="save Lidar data to disk", default=False)
  
    args = arg_parser.parse_args(args)  
    
    


    lidarTest = LidarTest()
    # print(client.time_stamp)
    # print('Press after 5 sec and check time stamp')
    # print(time_stamp)
    try:
        lidarTest.execute()
    finally:
        lidarTest.stop()