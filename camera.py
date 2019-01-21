import numpy as np
from imutils.video import VideoStream
from imutils import resize

theCam = VideoStream().start()


# 4 seconds at 30 fps
beforeFrames = 120

# resize the input image to be smaller for inference
frame = theCam.read()
frame = resize(frame, width=512)

# fill the buffer with the resized image shape, and the number of frames
theBuffer = np.zeros((frame.shape[0], frame.shape[1], frame.shape[2], beforeFrames), dtype='uint8')

# prefill buffer with frames
def prefillBuffer():
    for i in range(beforeFrames):
        frame = theCam.read()
        frame = resize(frame, width=512)
        theBuffer[:,:,:,i] = frame
        
prefillBuffer()

# in a loop, roll the last element to be the first element
# and then replace the first element with the latest frame

while True:
    # this is the numpy implementation of our circular buffer
    theBuffer = np.roll(theBuffer, -1, axis=3)
    frame = theCam.read()
    frame = resize(frame, width=512)

    theBuffer[:,:,:,-1] = frame
    # your inference code goes here...