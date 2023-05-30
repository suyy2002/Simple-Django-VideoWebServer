[TOC]

# 用户API接口文档

## /api/user/

### 请求方法

- GET：获取用户信息
- POST：修改用户信息

### 请求参数

- GET 请求需要传递以下参数：

| 参数名 | 类型 | 必填 | 描述         |
| ------ | ---- | ---- | ------------ |
| uid    | int  | 是   | 用户唯一标识 |

- POST 请求需要传递以下数据：

| 参数名    | 类型   | 必填 | 描述         |
| --------- | ------ | ---- | ------------ |
| uid       | int    | 是   | 用户唯一标识 |
| nickname  | string | 否   | 用户昵称     |
| avatar    | string | 否   | 用户头像 URL |
| signature | string | 否   | 用户个性签名 |

### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| uid       | int    | 用户唯一标识 |
| username  | string | 用户名       |
| nickname  | string | 用户昵称     |
| avatar    | string | 用户头像 URL |
| signature | string | 用户个性签名 |
| fans      | int    | 粉丝数       |
| follow    | int    | 关注数       |
| exp       | int    | 经验值       |
| level     | int    | 用户等级     |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 403    | Nickname or signature contains sensitive words.  | 存在敏感词 |
| 404    | User does not exist. | 用户不存在 |

### 示例

#### 获取用户信息

- 请求方法：GET
- 请求地址：/api/user/
- 请求参数：

```json
{
    "uid": 123
}
```

- 响应示例：

```json
{
    "uid": 123,
    "username": "testuser",
    "nickname": "Test User",
    "avatar": "https://example.com/avatar.jpg",
    "signature": "Hello, world!",
    "fans": 100,
    "follow": 50,
    "exp": 1000,
    "level": 2
}
```

#### 修改用户信息

- 请求方法：POST
- 请求地址：/api/user/
- 请求数据：

```json
{
    "uid": 123,
    "nickname": "New Nickname",
    "avatar": "https://example.com/new_avatar.jpg",
    "signature": "New Signature"
}
```

- 响应示例：

```json
{
    "uid": 123,
    "username": "testuser",
    "nickname": "New Nickname",
    "avatar": "https://example.com/new_avatar.jpg",
    "signature": "New Signature",
    "fans": 100,
    "follow": 50,
    "exp": 1000,
    "level": 2
}
```

## /api/login/

### 请求方法

- POST：用户登录

### 请求参数

- POST 请求需要传递以下数据：

| 参数名   | 类型   | 必填 | 描述     |
| -------- | ------ | ---- | -------- |
| username | string | 是   | 用户名   |
| password | string | 是   | 用户密码 |

### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| uid       | int    | 用户唯一标识 |
| username  | string | 用户名       |
| nickname  | string | 用户昵称     |
| avatar    | string | 用户头像 URL |
| signature | string | 用户个性签名 |
| fans      | int    | 粉丝数       |
| follow    | int    | 关注数       |
| exp       | int    | 经验值       |
| level     | int    | 用户等级     |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 403    | Wrong Password       | 用户名或密码错误 |
| 404    | User does not exist. | 用户不存在 |

### 示例

#### 用户登录

- 请求方法：POST
- 请求地址：/api/login/
- 请求数据：
  
```json
{
    "username": "testuser",
    "password": "123456"
}
```

- 响应示例：

```json
{
    "uid": 123,
    "username": "testuser",
    "nickname": "Test User",
    "avatar": "https://example.com/avatar.jpg",
    "signature": "Hello, world!",
    "fans": 100,
    "follow": 50,
    "exp": 1000,
    "level": 2
}
```

## /api/register/

### 请求方法

- POST：用户注册
- GET：检查用户名是否已被注册

### 请求参数

- POST 请求需要传递以下数据：

| 参数名   | 类型   | 必填 | 描述     |
| -------- | ------ | ---- | -------- |
| username | string | 是   | 用户名   |
| password | string | 是   | 用户密码 |
| nickname | string | 是   | 用户昵称 |
| avatar  | string | 是   | 用户头像 URL |

- GET 请求需要传递以下参数：

| 参数名   | 类型   | 必填 | 描述     |
| -------- | ------ | ---- | -------- |
| username | string | 是   | 用户名   |

### 响应参数

- POST 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| uid       | int    | 用户唯一标识 |
| username  | string | 用户名       |
| nickname  | string | 用户昵称     |
| avatar    | string | 用户头像 URL |
| signature | string | 用户个性签名 |
| fans      | int    | 粉丝数       |
| follow    | int    | 关注数       |
| exp       | int    | 经验值       |
| level     | int    | 用户等级     |

- GET 成功时返回以下参数：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Username Not Exists  | 用户名未被注册 |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 402    | Username Exists      | 用户名已被注册 |
| 403    | Username or nickname contains sensitive words.   | 存在敏感词 |

### 示例

#### 用户注册

- 请求方法：POST
- 请求地址：/api/register/
- 请求参数：

```json
{
    "username": "newuser",
    "password": "newpassword",
    "nickname": "New User",
    "avatar": "https://example.com/new_avatar.jpg"
}
```

- 响应示例：

```json
{
    "uid": 124,
    "username": "newuser",
    "nickname": "New User",
    "avatar": "https://example.com/new_avatar.jpg",
    "signature": "Hello, world!",
    "fans": 0,
    "follow": 0,
    "exp": 0,
    "level": 1
}
```

#### 检查用户名是否已被注册

- 请求方法：GET
- 请求地址：/api/register/

- 请求参数：

```json
{
    "username": "newuser"
}
```

- 响应示例：

```json
{
    "status": 200,
    "content": "Username Not Exists"
}
```

## /api/follow/

### 请求方法

- POST：关注用户
- GET：获取用户关注列表

### 请求参数

- POST 请求需要传递以下数据：

| 参数名 | 类型 | 必填 | 描述     |
| ------ | ---- | ---- | -------- |
| follower    | int  | 是   | 用户 ID  |
| followed    | int  | 是   | 被关注 ID |

- GET 请求需要传递以下参数：

| 参数名 | 类型 | 必填 | 描述     |
| ------ | ---- | ---- | -------- |
| uid    | int  | 是   | 用户 ID  |

### 响应参数

- POST 成功时返回以下参数：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Follow Success       | 关注成功   |
| 201    | Unfollow Success     | 取消关注成功 |

- POST 失败时返回以下参数：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request          | 请求错误   |
| 403    | Can't Follow Yourself     | 不能关注你自己 |
| 404    | User Not Found       | 用户不存在 |

- GET 成功时返回以下参数：

| 参数名 | 类型 | 描述     |
| ------ | ---- | -------- |
| uid    | int  | 用户 ID  |
| nickname    | string  | 用户昵称 |
| avatar    | string  | 用户头像 URL |
| signature    | string  | 用户个性签名 |

- GET 失败时返回以下参数：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request          | 请求错误   |
| 404    | User Not Found       | 用户不存在 |

### 示例

#### 关注用户

- 请求方法：POST
- 请求地址：/api/follow/
- 请求参数：

```json
{
    "follower": 123,
    "followed": 124
}
```

- 响应示例：

```json
{
    "status": 200,
    "content": "Follow Success"
}
```

#### 取消关注用户

- 请求方法：POST
- 请求地址：/api/follow/
- 请求参数：

```json
{
    "follower": 123,
    "followed": 124
}
```

- 响应示例：

```json
{
    "status": 201,
    "content": "Unfollow Success"
}
```

#### 获取用户关注列表

- 请求方法：GET
- 请求地址：/api/follow/
- 请求参数：

```json
{
    "uid": 123
}
```

- 响应示例：

```json
[
    {
        "uid": 124,
        "nickname": "New User",
        "avatar": "https://example.com/new_avatar.jpg",
        "signature": "Hello, world!"
    },
    {
        "uid": 125,
        "nickname": "New User 2",
        "avatar": "https://example.com/new_avatar_2.jpg",
        "signature": "Hello, world!"
    }
]
```

## /api/fans/

### 请求方法

- GET：获取用户粉丝列表

### 请求参数

- GET 请求需要传递以下参数：

| 参数名 | 类型 | 必填 | 描述     |
| ------ | ---- | ---- | -------- |
| uid    | int  | 是   | 用户 ID  |

### 响应参数

- GET 成功时返回以下参数：

| 参数名 | 类型 | 描述     |
| ------ | ---- | -------- |
| uid    | int  | 用户 ID  |
| nickname    | string  | 用户昵称 |
| avatar    | string  | 用户头像 URL |
| signature    | string  | 用户个性签名 |

- GET 失败时返回以下参数：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request          | 请求错误   |
| 404    | User Not Found       | 用户不存在 |

### 示例

#### 获取用户粉丝列表

- 请求方法：GET
- 请求地址：/api/fans/
- 请求参数：

```json
{
    "uid": 123
}
```

- 响应示例：

```json
[
    {
        "uid": 124,
        "nickname": "New User",
        "avatar": "https://example.com/new_avatar.jpg",
        "signature": "Hello, world!"
    },
    {
        "uid": 125,
        "nickname": "New User 2",
        "avatar": "https://example.com/new_avatar_2.jpg",
        "signature": "Hello, world!"
    }
]
```

# 视频API接口文档

## /api/video/

### GET

#### 获取视频信息

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| uid    | int    | False | 用户编号 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| vid       | int    | 视频编号     |
| title    | string  | 视频标题 |
| intro    | string  | 视频简介 |
| cover    | string  | 视频封面 |
| url      | string  | 视频地址 |
| likes    | int     | 点赞数   |
| collects | int     | 收藏数   |
| comments | int     | 评论数   |
| play     | int     | 播放数   |
| pubtime  | string  | 发布时间 |
| duration | string  | 视频时长 |
| isLike   | bool    | 是否点赞 |
| isCollect| bool    | 是否收藏 |
| type.tid | int     | 分类编号 |
| type.name  | string  | 分类名称 |
| author.uid | int     | 作者编号 |
| author.nickname | string  | 作者昵称   |
| author.avatar   | string  | 作者头像   |
| author.fans     | int     | 作者粉丝数 |
| author.level    | int     | 作者等级   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
GET /api/video/?vid=1
```

###### 响应

```json
{
    "vid": 1,
    "title": "test video",
    "intro": "video intro",
    "cover": "cover url",
    "url": "video url",
    "likes": 0,
    "collects": 0,
    "comments": 1,
    "play": 0,
    "pubtime": "2023-05-29T18:00:39Z",
    "duration": "00:05:30",
    "isLike": false,
    "isCollect": false,
    "type": {
        "tid": 1,
        "name": "动画"
    },
    "author": {
        "uid": 1,
        "nickname": "测试用户1",
        "avatar": "头像",
        "fans": 1,
        "level": 0
    }
}
```

### POST

#### 编辑

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| title    | string  | False | 视频标题 |
| intro    | string  | False | 视频简介 |
| cover    | string  | False | 视频封面 |
| url      | string  | False | 视频地址 |
| type.tid | int     | False | 分类编号 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| vid       | int    | 视频编号     |
| title    | string  | 视频标题 |
| intro    | string  | 视频简介 |
| cover    | string  | 视频封面 |
| url      | string  | 视频地址 |
| duration | string  | 视频时长 |
| type.tid | int     | 分类编号 |
| type.name  | string  | 分类名称 |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
POST /api/video/
```

###### 请求体

```json
{
    "vid": 2,
    "title": "test video",
    "intro": "video intro",
    "cover": "cover url",
    "url": "video url",
    "type": {
        "tid": 2
    }
}
```

###### 响应

```json
{
    "vid": 2,
    "title": "test video",
    "intro": "video intro",
    "cover": "cover url",
    "url": "video url",
    "duration": "00:05:30",
    "type": {
        "tid": 2,
        "name": "游戏"
    }
}
```

### DELETE

#### 删除视频

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |

##### 响应参数

- 成功时返回以下参数：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 204    | Video deleted successfully.    | 删除成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```json
{
    "vid": 2
}
```

###### 响应

```json
{
    "status": 204,
    "content": "Video deleted successfully."
}
```

### PUT

#### 上传视频

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| uid     | int    | True  | 用户编号 |
| title    | string  | True | 视频标题 |
| intro    | string  | True | 视频简介 |
| cover    | string  | True | 视频封面 |
| url      | string  | True | 视频地址 |
| duration | string  | True | 视频时长 |
| tid      | int     | True | 分类编号 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| vid       | int    | 视频编号     |
| title    | string  | 视频标题 |
| intro    | string  | 视频简介 |
| cover    | string  | 视频封面 |
| url      | string  | 视频地址 |
| likes     | int    | 点赞数       |
| collects  | int    | 收藏数       |
| comments  | int    | 评论数       |
| play      | int    | 播放数       |
| pubtime   | string | 发布时间     |
| duration | string  | 视频时长 |
| isLike    | bool   | 是否点赞     |
| isCollect | bool   | 是否收藏     |
| type.tid | int     | 分类编号 |
| type.name  | string  | 分类名称 |
| author.uid | int    | 作者编号 |
| author.nickname | string | 作者昵称 |
| author.avatar | string | 作者头像 |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | User does not exist. | 用户不存在 |

##### 示例

###### 请求

```
PUT /api/video/
```

###### 请求体

```json
{
    "uid": 3,
    "title": "test video",
    "intro": "video intro",
    "cover": "cover url",
    "url": "video url",
    "duration": "00:05:30",
    "tid": 2
}
```

###### 响应

```json
{
    "vid": 2,
    "title": "test video",
    "intro": "video intro",
    "cover": "cover url",
    "url": "video url",
    "likes": 0,
    "collects": 0,
    "comments": 0,
    "play": 0,
    "pubtime": "2020-12-12 12:12:12",
    "duration": "00:05:30",
    "isLike": false,
    "isCollect": false,
    "type": {
        "tid": 2,
        "name": "游戏"
    },
    "author": {
        "uid": 3,
        "nickname": "test",
        "avatar": "avatar url"
    }
}
```

## /api/video/play/

### POST

#### 播放视频

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| uid     | int    | False  | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Play success.        | 播放成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
POST /api/video/play/
```

###### 请求体

```json
{
    "vid": 2,
    "uid": 3
}
```

###### 响应

```json
{
    "status": 200,
    "content": "Play success."
}
```

## /api/video/like/

### GET

#### 获取视频点赞状态

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| uid     | int    | True  | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | True                | 已点赞   |
| 201    | False                | 未点赞   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
GET /api/video/like/?vid=2&uid=3
```

###### 响应

```json
{
    "status": 200,
    "content": true
}
```

### POST

#### 点赞视频

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| uid     | int    | True  | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Like success.        | 点赞成功   |
| 201    | Cancel like.         | 取消点赞成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
POST /api/video/like/
```

###### 请求体

```json
{
    "vid": 2,
    "uid": 3
}
```

###### 响应

```json
{
    "status": 200,
    "content": "Like success."
}
```

## /api/video/collect/

### GET

#### 获取视频收藏状态

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| uid     | int    | True  | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | True                | 已收藏   |
| 201    | False                | 未收藏   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
GET /api/video/collect/?vid=2&uid=3
```

###### 响应

```json
{
    "status": 200,
    "content": true
}
```

### POST

#### 收藏/取消收藏视频

##### 请求参数

| 参数名 | 类型   | 是否必需 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int    | True  | 视频编号 |
| uid     | int    | True  | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Collect success.        | 收藏成功   |
| 201    | Cancel collect.         | 取消收藏成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
POST /api/video/collect/
```

###### 请求体

```json
{
    "vid": 2,
    "uid": 3
}
```

###### 响应

```json
{
    "status": 200,
    "content": "Collect success."
}
```

# 搜索API文档

## /api/search/video

### GET

#### 搜索视频

##### 请求参数

| 参数名 | 类型   | 必须 | 说明     |
| ------ | ------ | -------- | -------- |
| keyword     | string   |  True  | 关键字 |
| sortBy      | string   |  False  | 排序方式 |
| page   | int    |  False  | 页码     |
| size   | int    |  False  | 每页大小 |
| uid    | int    |  False | 用户编号 |

##### 响应参数

- 成功搜索时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| vid       | int    | 视频编号     |
| title    | string  | 视频标题 |
| intro    | string  | 视频简介 |
| cover    | string  | 视频封面 |
| play      | int    | 播放数       |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | No more videos.     | 没有更多视频 |

##### video示例

###### 请求

```
GET /api/search/video
```

###### 请求params

```json
{
    "keyword": "test",
    "search": "video",
    "sortBy": "play",
    "page": 1,
    "size": 10
}
```

###### 响应

```json
[
    {
        "vid": 1,
        "title": "test video",
        "intro": "video intro",
        "cover": "cover url",
        "play": 0
    },
    {
        "vid": 2,
        "title": "test video",
        "intro": "video intro",
        "cover": "cover url",
        "play": 0
    }
]
```

## /api/search/user

### GET

#### 搜索用户

##### 请求参数

| 参数名 | 类型   | 必须 | 说明     |
| ------ | ------ | -------- | -------- |
| keyword     | string   |  True  | 关键字 |
| sortBy      | string   |  False  | 排序方式 |
| page   | int    |  False  | 页码     |
| size   | int    |  False  | 每页大小 |
| uid    | int    |  False | 用户编号 |

##### 响应参数

- 成功搜索时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| uid       | int    | 用户编号     |
| nickname | string  | 用户昵称 |
| avatar   | string  | 用户头像 |
| signature | string  | 用户签名 |
| fans      | int    | 粉丝数       |
| isFollow  | bool   | 是否关注     |
| level     | int    | 用户等级     |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | No more users.     | 没有更多用户 |


##### 示例

###### 请求

```
GET /api/search/user
```

###### 请求pararm

```json
{
    "keyword": "test",
    "search": "user",
    "uid": 1,
    "page": 1,
    "size": 10
}
```

###### 响应

```json
[
    {
        "uid": 2,
        "nickname": "test",
        "avatar": "avatar url",
        "signature": "signature",
        "fans": 0,
        "isFollow": false,
        "level": 1
    },
    {
        "uid": 3,
        "nickname": "test",
        "avatar": "avatar url",
        "signature": "signature",
        "fans": 0,
        "isFollow": false,
        "level": 1
    }
]
```

# 评论API文档

## /api/comment/

### GET

#### 获取评论列表

##### 请求参数

| 参数名 | 类型   | 必须 | 说明     |
| ------ | ------ | -------- | -------- |
| vid     | int   |  True  | 视频编号 |
| uid    | int    |  False | 用户编号 |
| page   | int    |  False  | 页码     |
| size   | int    |  False  | 每页大小 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| cid       | int    | 评论编号     |
| content   | string | 评论内容     |
| pubtime   | string | 发布时间     |
| likes     | int    | 点赞数       |
| replys   | int    | 回复数       |
| isLike    | bool   | 是否点赞     |
| author.uid | int     | 作者编号 |
| author.nickname | string  | 作者昵称   |
| author.avatar   | string  | 作者头像   |
| author.level    | int     | 作者等级   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |

##### 示例

###### 请求

```
GET /api/comment/?vid=1&page=1&size=10
```

###### 响应

```json
[
    {
        "cid": 4,
        "content": "test5",
        "pubtime": "2023-05-29T16:19:09.282Z",
        "likes": 0,
        "replys": 0,
        "isLike": false,
        "author": {
            "uid": 5,
            "nickname": "test5",
            "avatar": "test",
            "level": 0
        }
    },
    {
        "cid": 2,
        "content": "test",
        "pubtime": "2023-05-29T16:18:09.167Z",
        "likes": 0,
        "replys": 0,
        "isLike": false,
        "author": {
            "uid": 4,
            "nickname": "test4",
            "avatar": "test",
            "level": 0
        }
    },
]
```

### POST

#### 发布评论

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| vid     | int     | 视频编号 |
| uid    | int    | 用户编号 |
| content   | string    | 评论内容 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| cid       | int    | 评论编号     |
| content   | string | 评论内容     |
| pubtime   | string | 发布时间     |
| likes     | int    | 点赞数       |
| replys   | int    | 回复数       |
| isLike    | bool   | 是否点赞     |
| author.uid | int     | 作者编号 |
| author.nickname | string  | 作者昵称   |
| author.avatar   | string  | 作者头像   |
| author.level    | int     | 作者等级   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Video does not exist. | 视频不存在 |
| 404    | User does not exist.  | 用户不存在 |

##### 示例

###### 请求

```
POST /api/comment/
```

###### 请求体

```json
{
    "vid": 1,
    "uid": 1,
    "content": "test"
}
```

###### 响应

```json
{
    "cid": 2,
    "content": "test",
    "pubtime": "2023-05-29T16:18:09.167Z",
    "likes": 0,
    "replys": 0,
    "isLike": false,
    "author": {
        "uid": 1,
        "nickname": "测试用户1",
        "avatar": "头像",
        "level": 0
    }
}
```

### DELETE

#### 删除评论

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| cid     | int     | 评论编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 204    | No Content.          | 删除成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Comment does not exist. | 评论不存在 |

##### 示例

###### 请求

```
DELETE /api/comment/

```

###### 请求体

```json
{
    "cid": 2
}
```

###### 响应

```
204 No Content
```

### PUT

#### 点赞/取消点赞评论

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| cid     | int     | 评论编号 |
| uid    | int    | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Like success.        | 点赞成功   |
| 201    | Cancel like.         | 取消点赞成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Comment does not exist. | 评论不存在 |

##### 示例

###### 请求

```
PUT /api/comment/
```

###### 请求体

```json
{
    "cid": 2,
    "uid": 1
}
```

###### 响应

```
200 Like success.
```

## /api/reply/

### GET

#### 获取评论回复列表

##### 请求参数

| 参数名 | 类型   | 是否必需  | 说明     |
| ------ | ------ | -------- |-------- |
| cid     | int     | True | 评论编号 |
| uid    | int    | False | 用户编号 |
| page    | int    | False | 页码 |
| size    | int    | False | 每页大小 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| rid       | int    | 回复编号     |
| content   | string | 回复内容     |
| pubtime   | string | 发布时间     |
| likes     | int    | 点赞数       |
| isLike    | bool   | 是否点赞     |
| author.uid | int     | 作者编号 |
| author.nickname | string  | 作者昵称   |
| author.avatar   | string  | 作者头像   |
| author.level    | int     | 作者等级   |

- 失败时返回 HTTP 状态码和错误信息:

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Comment does not exist. | 评论不存在 |

##### 示例

###### 请求

```
GET /api/reply/?cid=1&uid=1&page=1&size=10
```

###### 响应

```json
[
    {
        "rid": 1,
        "content": "test",
        "pubtime": "2023-05-29T16:18:09.167Z",
        "likes": 0,
        "isLike": false,
        "author": {
            "uid": 1,
            "nickname": "测试用户1",
            "avatar": "头像",
            "level": 0
        }
    }
]
```

### POST

#### 发布回复

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| cid     | int     | 评论编号 |
| uid    | int    | 用户编号 |
| content    | string    | 回复内容 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| rid       | int    | 回复编号     |
| content   | string | 回复内容     |
| pubtime   | string | 发布时间     |
| likes     | int    | 点赞数       |
| isLike    | bool   | 是否点赞     |
| author.uid | int     | 作者编号 |
| author.nickname | string  | 作者昵称   |
| author.avatar   | string  | 作者头像   |
| author.level    | int     | 作者等级   |

- 失败时返回 HTTP 状态码和错误信息:

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 403    | User does not exist. | 用户不存在 |
| 404    | Comment does not exist. | 评论不存在 |

##### 示例

###### 请求

```
POST /api/reply/
```

###### 请求体

```json
{
    "cid": 1,
    "uid": 1,
    "content": "test"
}
```

###### 响应

```json
{
    "rid": 1,
    "content": "test",
    "pubtime": "2023-05-29T16:18:09.167Z",
    "likes": 0,
    "isLike": false,
    "author": {
        "uid": 1,
        "nickname": "测试用户1",
        "avatar": "头像",
        "level": 0
    }
}
```

### DELETE

#### 删除回复

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| rid     | int     | 回复编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 204    | No Content.          | 删除成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | Reply does not exist. | 回复不存在 |

##### 示例

###### 请求

```
DELETE /api/reply/

```

###### 请求体

```json
{
    "rid": 2
}
```

###### 响应

```
204 No Content
```

### PUT

#### 点赞/取消点赞回复

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| rid     | int     | 回复编号 |
| uid    | int    | 用户编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 200    | Like success.        | 点赞成功   |
| 201    | Cancel like.         | 取消点赞成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 403    | User does not exist. | 用户不存在 |
| 404    | Reply does not exist. | 回复不存在 |

##### 示例

###### 请求

```
PUT /api/reply/
```

###### 请求体

```json
{
    "rid": 2,
    "uid": 1
}
```

###### 响应

```
200 Like success.
```

# 记录API文档

## /api/history/

### GET

#### 获取历史记录

##### 请求参数

| 参数名 | 类型   | 是否必须 | 说明     |
| ------ | ------ | -------- | -------- |
| uid    | int    | True | 用户编号 |
| page    | int    | False | 页码 |
| size    | int    | False | 每页大小 |

##### 响应参数

- 成功时返回以下参数：

| 参数名    | 类型   | 描述         |
| --------- | ------ | ------------ |
| hid       | int    | 历史记录编号     |
| video.vid | int    | 视频编号     |
| video.title | string | 视频标题     |
| video.cover | string | 视频封面     |
| pubtime   | string | 观看时间     |

- 失败时返回 HTTP 状态码和错误信息:

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | User does not exist. | 用户不存在 |

##### 示例

###### 请求

```
GET /api/history/?uid=1&page=1&size=10
```

###### 响应

```json
[
    {
        "hid": 1,
        "video": {
            "vid": 1,
            "title": "test",
            "cover": "封面"
        },
        "pubtime": "2023-05-29T16:18:09.167Z"
    }
]
```

### POST

#### 删除历史记录

##### 请求参数

| 参数名 | 类型   | 说明     |
| ------ | ------ | -------- |
| hid     | int     | 历史记录编号 |

##### 响应参数

- 成功时返回以下Http状态码：

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 204    | Delete success.      | 删除成功   |

- 失败时返回 HTTP 状态码和错误信息。

| 状态码 | 内容                 | 描述       |
| ------ | -------------------- | ---------- |
| 400    | Bad Request.         | 请求错误   |
| 404    | History does not exist. | 历史记录不存在 |

##### 示例

###### 请求

```
DELETE /api/history/
```

###### 请求体

```json
{
    "hid": 1
}
```

###### 响应

```
204 Delete success.
```
