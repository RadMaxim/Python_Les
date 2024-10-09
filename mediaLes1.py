import mediapipe as mp
import cv2
cam = cv2.VideoCapture(0)
mpDraw = mp.solutions.drawing_utils # подключение утилиты
drawStyles = mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style()
drawSpec = mp.solutions.drawing_utils.DrawingSpec(thickness=1, circle_radius=1,color=(100,100,100))
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
while True:
    frame = cam.read()[1]
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(rgb)
    if results.multi_face_landmarks:
        for faces in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,faces,mpFaceMesh.FACEMESH_TESSELATION,drawStyles,drawStyles)
            for id,lm in enumerate(faces.landmark):
                # print(f'x:{lm.x},y:{lm.y},z:{lm.z}, index:{id}')
                w,h,d=frame.shape
                x=int(lm.x*w)
                y=int(lm.y*h)

                print(x,y)
    cv2.imshow("rgb",frame)
    cv2.waitKey(1)
