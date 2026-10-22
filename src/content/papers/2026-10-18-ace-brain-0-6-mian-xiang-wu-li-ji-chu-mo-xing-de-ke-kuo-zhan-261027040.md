---
title: 'ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models'
title_zh: ACE-Brain-0.6：面向物理基础模型的可扩展空间定位能力构建
authors:
- Yinhe Wang
- Tao Tao
- Zexin He
- Shuang Luo
- Wei Mao
- Yao Mu
- Feng Pan
- Hanming Deng
- Lewei Lu
- Zhi Hou
affiliations:
- ACE-Brain Team
arxiv_id: '2610.27040'
url: https://arxiv.org/abs/2610.27040
pdf_url: https://arxiv.org/pdf/2610.27040
published: '2026-10-18'
collected: '2026-10-22'
category: Agent
direction: 具身Agent · 空间视觉定位优化
tags:
- Spatial Grounding
- Multimodal LLM
- Embodied Agent
- Fine-tuning
- Data Pipeline
one_liner: 基于150万多源可验证定位标注微调Qwen3.5-9B，整体空间定位性能优于GPT-6 Astra
practical_value: '- 多模态商品检索/AR导购场景可复用多源混合标注数据pipeline，用业务交互日志+公开视觉数据自动生成可验证的视觉grounding监督信号，降低标注成本

  - 小参数多模态基座优化可参考「固定基座+逐步扩充场景化标注数据」的迭代路线，保证性能随数据覆盖范围提升稳定增长

  - 电商直播/虚拟试穿等具身导购Agent的空间感知模块可复用该思路，针对交互场景优化空间定位能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
通用多模态大模型的具身操作能力高度依赖空间感知能力，而空间定位是连接高层推理与物理场景的核心环节，亟需构建可扩展的空间定位能力优化方案。
### 方法关键点
1. 搭建统一数据pipeline，融合机器人操作记录与多源互补视觉数据，自动标注后转换为可验证的定位监督信号
2. 基于150万该pipeline生成的样本对Qwen3.5-9B做微调，得到ACE-Brain-0.6
### 关键结果数字
在7个公开定位基准中4个超过GPT-6 Astra，整体平均得分75.41，高于Astra的73.68；固定微调设置下，模型定位性能随训练数据场景覆盖范围扩大稳定提升
