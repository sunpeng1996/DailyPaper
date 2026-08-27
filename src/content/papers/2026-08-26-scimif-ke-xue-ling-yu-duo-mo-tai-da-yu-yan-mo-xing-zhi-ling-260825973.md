---
title: 'SciMIF: Understanding Multimodal Instruction Following in Scientific Domains'
title_zh: SciMIF：科学领域多模态大语言模型指令遵循能力评估基准
authors:
- Ye Shen
- Yuting Zheng
- Dun Pei
- Zijian Chen
- Wenlong Zhang
- Qi Jia
- Guangtao Zhai
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
arxiv_id: '2608.25973'
url: https://arxiv.org/abs/2608.25973
pdf_url: https://arxiv.org/pdf/2608.25973
published: '2026-08-26'
collected: '2026-08-27'
category: Eval
direction: 多模态大模型 · 科学领域能力评估
tags:
- MLLM
- Instruction Following
- Benchmark
- Scientific LLM
- Multimodal Evaluation
one_liner: 构建覆盖5大学科22类任务的科学多模态指令遵循评估基准SciMIF，揭示现有MLLM性能短板
practical_value: '- 可复用其「基于约束分类体系的指令注入流水线」，快速扩充电商商品、广告素材等垂类的多模态指令微调数据集，提升垂域MLLM指令遵循准确率

  - 其“模型参数缩放不必然提升约束遵循能力”的结论可指导垂域MLLM选型，无需盲目追大模型，优先针对细粒度约束做对齐优化

  - 针对广告合规文案生成、商品参数问答等需严格遵循规则的业务场景，可参考其10类约束分组思路设计评估用例，提前校验输出合规性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有科学领域MLLM评估多聚焦事实类问答任务，缺乏对复杂指令遵循能力的系统性评测，无法适配科学Agent、AI驱动科研等复杂场景的模型能力校验需求。
### 方法关键点
1. 分析5个代表性科学学科的22类差异化任务，提出包含10组约束的分类体系，同时覆盖通用功能要求与学科专属特性；
2. 基于上述分类体系开发高保真指令注入流水线，可对现有科学数据集做系统性扩充生成评测样本；
3. 对多款开源/闭源SOTA MLLM开展全面评测。
### 关键结果
不同学科性能差异显著，化学类任务对现有MLLM挑战最大；模型规模提升未带来约束遵循能力的对应提升，现有模型在细粒度约束、需深度应用学科知识的指令上表现极差。
