import mediapipe as mp
import cv2
import pyautogui
mp_drwaing= mp.solutions.drawing_utils #drwaing utils

def count_fingers(list):
    cnt=0

    thresh=(list.landmark[0].y*100-list.landmark[9].y*100)/2
    if (list.landmark[5].y*100- list.landmark[8].y*100)>thresh:
        print()
        cnt+=1
    if (list.landmark[9].y*100- list.landmark[12].y*100)>thresh:
        cnt+=1
    if (list.landmark[13].y*100- list.landmark[16].y*100)>thresh:
        cnt+=1
    if (list.landmark[17].y*100- list.landmark[20].y*100)>thresh:
        cnt+=1
    if (list.landmark[5].x*100- list.landmark[4].x*100)>thresh:
        cnt+=1
    return cnt


x1=y1=x2=y2=0
cap=cv2.VideoCapture(0)
drawing=mp.solutions.drawing_utils
handss=mp.solutions.hands

hand_obj=handss.Hands(max_num_hands=1)
prev=-1

with mp_hlistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as Holist:
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)


        res=hand_obj.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        mpholres = Holist.process(frame)
        mp_drwaing.draw_landmarks(frame, mpholres.face_landmarks, mp_hlistic.FACEMESH_TESSELATION,
                                  mp_drwaing.DrawingSpec(color=(255, 165, 0), thickness=1, circle_radius=1),
                                  mp_drwaing.DrawingSpec(color=(255, 165, 0), thickness=1, circle_radius=1))

        mp_drwaing.draw_landmarks(frame, mpholres.right_hand_landmarks, mp_hlistic.HAND_CONNECTIONS,
                                       mp_drwaing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                       mp_drwaing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                       )#medaipipe right hand connection mp_hlosict.hand connection ,mediapipe.solutions.drawing_utils.drawing specs =(color=(80.90.255) -rgb color,thisckness-evalo thickness irrukunum solrathuku,circleradius=1 -landmark handla circle evalo thick irrukunumathuku poduvanga
        mp_drwaing.draw_landmarks(frame, mpholres.left_hand_landmarks, mp_hlistic.HAND_CONNECTIONS,
                                       mp_drwaing.DrawingSpec(color=(121,22,76), thickness=2 ,circle_radius=4),
                                       mp_drwaing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                       )#medaipipe right hand connection mp_hlosict.hand connection ,mediapipe.solutions.drawing_utils.drawing specs=(color=(80.90.255) -rgb color,thisckness-evalo thickness irrukunum solrathuku,circleradius=1 -landmark handla circle evalo thick irrukunumathuku poduvanga
        mp_drwaing.draw_landmarks(frame,mpholres.pose_landmarks,mp_hlistic.POSE_CONNECTIONS,
                                       mp_drwaing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                       mp_drwaing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                     )#medaipipe bodyla connection mp_hlosict.pose connection ,mediapipe.solutions.drawing_utils.drawing specs =(color=(80.90.255) -rgb color,thisckness-evalo thickness irrukunum solrathuku,circleradius=1 -landmark bodyla  circle evalo thick irrukunumathuku poduvanga

        if res.multi_hand_landmarks:
            hand_keypoints=res.multi_hand_landmarks[0]
            landmarks=hand_keypoints.landmark

            cnt= count_fingers(hand_keypoints)


            if (cnt==1):
                mp_drwaing.draw_landmarks(frame,mpholres.face_landmarks,mp_hlistic.FACEMESH_TESSELATION,mp_drwaing.DrawingSpec(color=(255,0,0), thickness=1, circle_radius=1),
                              mp_drwaing.DrawingSpec(color=(255,0,0), thickness=1, circle_radius=1))

                # pyautogui.press("right")
            elif (cnt==2):
                mp_drwaing.draw_landmarks(frame, mpholres.face_landmarks, mp_hlistic.FACEMESH_TESSELATION,
                                          mp_drwaing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                                          mp_drwaing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1))

            elif(cnt==3):
                mp_drwaing.draw_landmarks(frame, mpholres.face_landmarks, mp_hlistic.FACEMESH_TESSELATION,
                                          mp_drwaing.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1),
                                          mp_drwaing.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1))

            elif(cnt==4):
                mp_drwaing.draw_landmarks(frame, mpholres.face_landmarks, mp_hlistic.FACEMESH_TESSELATION,
                                          mp_drwaing.DrawingSpec(color=(238, 130, 168), thickness=1, circle_radius=1),
                                          mp_drwaing.DrawingSpec(color=(238, 130, 168), thickness=1, circle_radius=1))

            elif(cnt==5):
                mp_drwaing.draw_landmarks(frame, mpholres.face_landmarks, mp_hlistic.FACEMESH_TESSELATION,
                                          mp_drwaing.DrawingSpec(color=(255, 255, 0), thickness=1, circle_radius=1),
                                          mp_drwaing.DrawingSpec(color=(255, 255, 0), thickness=1, circle_radius=1))

            drawing.draw_landmarks(frame, res.multi_hand_landmarks[0], handss.HAND_CONNECTIONS)


        cv2.imshow("wimdow", frame)
        cv2.waitKey(1)