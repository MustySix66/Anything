import cv2
from ascii_magic import AsciiArt
from PIL import Image

cap = cv2.VideoCapture('prueba.mp4') # Here goes the .mp4 archive
frame_count=0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count %4 == 0:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
        pil_image = Image.fromarray(frame_rgb)
        frame = AsciiArt.from_pillow_image(pil_image)
        frame.to_terminal()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows