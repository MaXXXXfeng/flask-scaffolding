# flask-scaffolding
一个简单的flask脚手架

## 用法

```
git clone xxxxx
cd flask-scaffolding
```

执行下面命令：

```python
python main.py create --help

Usage: main.py create [OPTIONS] PROJECT_NAME

  create a flask scaffolding

Options:
  -p, --path TEXT         path of the project you want to create
  --help                  Show this message and exit.
```

示例：

```python
python main.py create -p ~/project/ sample_project
```

执行命令后会在~/project目录下生成名为sample_project的flask项目文件夹

## 模板内容

当前生成的项目模板支持内容如下：

### 数据库

同时支持MySQL和MongoDB

具体数据库的配置信息在config.py

数据库信息在models文件下的对应文件中

### 异步任务

使用celery实现简单的异步任务和定时任务

相关配置信息在config.py中

celery的启动命令

```python
celery -A celery_worker.celery worker -c 8 -l info
```

celery 定时任务启动命令

```
celery -A celery_worker.celery beat -l info
```



### etcd

当前支持etcd v3,对应配置信息在config.py文件中

使用方法：

```python
from project_name.extensions import etcd
etcd.put(key, value)
```

### 常用方法

项目内置了一些常见方法，具体位置在```project/utils/__init__.py```

包括文件解压缩，格式检查等

同时，在```project/handlers/main.py```中内置了几个简单的api接口

### 项目启动

项目启动支持flask启动方式和gunicorn启动方式

```python
# flask启动
python manage.py runserver -p 5001

# gunicorn 启动
gunicorn -c gunicorn_conf_docker.py wsgi:app
```



### Docker

项目对应的dockerfile集中在docker文件夹内，可以根据个人需求创建和拉取镜像。

```
# build image
docker build -t REGISTRY_IMAGE:VERSION -f docker/Dockerfile .
# push image
docker push REGISTRY_IMAGE:VERSION
# run image
docker run REGISTRY_IMAGE:VERSION
```




