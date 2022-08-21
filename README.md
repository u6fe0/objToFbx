# obj批量转fbx
使用之前需要安装 Python 和 FBX SDK Python 2019.x.

[FBX SDK Python Official Website](http://help.autodesk.com/view/FBX/2019/ENU/?guid=FBX_Developer_Help_scripting_with_python_fbx_installing_python_fbx_html)

在 **resources/obj** 文件夹底下放你需要转换的 **obj** 文件

执行命令
```
python objToFbx.py
```

最终会批量转成 **fbx** 到 **resources/fbx** 文件夹中。


注意：
本例子使用的是python2.7 和  FBX SDK Python 2019.5.