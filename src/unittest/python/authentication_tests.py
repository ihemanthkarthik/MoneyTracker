import sys
import pytest
from unittest.mock import Mock, patch

sys.path.append('./')

from src.main.python.authentication import Authorization


@pytest.fixture
def mock_cursor():
    return Mock()


@pytest.fixture
def mock_conn(mock_cursor):
    conn = Mock()
    conn.cursor.return_value = mock_cursor
    return conn


# Test valid login
@patch('builtins.input')
def test_login_valid_credentials(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['validuser', 'validpassword']
    mock_cursor.fetchone.return_value = (1,)
    assert Authorization.login(mock_conn, mock_cursor) == 1
    mock_conn.commit.assert_called_once()


# Test minimum username length
@patch('builtins.input')
def test_login_invalid_username_length(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['adm']
    assert Authorization.login(mock_conn, mock_cursor) == -1
    mock_conn.commit.assert_not_called()  # Ensure commit method is not called


# Test minimum password length
@patch('builtins.input')
def test_login_invalid_password_length(mock_input, mock_conn, mock_cursor):
    # Mocking user input
    mock_input.side_effect = ['admin', 'pass']
    mock_cursor.fetchone.return_value = (1,)
    result = Authorization.login(mock_conn, mock_cursor)
    assert result == -1
    mock_conn.commit.assert_not_called()


# Test non-existent username
@patch('builtins.input')
def test_login_non_existent_username(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['nonexistentuser', 'invalidpassword']
    mock_cursor.fetchone.return_value = (0,)
    assert Authorization.login(mock_conn, mock_cursor) == -1
    assert mock_conn.commit.call_count == 0


# Test incorrect password
@patch('builtins.input')
def test_login_incorrect_password(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['validuser', 'wrongpassword']
    mock_cursor.fetchone.side_effect = [(1,), None]
    assert Authorization.login(mock_conn, mock_cursor) == -1
    assert mock_conn.commit.call_count == 0


# Test empty password
@patch('builtins.input')
def test_login_empty_password(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['validuser', '']
    mock_cursor.fetchone.return_value = (1,)
    result = Authorization.login(mock_conn, mock_cursor)
    assert result == -1
    mock_conn.commit.assert_not_called()


# Test no account associated with username
@patch('builtins.input')
def test_login_no_account_associated(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['nonexistentuser', 'validpassword']
    mock_cursor.fetchone.return_value = (0,)
    assert Authorization.login(mock_conn, mock_cursor) == -1
    assert mock_conn.commit.call_count == 0


@patch('builtins.input')
def test_register_valid_registration(mock_input, mock_conn, mock_cursor):
    mock_input.side_effect = ['testemail@example.com', 'Test Name', 'M', '1990-01-01', 'testuser', 'testpassword']
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1
    mock_cursor.lastrowid = 1
    assert Authorization.register(mock_conn, mock_cursor) == 0
    mock_conn.commit.assert_called_once()


# Write tests for other scenarios for registration, forgot password, forgot username, etc.

if __name__ == "__main__":
    pytest.main()
