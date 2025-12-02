from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input').fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input').fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input').fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button').click()

    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text('Dashboard')
