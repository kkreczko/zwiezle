# Benchmark redukcji tokenów — wyniki empiryczne

Tokenizer: `o200k_base` | Próbek: 42

## Wyniki per tryb (średnia ze wszystkich kategorii)

| Tryb      | Średnia oszcz.   | Min   | Max   |   N |
|-----------|------------------|-------|-------|-----|
| polsko1   | 57.8%            | 47.8% | 66.7% |   6 |
| polsko2   | 64.1%            | 60.2% | 68.2% |   6 |
| polsko3   | 80.3%            | 74.8% | 83.7% |   6 |
| suwalsko1 | 59.2%            | 52.2% | 65.2% |   6 |
| suwalsko2 | 56.1%            | 51.5% | 59.7% |   6 |
| suwalsko3 | 42.2%            | 35.6% | 52.8% |   6 |
| terse-en  | 69.7%            | 60.6% | 81.9% |   6 |

## Wyniki per kategoria (średnia ze wszystkich trybów)

| Kategoria      |   Norm. tok. (śr.) |   Zwięzłe tok. (śr.) | Oszcz. (śr.)   |
|----------------|--------------------|----------------------|----------------|
| short_error    |                 72 |                 23.3 | 67.7%          |
| short_notfound |                 66 |                 24.9 | 62.3%          |
| mid_explain    |                118 |                 48.9 | 58.6%          |
| mid_install    |                151 |                 56.4 | 62.6%          |
| long_review    |                259 |                105.1 | 59.4%          |
| long_arch      |                251 |                106.9 | 57.4%          |

## Szczegółowe wyniki

| Kategoria      | Tryb      |   Normal tok. |   Zwięzłe tok. | Oszczędność   |
|----------------|-----------|---------------|----------------|---------------|
| short_error    | polsko1   |            72 |             24 | 66.7%         |
| short_error    | polsko2   |            72 |             24 | 66.7%         |
| short_error    | polsko3   |            72 |             12 | 83.3%         |
| short_error    | suwalsko1 |            72 |             27 | 62.5%         |
| short_error    | suwalsko2 |            72 |             29 | 59.7%         |
| short_error    | suwalsko3 |            72 |             34 | 52.8%         |
| short_error    | terse-en  |            72 |             13 | 81.9%         |
| short_notfound | polsko1   |            66 |             27 | 59.1%         |
| short_notfound | polsko2   |            66 |             26 | 60.6%         |
| short_notfound | polsko3   |            66 |             11 | 83.3%         |
| short_notfound | suwalsko1 |            66 |             23 | 65.2%         |
| short_notfound | suwalsko2 |            66 |             32 | 51.5%         |
| short_notfound | suwalsko3 |            66 |             38 | 42.4%         |
| short_notfound | terse-en  |            66 |             17 | 74.2%         |
| mid_explain    | polsko1   |           118 |             49 | 58.5%         |
| mid_explain    | polsko2   |           118 |             47 | 60.2%         |
| mid_explain    | polsko3   |           118 |             27 | 77.1%         |
| mid_explain    | suwalsko1 |           118 |             47 | 60.2%         |
| mid_explain    | suwalsko2 |           118 |             55 | 53.4%         |
| mid_explain    | suwalsko3 |           118 |             76 | 35.6%         |
| mid_explain    | terse-en  |           118 |             41 | 65.3%         |
| mid_install    | polsko1   |           151 |             57 | 62.3%         |
| mid_install    | polsko2   |           151 |             48 | 68.2%         |
| mid_install    | polsko3   |           151 |             38 | 74.8%         |
| mid_install    | suwalsko1 |           151 |             63 | 58.3%         |
| mid_install    | suwalsko2 |           151 |             62 | 58.9%         |
| mid_install    | suwalsko3 |           151 |             82 | 45.7%         |
| mid_install    | terse-en  |           151 |             45 | 70.2%         |
| long_review    | polsko1   |           259 |            124 | 52.1%         |
| long_review    | polsko2   |           259 |             85 | 67.2%         |
| long_review    | polsko3   |           259 |             53 | 79.5%         |
| long_review    | suwalsko1 |           259 |            111 | 57.1%         |
| long_review    | suwalsko2 |           259 |            111 | 57.1%         |
| long_review    | suwalsko3 |           259 |            164 | 36.7%         |
| long_review    | terse-en  |           259 |             88 | 66.0%         |
| long_arch      | polsko1   |           251 |            131 | 47.8%         |
| long_arch      | polsko2   |           251 |             96 | 61.8%         |
| long_arch      | polsko3   |           251 |             41 | 83.7%         |
| long_arch      | suwalsko1 |           251 |            120 | 52.2%         |
| long_arch      | suwalsko2 |           251 |            111 | 55.8%         |
| long_arch      | suwalsko3 |           251 |            150 | 40.2%         |
| long_arch      | terse-en  |           251 |             99 | 60.6%         |
