QDesktopWidget的实例通过QApplication类的静态方法desktop()获取

使用desktop的screenCount()方法获取显示器数量

使用desktop的screenGeometry()方法获取显示屏的几何位置和尺寸；使用desktop的availableGeometry()获取可用位置和尺寸（除去任务栏等）

screen_rect.width(),screen_rect.height()分别返回宽和高

self.resize()重新定义大小