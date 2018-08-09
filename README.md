# Luban-Py

[Luban](https://github.com/Curzibn/Luban/) is an image compressing tool for android with efficacy very close to that of `WeChat` Moments. This project [Luban-Py](https://github.com/Freefighter/Luban-Py) ports its algorithm to Python and offers an executable program for Windows.

# Description for [Luban](https://github.com/Curzibn/Luban/)

With the ever increasing resolution of smartphone cameras, image compression has become a rather important concern.

Although there are already a lot of writings on the internet on the topic, a great number of possible scenarios still have to be though of, like unsuccessful compressions, too small pictures (eg. for profile pictures) or too bad image quality.

Naturally, the first idea was to see how the `WeChat`, the app giant manages this task in action. To gather data, 100 images with different resolutions were sent through `WeChat` Moments, then the compressed images were compared with the original ones. `Luban`'s foundation is the result of this analysis on `WeChat`'s compression method.

Because the process was analyzed backwards, `Luban`'s efficacy is not yet exactly the same as that of `WeChat`, but the results are already very close to what `WeChat` Moments' image compression produces.

Translation by: [_Szabolcs Pasztor_](https://github.com/spqpad)

# Usage

### Methods

Methods | Description
---- | ----
load | load the image
setTargetDir | set the path where compressed images are saved
compress | compress the image if its size is greater than the threshold (set by self.ignoreBy)

### How to Use

- Drop one or more images to "Drop your images here.bat"

In this way, you can rewrite "luban.py" to meet your requirement. However the images have to be in the same folder with the .bat file.

- Drop one or more images to "compress.exe"

In this way, the images can be from anywhere.

> The compressed images will appear in the folder "target" under the same path with the original images.

# License

    Copyright 2018 Yifan Chen
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

