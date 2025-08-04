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
    }
]
