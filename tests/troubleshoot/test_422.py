import pytest
from playwright.sync_api import Page
from qase.pytest import qase


@qase.id(8528)
@qase.title("Example Playwright System Test")
@qase.fields(
    ("layer", "ui"),
    ("type", "functional"),
    ("behavior", "positive"),
    ("description", "This is an example Playwright system test."),
)
def test_google_search(page: Page):
    """
    Test function to verify that the Google search page loads correctly.
    """
    # Navigate to Google
    page.goto("https://www.google.com")

    # Get the page title
    page_title = page.title()

    # Verify the page title is "Google"
    assert page_title == "Google"
