# hackthon-rearend
[![Build Status](https://travis-ci.com/snnucs/hackthon-rearend.svg?branch=master)](https://travis-ci.com/snnucs/hackthon-rearend)
[![LICENSE](https://img.shields.io/github/license/snnucs/hackthon-rearend.svg)](https://github.com/snnucs/hackthon-rearend/blob/master/LICENSE)
![image](https://img.shields.io/pypi/pyversions/snnusdk.svg)

2019.04.20 - 2019.04.21 西安电子科技大学-微软俱乐部-hackathon。 PPT 队，后端部分，微信小程序

## 项目结构
```                  
│  manage.py
│ 
│  
├─activity
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  Serializer.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│      0001_initial.py
│      0002_auto_20190420_2108.py
│      0003_activity_number.py
│      0004_auto_20190421_0056.py
│      __init__.py
│              
├─hackthon
│    settings.py
│    urls.py
│    wsgi.py
│    __init__.py
│         
└─user
    │  admin.py
    │  apps.py
    │  models.py
    │  Serializer.py
    │  tests.py
    │  urls.py
    │  views.py
    │  __init__.py
    │  
    ├─migrations
         0001_initial.py
         0002_auto_20190421_0225.py
         0003_auto_20190421_0228.py
         __init__.py
```
## 开发流程
* python环境:`python3.5+`
* mySQL:`3.5以上`
* Django:`2.0以上`

```bash
pip3 install -r dev-requirment.txt
python manage.py migrate
✨🍰✨
```
## 测试
```bash
pytest --pep8
pytest
```
## 启动服务
`python manage.py runserver`

# 致谢
感谢西安电子科技大学微软俱乐部提供优异的条件和愉快的体验。
