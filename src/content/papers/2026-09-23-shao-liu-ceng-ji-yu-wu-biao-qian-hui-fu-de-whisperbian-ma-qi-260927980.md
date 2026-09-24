---
title: 'Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery'
title_zh: 少六层：基于无标签恢复的Whisper编码器剪枝方法
authors:
- Rasmus Aagaard
- Nicki Skafte Detlefsen
affiliations:
- Technical University of Denmark
- Laerdal Medical
arxiv_id: '2609.27980'
url: https://arxiv.org/abs/2609.27980
pdf_url: https://arxiv.org/pdf/2609.27980
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 大模型压缩 · 编码器剪枝与无标签蒸馏
tags:
- Model Pruning
- Whisper
- ASR
- Knowledge Distillation
- Label-free Training
one_liner: 通过留一法WER排序剪去Whisper编码器6层，无标签蒸馏恢复性能，无需自定义推理代码
practical_value: '- 可复用留一法按业务核心指标（如推荐NDCG、电商转化率）排序剪Transformer冗余层，剪后模型兼容原推理框架，无需改代码降低部署成本

  - 剪枝后的性能掉点可采用领域无标签数据蒸馏恢复，大幅节省标注成本，适合电商语音导购、语音搜索场景的ASR模型轻量化

  - 该剪枝方案可直接落地端侧语音交互Agent的ASR模块，降低推理延迟，提升语音交互响应速度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Whisper类ASR大模型压缩方案多针对解码器优化，编码器剪枝方案因需自定义推理代码难以大规模落地，亟需低成本可直接复用原框架的编码器压缩方法。
### 方法关键点
1. 采用留一层法计算单编码器层移除后的WER变化，排序后移除对WER影响最小的6层（占编码器总层数的18.5%），剪枝后模型结构完全兼容原推理框架，无需自定义实现；
2. 引入无标签单语种语音数据做知识蒸馏，恢复剪枝带来的性能损失。
### 关键结果
原模型基线平均WER为18.2%，零样本剪枝后平均WER为21.9%，经无标签蒸馏后降至20.1%，仅比基线高1.9个百分点，编码器体积缩减18.5%，推理速度同步提升。
