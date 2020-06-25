import pytest

from google_patent_scraper import scraper_class

patset1 = [
    "US6180917_B1",
    "US2018168802_A1",
    "US2005095074_A1",
    "US2015139587_A1",
    "US2018108568_A1",
    "US2017133817_A1",
    "US9276456_B2",
    "US2009007675_A1",
    "US9927638_B2",
    "US10090633_B2",
    "US2013114285_A1",
    "US2015192778_A1",
    "US9985408_B2",
    "US2006102603_A1",
    "US2015205136_A1",
    "US2017211915_A1",
    "US2017199359_A1",
    "US2015185485_A1",
    "US9897787_B2",
    "US10162151_B2",
]

patset2 = [
    "US5873931_A",
    "US2008271737_A1",
    "US2017209308_A1",
    "US2014196187_A1",
    "US2014196200_A1",
    "US2016316831_A1",
    "US4312338_A",
    "US2018160749_A1",
    "US2008290081_A1",
    "US5813398_A",
    "US6988500_B1",
    "US5584078_A",
    "US4821340_A",
    "US2011079225_A1",
    "US2002023651_A1",
    "US2004084048_A1",
    "US2009014006_A1",
    "US2012160246_A1",
    "US4944293_A",
    "US5842470_A",
]

patset3 = [
    "US7243765_B2",
    "US7334667_B2",
    "US7841437_B2",
    "US7264251_B2",
    "US9688305_B2",
    "US6763905_B2",
    "US6250649_B1",
    "US7274164_B2",
    "US7073806_B2",
    "US7467802_B2",
    "US5765846_A",
    "US7568541_B2",
    "US4351410_A",
    "US7571787_B2",
    "US7591337_B2",
    "US7562885_B2",
    "US7665742_B2",
    "US8070172_B1",
    "US8286978_B2",
    "US8641064_B2",
]


@pytest.mark.slow()
def test_cluster_patents():
    scraper = scraper_class()
    for patset in (patset1, patset2, patset3):
        for pat in patset:
            scraper.add_patents(pat)
