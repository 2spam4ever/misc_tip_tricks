#For in terminal

```bash
for i in {0..9}; do cat temp_posture.log | grep "22:34:5${i}." | wc; done
```

```bash
for i in {0..9}; do for j in {10..13}; do echo "${i} ${j}"; done; done
```

```bash
for g in {21..23}; do for i in {00..59}; do for j in {00..59}; do x=$(cat temp_posture.log | grep "${g}:${i}:${j}." | wc -l) && y=$(cat temp_posture.log | grep "${g}:${i}:${j}." | head -n 1) && echo "<msg_count = $x> <time $g:$i:$j> <info = $y>"
```
