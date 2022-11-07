# 이분탐색 이진탐색 Binary Search

* 탐색전에 반드시 정렬 되어 있어야 한다.
* 탐색 범위를 절반씩 줄여가면서 답을 찾는다.
* 정렬 O(NlogN) + 이진탐색 O(logN) -> 결과적으로 O(NlogN)
* 미리 정렬되어 있따면 O(logN)
* 선형탐색과 비교하여 N회 탐색을 수행 할 시 이분탐색이 유리 하다

```python
# bisect_left/right
from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)
print(f"number of 3: {three}")  # 2
print(f"number of 4: {four}")  # 0
print(f"number of 6: {six}")  # 3
```