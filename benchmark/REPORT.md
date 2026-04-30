# Benchmark redukcji tokenów — wyniki empiryczne

Tokenizer: `o200k_base` | Próbek: 96

## Wyniki per tryb (średnia ze wszystkich kategorii)

| Tryb       | Średnia oszcz.   | Min   | Max   |   N |
|------------|------------------|-------|-------|-----|
| godka1     | 58.3%            | 50.6% | 62.1% |   6 |
| godka2     | 53.6%            | 48.5% | 61.1% |   6 |
| godka3     | 27.0%            | 7.6%  | 38.9% |   6 |
| grypsera1  | 52.1%            | 41.2% | 65.3% |   6 |
| grypsera2  | 54.1%            | 44.1% | 59.7% |   6 |
| grypsera3  | 64.0%            | 48.0% | 70.8% |   6 |
| kaszebsko1 | 57.9%            | 51.8% | 62.1% |   6 |
| kaszebsko2 | 48.5%            | 33.3% | 55.6% |   6 |
| kaszebsko3 | 24.5%            | 4.5%  | 37.5% |   6 |
| polsko1    | 57.8%            | 47.8% | 66.7% |   6 |
| polsko2    | 64.1%            | 60.2% | 68.2% |   6 |
| polsko3    | 80.3%            | 74.8% | 83.7% |   6 |
| suwalsko1  | 59.2%            | 52.2% | 65.2% |   6 |
| suwalsko2  | 56.1%            | 51.5% | 59.7% |   6 |
| suwalsko3  | 42.2%            | 35.6% | 52.8% |   6 |
| terse-en   | 69.7%            | 60.6% | 81.9% |   6 |

## Wyniki per kategoria (średnia ze wszystkich trybów)

| Kategoria      |   Norm. tok. (śr.) |   Zwięzłe tok. (śr.) | Oszcz. (śr.)   |
|----------------|--------------------|----------------------|----------------|
| short_error    |               72   |                 27.7 | 61.5%          |
| short_notfound |               66   |                 31.8 | 51.8%          |
| mid_explain    |              120.4 |                 56.9 | 52.6%          |
| mid_install    |              141.8 |                 63.8 | 54.4%          |
| long_review    |              259   |                117.2 | 54.7%          |
| long_arch      |              247.1 |                121.2 | 51.0%          |

## Szczegółowe wyniki

| Kategoria      | Tryb       |   Normal tok. |   Zwięzłe tok. | Oszczędność   |
|----------------|------------|---------------|----------------|---------------|
| short_error    | polsko1    |            72 |             24 | 66.7%         |
| short_error    | polsko2    |            72 |             24 | 66.7%         |
| short_error    | polsko3    |            72 |             12 | 83.3%         |
| short_error    | suwalsko1  |            72 |             27 | 62.5%         |
| short_error    | suwalsko2  |            72 |             29 | 59.7%         |
| short_error    | suwalsko3  |            72 |             34 | 52.8%         |
| short_error    | terse-en   |            72 |             13 | 81.9%         |
| short_notfound | polsko1    |            66 |             27 | 59.1%         |
| short_notfound | polsko2    |            66 |             26 | 60.6%         |
| short_notfound | polsko3    |            66 |             11 | 83.3%         |
| short_notfound | suwalsko1  |            66 |             23 | 65.2%         |
| short_notfound | suwalsko2  |            66 |             32 | 51.5%         |
| short_notfound | suwalsko3  |            66 |             38 | 42.4%         |
| short_notfound | terse-en   |            66 |             17 | 74.2%         |
| mid_explain    | polsko1    |           118 |             49 | 58.5%         |
| mid_explain    | polsko2    |           118 |             47 | 60.2%         |
| mid_explain    | polsko3    |           118 |             27 | 77.1%         |
| mid_explain    | suwalsko1  |           118 |             47 | 60.2%         |
| mid_explain    | suwalsko2  |           118 |             55 | 53.4%         |
| mid_explain    | suwalsko3  |           118 |             76 | 35.6%         |
| mid_explain    | terse-en   |           118 |             41 | 65.3%         |
| mid_install    | polsko1    |           151 |             57 | 62.3%         |
| mid_install    | polsko2    |           151 |             48 | 68.2%         |
| mid_install    | polsko3    |           151 |             38 | 74.8%         |
| mid_install    | suwalsko1  |           151 |             63 | 58.3%         |
| mid_install    | suwalsko2  |           151 |             62 | 58.9%         |
| mid_install    | suwalsko3  |           151 |             82 | 45.7%         |
| mid_install    | terse-en   |           151 |             45 | 70.2%         |
| long_review    | polsko1    |           259 |            124 | 52.1%         |
| long_review    | polsko2    |           259 |             85 | 67.2%         |
| long_review    | polsko3    |           259 |             53 | 79.5%         |
| long_review    | suwalsko1  |           259 |            111 | 57.1%         |
| long_review    | suwalsko2  |           259 |            111 | 57.1%         |
| long_review    | suwalsko3  |           259 |            164 | 36.7%         |
| long_review    | terse-en   |           259 |             88 | 66.0%         |
| long_arch      | polsko1    |           251 |            131 | 47.8%         |
| long_arch      | polsko2    |           251 |             96 | 61.8%         |
| long_arch      | polsko3    |           251 |             41 | 83.7%         |
| long_arch      | suwalsko1  |           251 |            120 | 52.2%         |
| long_arch      | suwalsko2  |           251 |            111 | 55.8%         |
| long_arch      | suwalsko3  |           251 |            150 | 40.2%         |
| long_arch      | terse-en   |           251 |             99 | 60.6%         |
| short_error    | kaszebsko1 |            72 |             28 | 61.1%         |
| short_error    | kaszebsko2 |            72 |             32 | 55.6%         |
| short_error    | kaszebsko3 |            72 |             45 | 37.5%         |
| short_notfound | kaszebsko1 |            66 |             25 | 62.1%         |
| short_notfound | kaszebsko2 |            66 |             44 | 33.3%         |
| short_notfound | kaszebsko3 |            66 |             63 | 4.5%          |
| mid_explain    | kaszebsko1 |           118 |             48 | 59.3%         |
| mid_explain    | kaszebsko2 |           118 |             64 | 45.8%         |
| mid_explain    | kaszebsko3 |           118 |             98 | 16.9%         |
| mid_install    | kaszebsko1 |           151 |             65 | 57.0%         |
| mid_install    | kaszebsko2 |           151 |             67 | 55.6%         |
| mid_install    | kaszebsko3 |           151 |            100 | 33.8%         |
| long_review    | kaszebsko1 |           259 |            114 | 56.0%         |
| long_review    | kaszebsko2 |           259 |            125 | 51.7%         |
| long_review    | kaszebsko3 |           259 |            195 | 24.7%         |
| long_arch      | kaszebsko1 |           251 |            121 | 51.8%         |
| long_arch      | kaszebsko2 |           251 |            128 | 49.0%         |
| long_arch      | kaszebsko3 |           251 |            177 | 29.5%         |
| short_error    | godka1     |            72 |             28 | 61.1%         |
| short_error    | godka2     |            72 |             28 | 61.1%         |
| short_error    | godka3     |            72 |             44 | 38.9%         |
| short_notfound | godka1     |            66 |             25 | 62.1%         |
| short_notfound | godka2     |            66 |             34 | 48.5%         |
| short_notfound | godka3     |            66 |             61 | 7.6%          |
| mid_explain    | godka1     |           118 |             47 | 60.2%         |
| mid_explain    | godka2     |           118 |             60 | 49.2%         |
| mid_explain    | godka3     |           118 |             92 | 22.0%         |
| mid_install    | godka1     |           151 |             64 | 57.6%         |
| mid_install    | godka2     |           151 |             63 | 58.3%         |
| mid_install    | godka3     |           151 |             96 | 36.4%         |
| long_review    | godka1     |           259 |            108 | 58.3%         |
| long_review    | godka2     |           259 |            114 | 56.0%         |
| long_review    | godka3     |           259 |            181 | 30.1%         |
| long_arch      | godka1     |           251 |            124 | 50.6%         |
| long_arch      | godka2     |           251 |            129 | 48.6%         |
| long_arch      | godka3     |           251 |            183 | 27.1%         |
| short_error    | grypsera1  |            72 |             25 | 65.3%         |
| short_error    | grypsera2  |            72 |             29 | 59.7%         |
| short_error    | grypsera3  |            72 |             21 | 70.8%         |
| short_notfound | grypsera1  |            66 |             32 | 51.5%         |
| short_notfound | grypsera2  |            66 |             30 | 54.5%         |
| short_notfound | grypsera3  |            66 |             21 | 68.2%         |
| mid_explain    | grypsera1  |           131 |             66 | 49.6%         |
| mid_explain    | grypsera2  |           131 |             53 | 59.5%         |
| mid_explain    | grypsera3  |           131 |             40 | 69.5%         |
| mid_install    | grypsera1  |           102 |             60 | 41.2%         |
| mid_install    | grypsera2  |           102 |             57 | 44.1%         |
| mid_install    | grypsera3  |           102 |             53 | 48.0%         |
| long_review    | grypsera1  |           259 |            107 | 58.7%         |
| long_review    | grypsera2  |           259 |            115 | 55.6%         |
| long_review    | grypsera3  |           259 |             80 | 69.1%         |
| long_arch      | grypsera1  |           230 |            123 | 46.5%         |
| long_arch      | grypsera2  |           230 |            112 | 51.3%         |
| long_arch      | grypsera3  |           230 |             95 | 58.7%         |
