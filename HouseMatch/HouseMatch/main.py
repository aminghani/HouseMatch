import multiprocessing
from scrapy.cmdline import execute

def run_spider(spider_name):
    execute(['scrapy', 'crawl', spider_name])

def main():
    spiders = ['house_sheypoor']  # Replace with your spider names
    processes = []
    for spider in spiders:
        p = multiprocessing.Process(target=run_spider, args=(spider,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    
main()