import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_1og.settings")

import django

django.setup()

from Mainapp.models import topic, Entry

topics = topic.objects.all()

for topic in topics:
    print(topic.id, topic)

t = topic.__class__.objects.get(id=1)

print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for entry in entries:
    print(entry)
