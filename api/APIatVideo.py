from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.db.models import Q
from .models import *
from .DFA import DFA

DFAfilter = DFA()
def setACAO(response):
    response['Access-Control-Allow-Origin'] = '*' # 允许所有源
    return response

# 视频信息API
class VideoAPI(APIView):
    # 获取视频信息
    def VideoBasicInfo(self, request):
        try:
            vid = request.GET['vid']
            video = Video.objects.get(vid=vid, status=True)
            isLike = False
            isCollect = False
            try:
                uid = request.GET['uid']
                user = User.objects.get(uid=uid)
                try:
                    Like.objects.get(liker=user, video=video)
                    isLike = True
                except:
                    pass
                try:
                    Collect.objects.get(collector=user, video=video)
                    isCollect = True
                except:
                    pass
            except:
                pass
            data = {
                'vid': video.vid,
                'title': video.title,
                'intro': video.intro,
                'cover': video.cover,
                'url': video.url,
                'likes': video.likes,
                'collects': video.collects,
                'comments': video.comments,
                'play': video.play,
                'pubtime': video.pubtime,
                'duration': video.duration,
                'isLike': isLike,
                'isCollect': isCollect,
                'type': {
                    'tid': video.type.tid,
                    'name': video.type.name
                },
                'author': {
                    'uid': video.author.uid,
                    'nickname': video.author.nickname,
                    'avatar': video.author.avatar,
                    'fans': video.author.fans,
                    'level': video.author.getLevel()
                }
            }
            return JsonResponse(data)
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 编辑视频信息
    def VideoModify(self, request):
        try:
            vid = request.POST['vid']
            video = Video.objects.get(vid=vid)
            try:
                video.title = DFAfilter.filter_all(request.POST['title'])
            except:
                pass
            try:
                video.intro = DFAfilter.filter_all(request.POST['intro'])
            except:
                pass
            try:
                video.cover = request.POST['cover']
            except:
                pass
            try:
                video.url = request.POST['url']
                video.duration = request.POST['duration']
            except:
                pass
            try:
                video.type = Types.objects.get(tid=request.POST['tid'])
            except:
                pass
            video.save()
            data = {
                'vid': video.vid,
                'title': video.title,
                'intro': video.intro,
                'cover': video.cover,
                'url': video.url,
                'duration': video.duration,
                'type': {
                    'tid': video.type.tid,
                    'name': video.type.name
                }
            }
            return JsonResponse(data)
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 删除视频
    def VideoDelete(self, request):
        try:
            vid = request.POST['vid']
            video = Video.objects.get(vid=vid)
            video.status = False
            video.save()
            return HttpResponse(status=204, content='Video deleted successfully.')
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 上传视频
    def VideoUpload(self, request):
        try:
            uid = request.POST['uid']
            user = User.objects.get(uid=uid)
            title = DFAfilter.filter_all(request.POST['title'])
            intro = DFAfilter.filter_all(request.POST['intro'])
            cover = request.POST['cover']
            url = request.POST['url']
            duration = request.POST['duration']
            type = Types.objects.get(tid=request.POST['tid'])
            video = Video.objects.create(author=user, 
                                         title=title, 
                                         intro=intro, 
                                         cover=cover, 
                                         url=url, 
                                         duration=duration, 
                                         type=type)
            data = {
                'vid': video.vid,
                'title': video.title,
                'intro': video.intro,
                'cover': video.cover,
                'url': video.url,
                'likes': 0,
                'collects': 0,
                'comments': 0,
                'play': 0,
                'pubtime': video.pubtime,
                'duration': video.duration,
                'isLike': False,
                'isCollect': False,
                'type': {
                    'tid': video.type.tid,
                    'name': video.type.name
                },
                'author': {
                    'uid': video.author.uid,
                    'nickname': video.author.nickname,
                    'avatar': video.author.avatar,
                }
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return HttpResponse(status=404, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
    
    def get(self, request):
        return setACAO(self.VideoBasicInfo(request))
    
    def post(self, request):
        return setACAO(self.VideoModify(request))
    
    def delete(self, request):
        return setACAO(self.VideoDelete(request))
    
    def put(self, request):
        return setACAO(self.VideoUpload(request))


# 视频搜索API
class SearchVideoAPI(APIView):
    # 搜索视频
    def SearchVideo(self, request):
        try:
            keyword = request.GET['keyword']
            try:
                page = int(request.GET['page'])
            except:
                page = 1
            try:
                size = int(request.GET['size'])
            except:
                size = 20
            try:
                sortBy = request.GET['sortBy']
            except:
                sortBy = 'likes'
            # 根据page和size搜索
            videos = Video.objects.filter(Q(title__contains=keyword) | Q(intro__contains=keyword), 
                                          status=True).order_by(sortBy)[(page-1)*size:page*size]
            if len(videos) == 0:
                return HttpResponse(status=404, content='No more videos.')
            data = []
            for video in videos:
                data.append({
                    'vid': video.vid,
                    'title': video.title,
                    'intro': video.intro,
                    'cover': video.cover,
                    'play': video.play,
                })
            return JsonResponse(data, safe=False)
        except Exception as e:
            return HttpResponse(status=400, content=e)
    
    def get(self, request):
        return setACAO(self.SearchVideo(request))


# 用户搜索API
class SearchUserAPI(APIView):
    # 搜索用户
    def SearchUser(self, request):
        try:
            keyword = request.GET['keyword']
            try:
                page = int(request.GET['page'])
            except:
                page = 1
            try:
                size = int(request.GET['size'])
            except:
                size = 20
            try:
                uid = request.GET['uid']
                user = User.objects.get(uid=uid)
            except:
                user = None
            try:
                sortBy = request.GET['sortBy']
            except:
                sortBy = 'fans'
            # 根据page和size搜索
            users = User.objects.filter(Q(nickname__contains=keyword) | Q(signature__contains=keyword)).order_by(sortBy)[(page-1)*size:page*size]
            # 如果users为空，返回201
            if len(users) == 0:
                return HttpResponse(status=404, content='No more users.')
            data = []
            for user in users:
                # 检查是否关注该用户
                if user:
                    isFollow = Follow.objects.filter(follower=user, followed=user).exists()
                else:
                    isFollow = False
                data.append({
                    'uid': user.uid,
                    'nickname': user.nickname,
                    'avatar': user.avatar,
                    'signature': user.signature,
                    'isFollow': isFollow,
                    'fans': user.fans,
                    'level': user.getLevel()
                })
            return JsonResponse(data, safe=False)
        except Exception as e:
            return HttpResponse(status=400, content=e)
    
    def get(self, request):
        return setACAO(self.SearchUser(request))
        

# 评论信息API
class CommentAPI(APIView):
    # 获取视频评论列表
    def CommentsList(self, request):
        try:
            vid = request.GET['vid']
            video = Video.objects.get(vid=vid)
            try:
                uid = request.GET['uid']
                user = User.objects.get(uid=uid)
            except:
                user = None
            try:
                page = int(request.GET['page'])
            except:
                page = 1
            try:
                size = int(request.GET['size'])
            except:
                size = 20
            # 根据page和size评论
            comments = Comment.objects.filter(video=video, status=True).order_by('likes')[(page-1)*size:page*size]
            # 如果comments为空，返回201
            if len(comments) == 0:
                return HttpResponse(status=201, content='No more comments.')
            data = []
            for comment in comments:
                # 判断当前用户是否点赞
                isLike = False
                if LikeComment.objects.filter(liker=user, comment=comment).exists():
                    isLike = True
                data.append({
                    'cid': comment.cid,
                    'content': comment.content,
                    'pubtime': comment.pubtime,
                    'likes': comment.likes,
                    'replys': comment.replys,
                    'isLike': isLike,
                    'author': {
                        'uid': comment.author.uid,
                        'nickname': comment.author.nickname,
                        'avatar': comment.author.avatar,
                        'level': comment.author.getLevel()
                    }
                })
            return JsonResponse(data, safe=False)
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 发表评论
    def CommentPublish(self, request):
        try:
            vid = request.POST['vid']
            video = Video.objects.get(vid=vid)
            uid = request.POST['uid']
            user = User.objects.get(uid=uid)
            # 过滤敏感词
            content = DFAfilter.filter_all(request.POST['content'])
            comment = Comment.objects.create(video=video, author=user, content=content)
            # 更新视频评论数
            video.comments += 1
            video.save()
            # 给视频作者增加经验
            video.author.exp += 1
            video.author.save()
            # 如果评论作者不是视频作者，则增加经验
            if video.author.uid != user.uid:
                user.exp += 1
                user.save()
            data = {
                'cid': comment.cid,
                'content': comment.content,
                'pubtime': comment.pubtime,
                'likes': comment.likes,
                'replys': comment.replys,
                'isLike': False, # 发表评论时，当前用户未点赞，所以isLike为False
                'author': {
                    'uid': comment.author.uid,
                    'nickname': comment.author.nickname,
                    'avatar': comment.author.avatar,
                    'level': comment.author.getLevel()
                }
            }
            return JsonResponse(data)
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except User.DoesNotExist:
            return HttpResponse(status=404, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)

    # 删除评论
    def CommentDelete(self, request):
        try:
            cid = request.POST['cid']
            comment = Comment.objects.get(cid=cid, status=True)
            # 更改评论状态
            comment.status = False
            comment.save()
            # 更新视频评论数
            video = comment.video
            video.comments -= 1
            video.save()
            return HttpResponse(status=204)
        except Comment.DoesNotExist:
            return HttpResponse(status=404)
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 点赞/取消点赞评论
    def CommentLike(self, request):
        try:
            cid = request.POST['cid']
            comment = Comment.objects.get(cid=cid)
            uid = request.POST['uid']
            liker = User.objects.get(uid=uid)
            try:
                LikeC = LikeComment.objects.get(comment=comment, liker=liker)
                # 如果已经点赞，则取消点赞
                LikeC.delete()
                # 更新评论点赞数
                comment.likes -= 1
                comment.save()
                return HttpResponse(status=201, content='Cancel like.')
            except LikeComment.DoesNotExist:
                # 如果没有点赞，则点赞
                LikeComment.objects.create(comment=comment, liker=liker)
                # 更新评论点赞数
                comment = Comment.objects.get(cid=cid)
                comment.likes += 1
                comment.save()
                return HttpResponse(status=200, content='Like success.')
        except Comment.DoesNotExist:
            return HttpResponse(status=404, content='Comment does not exist.')
        
        except Exception as e:
            return HttpResponse(status=400, content=e)

    def get(self, request):
        return setACAO(self.CommentsList(request))
    
    def post(self, request):
        return setACAO(self.CommentPublish(request))
    
    def delete(self, request):
        return setACAO(self.CommentDelete(request))
    
    def put(self, request):
        return setACAO(self.CommentLike(request))


# 评论回复API
class ReplyAPI(APIView):
    def RepliesList(self, request):
        try:
            cid = request.GET['cid']
            comment = Comment.objects.get(cid=cid)
            try:
                uid = request.GET['uid']
                user = User.objects.get(uid=uid)
            except:
                user = None
            try:
                page = int(request.GET['page'])
            except:
                page = 1
            try:
                size = int(request.GET['size'])
            except:
                size = 10
            # 按照时间顺序，获取前page*size个回复
            replies = Reply.objects.filter(comment=comment, status=True).order_by('pubtime')[(page-1)*size:page*size]
            # 如果replies为空，返回201
            if len(replies) == 0:
                return HttpResponse(status=201, content='No more replies.')
            data = []
            for reply in replies:
                # 判断当前用户是否点赞
                isLike = False
                if LikeReply.objects.filter(liker=user, reply=reply).exists():
                    isLike = True
                data.append({
                    'rid': reply.rid,
                    'content': reply.content,
                    'pubtime': reply.pubtime,
                    'likes': reply.likes,
                    'isLike': isLike,
                    'author': {
                        'uid': reply.author.uid,
                        'nickname': reply.author.nickname,
                        'avatar': reply.author.avatar,
                        'level': reply.author.getLevel()
                    }
                })
            return JsonResponse(data, safe=False)
        except Comment.DoesNotExist:
            return HttpResponse(status=404, content='Comment does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 发表回复
    def ReplyPublish(self, request):
        try:
            cid = request.POST['cid']
            comment = Comment.objects.get(cid=cid)
            uid = request.POST['uid']
            user = User.objects.get(uid=uid)
            # 过滤敏感词
            content = DFAfilter.filter_all(request.POST['content'])
            reply = Reply.objects.create(comment=comment, author=user, content=content)
            # 更新评论回复数
            comment.replys += 1
            comment.save()
            # 给评论作者增加经验
            comment.author.exp += 1
            comment.author.save()
            # 如果回复作者不是评论作者，则增加经验
            if comment.author.uid != user.uid:
                user.exp += 1
                user.save()
            data = {
                'rid': reply.rid,
                'content': reply.content,
                'pubtime': reply.pubtime,
                'likes': reply.likes,
                'isLike': False, # 发表回复时，当前用户未点赞，所以isLike为False
                'author': {
                    'uid': reply.author.uid,
                    'nickname': reply.author.nickname,
                    'avatar': reply.author.avatar,
                    'level': reply.author.getLevel()
                }
            }
            return JsonResponse(data)
        except Comment.DoesNotExist:
            return HttpResponse(status=404, content='Comment does not exist.')
        except User.DoesNotExist:
            return HttpResponse(status=403, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 删除回复
    def ReplyDelete(self, request):
        try:
            rid = request.POST['rid']
            reply = Reply.objects.get(rid=rid, status=True)
            # 更改回复状态
            reply.status = False
            reply.save()
            # 更新评论回复数
            comment = reply.comment
            comment.replys -= 1
            comment.save()
            return HttpResponse(status=204)
        except Reply.DoesNotExist:
            return HttpResponse(status=404)
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 点赞/取消点赞回复
    def ReplyLike(self, request):
        try:
            rid = request.POST['rid']
            reply = Reply.objects.get(rid=rid)
            uid = request.POST['uid']
            liker = User.objects.get(uid=uid)
            try:
                LikeR = LikeReply.objects.get(reply=reply, liker=liker)
                # 如果已经点赞，则取消点赞
                LikeR.delete()
                # 更新回复点赞数
                reply.likes -= 1
                reply.save()
                return HttpResponse(status=201, content='Cancel like.')
            except LikeReply.DoesNotExist:
                # 如果没有点赞，则点赞
                LikeReply.objects.create(reply=reply, liker=liker)
                # 更新回复点赞数
                reply = Reply.objects.get(rid=rid)
                reply.likes += 1
                reply.save()
                return HttpResponse(status=200, content='Like success.')
        except Reply.DoesNotExist:
            return HttpResponse(status=404, content='Reply does not exist.')
        except User.DoesNotExist:
            return HttpResponse(status=403, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    def get(self, request):
        return self.RepliesList(request)
    
    def post(self, request):
        return self.ReplyPublish(request)
    
    def delete(self, request):
        return self.ReplyDelete(request)
    
    def put(self, request):
        return self.ReplyLike(request)
    

# 点赞视频API
class LikeVideoAPI(APIView):
    # 点赞/取消点赞视频
    def VideoLike(self, request):
        try:
            vid = request.POST['vid']
            video = Video.objects.get(vid=vid)
            uid = request.POST['uid']
            liker = User.objects.get(uid=uid)
            try:
                LikeV = Like.objects.get(video=video, liker=liker)
                # 如果已经点赞，则取消点赞
                LikeV.delete()
                # 更新视频点赞数
                video.likes -= 1
                video.save()
                return HttpResponse(status=201, content='Cancel like.')
            except Like.DoesNotExist:
                # 如果没有点赞，则点赞
                Like.objects.create(video=video, liker=liker)
                # 更新视频点赞数
                video = Video.objects.get(vid=vid)
                video.likes += 1
                video.save()
                return HttpResponse(status=200, content='Like success.')
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 检查是否点赞视频
    def VideoLikeCheck(self, request):
        try:
            vid = request.GET['vid']
            video = Video.objects.get(vid=vid)
            uid = request.GET['uid']
            liker = User.objects.get(uid=uid)
            try:
                Like.objects.get(video=video, liker=liker)
                return HttpResponse(status=200, content='True')
            except Like.DoesNotExist:
                return HttpResponse(status=201, content='False')
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    def get(self, request):
        return self.VideoLikeCheck(request)
    
    def post(self, request):
        return self.VideoLike(request)
    

# 收藏视频API
class CollectVideoAPI(APIView):
    # 收藏/取消收藏视频
    def VideoCollect(self, request):
        try:
            vid = request.POST['vid']
            video = Video.objects.get(vid=vid)
            uid = request.POST['uid']
            collector = User.objects.get(uid=uid)
            try:
                Collection = Collect.objects.get(video=video, collector=collector)
                # 如果已经收藏，则取消收藏
                Collection.delete()
                # 更新视频收藏数
                video.collects -= 1
                video.save()
                return HttpResponse(status=201, content='Cancel collect.')
            except Collect.DoesNotExist:
                # 如果没有收藏，则收藏
                Collect.objects.create(video=video, collector=collector)
                # 更新视频收藏数
                video = Video.objects.get(vid=vid)
                video.collects += 1
                video.save()
                return HttpResponse(status=200, content='Collect success.')
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # 检查是否收藏视频
    def VideoCollectCheck(self, request):
        try:
            vid = request.GET['vid']
            video = Video.objects.get(vid=vid)
            uid = request.GET['uid']
            collector = User.objects.get(uid=uid)
            try:
                Collect.objects.get(video=video, collector=collector)
                return HttpResponse(status=200, content='True')
            except Collect.DoesNotExist:
                return HttpResponse(status=201, content='False')
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    def get(self, request):
        return setACAO(self.VideoCollectCheck(request))
    
    def post(self, request):
        return setACAO(self.VideoCollect(request))
    
# 收藏夹API
class CollectionAPI(APIView):
    def CollectionList(self, request):
        try:
            uid = request.GET['uid']
            user = User.objects.get(uid=uid)
            try:
                page = request.GET['page']
            except:
                page = 1
            try:
                size = request.GET['size']
            except:
                size = 10
            collections = Collect.objects.filter(user=user).order_by('-pubtime')[(page-1)*size:page*size]
            data = []
            for c in collections:
                data.append({
                    'cid': c.cid,
                    'video': {
                        'vid': c.video.vid,
                        'title': c.video.title,
                        'cover': c.video.cover,
                    },
                    'pubtime': c.pubtime,
                })
            return JsonResponse(data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)

    def get(self, request):
        return setACAO(self.CollectionList(request))

# 历史记录API
class HistoryAPI(APIView):
    # 获取历史记录
    def HistoryList(self, request):
        try:
            uid = request.GET['uid']
            user = User.objects.get(uid=uid)
            try:
                page = request.GET['page']
            except:
                page = 1
            try:
                size = request.GET['size']
            except:
                size = 10
            historys = History.objects.filter(user=user).order_by('-pubtime')[(page-1)*size:page*size]
            data = []
            for h in historys:
                data.append({
                    'hid': h.hid,
                    'video': {
                        'vid': h.video.vid,
                        'title': h.video.title,
                        'cover': h.video.cover,
                    },
                    'pubtime': h.pubtime,
                })
            return JsonResponse(data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
    
    # 删除历史记录
    def HistoryDelete(self, request):
        try:
            hid = request.POST['hid']
            history = History.objects.get(hid=hid)
            history.delete()
            return HttpResponse(status=204, content='Delete success.')
        except History.DoesNotExist:
            return HttpResponse(status=404, content='History does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    def get(self, request):
        return setACAO(self.HistoryList(request))
    
    def delete(self, request):
        return setACAO(self.HistoryDelete(request))
    

# 播放API
class PlayAPI(APIView):
    def PlayVideo(self, request):
        try:
            vid = request.POST['vid']
            video = Video.objects.get(vid=vid)
            video.play += 1
            video.save()
            # 作者经验值+3
            video.author.exp += 3
            video.author.save()
            try:
                user = User.objects.get(uid=request.POST['uid'])
                # 如果用户曾经播放过该视频，则更新播放时间
                try:
                    history = History.objects.get(user=user, video=video)
                    from datetime import datetime
                    history.pubtime = datetime.now()
                    history.save()
                    user.exp += 1
                    user.save()
                # 如果用户没有播放过该视频，则创建历史记录
                except History.DoesNotExist:
                    History.objects.create(user=user, video=video)
                    user.exp += 2
                    user.save()
            # 如果用户未登录，则不记录历史记录
            except:
                pass
            return HttpResponse(status=200, content='Play success.')
        except Video.DoesNotExist:
            return HttpResponse(status=404, content='Video does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    def post(self, request):
        return setACAO(self.PlayVideo(request))
