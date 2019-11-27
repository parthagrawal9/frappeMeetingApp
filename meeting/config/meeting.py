from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Meeting"),
            "icon": "octicon octicon-briefcase",
			"items":[
				{
					"type": "doctype",
					"name": "meeting",
                    "label": _("First app"),
					"description": _("Test")
				}
            ]
        }
    ]