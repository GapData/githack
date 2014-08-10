import os
from uuid import uuid4
from django.utils.text import slugify

import threading

# Send emails asynchronously
class EmailThread(threading.Thread):
    def __init__(self, msg):
        self.msg = msg
        threading.Thread.__init__(self)

    def run (self):
        self.msg.send(fail_silently=True)

def send_async_mail(msg, *args, **kwargs):
    EmailThread(msg).start()


def path_and_rename(path, type):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        rstring = uuid4().get_hex()
        fname = slugify(unicode(rstring) + u'_' + type) + "." + ext

        return os.path.join(path, fname)
    return wrapper

# Experience is based on what is expected for users to achieve in 1 year.
# With these formulas, a programmer would be expected to:
#       >  14,160 minute
#       >  106,200 LOC
#
# With this said, this is based in the following calculation
#    time = 5*level*1.6
#    loc = 30*level*2
#
# The experience required itself will be:
#   experience =

def experience_required(level):
    return int(60*1.2**level)

#def time_loc_required(level):
#    time = 4*level
#    loc = 30*level


def calculate_experience(level, linesadded, linesremoved, time, inputsessions):
#    return int(min(linesadded+linesremoved, time*7.5)*1.2**(level-1))
    return int((linesadded+linesremoved)*1.2**(level-1))


def check_badges(user):

    from githack.models import Badges

    all_badges = []

    def badges_1():
        try:
            print "trying 1"
            print user.gitscore.level
            print Badges.objects.filter(value__lt=user.gitscore.level).order_by('-value')
            closest_badge = Badges.objects.filter(type=1, value__lt=user.gitscore.level).order_by('-value')[0]
            print closest_badge
            if user.gitscore.badges.filter(id=closest_badge.id).exists():
                all_badges.append(closest_badge)
        except:
            pass

    def badges_2():
        try:
            print "trying 2"
            print user.gitscore.totalloc
            print Badges.objects.filter(value__lt=user.gitscore.totalloc).order_by('-value')
            closest_badge = Badges.objects.filter(value__lt=user.gitscore.totalloc).order_by('-value')[0]
            print closest_badge
            if user.gitscore.badges.filter(id=closest_badge.id).exists():
                all_badges.append(closest_badge)
        except:
            pass

    def badges_3():
        try:
            print "trying 3"
            print user.gitscore.totaltime
            print Badges.objects.filter(value__lt=user.gitscore.totaltime).order_by('-value')
            closest_badge = Badges.objects.filter(value__lt=user.gitscore.totaltime).order_by('-value')[0]
            print closest_badge
            if user.gitscore.badges.filter(id=closest_badge.id).exists():
                all_badges.append(closest_badge)
        except:
            pass

    def badges_4():
        try:
            print "trying 4"
            print user.gitscore.totalcommits
            print Badges.objects.filter(value__lt=user.gitscore.totalcommits).order_by('-value')
            closest_badge = Badges.objects.filter(value__lt=user.gitscore.totalcommits).order_by('-value')[0]
            print closest_badge
            if user.gitscore.badges.filter(id=closest_badge.id).exists():
                all_badges.append(closest_badge)
        except:
            pass

    badges_1()
    badges_2()
    badges_3()
    badges_4()
    return all_badges



