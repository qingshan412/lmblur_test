from PIL import Image
from LinearMotionBlur import *

imgL = Image.open('../BluredImages/orig.png').convert('L')
blurred = LinearMotionBlur(imgL, 11, 179, 'full')