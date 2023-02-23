from . import __version__ as app_version

app_name = "ars_usd_addon"
app_title = "Ars Usd Addon"
app_publisher = "IT-IEA"
app_description = "Conversor connected to DolarSi API (https://www.dolarsi.com/api/api.php?type=dolar)"
app_email = "it@iea.com.ar"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ars_usd_addon/css/ars_usd_addon.css"
# app_include_js = "/assets/ars_usd_addon/js/ars_usd_addon.js"

# include js, css files in header of web template
# web_include_css = "/assets/ars_usd_addon/css/ars_usd_addon.css"
# web_include_js = "/assets/ars_usd_addon/js/ars_usd_addon.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ars_usd_addon/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Item" : "public/js/ars_to_usd.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ars_usd_addon.utils.jinja_methods",
#	"filters": "ars_usd_addon.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ars_usd_addon.install.before_install"
# after_install = "ars_usd_addon.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ars_usd_addon.uninstall.before_uninstall"
# after_uninstall = "ars_usd_addon.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ars_usd_addon.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ars_usd_addon.tasks.all"
#	],
#	"daily": [
#		"ars_usd_addon.tasks.daily"
#	],
#	"hourly": [
#		"ars_usd_addon.tasks.hourly"
#	],
#	"weekly": [
#		"ars_usd_addon.tasks.weekly"
#	],
#	"monthly": [
#		"ars_usd_addon.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ars_usd_addon.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ars_usd_addon.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ars_usd_addon.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ars_usd_addon.utils.before_request"]
# after_request = ["ars_usd_addon.utils.after_request"]

# Job Events
# ----------
# before_job = ["ars_usd_addon.utils.before_job"]
# after_job = ["ars_usd_addon.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ars_usd_addon.auth.validate"
# ]
