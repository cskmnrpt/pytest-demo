from qase.pytest import qase


class Suite:

    @qase.step("Go to login page", expected="Expected result text")
    def go_to_login_page(self):
        self.verify_page_loading()

    @qase.step("Verify page loading")
    def verify_page_loading(self):
        assert True, "Page loaded successfully"

    @qase.step("Fill the required fields")
    def fill_the_required_fields(self):
        self.fill_username()
        self.fill_password()

    @qase.step("Fill username")
    def fill_username(self):
        assert True, "Username filled"

    @qase.step("Fill password")
    def fill_password(self):
        assert True, "Password filled"

    @qase.step("Click the login button", expected="Expected result text")
    def click_login_button(self):
        assert True, "Login button clicked"

    @qase.step("Verify the landing page header")
    def verify_landing_page_header(self):
        header_text = "Welcome, User!"
        assert header_text == "Welcome, User!", "Header text is incorrect"

    @qase.title("Testing if expected result field can be create from code")
    def test_login_flow(self):
        self.go_to_login_page()
        self.fill_the_required_fields()
        self.click_login_button()
        self.verify_landing_page_header()


class TestDeleteProject:

    @qase.title("Random test 34325")
    def test_delete_project(self):
        """
        Using the 'with' syntax.
        """
        with qase.step("Action updated", expected="result text"):
            self.verify_page_loading()

        with qase.step("Select the project to delete"):
            self.click_delete_button()

        with qase.step("Click the delete button"):
            assert True, "Delete button clicked"

        with qase.step("Action text", expected="Expected result text"):
            assert True, "Project deletion confirmed"

        with qase.step("Verify the project was deleted"):
            self.verify_project_deleted()

    def verify_page_loading(self):
        assert True, "Projects page loaded successfully"

    def click_delete_button(self):
        assert True, "Delete button clicked"

    def verify_project_deleted(self):
        assert True, "Project deleted successfully"
