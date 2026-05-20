
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



@patch("web_scraping.cli.fetch_html")
def test_cli_handles_fetch_errors(mock_fetch, capsys):
    """
    Tests that the CLI displays a controlled error message when fetching the HTML fails.
    """
    mock_fetch.side_effect = Exception("Connection failed")

    test_args = [
        "prog",
        "https://example.com",
        "blog",
    ]

    with patch.object(sys, "argv", test_args):
        run()

    captured = capsys.readouterr()

    assert "Error: Connection failed" in captured.out



@patch("web_scraping.cli.export_to_json")
@patch("web_scraping.cli.export_to_csv")
@patch("web_scraping.cli.extract_matching_links")
@patch("web_scraping.cli.fetch_html")
def test_cli_calls_exporters_when_flags_are_used(
    mock_fetch,
    mock_extract,
    mock_export_csv,
    mock_export_json,
    capsys,
):
    """
    Tests that the CLI calls CSV and JSON exporters when
    the corresponding flags are provided.
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
        "--csv",
        "results.csv",
        "--json",
        "results.json",
    ]

    with patch.object(sys, "argv", test_args):
        run()

    mock_export_csv.assert_called_once_with(
        mock_extract.return_value,
        "results.csv",
    )
    mock_export_json.assert_called_once_with(
        mock_extract.return_value,
        "results.json",
    )

    captured = capsys.readouterr()

    assert "Results exported to CSV: results.csv" in captured.out
    assert "Results exported to JSON: results.json" in captured.out
