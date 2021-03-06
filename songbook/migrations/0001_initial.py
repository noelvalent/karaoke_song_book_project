# Generated by Django 3.0.5 on 2020-04-21 15:45

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumArtImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='앨범 아트 이름', max_length=100)),
                ('image', models.ImageField(help_text='앨범아트 이미지 파일', null=True, upload_to='img/album_arts')),
            ],
        ),
        migrations.CreateModel(
            name='SongGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(help_text='그룹 이름 (애니메이션 제목/보컬로이드)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name_origin', models.CharField(help_text='노래 제목 (일본어)', max_length=100)),
                ('song_name_korean', models.CharField(help_text='노래 제목 (한국어)', max_length=100)),
                ('singer', models.CharField(help_text='가수(프로듀서)', max_length=20)),
                ('tj', models.CharField(help_text='TJ 노래방 번호', max_length=8, null=True)),
                ('ky', models.CharField(help_text='KY 노래방 번호', max_length=8, null=True)),
                ('dam', models.CharField(help_text='DAM 노래방 번호', max_length=8, null=True)),
                ('uga', models.CharField(help_text='UGA 노래방 번호', max_length=8, null=True)),
                ('joy', models.CharField(help_text='Joy Sounds 노래방 번호', max_length=8, null=True)),
                ('lyrics', models.TextField(help_text='가사', null=True)),
                ('view_count', models.IntegerField(default=0, help_text='검색 횟수')),
                ('album_art', models.ForeignKey(help_text='앨범아트', on_delete=django.db.models.deletion.CASCADE, to='songbook.AlbumArtImage')),
                ('group', models.ForeignKey(help_text='그룹 (애니메이션 제목/보컬로이드)', on_delete=django.db.models.deletion.CASCADE, to='songbook.SongGroup')),
            ],
        ),
        migrations.CreateModel(
            name='VocaloidSong',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('songbook.song',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
