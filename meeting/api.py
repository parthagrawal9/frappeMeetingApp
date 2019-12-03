import frappe 
from frappe import _
@frappe.whitelist()
def send_invitation_mails(meeting):
    meeting = frappe.get_doc("meeting",meeting)
    meeting.check_permission("email")
    if meeting.status == "Planned":
        frappe.sendmail(
            recipients=[d.attendee for d in meeting.attendee],
            sender=frappe.session.user,
            subject=meeting.title,
            message=meeting.invitation_message
        )

        meeting.status = "Invitation Sent"
        meeting.save()
        
        frappe.msgprint(_("Invitation Sent!"))
    
    else:
        frappe.msgprint(_("Status should be Planning!"))

# Test API

@frappe.whitelist(allow_guest=True)
def get_hi():
    return "Hello"

@frappe.whitelist(allow_guest=True)
def get_hi_name(name):
    return name

@frappe.whitelist(allow_guest=True)
def get_add(n1,n2):
    return int(n1)+int(n2)

@frappe.whitelist(allow_guest=True)
def get_meeting(meeting):
    return frappe.get_doc('meeting',meeting)

@frappe.whitelist(allow_guest=True)
def get_meeting_all():
    return frappe.get_doc('meeting')