from stockticker.clients.file_secrets import FileSecrets
from unittest import patch, mock_open


@patch("builtins.open", new_callable=mock_open, read_data='{"x": 2}')
def test_file_secrets():
    file_secrets = FileSecrets("/some/path")
    assert file_secrets.get("x") == 2
