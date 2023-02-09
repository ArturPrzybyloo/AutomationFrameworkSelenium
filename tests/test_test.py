class TestSearch:
    def test_search_multiple_results(self, driver):
        """ Tests search for specific word and verify results"""
        driver.get("https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/")
        print(driver.title)