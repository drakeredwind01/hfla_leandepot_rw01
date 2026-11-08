from django.shortcuts import get_object_or_404, render

from .models import Member, Permission, Project


def home(request):
    return render(request, 'projects/home.html')


def org_projects_members_permissions(request):
    projects = Project.objects.all()
    return render(request, 'projects/org_pmp.html', {'projects': projects})


def org_projects_permissions_members(request):
    projects = Project.objects.all()
    return render(request, 'projects/org_ppm.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    permissions = Permission.objects.filter(project=project).select_related('member')
    return render(request, 'projects/project_detail.html', {'project': project, 'permissions': permissions})


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    permissions = Permission.objects.filter(member=member).select_related('project')
    return render(request, 'projects/member_detail.html', {'member': member, 'permissions': permissions})


def permission_detail(request, pk):
    permission = get_object_or_404(Permission, pk=pk)
    return render(request, 'projects/permission_detail.html', {'permission': permission})
