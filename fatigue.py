import cv2
import numpy as np
import matplotlib.pyplot as plt

video_file = "/Users/zhangmingxuan/Documents/CMU/Fall2022/02262/CB1091_G3_083122_Leon.avi"

video=cv2.VideoCapture(video_file)

prev_frame = None
diff = []
res = []
count = 0
while video.isOpened():
        ret,frame=video.read()
        if ret:
            if prev_frame is not None:
                diff.append(np.sum(np.absolute(frame - prev_frame)))
                if len(diff) == 60:
                    res.append(sum(diff))
                    count += 1
                    diff = []
            else:
                prev_frame = frame

        if not ret:
            video.release()


x_axis = np.arange(count)
y_axis = np.array(res)

plt.plot(x_axis, y_axis)
plt.title("C.elegan activeness v.s time")
plt.xlabel("time(second)")
plt.ylabel("activeness")
plt.show()

