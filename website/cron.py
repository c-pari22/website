from django_cron import CronJobBase, Schedule
from users.models import InterviewSlot
from django.utils import timezone

class InterviewSlotCronJob(CronJobBase):
	RUN_AT_TIMES = ['00:01']
	#RUN_EVERY_MINS = 1

	schedule = Schedule(run_at_times=RUN_AT_TIMES)
	#schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'website.interview_slot_cron_job'

	def do(self):
		print("Ran Job!")
		now  = timezone.now()
		yesterday = now - timezone.timedelta(days=1)
		old_slots = InterviewSlot.objects.all().filter(date < now)		
		for slot in old_slots:
			print("Old Slot")
			slot.student = ""
			slot.student_email = ""
			slot.availability = True
			slot.date = yesterday + timezone.timedelta(days=6)
			slot.save()

			