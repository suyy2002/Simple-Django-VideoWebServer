from django.db import models

# Create your models here.
class User(models.Model):
    # 账号
    uid = models.AutoField(primary_key=True)
    # 用户名
    username = models.CharField(max_length=20, unique=True)
    # 密码
    password = models.CharField(max_length=128)
    # 昵称
    nickname = models.CharField(max_length=20)
    # 头像
    avatar = models.TextField()
    # 个性签名
    signature = models.TextField()
    # 粉丝数
    fans = models.IntegerField()
    # 关注数
    follow = models.IntegerField()
    # 经验
    exp = models.IntegerField()

    def __str__(self):
        return self.username
    
    class Meta:
        indexes = [
            models.Index(fields=['uid']),
            models.Index(fields=['username']),
        ]

    def getLevel(self):
        if self.exp < 100:
            return 0
        elif self.exp < 500:
            return 1
        elif self.exp < 1000:
            return 2
        elif self.exp < 2000:
            return 3
        elif self.exp < 5000:
            return 4
        elif self.exp < 10000:
            return 5
        elif self.exp < 17000:
            return 6
        elif self.exp < 25000:
            return 7
        elif self.exp < 35000:
            return 8
        else:
            return 9


class Video(models.Model):
    # 视频id
    vid = models.AutoField(primary_key=True)
    # 视频标题
    title = models.CharField(max_length=50)
    # 视频简介
    intro = models.TextField()
    # 视频封面
    cover = models.TextField()
    # 视频地址
    url = models.TextField()
    # 视频发布时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 视频作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 视频点赞数
    likes = models.IntegerField(default=0)
    # 视频收藏数
    collects = models.IntegerField(default=0)
    # 视频评论数
    comments = models.IntegerField(default=0)
    # 视频播放量
    play = models.IntegerField(default=0)
    # 视频时长
    duration = models.TimeField()
    # 视频类型
    type = models.ForeignKey('Types', on_delete=models.CASCADE)
    # 视频状态
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Types(models.Model):
    # 类型id
    tid = models.AutoField(primary_key=True)
    # 类型名称
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['tid']),
            models.Index(fields=['name']),
        ]


class Comment(models.Model):
    # 评论id
    cid = models.AutoField(primary_key=True)
    # 评论内容
    content = models.TextField()
    # 评论时间,自动设置为当前时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 评论作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 评论视频
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # 评论点赞数
    likes = models.IntegerField(default=0)
    # 评论回复数
    replys = models.IntegerField(default=0)
    # 评论状态
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.content
    
    class Meta:
        indexes = [
            models.Index(fields=['cid']),
            models.Index(fields=['video']),
        ]
    

class LikeComment(models.Model):
    # 点赞id
    lid = models.AutoField(primary_key=True)
    # 点赞时间，自动设置为当前时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 点赞者
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    # 点赞评论
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.liker.username + '->' + self.comment.content
    
    class Meta:
        indexes = [
            models.Index(fields=['lid']),
            models.Index(fields=['liker']),
            models.Index(fields=['comment']),
        ]


class Reply(models.Model):
    # 回复id
    rid = models.AutoField(primary_key=True)
    # 回复内容
    content = models.TextField()
    # 回复时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 回复作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 回复评论
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # 回复点赞数
    likes = models.IntegerField(default=0)
    # 回复状态
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.content
    
    class Meta:
        indexes = [
            models.Index(fields=['rid']),
            models.Index(fields=['comment']),
        ]


class LikeReply(models.Model):
    # 点赞id
    lid = models.AutoField(primary_key=True)
    # 点赞时间，自动设置为当前时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 点赞者
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    # 点赞评论
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)

    def __str__(self):
        return self.liker.username + '->' + self.reply.content
    
    class Meta:
        indexes = [
            models.Index(fields=['lid']),
            models.Index(fields=['reply']),
        ]


class Follow(models.Model):
    # 关注id
    fid = models.AutoField(primary_key=True)
    # 关注时间，自动设置为当前时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 关注者
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    # 被关注者
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')

    def __str__(self):
        return self.follower.username + '->' + self.followed.username
    
    class Meta:
        indexes = [
            models.Index(fields=['fid']),
            models.Index(fields=['follower']),
            models.Index(fields=['followed']),
        ]
    

class Collect(models.Model):
    # 收藏id
    cid = models.AutoField(primary_key=True)
    # 收藏时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 收藏者
    collector = models.ForeignKey(User, on_delete=models.CASCADE)
    # 被收藏视频
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.collector.username + '->' + self.video.title
    
    class Meta:
        indexes = [
            models.Index(fields=['cid']),
            models.Index(fields=['collector']),
        ]


class Like(models.Model):
    # 点赞id
    lid = models.AutoField(primary_key=True)
    # 点赞时间
    pubtime = models.DateTimeField(auto_now_add=True)
    # 点赞者
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    # 被点赞视频
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.liker.username + '->' + self.video.title
    
    class Meta:
        indexes = [
            models.Index(fields=['lid']),
            models.Index(fields=['liker']),
            models.Index(fields=['video']),
        ]
    

class History(models.Model):
    # 历史记录id
    hid = models.AutoField(primary_key=True)
    # 历史记录时间
    pubtime = models.DateTimeField(auto_now=True)
    # 历史记录者
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 历史记录视频
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '->' + self.video.title
    
    class Meta:
        indexes = [
            models.Index(fields=['hid']),
            models.Index(fields=['user']),
            models.Index(fields=['video']),
        ]
    

