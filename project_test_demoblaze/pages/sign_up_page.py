from selene import browser, be

class SignUpPage:
    def submit_registration(self):
        modal = browser.element('#signInModal')
        modal.should(be.visible)
        modal.element('button.btn.btn-primary').should(be.visible).click()