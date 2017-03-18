from django_cron import CronJobBase, Schedule
from users.models import InterviewSlot
from django.utils import timezone

class InterviewSlotCronJob(CronJobBase):
	#RUN_AT_TIMES = ['00:00']
	RUN_EVERY_MINS = 1000

	#schedule = Schedule(run_at_times=RUN_AT_TIMES)
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'website.interview_slot_cron_job'

	def do(self):
		now  = timezone.now()
		now = now.replace(hour=0)
		now = now.replace(minute=0)
		now = now.replace(second=0)
		yesterday = now - timezone.timedelta(days=1)
		old_slots = InterviewSlot.objects.all().filter(date__lt=now)	
		for slot in old_slots:
			slot.student = ""
			slot.student_email = ""
			slot.availability = True
			date = yesterday + timezone.timedelta(days=14)
			slot.date = date
			slot.save()

			