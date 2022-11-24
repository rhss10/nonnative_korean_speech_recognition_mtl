## 해야 될 실험들 (221124 16:37 기준)
0. CSV 기준: 소분류, 과제, train, valid, test
1. BASELINE
    - (1) STL,L2 250시간(각 17초 이하), L2 전부(각 17초 이하) 50%, L2 전부(각 17초 이하) 50%
    - (2) STL,L1 125시간(각 17초 이하) + L2 125시간(각 17초 이하), L2 전부(각 17초 이하) 50%, L2 전부(각 17초 이하) 50% **===> 류형신**
    - (3) STL,L1 250시간(각 17초 이하), L2 전부(각 17초 이하) 50%, L2 전부(각 17초 이하) 50% **===> 이선우**
2. PROPOSED METHODS
    - (1) MTL,L1 125시간(각 17초 이하) + L2 125시간(각 17초 이하), L2 전부(각 17초 이하) 50%, L2 전부(각 17초 이하) 50%
    - (2) MTL,L2 250시간(각 17초 이하), L2 전부(각 17초 이하) 50%, L2 전부(각 17초 이하) 50%
    - (3) X ==> L1 은 분류할 게 없음
3. ABLATION
    - (1) STL,L2 영어 180시간(각 17초 이하), 영어 전부(각 17초 이하), L2 나머지(각 17초 이하)
    - (2) STL,L2 일본어 250시간(각 17초 이하), 일본어 전부(각 17초 이하), L2 나머지(각 17초 이하)
    - (3) .... ==> 시간 남을 경우

## 코드
0. 통일한 파라미터: --num_epochs 50 **--num_classes 6** --csv_path dataset.csv **--batch_size 16**
1. STL: -ctc_weight 1.0 --cls_weight 0.0
2. MTL: --cls_weight 0.5 --ctc_weight 1.0 --enable_cls_epochs 0 ==> **좋은 결과 나올때까지 계속 조정**
