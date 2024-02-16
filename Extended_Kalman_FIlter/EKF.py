import numpy as np
from python_ugv_sim import vehicles,environment
import pygame

#odometry_data = [velocity,omega,ts]
n_state = 3
n_landmarks = 2
Fx = np.block([[np.eye(3),np.zeros((n_state,2*n_landmarks))]]) # Used in both prediction and measurement updates

def normalize_angle(angle):
    while angle > np.pi or angle <-np.pi:
        if angle > np.pi:
            angle -= 2*np.pi
        elif angle < -np.pi:
            angle += 2*np.pi
    return angle

# This will identify if the landmark is the same position or not.
def global_frame(mu, landmarks, global_coordinates, ID):
    landmarksts = np.size(landmarks,axis=1)
    ## THIS WILL DEPEND ON HOW MY LIDAR WORKS, HOW IT READS DATA AND HOW IT TAKES MEASUREMENTS
    ## Assumption - LIDAR will begin from north bearing + 180 to the left, - 180 to the right
    for i in range(0,landmarksts):
        x_coord = landmarks[i,0]*np.sin(landmarks[i,1])
        y_coord = landmarks[i,0]*np.cos(landmarks[i,1])
        global_coord_append = np.array([x_coord+mu[0],y_coord+mu[1]])

        # Checks whether or not the coordinate exists in the current map.
    if any(np.isclose(global_coordinates, global_coord_append[0], atol=0.01)) and any(np.isclose(global_coordinates, global_coord_append[1], atol=0.01)): # atol is tolerance, can probably be substituted for the mean
        pass#PERFORM LOOP CLOSURE OMG OMG OMG OMG OMG OMG
    else:
        global_coordinates = np.append(global_coordinates,np.transpose(global_coord_append))
        ID.append(len(ID))

    return global_coordinates, ID

def prediction_step(mu, sigma, dt, u):
    # Updates the main belief of the system
    cols = sigma.shape[1]
    v = u[0]
    omg = u[1]
    theta = mu[2,2]
    ts = dt
    Gx = np.eye(cols)

    # Our predicted belief
    if omg>0.:
        mu[0,0] = mu[0,0] + -(v/omg)*np.sin(theta)+(v/omg)*np.sin(theta+omg*ts)
        mu[1,1] = mu[1,1] + (v/omg)*np.cos(theta)-(v/omg)*np.cos(theta+omg*ts)
        
        # Jacobian of the motion Gxt
        Gx[0,2] = -(v/omg)*np.cos(theta)+(v/omg)*np.cos(theta+omg*ts)
        Gx[1,2] = -(v/omg)*np.sin(theta)+(v/omg)*np.sin(theta+omg*ts)

    else:
        mu[0,0] = mu[0,0] + v*np.cos(theta)*ts
        mu[1,1] = mu[1,1] + v*np.sin(theta)*ts

        # Jacobian of the motion Gxt
        Gx[0,2] =  -v*np.sin(theta)*ts
        Gx[1,2] = v*np.cos(theta)*ts

    mu[2,2] = normalize_angle(theta+omg*ts)

    motion_noise = 0.01
    R3 = np.eye(3)*motion_noise
    R3[2,2] /= 5
    R = np.zeros((cols,cols))
    R[0:3,0:3] = R3

    Newsigma = Gx@sigma@np.transpose(Gx) + R

    return Newsigma, mu

# landmarks will be a 2 by n array with row 0 representing the distance from the landmark and its relative orientation
# landmarks = [[r1,r2...rn],[phi_1,phi_2...phi_n]]

def correction_step(mu,sigma,landmarks):
    sensor_noise = np.array([[0.01,0],[0,0.01]]) #r is top left, phi is bottom right
    landmarkcountts = np.size(landmarks,axis=1) # number of landmarks recorded in this timestep

    for i in range(0,landmarkcountts):
        pass

#main()
''' ADAPTED FROM https://github.com/jacobhiggins/ekf_slam_demo/blob/main/main.py TO VISUALISE IMPLEMENTATION'''

landmarks = [(4,4),
             (4,8),
             (8,8),
             (12,8),
             (16,8),
             (16,4),
             (12,4),
             (8,4)]

n_landmarks = len(landmarks)

def sim_measurement(x,landmarks):
    robot_fov = 3 # robot field of view radius (m)
    '''
    This function simulates a measurement between robot and landmark
    Inputs:
     - x: robot state (3x1 numpy array)
     - landmarks: list of 2-tuples, each of (lx,ly) actual position of landmark
    Outputs:
     - zs: list of 3-tuples, each (r,phi,lidx) of range (r) and relative bearing (phi) from robot to landmark,
           and lidx is the (known) correspondence landmark index.
    '''
    rx, ry, rtheta = x[0], x[1], x[2]
    zs = [] # List of measurements
    for (lidx,landmark) in enumerate(landmarks): # Iterate over landmarks and indices
        lx,ly = landmark
        dist = np.linalg.norm(np.array([lx-rx,ly-ry])) # distance between robot and landmark
        phi = np.arctan2(ly-ry,lx-rx) - rtheta # angle between robot heading and landmark, relative to robot frame
        phi = np.arctan2(np.sin(phi),np.cos(phi)) # Keep phi bounded, -pi <= phi <= +pi
        if dist<robot_fov: # Only append if observation is within robot field of view
            zs.append((dist,phi,lidx))
    return zs

def show_robot_estimate(mu,sigma,env):
    '''
    Visualize estimated position and uncertainty of the robot
    Inputs:
     - mu: state estimate (robot pose and landmark positions)
     - sigma: state uncertainty (covariance matrix)
     - env: Environment class (from python_ugv_sim)
    '''

    rx,ry = mu[0,0],mu[1,1]
    p_pixel = env.position2pixel((rx,ry)) # Transform robot position to pygame surface pixel coordinates
    eigenvals,angle = sigma2transform(sigma[0:3,0:3]) # Get eigenvalues and rotation angle
    sigma_pixel = env.dist2pixellen(eigenvals[0]), env.dist2pixellen(eigenvals[1]) # Convert eigenvalue units from meters to pixels
    show_uncertainty_ellipse(env,p_pixel,sigma_pixel,angle) # Show the ellipse

def sigma2transform(sigma):
    '''
    Finds the transform for a covariance matrix, to be used for visualizing the uncertainty ellipse
    '''
    [eigenvals,eigenvecs] = np.linalg.eig(sigma) # Finding eigenvalues and eigenvectors of the covariance matrix
    angle = 180.*np.arctan2(eigenvecs[1][0],eigenvecs[0][0])/np.pi # Find the angle of rotation for the first eigenvalue
    return eigenvals, angle

def show_landmark_location(landmarks,env):
    '''
    Visualize actual landmark location
    '''
    for landmark in landmarks:
        lx_pixel, ly_pixel = env.position2pixel(landmark)
        r_pixel = env.dist2pixellen(0.2) # Radius of the circle for the ground truth locations of the landmarks
        pygame.gfxdraw.filled_circle(env.get_pygame_surface(),lx_pixel,ly_pixel,r_pixel,(0,255,255)) # Blit the circle onto the surface

def show_measurements(x,zs,env):
    '''
    Visualize measurements the occur between the robot and landmarks
    '''
    rx,ry = x[0], x[1]
    rx_pix, ry_pix = env.position2pixel((rx,ry)) # Convert robot position units from meters to pixels
    for z in zs: # For each measurement
        dist,theta,lidx = z # Unpack measurement tuple
        lx,ly = x[0]+dist*np.cos(theta+x[2]),x[1]+dist*np.sin(theta+x[2]) # Set the observed landmark location (lx,ly)
        lx_pix,ly_pix = env.position2pixel((lx,ly)) # Convert observed landmark location units from meters to pixels
        pygame.gfxdraw.line(env.get_pygame_surface(),rx_pix,ry_pix,lx_pix,ly_pix,(155,155,155)) # Draw a line between robot and observed landmark

def show_uncertainty_ellipse(env,center,width,angle):
    '''
    Visualize an uncertainty ellipse
    Adapted from: https://stackoverflow.com/questions/65767785/how-to-draw-a-rotated-ellipse-using-pygame
    '''
    target_rect = pygame.Rect(center[0]-int(width[0]/2),center[1]-int(width[1]/2),width[0],width[1])
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, env.red, (0, 0, *target_rect.size), 2)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    env.get_pygame_surface().blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def main():
    # Initialize pygame
    pygame.init()

    # Initialize robot and time step
    x_init = np.array([1,1,np.pi/2])
    robot = vehicles.DifferentialDrive(x_init)
    dt = 0.01
    Sigma = np.eye(4)
    u = np.array([0.,0.]) # Controls
    update = 0

    # Initialize and display environment
    env = environment.Environment(map_image_path="./Extended_Kalman_FIlter/python_ugv_sim/maps/map_blank.png")
    mu = np.eye(np.size(Sigma,0),3)
    mu[0,0] = x_init[0]
    mu[1,1] = x_init[1]
    mu[2,2] = x_init[2]
    running = True

    while running:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
            if event.type==pygame.KEYUP or event.type==pygame.KEYDOWN:
                u = robot.update_u(u,event) # Update controls based on key states 

                
        robot.move_step(u,dt) # Integrate EOMs forward, i.e., move robot
        # Get measurements
        zs = sim_measurement(robot.get_pose(),landmarks) # Simulate measurements between robot and landmarks
        # EKF Slam Logic
        Sigma, mu = prediction_step(mu, Sigma, dt, u)
        env.show_map() # Re-bulit map
        # Show measurements
        show_measurements(robot.get_pose(),zs,env)

        env.show_robot(robot) # Re-bulit robot
        show_landmark_location(landmarks,env)

        print(Sigma)
        show_robot_estimate(mu,Sigma,env)
        pygame.display.update() # Update display

'''
a=np.array([[1,2,4],[3,4,8]])
c=np.array([[1,2,5],[3,4,8]])
b=np.array([[1,2],[3,4],[7,8]])
print(np.transpose(a))
'''
main()