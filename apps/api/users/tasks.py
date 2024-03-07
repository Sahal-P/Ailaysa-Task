from celery import shared_task


@shared_task
def count_pathname(path):
    """
    Task to count the number of path components in a given path.

    Args:
        path (str): The path string to be processed.

    Returns:
        int: The number of path components in the given path.
    """
    words = [word.strip() for word in path.split('/')]
    print('------------------------ words: ',words,'------------------------')
    print('------------------------ count: ',len(words),'------------------------')