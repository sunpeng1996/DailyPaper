---
title: Design of the IBM Granite 5.0 TurboCTC ASR Model
title_zh: IBM Granite 5.0 TurboCTC 自动语音识别模型设计
authors:
- Brian Kingsbury
- George Saon
- Masayuki Suzuki
- Hong-Kwang J. Kuo
- Takashi Fukuda
- Samuel Thomas
- Vishal Sunder
- Avihu Dekel
affiliations:
- IBM Research
arxiv_id: '2609.20104'
url: https://arxiv.org/abs/2609.20104
pdf_url: https://arxiv.org/pdf/2609.20104
published: '2026-09-17'
collected: '2026-09-18'
category: Other
direction: 语音识别 · ASR速度精度权衡优化
tags:
- ASR
- Conformer
- CTC
- Model Optimization
- Muon Optimizer
one_liner: 470M参数量encoder-only ASR模型，速度达同精度最快竞品2倍
practical_value: '- 序列模型训练可尝试引入Muon优化器替代传统AdamW，验证是否能在不损失精度的前提下降低训练开销

  - 序列模型推理提速可复用两个通用trick：将1×1卷积替换为线性层、优化Conformer块的注意力计算逻辑

  - 电商语音搜索、直播实时字幕等低延迟ASR场景，可直接选型该开源可商用模型，兼顾精度与速度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有结合LLM的ASR方案参数量大、推理延迟高，大量仅需语音转文字的场景对高性价比低延迟ASR需求迫切

### 方法关键点
1. 架构为470M参数量encoder-only Conformer结构，采用带步长深度卷积实现金字塔时间下采样、块对角（分块）自注意力、中层中间预测作为条件约束
2. 训练仅用公开数据，首次引入Muon优化器搭配平衡数据采样策略
3. 推理侧做两项针对性优化：将1×1卷积替换为线性层、优化Conformer块的注意力计算逻辑

### 关键结果数字
在英文短语音Open ASR榜单上处于速度-精度帕累托最优区间，推理速度是同精度最快竞品的2倍，开源且可商用
