from apscheduler.jobstores.base import JobLookupError

from apscheduler.schedulers.background import BackgroundScheduler


def schedule(id, func, task, start_date):
    # url = "sqlite:///task.sqlite"
    if not task:
        scheduler = BackgroundScheduler(daemonic=False)
        # scheduler.add_jobstore("sqlalchemy", url=url)
        scheduler.add_job(func, "interval", hours=24, id=id, start_date=start_date)
        scheduler.start()
        # saveOrderInfo()
        print "yes"
        return scheduler
    else:
        return False


def stop_schedule(scheduler):
    print scheduler
    if not scheduler:
        return False
    try:
        scheduler.remove_job("name")
        return True
    except JobLookupError, e:
        print e.message
        return False
