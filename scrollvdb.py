SCROLLS = [
    {
        "valid": ["abc", "def"],
        "invalid": ["123", "456"],
        "gree_expression": r"^\D+$"
    },
    {
        "valid": ["abc-1", "bbb-1", "cde-1"],
        "invalid": ["abc1", "bbb1", "cde1"],
        "gree_expression": r"^.+-.+$"
    },
    {
        "valid": ["aaa", "abb", "acc"],
        "invalid": ["bbb", "bcc", "bca"],
        "gree_expression": r"^[a].+$"
    },
    {
        "valid": ["foo@abc.com", "bar@def.net"],
        "invalid": ["baz@abc", "qux.com"],
        "gree_expression": r"^\D+@\w+\.\w+$"
    },
    {
        "valid": ["abc1", "bbb1", "ccc1"],
        "invalid": ["abc", "bbb", "ccc"],
        "gree_expression": r"^.+[1]$"
    },

    # Added 070825 2:43AM
    {
        "valid": ["_start", "_init", "_config"],
        "invalid": ["start_", "init_", "config"],
        "gree_expression": r"^_\w+$"
    },
    {
        "valid": ["hello123", "test456", "data789"],
        "invalid": ["123hello", "456test", "789data"],
        "gree_expression": r"^[A-Za-z]+\d+$"
    },
    {
        "valid": ["2023-01-01", "1999-12-31"],
        "invalid": ["01-01-2023", "12/31/1999"],
        "gree_expression": r"^\d{4}-\d{2}-\d{2}$"
    },
    {
        "valid": ["a1b2c3", "x9y8z7"],
        "invalid": ["abc123", "123abc"],
        "gree_expression": r"^([a-z]\d){3}$"
    },
    {
        "valid": ["a_b", "x_y", "i_o"],
        "invalid": ["ab", "xy", "io"],
        "gree_expression": r"^[a-z]_[a-z]$"
    },
    {
        "valid": ["John", "Alice", "Zack"],
        "invalid": ["john", "alice", "zack"],
        "gree_expression": r"^[A-Z][a-z]+$"
    },
    {
        "valid": ["car!", "go?", "yes."],
        "invalid": ["car", "go", "yes"],
        "gree_expression": r"^\w+[!?\.]$"
    },
    {
        "valid": ["192.168.0.1", "10.0.0.1"],
        "invalid": ["192.168.0", "10.0.0.256"],
        "gree_expression": r"^\d{1,3}(\.\d{1,3}){3}$"
    },
    {
        "valid": ["[abc]", "[123]", "[xyz]"],
        "invalid": ["abc", "123", "xyz"],
        "gree_expression": r"^\[\w+\]$"
    },
    {
        "valid": ["abc_def", "foo_bar"],
        "invalid": ["abc def", "foo bar"],
        "gree_expression": r"^\w+_\w+$"
    },
    {
        "valid": ["$100", "$5", "$0.99"],
        "invalid": ["100$", "5$", "0.99$"],
        "gree_expression": r"^\$\d+(\.\d{2})?$"
    },
    {
        "valid": ["xXx", "aAa", "bBb"],
        "invalid": ["xxx", "aaa", "bbb"],
        "gree_expression": r"^[a-z][A-Z][a-z]$"
    },
    {
        "valid": ["pass1234", "code5678"],
        "invalid": ["pass", "1234", "code"],
        "gree_expression": r"^[a-z]+[0-9]{4}$"
    },
    {
        "valid": ["A1B2C3", "X9Y8Z7"],
        "invalid": ["ABC123", "123ABC"],
        "gree_expression": r"^([A-Z]\d){3}$"
    },
    {
        "valid": ["abc.com", "site.net", "host.org"],
        "invalid": ["abccom", "sitenet", "hostorg"],
        "gree_expression": r"^\w+\.(com|net|org)$"
    },
    {
        "valid": ["(123)", "(abc)", "(xyz)"],
        "invalid": ["123", "abc", "xyz"],
        "gree_expression": r"^\(\w+\)$"
    },
    {
        "valid": ["abc123xyz", "foo456bar"],
        "invalid": ["abcxyz123", "123abcxyz"],
        "gree_expression": r"^[a-z]+[0-9]+[a-z]+$"
    },
    {
        "valid": ["no spaces", "some text"],
        "invalid": ["nospaces", "sometext"],
        "gree_expression": r"^\w+\s\w+$"
    },
    {
        "valid": ["a1", "b2", "z9"],
        "invalid": ["1a", "2b", "9z"],
        "gree_expression": r"^[a-z]\d$"
    }
]
