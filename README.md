# Video2PPT
get the ppt content as video-capture from video tutorial by python

# Why:
看一些视频教程的时候经常遇到需要对视频中的讲义或者 ppt 进行截图的情况，一张一张截图实在是重复劳动！！！shame!!!

# How:
所以，我利用了 python opencv sklearn-image 等工具包：
> 1. 对视频中帧进行截取
> 2. 利用图像相似度进行图片取舍
具体的实现思路在 notebook 中，考虑到 markdown 中有对应的输出信息，会比较好理解

# Result:
利用这份小代码就可以将视频中的ppt等讲义信息，按顺序，无重复的获取到了，可以以图片形式输出，也可以输出位 pdf 或者 markdown 等文件
