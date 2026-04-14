app_name = "erpnext_custom_theme"
app_title = "ERPNext Custom Theme"
app_publisher = "Custom"
app_description = "Custom theme for ERPNext based on ThemeRef styling"
app_icon = "fa fa-paint-brush"
app_color = "#0891b2"
app_email = "custom@example.com"
app_version = "0.0.1"
app_license = "MIT"
is_frappe_app = True

# Website CSS injection - loads Google Fonts and theme CSS
website_context = {
    "add_head_html": """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    <link type="text/css" rel="stylesheet" href="/assets/erpnext_custom_theme/css/theme.css">
    """
}
