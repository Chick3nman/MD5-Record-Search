# MD5-Record-Search
Searches for MD5's that break records shown here: http://0xf.kr/md5/

A newly found record can be submitted via the API on http://0xf.kr/md5/

API info (source:http://0xf.kr/md5/)

Through http://0xF.kr/md5/update.php, you can submit a candidate.

Request(GET): update.php?c=CATEGORY&t=TEXT&n=NAME
CATEGORY is a category, TEXT is a candidate text for the category, and NAME is your name.
TEXT will be trimmed and non-printable or non-ASCII characters will be removed.

Please, don't submit very long TEXTes (>100b), and do not send request too rapidly.

Result(JSON): Something like {"error":null, "result":false}.
error: if there's an error, a string describing the error will be specified.
result: a boolean value whether the given candidate set a new record.

Through http://0xF.kr/md5/get.php, you can get the data about a category.

Request(GET): get.php?c=CATEGORY

Result(JSON): Something like {"error":null, "hash":"...", "text":"...", "by":"..."}.
