from PIL import Image
import os
from shutil import copyfile
from math import ceil

class Luban(object):
    
    def __init__(self, ignoreBy=102400, quality=60):
        self.ignoreBy = ignoreBy
        self.quality = quality
    
    def setPath(self, path):
        self.path = path
    
    def setTargetDir(self, foldername="target"):
        self.dir, self.filename = os.path.split(self.path)
        self.targetDir = os.path.join(self.dir, foldername)
        
        if not os.path.exists(self.targetDir): 
            os.makedirs(self.targetDir)
            
        self.targetPath = os.path.join(self.targetDir, "c_"+self.filename)
            
    def load(self):
        self.img = Image.open(self.path)
        
        if self.img.mode == "RGB": 
            self.type = "JPEG"
        elif self.img.mode == "RGBA": 
            self.type = "PNG"
        else: # 其他的图片就转成JPEG
            self.img = self.img.convert("RGB")
            self.type = "JPEG"
    
    def computeScale(self):
        # 计算缩小的倍数
    
        srcWidth, srcHeight = self.img.size
        
        
        srcWidth = srcWidth + 1 if srcWidth % 2 == 1 else srcWidth
        srcHeight = srcHeight + 1 if srcHeight % 2 == 1 else srcHeight
        
        longSide = max(srcWidth, srcHeight)
        shortSide = min(srcWidth, srcHeight)

        scale = shortSide / longSide
        if (scale <= 1 and scale > 0.5625):
            if (longSide < 1664): 
                return 1
            elif (longSide < 4990):
                return 2
            elif (longSide > 4990 and longSide < 10240):
                return 4
            else:
                return max(1, longSide // 1280)
            
        elif (scale <= 0.5625 and scale > 0.5):
            return max(1, longSide // 1280)
            
        else: 
            return ceil(longSide / (1280.0 / scale))
    
    def compress(self):
        self.setTargetDir()
        # 先调整大小，再调整品质
        if os.path.getsize(self.path) <= self.ignoreBy:
            copyfile(self.path, self.targetPath)
            
        else:
            self.load()
            
            scale = self.computeScale()
            srcWidth, srcHeight = self.img.size
            cache = self.img.resize((srcWidth//scale, srcHeight//scale), 
                                        Image.ANTIALIAS)
            
            cache.save(self.targetPath, self.type, quality=self.quality)
            
if __name__ == '__main__':
    path = r"C:\Users\William\Documents\GitHub\Luban-Py\example_lena.png"
    
    compressor = Luban()
    compressor.setPath(path)
    compressor.compress()