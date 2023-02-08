class TestSearch:
    def test_search_multiple_results(self, driver):
        """ Tests search for specific word and verify results"""
        driver.get("www.goolgle.pl")