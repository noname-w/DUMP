# Protocols for private-preserving histogram estimation in shuffle model

This project contains 7 protocols of private-preserving histogram estimation in shuffle model.

## Requirement

Python 3 with the numpy, xxhash, and scipy.linalg libraries.

## Protocol

|    Protocol     |                        Related paper                         |
| :-------------: | :----------------------------------------------------------: |
|    pureDUMP     | DUMP: A Dummy-Point-Based Framework with Improved Utility and Privacy for Histogram Estimation in Shuffle Model |
|     mixDUMP     | DUMP: A Dummy-Point-Based Framework with Improved Utility and Privacy for Histogram Estimation in Shuffle Model |
|  shuffle_based  | The Privacy Blanket of the Shuffle Model (https://link.springer.com/chapter/10.1007/978-3-030-26951-7_22) |
| private_shuffle | Separating Local & Shuffled Differential Privacy via Histograms (https://arxiv.org/abs/1911.06879) |
|  private_coin   | On the Power of Multiple Anonymous Messages (https://eprint.iacr.org/2019/1382.pdf) |
|   public_coin   | On the Power of Multiple Anonymous Messages (https://eprint.iacr.org/2019/1382.pdf) |
|      SOLH       | Improving utility and security of the shuffler based differential privacy (https://dl.acm.org/doi/abs/10.14778/3424573.3424576) |

## Run

```
python test.py
```

(Note that the private_coin protocol requires that the size of data domian must be a number based on 2)