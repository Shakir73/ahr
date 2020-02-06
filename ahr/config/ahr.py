from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Employee"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Employee",
              "label": _("Employee"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Employment Type",
              "label": _("Employment Type"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Branch",
              "label": _("Branch"),
              "description": _("Articles which members issue and return."),
            },

            {
              "type": "doctype",
              "name": "Department",
              "label": _("Department"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Designation",
              "label": _("Designation"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Employee Grade",
              "label": _("Employee Grade"),
              "description": _("Articles which members issue and return."),
            },

          ]
      },

      {
        "label":_("Leave"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Leave Policy",
              "label": _("Leave Policy"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Leave Type",
              "label": _("Leave Type"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Holiday List",
              "label": _("Holiday List"),
              "description": _("Articles which members issue and return."),
            },

          ]
      },

      {
        "label":_("Recruitment"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Job Opening",
              "label": _("Job Opening"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Job Applicant",
              "label": _("Job Applicant"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Staffing Plan",
              "label": _("Staffing Plan"),
              "description": _("Articles which members issue and return."),
            },

          ]
      },

      {
        "label":_("Settings"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "HR Settings",
              "label": _("HR Settings"),
              "description": _("Articles which members issue and return."),
            },
            # {
            #   "type": "doctype",
            #   "name": "Holiday List",
            #   "label": _("Holiday List"),
            #   "description": _("Articles which members issue and return."),
            # },

          ]
      },
      
  ]