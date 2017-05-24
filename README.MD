
# 使用Docker构建Flask 开发环境

app.py的程序如下:

```py
# -*- coding: UTF-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    fo = open("foo.txt", "wb")
    fo.write(b"I'am run in docker!")
    fo.close()
    return 'Flask Dockerized fred hhaha'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

```

创建Docker镜像

一.在app目录下生成一个Dockerfile文件,文件内容如下:


```
FROM python:3.5
MAINTAINER fred "fred@qzcool.com"
COPY requirements.txt /usr/www/app/
WORKDIR /usr/www/app
RUN pip install -r requirements.txt
CMD ["python"]

```

该Dockerfile执行的语句意思是

从官方拖取python:3.5镜像

把requirements.txt拷贝到docker /usr/www/app 目录下

却换工作目录到 /usr/www/app

安装通过requirements.txt执行安装依赖文件

二.生成镜像文件

命令窗口记得要却换到当前的目录下

```

docker build -t flask-sample:latest .

```

三.运行测试

```
docker run -v $PWD/app:/usr/www/app -w /usr/www/app -p 5000:5000 flask-sample-one python app.py
```
命令说明：

-v $PWD:/usr/src/myapp :将主机中当前目录挂载到容器的/usr/src/app

-w /usr/src/app :指定容器的/usr/src/app目录为工作目录

python app.py :使用容器的python命令来执行工作目录中的app.py文件

其他:删除没用的镜像文件

docker 删除<none>镜像

The reason for the error is that eventhough the image did not have any tag, there still exists a container created on that image which might be in the exited state. So you need to ensure that you have stopped and deleted all containers created on those images. The following command helps you in removing all containers that are not running:

docker rm `docker ps -aq --no-trunc --filter "status=exited"`

Now this removes all the dangling non intermediate <none> images:

docker rmi `docker images --filter 'dangling=true' -q --no-trunc`


git 使用

1.初始化

```
git init
```

生成.gitignore 文件

```
touch .gitignore
```

添加到本地仓库

```
git add .
```

添加远程仓库地址:

```
git remote add dockerflask https://github.com/fredliu168/docker-for-flask.git

```

推送到远程仓库:
```
git push -u dockerflask master
```

删除远程仓库地址:
```
git remote rm dockerflask
```


