from pywebcopy import save_website
save_website(
url="https://httpbin.org/",
project_folder="D://savedpages//",
project_name="my_site",
bypass_robots=True,
debug=True,
open_in_browser=True,
delay=None,
threaded=False,
)