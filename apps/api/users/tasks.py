from celery import shared_task


@shared_task
def count_pathname(path):
    words = [word.strip() for word in path.split('/')]
    print('------------------------ words: ',words,'------------------------')
    print('------------------------ count: ',len(words),'------------------------')