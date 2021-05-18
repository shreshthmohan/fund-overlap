import re
import scrapy
from bs4 import BeautifulSoup
import bs4


class FundSpider(scrapy.Spider):
    name = "fundspider"
    # bse_url_codes = ["1", "2", "4", "12", "63", "67", "100"]
    # scrape urls from https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/index-fundsetfs.html and similar
    # use those urls here 👇
    allowed_domains = ["www.moneycontrol.com"]
    start_urls = [
        # "https://www.moneycontrol.com/mutual-funds/icici-prudential-nifty-low-vol-30-etf/portfolio-holdings/MPI3352",
        # "https://www.moneycontrol.com/mutual-funds/icici-prudential-nifty-etf/portfolio-holdings/MPI1312",
        # "https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/multi-cap-fund.html",
        "https://www.moneycontrol.com/mutual-funds/icici-prudential-multicap-fund-growth/portfolio-holdings/MPI028"
    ]
    # bse_url_base = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=BSE&opttopic=indexcomp&index="
    # for cd in bse_url_codes:
    #     start_urls.append(bse_url_base + cd)

    def parse(self, response):
        f_name = response.css(".page_heading.navdetails_heading")
        if f_name:
            fund_name = BeautifulSoup(f_name.get(), "html.parser").string

            # print(fund_name)

            if fund_name:

                table_data = response.css("table#equityCompleteHoldingTable").get()
                soup = BeautifulSoup(table_data, "html.parser")

                heads_row = soup.contents[0].contents[1].contents[1].contents

                first_head = heads_row[1].contents[0].string
                second_head = heads_row[3].contents[0].string
                third_head = heads_row[5].contents[0].string
                fourth_head = heads_row[7].contents[0].string
                fifth_head = heads_row[9].contents[0].string

                table_body_data = soup.contents[0].contents[3].contents
                # table_body_data = soup.contents[0].contents[3]
                # print(table_body_data[1].contents[1].contents[3])
                print(table_body_data[161])

                core_data = []
                # for i in range(0, len(table_body_data) - 1):
                #     # for i in range(0, 5):
                #     if not (
                #         (table_body_data[i] == "\n")
                #         or (isinstance(table_body_data[i], bs4.element.Comment))
                #     ):
                #         # print(i)
                #         row_data = table_body_data[i].contents
                #         # col1 = row_data[1].contents[1]
                #         print(i)
                # instead of doing this, find a tag in this td
                #         col1 = row_data[1].contents[3].contents[0].string
                # col2 = row_data[3].string
                # col3 = row_data[5].string
                # col4 = row_data[7].string
                # col5 = row_data[9].string
                # parsed_data = {
                #     first_head: col1,
                #     second_head: col2,
                #     third_head: col3,
                #     fourth_head: col4,
                #     fifth_head: col5,
                # }
                # core_data.append(parsed_data)

                # # # print(len(core_data))

                yield {fund_name: core_data}

        # for a in response.css("a.robo_medium::attr(href)"):
        #     if a is not None:
        #         a_ = re.sub(r"/nav/", "/", a.get())
        #         a__ = re.sub(r"\/(?!.*\/)", "/portfolio-holdings/", a_)
        #         # print(a__)
        #         if not re.match("javascript", a__):
        #             yield response.follow(a__, self.parse)
