from celery import shared_task
#  sudo service redis-server restart
# celery -A core worker -l info -P gevent

@shared_task
def my_task():
    print("heyy re-------------------------")
    for i in range(10):
        print("celery task", i)