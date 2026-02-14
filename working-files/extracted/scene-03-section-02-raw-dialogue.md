# Scene 03 Section 02 — Raw Dialogue (Cleaned)

- Source pages: 13-14
- Scope: Infection alert, butler-isolation panic song, and opening of next scene setup.

| Line ID | Page | Speaker (Chinese) | Chinese dialogue (verbatim/normalized) | Notes |
|---|---:|---|---|---|
| S03-SEC02-L001 | 13 | 芬尼 | 聽講最近有一種嚴重嘅病毒，中咗之後會成日打乞嗤……（再大聲）乞嗤…… | Carry-over completion for `S03-SEC01-L041`; OCR normalized |
| S03-SEC02-L002 | 13 | 奧妙妮 | 如果唔小心感染病毒，我哋咪要隔離，照顧唔到少爺小姐？ | OCR normalized |
| S03-SEC02-L003 | 13 | 占士 | 你打乞嗤？ | OCR normalized |
| S03-SEC02-L004 | 13 | 幕外聲 | 各位管家，因為懷疑你哋中咗管家界絕症——懶惰感冒，管家會議而家進入緊急狀態。 | OCR normalized from split noisy lines |
| S03-SEC02-L005 | 13 | 幕外聲 | 個個都唔可以離開呢間房。 | OCR normalized |
| S03-SEC02-L006 | 13 | 管家 | 吓！少爺小姐點算呀？ | OCR normalized |
| S03-SEC02-L007 | 13 | 管家甲 | 手腳也軟。 | Song line; OCR normalized |
| S03-SEC02-L008 | 13 | 管家甲 | 人像已經失控。 | Song line; OCR normalized |
| S03-SEC02-L009 | 13 | 管家甲 | 我頭極痛。 | Song line; OCR normalized |
| S03-SEC02-L010 | 13 | 管家甲 | 如像墮進惡夢。 | Song line; normalized (low confidence token) |
| S03-SEC02-L011 | 13 | 管家甲 | 怎會接觸這種奇異病菌。 | Song line; OCR normalized |
| S03-SEC02-L012 | 13 | 管家甲 | 心煩無奈，累了未放鬆。 | Song line; OCR normalized |
| S03-SEC02-L013 | 13 | 合唱 | 隔離被困，小姐晚餐如何能送。 | Song line; OCR normalized |
| S03-SEC02-L014 | 13 | 合唱 | 命運被愚弄。 | Song line; OCR normalized |
| S03-SEC02-L015 | 13 | 管家甲 | 小姐慣常被我寵。 | Song line; OCR normalized |
| S03-SEC02-L016 | 13 | 管家甲 | 曬被鋪床，涼又凍。 | Song line; normalized (very low OCR confidence) |
| S03-SEC02-L017 | 13 | 管家甲 | 穿上校衫，刷牙梳洗。 | Song line; OCR normalized |
| S03-SEC02-L018 | 13 | 合唱 | 沒我在，放學發現漏，擔心她哭叫難自控。 | Song line; OCR normalized from fragmented lines |
| S03-SEC02-L019 | 13 | 合唱 | 早日結束，能為我解封。 | Song line; OCR normalized |
| S03-SEC02-L020 | 13 | 合唱 | 擺脫這惡夢。 | Song line; OCR normalized |
| S03-SEC02-L021 | 14 | 合唱團 | 我一定做得到。 | Opening chorus line; mapped to Scene 04 setup in same OCR batch |
| S03-SEC02-L022 | 14 | 合唱團 | 身體要健康。 | Opening chorus line; mapped to Scene 04 setup in same OCR batch |

## Uncertainty Tracking

- `S03-SEC02-L010`, `S03-SEC02-L016` use conservative normalization due heavy OCR degradation.
- Page 14 content starts Scene 04 (`第四幕`) contextually; only first two chorus anchor lines are staged here to preserve page-range continuity, and Scene 04 extraction should restart cleanly from page 14 with fresh section IDs.
