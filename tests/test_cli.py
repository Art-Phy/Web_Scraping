
from unittest.mock import patch
import sys

from web_scraping.cli import run



@patch("web_scraping.cli.extract_matching_links")
@patch("web_scraping.cli.fetch_html")
def test_cli_outputs_results(mock_fetch, mock_extract, capsys):
    """
    Tests that the CLI prints extracted results correctly
    """
    mock_fetch.return_value = "<html></html>"
    mock_extract.return_value = [
        {
            "text": "Blog",
            "href": "https://example.com/blog",
        }
    ]

    test_args = [
        "prog",
        "https://example.com",
        "blog",
    ]

    with patch.object(sys, "argv", test_args):
        run()

    captured = capsys.readouterr()

    assert "Matches found" in captured.out
    assert "Blog" in captured.out
    assert "https://example.com/blog" in captured.out



@patch("web_scraping.cli.extract_matching_links")
@patch("web_scraping.cli.fetch_html")
def test_cli_handles_no_results(mock_fetch, mock_extract, capsys):
    """
    Tests that the CLI shows the correct message when no matches are found.
    """
    mock_fetch.return_value = "<html></html>"
    mock_extract.return_value = []

    test_args = [
        "prog",
        "https://example.com",
        "blog",
    ]

    with patch.object(sys, "argv", test_args):
        run()

    captured = capsys.readouterr()

    assert "No matches found" in captured.out
