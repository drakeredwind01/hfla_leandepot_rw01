from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='permissions')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='permissions')

    class Meta:
        # This prevents the same member from having the same 
        # permission name twice on the same project.
        unique_together = ('name', 'project', 'member')
        
    def __str__(self):
        return f"{self.name}: {self.member} on {self.project}"
