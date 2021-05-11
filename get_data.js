const axios = require("axios").default;
const fs = require("fs");
const cheerio = require("cheerio");

const URLS = {
  nifty50:
    "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9",
};

// fs.writeFileSync("data/nifty50.html", response.data);
(async () => {
  const response = await axios.get(URLS.nifty50);
  // console.log(response);
  const $ = cheerio.load(response.data);
  const header = $("table.tbldata14 > tbody > tr:nth-child(1)");
  const contents = $("table.tbldata14 > tbody > tr:not(:nth-child(1))");

  // console.log(header("b"));
  const header_names = [];

  const firstHead = $($($(header.children()[0]).children()[0]).children()[0]);
  header_names.push(firstHead);
  const ys = $($($(header.children()[1]).children()[0]).children()[0]);
  console.log(ys.html());

  // .each((x, y) => {
  //   // return y;
  //   $(y).
  // });
  // console.log(ys[0].html());
})();
