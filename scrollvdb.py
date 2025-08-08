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
        "valid": ["abc1", "bbb1", "ccc1"],
        "invalid": ["abc", "bbb", "ccc"],
        "gree_expression": r"^.+[1]$"
    },
    {
        "valid": ["foo@abc.com", "bar@def.net"],
        "invalid": ["baz@abc", "qux.com"],
        "gree_expression": r"^\D+@\w+\.\w+$"
    },
    # Added 070825 2:43AM

    { #6: start with underscore
        "valid": ["_start", "_init", "_config"],
        "invalid": ["start_", "init_", "config"],
        "gree_expression": r"^_\w+$"
    },
    { # non-digit followed by digit
        "valid": ["hello123", "test456", "data789"],
        "invalid": ["123hello", "456test", "789data"],
        "gree_expression": r"^[A-Za-z]+\d+$"
    },
    { # set number & format of characters / digits 
        "valid": ["2023-01-01", "1999-12-31"],
        "invalid": ["01-01-2023", "12/31/1999"],
        "gree_expression": r"^\d{4}-\d{2}-\d{2}$"
    },
    { #9: specific character & digit pattern 
        "valid": ["a1b2c3", "x9y8z7"],
        "invalid": ["abc123", "123abc"],
        "gree_expression": r"^([a-z]\d){3}$"
    },
    { # underscore between words                            -- REDUNDANT: covered in #6 -- 
        "valid": ["a_b", "x_y", "i_o"],
        "invalid": ["ab", "xy", "io"],
        "gree_expression": r"^[a-z]_[a-z]$"
    },
    { #11: capitalised words 
        "valid": ["John", "Alice", "Zack"],
        "invalid": ["john", "alice", "zack"],
        "gree_expression": r"^[A-Z][a-z]+$"
    },
    { # punctuation at the end                             -- REDUNDANT: covered in #5 -- 
        "valid": ["car!", "go?", "yes."],
        "invalid": ["car"],
        "gree_expression": r"^\w+[!?\.]$"
    },
    { # 13 set number of punctuation characters
        "valid": [".168.0.1", ".0.0.1", "..."],
        "invalid": ["192.168.0", "10.0.0.256"],
        "gree_expression": r"^\.(\d*\.){2}\d*$"
    },
    { # position of specific characters 
        "valid": ["[abc]", "[123]", "[xyz]"],
        "invalid": ["abc", "123", "xyz"],
        "gree_expression": r"^\[\w+\]$"
    },
    { # underscore between words                             -- REDUNDANT: covered in #6 --  
        "valid": ["abc_def", "foo_bar"],
        "invalid": ["abc def", "foo bar"],
        "gree_expression": r"^\w+_\w+$"
    },
    { # position of specific characters                             -- REDUNDANT: covered in #13 --  
        "valid": ["$100", "$5", "$0.99"],
        "invalid": ["100$", "5$", "0.99$"],
        "gree_expression": r"^\$\d+(\.\d{2})?$"
    },
    { # capitalised words at specific position                  -- REDUNDANT: covered in #11 --
        "valid": ["xXx", "aAa", "bBb"],
        "invalid": ["xxx", "aaa", "bbb"],
        "gree_expression": r"^[a-z][A-Z][a-z]$" # this should be changed to be broader e.g \D or \w
    },
    { # pattern of digits and letters 
        "valid": ["pass1234", "code5678"],
        "invalid": ["pass", "1234", "code"],
        "gree_expression": r"^[a-z]+[0-9]{4}$"
    },
    { # same one
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
    }, 

    # Added 070825 10:14AM 
    {
        "valid": ["X"],
        "invalid": ["x", "XX", "xX", "1"],
        "gree_expression": r"^[A-Z]$"
    },
    {
        "valid": ["#mid#"],
        "invalid": ["#start", "end#", "##"],
        "gree_expression": r"^#\w+#$"
    },
    {
        "valid": ["a12", "b99", "z01", "k33"],
        "invalid": ["aa1"],
        "gree_expression": r"^[a-z]\d{2}$"
    },
    {
        "valid": ["[]!@#)(_)", ".,<<:""''", "#$%&@*?!#", "|}{_-'+=^'}{", "( . )( . )"],
        "invalid": ["Aa1"],
        "gree_expression": r"^[^A-Za-z0-9]+$"
    },
    {
        "valid": ["1234", "5678", "9012"],
        "invalid": ["12345", "56789", "90123"],
        "gree_expression": r"^\d{4}$"
    },
    {
        "valid": ["hello world", "foo bar"],
        "invalid": ["helloworld", "foobar"],
        "gree_expression": r"^\w+\s\w+$"
    },
    {
        "valid": ["fy98uDs9aidSk", "732qi$(ds/m", "jA84t5fk)+=1!", "lp@<>,./';:", "[]"],
        "invalid": ["jsks,aceaoisasd~", " ", "safbhsvj~", "`adsdSDA)92"],
        "gree_expression": r"^[^\s~`]+$"
    },
    
    # Added 080825 11:43AM 
    {
        # No vowels (a, e, i, o, u, A, E, I, O，U) in the string
        "valid": ["FyL%Qscnjldfs", "g|rwdjsltxzb214[w.", "v 002177", "          \n        "],
        "invalid": ["iatedonut", "IOU"],
        "gree_expression": r"^[^aeiouAEIOU]*$" 
    },
    {
        # Each valid string contains a repeating pattern (minimum twice) of at least 4 characters
        "valid": ["+-*/=+-*/=+-*/=", "432k432k", "FUNnyFUNny"],
        "invalid": ["hahahahaha","wowwow", "i0"],
        "gree_expression": r"^(.{4,})\1+$"
    },
    {
        "valid": ["I like 海底捞火锅。", "ü -> lol00456", ":nñIIagree"], 
        "invalid": ["haa:","::l", "i0/sadw%al':/"], 
        "gree_expression": r"^.*[^\W\d_].*[^:/]$"
    },
    {
        # Any string that does not contain the words "eat" or "chair"
        "valid": ["I", "love", "eating", "food"],
        "invalid": ["eat", "chair"],
        "gree_expression": r"^(?!eat$|chair$).+$"
    },
    {
        # Any string that contains at least one non-ASCII character (includes characters from languages like Chinese, Arabic, etc.)
        "valid": ["هاهاها", "𓀐𓀢 (:^O", "aka哈哈akah"],
        "invalid": ["Helicopter", "hehehe >:^)"],
        "gree_expression": r"^.*[^\x00-\x7F].*$" 
    },
    {
        # Any string that contains at least one digit followed by a hyphen or a hyphen followed by a digit
        "valid": ["1трыугс3-Фхиеща2", "5سل2-ام0", "8Xin-8chào8"],
        "invalid": ["3oühh-lalala44"],
        "gree_expression": r"^.*(?:\d-|-\d).*$"
    },
    {
        # Exactly one Chinese–Japanese–Korean unified ideograph character (any character in the Unicode range U+4E00 to U+9FFF)
        "valid": ["一", "二", "三"],
        "invalid": ["1", "one", "ഹലോ"],
        "gree_expression": r"^[\u4e00-\u9fff]$" 
    },
    {
        # Any character except colon, followed by a colon and space, then any character except parentheses
        "valid": ["Tel: +69 8123 4567", "Huatline: 88888888 "],
        "invalid": ["Billy: (555)555-1234"],
        "gree_expression": r"^[^:]+: [^()]+$" 
    },
    { # forward slash 
        "valid": ["(a1\n1\n1\n)", "\\Keyboard\\", "Goo Goo\n\rGa Ga "],
        "invalid": ["Billy: (555)555-1234"],
        "gree_expression": r"^(?:[^)]|\D\))*$"
    },
]