import cv2 as cv

# img = cv.imread('../photos/cat.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)


# Reading Videos
capture = cv.VideoCapture('../videos/dog.mp4')

while True:
    # capturing frame
    isTrue, frame = capture.read()

    # getting resized frame
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # waiting until 20 or key "d" pressed in keyboard to break
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# release the pointer
capture.release()
# destroy the opened windows
cv.destroyAllWindows()