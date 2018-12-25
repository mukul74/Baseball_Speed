# Baseball_Speed
Using the computer vision techniques for calculating the speed of baseball
* First Background Substraction Algorithm.
* Contour Algorithm to find the ball in the images.
* Trial and Error method to get the contour of the ball and drawing the bounding box around the ball.
* Bounding box gives the width,height,centroid value of box.
* Camera parameters are given.
* So Bounding box gives the pixel coordinates which can be converted form ( 2D - 3D(World Coordinates))
* Using the euclidiam distance and Distance = Velocity*Time formula for calculating the speed per frame 
* Taking mean of all the grabbed speed lead to average speed
* No ground truth so this just a shot in the dark.  
