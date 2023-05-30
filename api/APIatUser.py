from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from .models import *
from .DFA import DFA

DFAfilter = DFA()

def setACAO(response):
    response['Access-Control-Allow-Origin'] = '*' # 允许所有源
    return response

# 用户信息API
class UserAPI(APIView):
    # 获取用户信息
    def UserIform(self, request):
        try:
            uid = request.GET['uid']
            user = User.objects.get(uid=uid)
            data = {
                'uid': user.uid,
                'username': user.username,
                'nickname': user.nickname,
                'avatar': user.avatar,
                'signature': user.signature,
                'fans': user.fans,
                'follow': user.follow,
                'exp': user.exp,
                'level': user.getLevel()
            }
            print(data)
            return JsonResponse(data)
        except User.DoesNotExist:
            return HttpResponse(status=404, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
    
    # 修改用户信息
    def UserModify(self, request):
        try:
            uid = request.POST['uid']
            if DFAfilter.exists(request.POST['nickname']) or DFAfilter.exists(request.POST['signature']):
                return HttpResponse(status=403, content='Nickname or signature contains sensitive words.')
            user = User.objects.get(uid=uid)
            try:
                user.nickname = request.POST['nickname']
            except:
                pass
            try:
                user.avatar = request.POST['avatar']
            except:
                pass
            try:
                user.signature = request.POST['signature']
            except:
                pass
            user.save()
            data = {
                'uid': user.uid,
                'username': user.username,
                'nickname': user.nickname,
                'avatar': user.avatar,
                'signature': user.signature,
                'fans': user.fans,
                'follow': user.follow,
                'exp': user.exp,
                'level': user.getLevel()
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return HttpResponse(status=404, content='User does not exist.')
        except Exception as e:
            return HttpResponse(status=400, content=e)
        
    # get请求获取用户信息，post请求修改用户信息
    def get(self, request):
        return setACAO(self.UserIform(request))
    def post(self, request):
        return setACAO(self.UserModify(request))


# 登录功能API
class LoginAPI(APIView):
    # 登录检验
    def login(self, request):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.get(username=username)
            if user.password != password:
                return HttpResponse(status=403, content="Wrong Password")
            data = {
                'uid': user.uid,
                'username': user.username,
                'nickname': user.nickname,
                'avatar': user.avatar,
                'signature': user.signature,
                'fans': user.fans,
                'follow': user.follow,
                'exp': user.exp,
                'level': user.getLevel()
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return HttpResponse(status=404, content="User Not Found")
        except:
            return HttpResponse(status=400, content="Bad Request")
        
    # post请求为登录
    def post(self, request):
        return setACAO(self.login(request))
    

# 注册功能API
class RegisterAPI(APIView):
    # 注册
    def register(self, request):
        try:
            username = request.POST['username']
            password = request.POST['password']
            nickname = request.POST['nickname']
            avatar = request.POST['avatar']
            if DFAfilter.exists(username) or DFAfilter.exists(nickname):
                return HttpResponse(status=403, content='Username or nickname contains sensitive words.')
            user = User.objects.create(username=username, 
                                    password=password, 
                                    nickname=nickname, 
                                    avatar=avatar, 
                                    signature="", fans=0, 
                                    follow=0, exp=0)
            data = {
                'uid': user.uid,
                'username': user.username,
                'nickname': user.nickname,
                'avatar': user.avatar,
                'signature': user.signature,
                'fans': user.fans,
                'follow': user.follow,
                'exp': user.exp,
                'level': user.getLevel()
            }
            return JsonResponse(data)
        except:
            return HttpResponse(status=400, content="Bad Request")
        
    # 检查用户名是否存在
    def checkUsername(self, request):
        try:
            username = request.GET['username']
            user = User.objects.get(username=username)
            return HttpResponse(status=402, content="Username Exists")
        except User.DoesNotExist:
            return HttpResponse(status=200, content="Username Not Exists")
        except Exception as e:
            return HttpResponse(status=400, content=e)

    # post请求为注册，get请求为检查用户名是否存在
    def post(self, request):
        return setACAO(self.register(request))
    def get(self, request):
        return setACAO(self.checkUsername(request))


# 关注功能API
class FollowAPI(APIView):
    # 关注
    def follow(self, request):
        try:
            ider = request.POST['follower']
            ided = request.POST['followed']
            if ider == ided:
                return HttpResponse(status=403, content="Can't Follow Yourself")
            follower = User.objects.get(uid=ider)
            followed = User.objects.get(uid=ided)
            # 检查是否已关注，若已关注则取消关注
            follow, created = Follow.objects.get_or_create(follower=follower, followed=followed)
            if created:
                follower.follow += 1
                followed.fans += 1
                follower.save()
                followed.save()
                return HttpResponse(status=200, content="Follow Success")
            else:
                follow.delete()
                follower.follow -= 1
                followed.fans -= 1
                follower.save()
                followed.save()
                return HttpResponse(status=201, content="Unfollow Success")
        except User.DoesNotExist:
            return HttpResponse(status=404, content="User Not Found")
        except:
            return HttpResponse(status=400, content="Bad Request")

    # 获取关注列表
    def getFollowlist(self, request):
        try:
            follower = User.objects.get(uid=request.GET['uid'])
            followList = Follow.objects.filter(follower=follower)
            data = []
            for follow in followList:
                user = User.objects.get(uid=follow.followed.uid)
                data.append({
                    'uid': user.uid,
                    'nickname': user.nickname,
                    'avatar': user.avatar,
                    'signature': user.signature
                })
            return JsonResponse(data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404, content="User Not Found")
    
    # get请求为获取关注列表，post请求为关注
    def get(self, request):
        return setACAO(self.getFollowlist(request))
    def post(self, request):
        return setACAO(self.follow(request))
    
    
# 粉丝列表API
class FansAPI(APIView):
    # 获取粉丝列表
    def getFanslist(self, request):
        try:
            followed = User.objects.get(uid=request.GET['uid'])
            fansList = Follow.objects.filter(followed=followed)
            data = []
            for fans in fansList:
                user = User.objects.get(uid=fans.follower.uid)
                data.append({
                    'uid': user.uid,
                    'nickname': user.nickname,
                    'avatar': user.avatar,
                    'signature': user.signature
                })
            return JsonResponse(data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404, content="User Not Found")
    
    # get请求为获取粉丝列表
    def get(self, request):
        return setACAO(self.getFanslist(request))

