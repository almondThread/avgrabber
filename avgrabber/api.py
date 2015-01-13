# -*- coding: utf-8 -*-
from avgrabber import core


def update_project(project):
    ads = core.update_project(project)
    lines = []
    for ad in ads:
        lines.append(ad.to_dict())
    return lines


def list_projects():
    projects = core.list_projects()
    lines = []
    for project in projects:
        lines.append(project.to_dict())
    return lines


def new_project(name, query):
    project = core.new_project(name, query)
    return project.to_dict()


def list_updates(project):
    updates = core.list_updates(project)
    lines = []
    for update in updates:
        lines.append(update.to_dict())
    return lines