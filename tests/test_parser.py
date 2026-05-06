
from web_scraping.parser import extract_matching_links



def test_extract_matching_links_basic():
    html = """
    <html>
        <body>
            <a href="/blog">Blog</a>
            <a href="/about">About</a>
            <a href="/blog-post">Tech Blog</a>
        </body>
    </html>
    """

    results = extract_matching_links(html, "blog", "https://example.com")

    assert len(results) == 2
    assert results[0]["text"] == "Blog"
    assert results[0]["href"] == "https://example.com/blog"
    assert results[1]["text"] == "Tech Blog"



def test_extract_matching_links_no_results():
    html = "<html><body><a href='/home'>Home</a></body></html>"

    results = extract_matching_links(html, "blog", "https://example.com")

    assert results == []



def test_extract_matching_links_ignores_invalid_links():
    html = """
    <html>
        <body>
            <a href=""></a>
            <a>Missing href</a>
            <a href="/valid">Valid Link</a>
        </body>
    </html>
    """

    results = extract_matching_links(html, "valid", "https://example.com")

    assert len(results) == 1
    assert results[0]["text"] == "Valid Link"
    assert results[0]["href"] == "https://example.com/valid"
