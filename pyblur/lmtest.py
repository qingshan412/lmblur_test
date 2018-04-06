from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
    )
from LinearMotionBlur import *

imgL = Image.open('../../BluredImages/orig.png').convert('L')
blurred = LinearMotionBlur(imgL, 11, 179, 'full')
# >>> b = LinearMotionBlur(imgL, 51, 179, 'full')
# e = EdgeEnhance(b, 3, 9)
# >>> b.show()
# >>> ee = b.filter(EDGE_ENHANCE)
# >>> ee.show()
# >>> ee2 = ee.filter(EDGE_ENHANCE)
# >>> ee2.show()
# >>> ee3 = ee2.filter(EDGE_ENHANCE)
# >>> ee3.show()
# >>> b.show()
# >>> ee.show()
# >>> ee2.show()
# >>> ee3.show()

