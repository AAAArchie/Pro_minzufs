from django.contrib.auth.models import User
from django.db import models
from users.models import UserProfile


# 数据模型
class ImagesPost(models.Model):
    # 设置null=True，则仅表示在数据库中该字段可以为空，但使用后台管理添加数据时仍然要需要输入值，因为Django自动做了数据验证不允许字段为空
    # 如果想要在Django中也可以将字段保存为空值，则需要添加另一个参数：blank=True
    # related_name可以支持 user.images_posted 直接获取一个用户的所有照片的queryset
    # 这里允许空值，因为空值可以代表用户未登录
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='images_posted',
                             null=True, blank=True, default=None)

    upload_images = models.ImageField(upload_to='upload_images')  # 应该用单数
    nation1 = models.CharField(max_length=20, null=True, blank=True)
    nation2 = models.CharField(max_length=20, null=True, blank=True)
    nation3 = models.CharField(max_length=20, null=True, blank=True)
    modified_nation = models.CharField(max_length=20, null=True, blank=True)
    time_consuming = models.CharField(max_length=50, null=True, blank=True)

    # 以下为用户意见提交，无需展示到界面
    user_assess = models.CharField(max_length=50, null=True, blank=True, default='未填写')  # 用户满意程度
    user_update = models.CharField(max_length=50, null=True, blank=True, default='未修改')  # 用户更新的民族种类

    # is_changed is better
    # 其他字段都可以加一加verbose_name
    user_change = models.CharField(max_length=20, null=True, blank=True, default='否')  # 用户是否修改（不提交到前台显示）
    user_propose = models.TextField(max_length=50, null=True, blank=True, default='未填写')  # 用户建议（不提交到前台显示）
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        # 模型元数据是“任何不是字段的东西”，例如排序选项(ordering)、数据库表名(db_table)
        # 或人类可读的单复数名称(verbose_name and verbose_name_plural)。
        # 不需要，并且添加到模型是完全可选的。
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 带有可选的“-”前缀，表示降序。没有前导“-”的字段将按升序排列。使用字符串“？” 随机订购。
        ordering = ('-created',)
        verbose_name = '识别结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.title 将文章标题返回  __str__魔法方法，自己定义 输出打印对象时候的返回值
        return str(self.id)
