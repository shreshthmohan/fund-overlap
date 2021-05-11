import scrapy
from bs4 import BeautifulSoup


class BlogSpider(scrapy.Spider):
    name = "blogspider"
    start_urls = [
        "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
    ]

    def parse(self, response):
        table_data = response.css("table.tbldata14").get()
        soup = BeautifulSoup(table_data, "html.parser")

        heads_row = soup.contents[0].contents[1]

        first_head = heads_row.contents[1].contents[1].b.string
        second_head = heads_row.contents[3].contents[0].b.string
        third_head = (
            heads_row.contents[5].contents[0] + " " +
            heads_row.contents[5].contents[2]
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
        # for
        table_rows = soup.contents[0].contents
        for i in range(2, len(table_rows)):
            # table_core_data = soup.contents[0].contents[3]
            table_core_data = table_rows[i]

            if not table_core_data == "\n":
                col1 = table_core_data.contents[1].contents[0].b.string
                col2 = table_core_data.contents[3].b.string
                col3 = table_core_data.contents[5].string
                col4 = table_core_data.contents[7].string
                col5 = table_core_data.contents[9].string
                col6 = table_core_data.contents[11].string.replace(",", "")
                row_data = [col1, col2, col3, col4, col5, col6]
                core_data.append(row_data)

        print(core_data)
