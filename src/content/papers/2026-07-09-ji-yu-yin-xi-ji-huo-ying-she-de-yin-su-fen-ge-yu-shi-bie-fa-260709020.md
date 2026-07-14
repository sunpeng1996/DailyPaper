---
title: Phone Segmentation and Recognition through Phonological Activation Mapping
title_zh: 基于音系激活映射的音素分割与识别方法
authors:
- Shikhar Bharadwaj
- Kwanghee Choi
- Stephen McIntosh
- Chin-Jou Li
- Eunjung Yeo
- Daisuke Saito
- Nobuaki Minematsu
- Shinji Watanabe
- Jian Zhu
- David Harwath
affiliations:
- CMU
- UT Austin
- UTokyo
- UBC
arxiv_id: '2607.09020'
url: https://arxiv.org/abs/2607.09020
pdf_url: https://arxiv.org/pdf/2607.09020
published: '2026-07-09'
collected: '2026-07-14'
category: Other
direction: 低资源语音处理 · 音素分割与识别
tags:
- Self-Supervised Learning
- Phoneme Segmentation
- Phoneme Recognition
- Low-Resource Speech
- Speech Processing
one_liner: 基于自监督语音模型的音系激活映射加无梯度轻量头，实现低标注需求的音素分割与识别
practical_value: '- 低资源小样本任务可参考其「挖掘预训练模型隐层已有特征+无梯度轻量头」的架构，大幅降低标注需求与训练成本

  - 做多模态/语音交互类电商业务（如语音搜品、口语化query理解、口音适配）时，可复用SPAM框架实现低标注成本的音素处理

  - 小样本下需要做OOV类泛化的任务，可借鉴其用底层基础特征组合生成未见过的目标类的思路'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
音素分割与识别是语音处理的基础任务，现有方案通常将两个任务分开建模，且依赖大量专家标注：1小时语音需40~100小时的专家标注成本，低资源语种/场景落地难度极高。
### 方法关键点
1. 挖掘自监督语音模型（S3Ms）隐层天然存在的音系结构特征，搭建SPAM模块将每帧S3M表征映射为清浊、鼻音等通用音系特征激活向量；
2. 顶层新增两个无需梯度下降的轻量预测头，分别适配识别、分割任务，无需微调S3M主干；
3. 训练仅需不到1分钟的音素转录标注，支持训练阶段未出现的音素的少样本泛化。
### 关键结果
覆盖多语种、多场景的各类数据集上，均取得比肩全监督方案的音素分割与识别性能
