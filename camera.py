""" a security camera project done in python """

# importing the necessary modules for the project 

import cv2          # opencv to interact with video camera 
import time         # time module to get the current time 
import datetime     # datetime module to get the current date 

cap = cv2.VideoCapture(0)          # initializing the opencv module to capture the video from the camera 


# implementing the haarcasscade for the detection of body and face
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False                  # assigning the initial value of the detection mode 
detection_stopped_time = None      # assigning the initial value of timer after the detection is stopped
timer_started = False              # assigning the initial value of the timer after detection
SECONDS_TO_RECORD_AFTER_DETECTION = 5  # the time threshold to wait to again start recording after detetcting some movement 

frame_size = (int(cap.get(3)), int(cap.get(4))) # gathering the video capture size of the devive connected
file = cv2.VideoWriter_fourcc(*"mp4v")        # assighning the required type of file format for the video to be saved

while True:                        # opening an infinite loop to capture the video camera continously 
    _, frame = cap.read()          # getting all the frames captured by the camera

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # converting the frames from bgr to grayscale for the ease of detection 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # parsing  the gray frames to the face detector to detect the face 
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5) # parsing the grat frames to the body detector to detect the body 

    if len(faces) + len(bodies) > 0: # a condiiton statement to check whether a face or body is detcted in the frame 
        if detection:                # checks if the system is currently in detection mode or not 
            timer_started = False    # if yes sets the detetion to stop
        else:                        # if not in detection mode 
            detection = True         # sets the detection mode to true
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") # gets the current time and date
            out = cv2.VideoWriter(f"{current_time}.mp4", file, 20, frame_size)   # gives the output of the recorded video with name of current time and date
            print("Started Recording!") # prints the current state of the system 
    elif detection:                  # checks if no faces or body is detected but is in detection mode
        if timer_started:            # it checks whether the threshold has been met since the last detection 
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION: # if threshold is met then it deactivates all the detection mode
                detection = False    # sets detection to false
                timer_started = False # stops the timer
                out.release()        # stope the video recording 
                print('Stop Recording!') # prints stop recording 
        else:                        # if the system has detected a movement before the timer has started
            timer_started = True     # starts the timer
            detection_stopped_time = time.time()  # records the time when the last movement was made 

    if detection:                    # checks if the system is in detection mode if true
        out.write(frame)             # write the frames being recorded to the save file

    for (x, y, width, height) in faces:  # loop statement to go throgh all the locations in the face
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3) # draw a rectangle upon the frame detecting the face 

    cv2.imshow("Made By Parthiv", frame) # show the captured frames by the camera 

    if cv2.waitKey(1) == ord('q'):       # setting a key to eliminate the process with a wait period of 1 second 
        break                            # breaks the infinite loop thereby cutting the video capture

out.release()                            # stops the writing of frames into the save file  
cap.release()                            # releases the camera 
cv2.destroyAllWindows()                  # closes all the cv2 operational windows 