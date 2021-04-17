def main():
    import cv2
    import os

    print("In Process")

    def convert_to_frame(path):
        parent_dir_path = os.path.dirname(path)
        video_name = os.path.basename(os.path.normpath(path))
        frame_dir = os.path.join(parent_dir_path, "frames-"+video_name+"/")
        os.mkdir(frame_dir)

        video = cv2.VideoCapture(path)
        i = 0
        while(video.isOpened()):
            ret, frame = video.read()
            if ret == False:
                break
            cv2.imwrite(frame_dir+"frame"+str(i)+".jpg", frame)
            i += 1

        video.release()
        cv2.destroyAllWindows()

    path = "/media/qasim/STUDY/1uniBooksAndAssignments/FYP/week2(15-21 APR) L/practical_tasks/videos/ball.mp4"
    convert_to_frame(path)


if __name__ == "__main__":
    main()
    print("Done making frames")
