from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
    )
from LinearMotionBlur import *

imgL = Image.open('../../BluredImages/orig.png').convert('L')
blurred = LinearMotionBlur(imgL, 11, 179, 'full')
