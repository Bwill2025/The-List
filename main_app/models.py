from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('task_list')
class Selecting(models.Model):
    date = models.DateField('Priority Date')
    choice = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_CHOICES[0][0]
        )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_choice_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']        