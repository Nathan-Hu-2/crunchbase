from torpy.http.requests import TorRequests
with TorRequests() as tor_requests:
    with tor_requests.get_session() as sess:
        response = sess.get("https://webscraper.io/test-sites/e-commerce/allinone") # fire request
        print(response)