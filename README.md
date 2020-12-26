# Web Crawling & Visualization - Top Movies on Douban

In the project, I devised a web crawler that gets data of 250 popular movies from douban.com.

For visualization purposes I created a Python app via *Flask* as well, together with the help of `SQLite`, `ECharts`, `WordCloud`, `jieba`, etc.

## Usage

The folder `Web-Crawler-Douban/` contains the program of a web crawler, i.e. `spider.py`. After crawling data from the website, I store it in the form of both excel file `.xls` and SQLite database `.db`.

The folder `Douban-Flask/` contains code for the Flask app.

- `static/` contains assets like images, CSS and JavaScript files, some of which are inherited from the bootstrap [template](https://bootstrapmade.com/mamba-one-page-bootstrap-template-free/) I used.
- `templates/` is where the HTML file of web pages resides.
- `app.py` is where we set up and deploy our Flask app.
- `movie.db` is the SQLite file containing the data crawled, copied from `Web-Crawler-Douban/`. 
- `wordCloudGen.py` is where we generate our word cloud for the comments of movies.

## Deployment

To view the demo of the Flask app, run `app.py` in `Douban-Flask/`. 

Copy the link (localhost) prompted and open it in your browser.

It should look something similar to

![](/demo/1.png)

![](/demo/2.png)

![](/demo/3.jpg)

![](/demo/4.png)

## Comment

I believe I'll write a tutorial on how to do web crawling and stuff in the near future. 

So you are strongly recommended to stay tuned at my [blog](https://wwwCielwww.github.io) if you're interested!!  😃
