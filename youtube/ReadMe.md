pyqt5目前测试 python 3.7.2 可用其他版本不清楚
pipenv 包管理工具 
pip install pipenv
pipenv install 安装所有依赖
pipenv install 'pakeage' --dev


pip镜像设置，添加文件
c:/user/**/pip/pip.ini
内容
 [global]
 index-url = 
阿里云：http://mirrors.aliyun.com/pypi/simple/
豆瓣：http://pypi.douban.com/simple/
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple/
  