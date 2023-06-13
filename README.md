##### UCSD ECE/MAE 148 Spring 2023 Team 13


##### Team Members


##### **[Colin Szeto](mailto:cszeto@ucsd.edu)(MAE), Martin Flores Leon(CSE), Yusuf Morsi(ECE), [Dominic Quinonez](mailto:dmquinon@ucsd.edu)(MAE)![](https://lh3.googleusercontent.com/dl7DzsoTw9a-qfMl1YEQDC-yG9jjCdJ40EwMVY6Xo-X-T-P-oFADIdTgrFmx6jXdN7KAQt_WiWOj_6iKuVfvNjJSrhdr6pRwNpFF5qh4bnlSkXnR2RsO0E7QHu8qNZutgJqET8iEisjnQaiqmQ3ErHE)Final Project Overview: For our final project we decided to have our car drive from one point to another point and at each point take images and stitch them together into a panorama that will be saved and view later. Car Design:For our car design we decided to have a front hood type feature where underneath the hood we have our battery, wiring, and servo motors. On top of our hood we have our jetson nano mounted in the center of the car as it is the most important part. To the front of the car we have our camera mounted high on a gimbal to allow us to take images from different angles without having to move the car every single time. Having the camera in front was optimal for better images and also for optimal line following. In the rear we have mounted our lidar and our GNSS system.[Hardware:](https://docs.google.com/document/d/1mEGQXQIoFtz-QhsUaf_HwSmJxkk1sJeMCkNKta-pZkg/edit#heading=h.tanwpcc66t61)[Video Submissions](https://docs.google.com/document/d/1mEGQXQIoFtz-QhsUaf_HwSmJxkk1sJeMCkNKta-pZkg/edit#heading=h.udk2e3ymmvji)**


##### 


##### ****


##### 


##### Electrical Shcematic: 


##### **![](https://lh6.googleusercontent.com/GvkxAbsc6skmnlfbDdW40ZCeQSEg1BFxRmU2t48-SX1AZIW9KAzAkMnRY_ljog9fP1DsYVFn7flmvkFQ6cDwXQOQ_cQvG2l9GzyBJiUf7329r2aiWR_qk3SzghDzTbY2aqzYD2B3DcorUaxBfe7rUts)This is the schematic that we followed to successfully wire our vehicle and all of its components.**


##### Hardware: 


###### _V1: objective to utilize gears for compact packaging. The green gears would help the gimbal yaw while the red gears allow the gimbal to pitch._ 


##### **![](https://lh4.googleusercontent.com/0RMHIJkqZciwBVob0NYr1gFXtRLC5LZYtlYNb-pSV1WIPIbmlwplc5Qno1TL76ua5iTDh5YtWa39Vd82Hx8oVOJKA0AsH36UsfP597Vu8HTkzDNbNMto-1JliEPiIsgWLdxlQF_NguyWSuF4VUbe1zU)**


###### _V2: simply the assembly by utilizing servo blocks, these servo blocks can be leveraged as structural and mounting components and allow the servo to resist shear moments that may break the shaft_


##### **![](https://lh3.googleusercontent.com/4Nv6weLuFxTgQGlg6jjH9uTrQLoN_ucUuWlshqccugEu4LC_01bDBM2hLvU8K9OSQuZucHufZ-P_rNclfAKTmSDQT7kyX0zyf3Fz67aHEmfa7YAmn_aI591r_zJQUmPIvvZBdq0uxtMBmU5UVjrKJKs)**


###### _V3 gimbal. Objective was to get rid of the large moment arm and reduce the range of travel of the camera. Utilizing a linkage we can keep the camera in a similar position to the pivot point and reducing the length the camera is away from the pivot point (pitch)_


##### **![](https://lh5.googleusercontent.com/5F3UeZD5NsqNctflSAwpwgtXw9jZk7uCTjZ4pH4IdPYFUfdZs0j86Pz4RmHG589IHXgurGrTl8vAmWWSF7kUdlHxFmmX9fkBLOMU4KUpzMDrWJRlwEyuQg2VHZy2b-YASPmWL7KSwB59KFjkQLmX3s0)![](https://lh3.googleusercontent.com/6fjLonfaabsCnh_nHrkPOaa_paSKUXz_4UDRXkhfWeDmGAMsCC_uvtuVCZ386lBV_Fr1k9Zq9u0FzlVXWHLpo81kfa-4tki3VLDDHyV0onqMXFx6ib91OYTuURrhUWGYKgWZEkomDOlGXwFJGJ2I9Ls)**


###### _Servo moving:_


##### **<https://youtube.com/shorts/_F_l6TSckRs?feature=share>**


##### Video Submissions


###### _ROS inner lane:_ 


##### **<https://youtu.be/m73O68-RbmQ>**


###### _ROS laps:_ 


##### **<https://youtu.be/hEesrSbDkLY>**


###### _Human behavior cloning:_ 


##### **<https://youtu.be/lcpqX9XBoYo>**


###### _3 laps gps following_


##### **<https://youtu.be/PLP2RACh3PU>**


##### Final Project


##### ****


###### _Overview:_ 


##### **Initially our project had a different scope. Our original goal was to have the car drive around an object on the ground and using the OAK-D lite render a 3D mesh/mapping of the object. We were able to make significant progress on this first plan with generating point clouds and capturing them into files but it was the 3d rendering that was deemed overscoped with the time we had. So with one week till the deadline we decided to rethink our project and came up with our plan B. Plan B was to have our car drive to a couple of different GPS waypoints, stop and captured multiple images using the gimbal and then stitch them together to form a panorama. The gimbal would swivel a total of 180 degrees and in that span take around 18 images that would then be processed using OpenCV into a final panorama. **


###### _Algorithm Design:_ 


##### **Gimbal Movement & Image processing – Created a python script that handled the movement of the gimbal making it swivel 10 degrees at a time. With each swivel we included for the camera to save an image using openCV’s library. Once the gimbal movement and raw images were taken, we then use another python program called stitcND.py that utilizes the openCV library as well as numpy to correctly stitch the images and remove overlapping objects within the images. Thus our final product being a panorama consisting of 18 images stitched together. **


###### _GNSS Explanation_


##### ****


###### _DEMO:_ 


##### 
