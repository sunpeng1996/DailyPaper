---
title: 'TinyCNNDeep: Lightweight Attention-Based CNN for EEG Classification of Eye
  States and Sleep Deprivation'
title_zh: 'TinyCNNDeep: Lightweight Attention-Based CNN for E'
authors:
- Thien Nhan Vo
- Yen Nhi Tran Thi
- Ngan Nguyen Xuan Phuong
- Xuan-The Tran
arxiv_id: '2606.26506'
url: https://arxiv.org/abs/2606.26506
pdf_url: https://arxiv.org/pdf/2606.26506
published: '2026-06-25'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Sleep deprivation impairs vigilance and cognitive function, yet jointly
  identifying the sleep c...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 摘要

Sleep deprivation impairs vigilance and cognitive function, yet jointly identifying the sleep condition (normal vs deprived) and the eye state (open vs closed) from electroencephalography (EEG) remains underexplored. We address this four-class problem with TinyCNNDeep, a lightweight convolutional neural network that combines residual learning with a Squeeze-and-Excitation (SE) attention module. We convert short multi-channel EEG segments from five physiologically relevant channels (Fp1, Fp2, O1, Oz, O2) into 224x224 grayscale images through per-channel Z-score normalization, min-max scaling, and center padding, enabling 2D convolutions to jointly model inter-channel and temporal structure. On a 35-subject dataset recorded under normal-sleep and sleep-deprivation sessions, TinyCNNDeep attains a subject-wise mean accuracy of 83.69%, outperforming the strongest baseline (Random Forest with combined time-frequency features, 47.66%) by 36.03 percentage points, while three established EEG architectures (EEGNet, ShallowConvNet, DeepConvNet) operate near chance. Per-subject analysis quantifies inter-subject variability, and confusion-matrix inspection shows that residual misclassifications concentrate between eyes-closed states across sleep conditions. These results indicate that an image-based EEG representation paired with residual feature extraction and channel attention provides an accurate and computationally efficient framework for multiclass sleep-related EEG classification under a minimal electrode configuration.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
