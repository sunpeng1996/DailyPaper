---
title: 'SeGDeP: Semantic- and Geometric-Aware Decoupled Prompts for Reasoning Segmentation'
title_zh: SeGDeP：面向推理分割的语义与几何感知解耦提示方法
authors:
- Linnan Zhao
- Xu Liu
- Lingling Li
- Licheng Jiao
- Fang Liu
- Wenping Ma
affiliations:
- Xidian University
arxiv_id: '2609.08867'
url: https://arxiv.org/abs/2609.08867
pdf_url: https://arxiv.org/pdf/2609.08867
published: '2026-09-08'
collected: '2026-09-10'
category: Multimodal
direction: 多模态大模型 · 推理分割性能优化
tags:
- MLLM
- LoRA
- SAM
- Segmentation
- Policy Optimization
- Multimodal
one_liner: 提出语义几何双分支解耦的推理分割框架SeGDeP，仅微调0.38%参数即达SOTA性能
practical_value: '- 多模态任务解耦设计可复用：电商商品图像语义识别+定位任务可拆分语义/几何双分支，降低排障难度，提升两类子任务性能

  - 低参微调方案可借鉴：针对MLLM下游任务仅微调0.38%参数的LoRA配置，可复用在电商多模态理解场景降低训练成本

  - 多奖励平衡策略GDPO可迁移：多目标优化场景下分组解耦奖励的强化学习策略，可用于搜索推荐多指标平衡任务'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM与分割器的交互接口将语义识别、空间定位信号耦合，无法区分错误来自目标语义理解还是空间定位，同时两类任务监督信号差异大，耦合训练难以兼顾性能。
### 方法关键点
1. 设计双分支解耦接口SeGDeP，语义提示分支输出语义特征，独立几何投影路径输出DETR预测框，联合作为SAM 3掩码解码器的输入；
2. 采用两阶段训练，先对齐可执行接口，再用分组奖励解耦策略优化（GDPO）平衡格式、框IoU、掩码IoU三类反馈；
3. 仅通过LoRA微调Qwen3-VL 0.38%的参数。
### 关键结果数字
SeGDeP-4B在8个RefCOCO系列数据集split上平均cIoU达82.7，在ReasonSeg验证/测试集上gIoU达66.0/59.6，性能优于现有耦合设计方案。
