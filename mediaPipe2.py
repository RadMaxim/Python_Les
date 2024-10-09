import mipe as mp
import cv2
cap = cv2.VideoCapture(0)


mpDraw = mp.solutions.drawing_utils
drawStyles = mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style()
drawSpec = mp.solutions.drawing_utils.DrawingSpec(thickness=1, circle_radius=0)

