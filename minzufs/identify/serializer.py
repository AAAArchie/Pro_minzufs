from rest_framework import serializers

from identify.models import ImagesPost as ImagesPostLog


class ImagesPostLogSerializerV2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.SlugRelatedField('username', read_only=True)
    nation1 = serializers.CharField(read_only=True)
    nation2 = serializers.CharField(read_only=True)
    nation3 = serializers.CharField(read_only=True)
    modified_nation = serializers.CharField(read_only=True)
    upload_images = serializers.ImageField()
    time_consuming = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ImagesPostLog
        fields = ["id", "user", "upload_images", "nation1", "nation2", "nation3", 'modified_nation', "time_consuming",
                  "created", 'modified']
