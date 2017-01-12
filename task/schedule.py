from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler


def schedule(id, func, start_date):
    # url = "sqlite:///task.sqlite"

    scheduler = BackgroundScheduler(daemonic=False)
    # scheduler.add_jobstore("sqlalchemy", url=url)
    scheduler.add_job(func, "interval", seconds=1, id=id, start_date=start_date)
    scheduler.start()
    return scheduler


def stop_schedule(scheduler, id):
    print scheduler
    if not scheduler:
        return False
    try:
        scheduler.remove_job(id)
        return True
    except JobLookupError, e:
        print e.message
        return False
