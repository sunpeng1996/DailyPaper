---
title: 'Helping Music Co-Creation Agents ''Listen'' Well: Hierarchical Self-Supervised
  World Models for Understanding and Generation'
title_zh: 助力音乐协同创作Agent更好“聆听”：用于理解生成的分层自监督世界模型
authors:
- Scott H. Hawley
affiliations:
- Department of Chemistry & Physics, Belmont University
arxiv_id: '2608.04378'
url: https://arxiv.org/abs/2608.04378
pdf_url: https://arxiv.org/pdf/2608.04378
published: '2026-08-04'
collected: '2026-08-08'
category: Agent
direction: 协同创作Agent · 自监督世界模型
tags:
- World Model
- Self-Supervised Learning
- JEPA
- Flow Matching
- Symbolic Music
one_liner: 提出2.55M参数分层自监督世界模型，支撑音乐协同创作Agent的内容理解与生成，保留人类主导权
practical_value: '- 分层自监督JEPA目标+轻量监督头的架构可迁移至多模态内容创作Agent，用极小参数实现多粒度语义表征，降低端侧部署成本

  - 分层表征粒度匹配内容时间/结构尺度的结论可复用在短视频/直播内容推荐的多粒度用户兴趣建模中

  - 用条件流匹配模型替代训练解码器的范式，可降低生成式内容系统的训练成本，同时支持可控变异性与mask补全需求

  - 分层条件dropout控制生成变异程度的trick，可直接用在电商文案/商品图生成的可控性优化中'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
协同创作类Agent需要同时支撑内容理解与生成的高鲁棒性表征，且需保障人类在创作流程中的主导权，现有方案参数大、依赖领域先验标签，难以低延迟端侧部署。

### 方法关键点
1. 基于2.55M参数的Swin V2搭建分层自监督世界模型，采用JEPA训练目标（音高/时间平移等变性、掩码嵌入预测、分布正则化），无需标签与乐理先验；2. 可选轻量化监督头提升特定属性（和弦）识别能力；3. 采用条件流匹配模型替代训练解码器，基于分层条件dropout控制生成变异程度，无需专用采样器即可支持掩码补全。

### 关键结果数字
加小和弦监督头后，和弦恢复准确率从0.18升至0.54，无监督的调式检测准确率从0.16升至0.70；目标窗口生成像素F1达0.996；CPU推理耗时2.8s，Apple MPS仅0.6s。
