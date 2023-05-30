# 一个Django视频网站后端

## 项目介绍

本项目是一个Django视频网站后端，通过http接口提供服务，主要包括以下功能：

- 用户注册、登录
- 视频上传、删除
- 视频点赞、取消点赞
- 视频评论、回复评论
- 视频收藏、取消收藏
- 视频搜索
- 视频播放

## 项目结构

```
.
├── docs
│   └── API_doc.md
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── DFA.py
|   ├── APIatUser.py
│   └── APIatVideo.py
├── WebServer
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## 项目部署

### 1. 安装依赖

```
pip install -r requirements.txt
```

### 2. 数据库迁移

```
python manage.py makemigrations

```
```
python manage.py migrate
```

### 3. 创建超级用户

```
python manage.py createsuperuser
```

### 4. 运行项目

```
python manage.py runserver
```

## API文档

[API文档](docs/API_doc.md)
