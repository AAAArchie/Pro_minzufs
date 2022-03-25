import os
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import mixins, exceptions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

from users.models import UserProfile
from .models import ImagesPost
from .rename import BatchRename
from .serializer import ImagesPostLogSerializerV2


class ImagesPostViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = ImagesPost.objects.all()
    serializer_class = ImagesPostLogSerializerV2
    permission_classes = [AllowAny]
    # 让DRF可以识别图片，解析器
    # 解析器的作用就是服务端接收客户端传过来的数据，把数据解析成自己想要的数据类型的过程。本质就是对请求体中的数据进行解析。
    # 就是拿到请求的ContentType来判断前端给我的数据类型是什么，然后我们去拿相应的解析器去解析数据。
    parser_classes = [JSONParser, FormParser, MultiPartParser, FileUploadParser]

    # queryset-应该用于从该视图返回对象的查询集。通常，您必须设置此属性或重写get_queryset()方法。
    # 如果要覆盖视图方法，则应进行调用get_queryset()而不是直接访问此属性，这一点很重要，
    # 因为queryset它将被评估一次，并且这些结果将被缓存用于所有后续请求，这一点很重要
    def get_queryset(self):
        user: UserProfile = self.request.user
        if isinstance(user, AnonymousUser):
            return ImagesPost.objects.filter(user__isnull=True)
        return ImagesPost.objects.filter(user=user).all()

    def perform_create(self, serializer: ImagesPostLogSerializerV2):
        """
        创建一张照片，并进行识别
        """
        super(ImagesPostViewSet, self).perform_create(serializer)
        # 变量名后面的冒号是：类型注解，3.6 以后加入的，冒号右边是类型，仅仅是注释，有些鸡肋。
        # 变量注释的语法：注释变量类型, 明确指出变量类型，方便帮助复杂案例中的类型推断。
        # instance: ImagesPost = serializer.instance
        # 本质如下:
        # instance = serializer.instance   type就是var期望的类型
        instance: ImagesPost = serializer.instance
        instance.user = None if isinstance(self.request.user, AnonymousUser) else self.request.user
        # 获取IP地址
        if self.request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = self.request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = self.request.META.get("REMOTE_ADDR")
        print("ip : ", ip)
        print(self.request.data.dict())
        print(self.request)
        print(111111111111111)
        # 实例化重命名BatchRename()模块  运行predict.py与rename.py
        batch_rename = BatchRename()
        # 提取相应的返回值
        nation1, nation2, nation3, dst, time_consuming = batch_rename.rename()
        # dst：图片重新分类后保存的路径  new_url 截取的相对路径
        instance.upload_images = os.path.relpath(dst, settings.MEDIA_ROOT)
        # 类别
        instance.nation1 = nation1
        instance.nation2 = nation2
        instance.nation3 = nation3
        instance.time_consuming = time_consuming  # 耗费的时间
        instance.save()

    # 前端通过/images/23/change_nation可以调用这个方法
    # 使用action装饰器
    # methods，支持的请求方式，为一个列表，默认为[‘get’]
    # detail，必传参数，要处理的是否是详情资源对象（即是否通过url路径获取主键），True表示需要传递主键id，使用通过URL获取的主键对应的数据对象，False表示不需要传递主键id，不使用URL获取主键
    # url_path，指定url路由名称，默认为action名称
    # url_name，指定url的名称，默认为action名称

    # 修改民族类别 @action 额外的路由方法（drf视图集）
    @action(detail=True, url_path='change-nation', url_name='change-nation', methods=['GET'])
    def change_nation(self, request: Request, pk: str):
        instance: ImagesPost = self.get_object()
        try:
            # 获取字段名字
            name = request.query_params['name']
            print(name)
            print(request)

        except MultiValueDictKeyError:
            raise exceptions.ValidationError('参数name不存在')
        instance.modified_nation = name
        instance.save()
        return self.retrieve(request)

    # 用户提交建议
    @action(detail=True, url_path='user-assess', url_name='user-assess', methods=['GET'])
    def user_assess(self, request: Request, pk: str):
        instance: ImagesPost = self.get_object()
        try:
            name = request.query_params['assess']
            print(name)

        except MultiValueDictKeyError:
            raise exceptions.ValidationError('参数name不存在')
        instance.user_assess = name
        instance.save()
        return self.retrieve(request)
