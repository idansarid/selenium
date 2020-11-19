from pywebcopy.structures.WebPage import WebPage

url = 'http://example-site.com/index.html'
download_loc = 'C:\\Users\\1000263273\\PycharmProjects\\selenium\\outb'

wp = WebPage(url, download_loc)

# if you want assets only
wp.save_assets_only()

# if you want html only
wp.save_html_only()

# if you want complete webpage
wp.save_complete()