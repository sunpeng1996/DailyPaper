---
title: 'From Surface to Depth: Towards Cognitive Appraisal Reasoning in Multimodal
  Emotion Understanding'
title_zh: 从表层到深度：面向多模态情感理解的认知评价推理
authors:
- Jia Li
- Yichao He
- Yangchen Yu
- Qiankun Li
- Xinyi Li
- Baiyi Ye
- Zhenzhen Hu
- Richang Hong
- Erik Cambria
affiliations:
- Hefei University of Technology
- Nanyang Technological University
arxiv_id: '2610.11918'
url: https://arxiv.org/abs/2610.11918
pdf_url: https://arxiv.org/pdf/2610.11918
published: '2026-10-08'
collected: '2026-10-10'
category: Multimodal
direction: 多模态大模型 · 情感认知推理
tags:
- Multimodal LLM
- Emotion Understanding
- MoE
- Instruction Tuning
- Benchmark
one_liner: 提出认知评价驱动的多模态情感理解范式，配套指令数据集、轻量MoE模型与可解释评测基准
practical_value: '- 电商商品评价、广告素材情感分析场景可复用6维认知评价拆分思路，避免仅依赖表层特征误判，提升细粒度情感识别准确率

  - 垂域多模态模型优化可参考interleaved MoE块做任务专属适配，用更小参数量实现超过通用MLLM的垂域效果

  - 情感相关的推荐、客服Agent任务可借鉴AEQS思路，构建「结果+推理依据」双维度评测体系，而非仅评估预测准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态大模型的情感推理仅依赖表层可观测线索，易出现Clever Hans效应，在线索隐含、跨模态冲突、语言误导等场景可靠性差；传统情感指标仅评估预测结果，无法解释情感产生原因。
### 方法关键点
1. 受情绪评价理论启发，将多模态情感理解建模为从感知到认知评价的递进过程
2. 构建CogEmo-40K指令微调数据集，覆盖6类认知评价维度的证据支撑推理
3. 提出CogEmo-MoE轻量稀疏MLLM，通过interleaved MoE块实现评价维度专属适配
4. 发布CogEmo-Bench基准，用AEQS指标同时评估情感预测结果与推理依据质量
### 关键结果
CogEmo-MoE在CogEmo-Bench上AEQS达70.60，远超GPT-5.2的56.30；情感分类准确率71.43%、M-F1 57.17%，均优于Qwen3-Omni，且跨域泛化性优异。
