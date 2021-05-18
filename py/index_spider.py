import scrapy
from bs4 import BeautifulSoup


class BlogSpider(scrapy.Spider):
    name = "blogspider"
    bse_url_codes = ["1", "2", "4", "12", "63", "67", "100"]
    start_urls = []
    bse_url_base = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=BSE&opttopic=indexcomp&index="
    for cd in bse_url_codes:
        start_urls.append(bse_url_base + cd)

    def parse(self, response):
        index_name = BeautifulSoup(
            response.css("p.gL_12.PT15 > b").get(), "html.parser"
        ).string

        table_data = response.css("table.tbldata14").get()
        soup = BeautifulSoup(table_data, "html.parser")

        heads_row = soup.contents[0].contents[1]

        first_head = heads_row.contents[1].contents[1].b.string
        second_head = heads_row.contents[3].contents[0].b.string
        third_head = (
            heads_row.contents[5].contents[0] + " " + heads_row.contents[5].contents[2]
        )
        fourth_head = heads_row.contents[7].string
        fifth_head = heads_row.contents[9].string
        sixth_head = (
            heads_row.contents[11].contents[0]
            + " "
            + heads_row.contents[11].contents[2].string
        )

        heads = [
            first_head,
            second_head,
            third_head,
            fourth_head,
            fifth_head,
            sixth_head,
        ]

        core_data = []
        table_rows = soup.contents[0].contents
        for i in range(2, len(table_rows)):
            table_core_data = table_rows[i]

            if not table_core_data == "\n":
                col1 = table_core_data.contents[1].contents[0].b.string
                col2 = table_core_data.contents[3].b.string
                col3 = table_core_data.contents[5].string
                col4 = table_core_data.contents[7].string
                col5 = table_core_data.contents[9].string
                col6 = table_core_data.contents[11].string.replace(",", "")
                row_data = {
                    first_head: col1,
                    second_head: col2,
                    third_head: col3,
                    fourth_head: col4,
                    fifth_head: col5,
                    sixth_head: col6,
                }
                core_data.append(row_data)

        yield {index_name: core_data}
