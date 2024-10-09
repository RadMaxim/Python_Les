import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
mpDraw = mp.solutions.drawing_utils
drawStyles = mp.solutions.drawing_styles
drawSpec = mp.solutions.drawing_utils.DrawingSpec(thickness=1, circle_radius=1)
mpHandsMash = mp.solutions.hands
handsMash = mpHandsMash.Hands()
mpHeader = mp.solutions.face_mesh
faceMash = mpHeader.FaceMesh()
face1 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
while True:
   frame = cap.read()[1]
   face2 = face1.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),1.3,5)
   for (x,y,w,h) in face2:
       cv2.rectangle(frame,(x,y),(x+w//2,y+h//2),(0,0,0),1)
       cv2.rectangle(frame,(x+w//2,y),(x+w,y+h//2),(0,0,0),-1)
       # cv2.rectangle(frame,(x,y),(x+w//2,y+h//2),(0,0,0),1)
       # cv2.rectangle(frame,(x,y),(x+w//2,y+h//2),(0,0,0),1)
   rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   results = handsMash.process(rgb)
   results_face = faceMash.process(rgb)
   (y1,x1,d) = frame.shape
   points_faces = {}
   if results_face.multi_face_landmarks:
       for face in results_face.multi_face_landmarks:
           mpDraw.draw_landmarks(frame,face,mpHeader.FACEMESH_TESSELATION,drawStyles.get_default_face_mesh_tesselation_style(),drawStyles.get_default_face_mesh_tesselation_style())
           for id, f in enumerate(face.landmark,0):
               points_faces[id]=(int(f.x*x1),int(f.y*y1))
               if id%4 == 0:
                   cv2.putText(frame,str(id),(points_faces[id][0],points_faces[id][1]),1,1.1,(0,0,0),1)
   print(points_faces)

   hands_mark = {}
   if results.multi_hand_landmarks:
       for hands in results.multi_hand_landmarks:
           mpDraw.draw_landmarks(frame, hands, mpHandsMash.HAND_CONNECTIONS,
                                 drawStyles.get_default_hand_landmarks_style(),
                                 drawStyles.get_default_hand_connections_style())
           hands_mark = {}
           for id, elem in enumerate(hands.landmark,0):
               x = int(elem.x*x1)
               y = int(elem.y*y1)
               hands_mark[id]=(x,y)
               cv2.putText(frame,str(id),(int(x),int(y)),1,1.2,(0,0,0),2)
               print(id, elem)
           print(hands_mark)
           # print(hands_mark[4][0])
           cv2.line(frame,(hands_mark[4][0],hands_mark[4][1]),(hands_mark[8][0],hands_mark[8][1]),(0,0,100),2)
           # for lm in hands.landmark:
           #     print(lm)
   if  results.multi_hand_landmarks and results_face.multi_face_landmarks:
        cv2.line(frame,(hands_mark[4][0],hands_mark[4][1]),(points_faces[16][0],points_faces[16][1]),(0,0,0),4)
   cv2.imshow("frame", frame)
   if cv2.waitKey(1) == 27:
       break
cap.release()
cv2.destroyAllWindows()
