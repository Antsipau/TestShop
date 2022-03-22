import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        for index in range(12):
            homepage_nav.get_nav_links()[index].click()

        actual_links = homepage_nav.get_nav_links_text()
        print(actual_links)
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, "Validating Nav Links text"
