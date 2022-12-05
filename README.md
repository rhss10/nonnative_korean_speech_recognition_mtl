## 진행한 실험들
1. BASELINE

|Model|Train|Dev|Test|
|----|-----|------|------|
| STL | AIHUB-NONNATIVE/Train L2 250시간(각 17초 이하) | AIHUB-NONNATIVE/Validation L2(각 17초 이하) 50% | AIHUB-NONNATIVE/Validation L2 (각 17초 이하) 50% |
| STL | Ksponspeech/Train L1 125시간(각 17초 이하) + AIHUB-NONNATIVE/Train L2 125시간(각 17초 이하) | AIHUB-NONNATIVE/Validation L2 (각 17초 이하) 50% | AIHUB-NONNATIVE/Validation L2 (각 17초 이하) 50% |
| STL | Ksponspeech/Train L1 250시간(각 17초 이하) | AIHUB-NONNATIVE/Validation L2(각 17초 이하) 50% | AIHUB-NONNATIVE/Validation L2 (각 17초 이하) 50% |

2. PROPOSED METHODS

|Model|Train|Dev|Test|
|----|-----|------|------|
| MTL | Ksponspeech/Train L1 125시간(각 17초 이하) + AIHUB-NONNATIVE/Train L2 125시간(각 17초 이하) | AIHUB-NONNATIVE/Validation L2 (각 17초 이하) 50% | AIHUB-NONNATIVE/Validation L2 (각 17초 이하) 50% |
| MTL | AIHUB-NONNATIVE/Train L2 250시간(각 17초 이하) | AIHUB-NONNATIVE/Validation L2 전부(각 17초 이하) 50% | AIHUB-NONNATIVE/Validation L2 전부(각 17초 이하) 50% |

3. ABLATION STUDY

|Model|Train|Dev|Test|
|----|-----|------|------|
|STL| L2 일본어 250시간(각 17초 이하) | 기존 Dev+Test의 일본인 한국어 전부(각 17초 이하) | 나머지 Dev+Test (각 17초 이하)|
|MTL| L2 75 시간 (베트남어+영어+일본어 각 17초 이하) | 각 언어 발화 1000개 (각 17초 이하) | 각 언어 발화 1000개 (각 17초 이하)|

<br></br>
## 코드
```bash
# Ex) For STL on L1+L2 train set
python train-fp16.py --num_epochs 15 --num_classes 6 --csv_path data/korean+nonnative/90ver_dataset.csv  --batch_size 8 --ctc_weight 1.0 --cls_weight 0.0 --prefix STL_L1+L2

# Ex) For MTL on L2 only train set with cls_loss_alpha=100, cls_loss_start_epoch=10
python train-fp16.py --num_epochs 15 --num_classes 6 --csv_path data/nonnative_korean/90ver_dataset.csv --batch_size 8 --ctc_weight 1.0 --cls_weight 100.0 --enable_cls_epochs 10 --prefix MTL_100_L2_FROM10

# Ex) For Ablation study on Japanese L2 train set
python train-fp16.py --num_epochs 15 --num_classes 6 --csv_path data/nonnative_korean_jp/90ver_dataset.csv --batch_size 8 --ctc_weight 1.0 --cls_weight 0.0 --prefix STL_JP_L2
```

