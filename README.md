Project 루트에 .env 파일을 만들어서 아래와 같이 정의하세요. 

```
CHATGPT_API_KEY='나의API키'
```


Celery 실행 시 명령어

```
# windows
celery -A config worker --pool=solo -l info
```

```
# Linux
celery -A config worker -l info
```