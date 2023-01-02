#Import python library OpenCV 
import cv2

#Capture the video
cap = cv2.VideoCapture('oneLicenseNight.MOV')

#Set up the cascade classifier
cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

#Create a list to store the detected license plate numbers
licensePlateList = []

#Loop through the frames of the video
while True:
    #Capture the frame
    ret, frame = cap.read()

    #Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect the license plate in the frame
    licensePlate = cascade.detectMultiScale(gray, 1.1, 5)

    #Loop through the detected license plate
    for (x, y, w, h) in licensePlate:
        #Draw the rectangle around the license plate
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #Extract the license plate number from the frame
        licensePlateNumber = gray[y:y+h, x:x+w]

        #Convert the license plate number to string
        licensePlateNumber = str(licensePlateNumber)

        #Check if the license plate number is already in the list
        if licensePlateNumber not in licensePlateList:
            #Append the license plate number to the list
            licensePlateList.append(licensePlateNumber)

            #Print the license plate number
            print(licensePlateNumber)

    #Display the frame
    cv2.imshow('frame', frame)

    #Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#Release the video capture object
cap.release()

#Close all the windows
cv2.destroyAllWindows()

#Save the license plate numbers to a text file
with open('licensePlateNumbers.txt', 'w') as f:
    for item in licensePlateList:
        f.write("%s " % item) 

#Print the license plate numbers
print(licensePlateList)
