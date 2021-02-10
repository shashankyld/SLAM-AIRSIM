# SLAM-AIRSIM
Implementing SLAM (Simultaneous Localization and Mapping) using AirSim and MATLAB 


Basically, to use our work

1. You have to take the "corridor.py" code and take out the essential code snippet that (collects the Lidar_data and stores them in an Excel Workbook with multiple sheets.)
2. Now import the excel data to Matlab Navigation Tool Box and perform Pose Graph otimization.
If you are using offline MATALAB, first install Navigation ToolBox and then run the 2D offline SLAM example.
3. Adjust parameters to make it run for your map build (AIRSIM). Instead you can directly import our "lidarloader.mlx" and play with parameters urself using MATALB Navigation Box.
