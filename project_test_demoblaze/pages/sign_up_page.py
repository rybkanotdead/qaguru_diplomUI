from selene import browser, be


class SignUpPage:
    @staticmethod
    def submit_registration():
        modal = browser.element("#signInModal")
        modal.should(be.visible)
        modal.element("button.btn.btn-primary").should(be.visible).click()
