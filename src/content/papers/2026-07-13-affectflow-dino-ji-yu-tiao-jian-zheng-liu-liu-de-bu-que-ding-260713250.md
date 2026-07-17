---
title: 'AffectFlow-DINO: Uncertainty-Aware Multi-Task Affect Estimation via Conditional
  Rectified Flow'
title_zh: AffectFlow-DINO：基于条件整流流的不确定性感知多任务情感估计
authors:
- Salah Eddine Bekhouche
- Abdellah Zakaria Sellam
- Fadi Dornaika
- Abdenour Hadid
affiliations:
- University of the Basque Country (UPV/EHU)
- University of Salento
- Institute of Applied Sciences and Intelligent Systems (CNR)
- Universiti Malaysia Kelantan
arxiv_id: '2607.13250'
url: https://arxiv.org/abs/2607.13250
pdf_url: https://arxiv.org/pdf/2607.13250
published: '2026-07-13'
collected: '2026-07-17'
category: Other
direction: 多任务情感估计 · 整流流生成建模
tags:
- Multi-Task Learning
- Rectified Flow
- DINOv3
- Affect Estimation
- Imbalanced Classification
one_liner: 基于DINOv3与条件整流流的多任务人脸情感估计框架，解决标注歧义与类别不平衡问题，性能远超ABAW基线
practical_value: '- 多任务混合（连续值+分类）建模场景可复用条件整流流头替代确定性预测头，捕捉标注歧义，同时提升两类任务性能

  - 严重类别不平衡的分类任务可直接复用post-hoc阈值校准方法，无需重训练即可大幅提升稀有类识别效果

  - 大模型多任务落地可参考「冻结主干+轻量生成头+少量微调」的架构，大幅降低训练资源消耗'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
第11届ABAW多任务情感估计挑战存在三大痛点：多任务输出类型（连续值/分类）差异大、训练数据类别极不平衡（表情类8倍差距、动作单元类29倍差距）、野外人脸行为标注存在固有歧义，联合标注覆盖率仅37%。
### 方法关键点
1. 主干采用冻结的DINOv3 ViT-S/16，新增条件整流流头建模条件生成分布，通过蒙特卡洛采样实现不确定性感知的一对多预测
2. 联合完成连续valence-arousal估计、8类面部表情分类、12个Action Unit检测三个任务
3. 引入无需重训练的post-hoc阈值校准解决稀有类别不平衡问题
### 关键结果
- 整流流解码将valence-arousal估计CCC-V指标提升0.058
- 阈值校准将恐惧类等稀有类性能从3.8%提升至33.1%
- 最终模型P_MTL达1.177，远超官方基线的0.45
