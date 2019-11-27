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