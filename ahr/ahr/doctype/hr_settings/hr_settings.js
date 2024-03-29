// Copyright (c) 2020, AFS and contributors
// For license information, please see license.txt

frappe.ui.form.on('HR Settings', {
	encrypt_salary_slips_in_emails: function(frm) {
		let encrypt_state = frm.doc.encrypt_salary_slips_in_emails;
		frm.set_df_property('password_policy', 'reqd', encrypt_state);
	},

	validate: function(frm) {
		let policy = frm.doc.password_policy;
		if (policy) {
			if (policy.includes(' ') || policy.includes('--')) {
				frappe.msgprint(__("Password policy cannot contain spaces or simultaneous hyphens. The format will be restructured automatically"));
			}
			frm.set_value('password_policy', policy.split(new RegExp(" |-", 'g')).filter((token) => token).join('-'));
		}
	},

	restrict_backdated_leave_application: function(frm) {
		frm.toggle_reqd("role_allowed_to_create_backdated_leave_application", frm.doc.restrict_backdated_leave_application);
	}
});
