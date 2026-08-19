---
title: 'CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Guided
  Video Editing'
title_zh: CoinVE-200K：面向组合式指令引导视频编辑的大规模高质量数据集
authors:
- Fuchen Long
- Cong Wang
- Zitao Gao
- Wenhao Zhong
- Yu Cheng
- Xiaolu Hou
- Yan Li
- Xiao Cao
- Xinlong Sun
- Xi Chen
affiliations:
- Smart Creation Platform Department, Online Video BU, Tencent
arxiv_id: '2608.17566'
url: https://arxiv.org/abs/2608.17566
pdf_url: https://arxiv.org/pdf/2608.17566
published: '2026-08-17'
collected: '2026-08-19'
category: Multimodal
direction: 多模态 · 组合指令引导视频编辑数据集与模型
tags:
- Video Editing
- Multimodal Dataset
- Instruction Following
- Region-aware Attention
- Benchmark
one_liner: 发布200K规模组合式视频编辑数据集与基准，开源22B参数高精度多意图视频编辑模型
practical_value: '- 电商短视频批量生产场景可复用组合指令编辑思路，支持同时完成字幕添加、背景替换、商品修改等多操作批量生成，降低素材制作成本

  - 多意图指令理解的解耦region-aware注意力设计可迁移至多模态推荐的用户复杂query理解场景，精准识别用户多维度需求

  - 数据集生成+多维度质量过滤的pipeline可复用至多模态训练数据构造场景，保障指令对齐度、时序一致性等核心指标'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令驱动视频编辑数据集多聚焦单操作，无法支持同时包含多编辑意图的组合式视频编辑任务，也缺乏统一评估基准。

### 方法关键点
1. 发布CoinVE-200K数据集，包含201帧以内的1080P视频编辑对，每个样本覆盖2~5种原子编辑操作，涉及人、物、背景的增删改、风格化等场景，经生成+过滤pipeline保障指令对齐度、视觉质量、时序一致性与组合多样性；
2. 配套推出CoinVE-Bench基准，覆盖不同编辑主体、操作类型、指令复杂度的评估场景；
3. 推出22B参数CoinVE-Edit模型，基于Wan2.1-T2V-14B与Qwen3-VL-8B构建，通过解耦区域感知注意力实现精准多区域编辑，保留无关内容与时序连贯性。

### 关键结果
在CoinVE-Bench上，CoinVE-Edit在指令遵循度、组合编辑准确率、视觉质量、时序一致性指标上均达到领先水平。
