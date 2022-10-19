# 실버0 - 10930. SHA-256 (https://www.acmicpc.net/problem/10930)

import hashlib

s = input()
hash = hashlib.sha256(s.encode()).hexdigest()
print(hash)
