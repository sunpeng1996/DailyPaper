---
title: 'BDH-CQ: In-Context Learning with Recurrent Latent Reasoning'
title_zh: BDH-CQ：融合上下文学习与循环隐式推理的高效推理模型
authors:
- Björn Engdahl
- Adrian Kosowski
- Jan Chorowski
- Zuzanna Stamirowska
- Przemysław Uznański
- Junlin Jiang
- Rohan Phadke
- Remigiusz Kinas
- Richard Zhong
affiliations:
- Pathway
- Bielik AI
- New York University
arxiv_id: '2608.09888'
url: https://arxiv.org/abs/2608.09888
pdf_url: https://arxiv.org/pdf/2608.09888
published: '2026-08-10'
collected: '2026-08-11'
category: Reasoning
direction: 隐式推理 · 低成本上下文学习
tags:
- Latent Reasoning
- In-Context Learning
- ARC-AGI
- Recurrent Model
- Cost Efficiency
one_liner: 150M参数BDH-CQ在ARC-AGI-1达29.5% pass@2，成本仅$0.0007/任务，打破成本精度帕累托前沿
practical_value: '- 可复用循环隐式推理架构替代CoT，减少推理Token消耗，降低LLM驱动的推荐Query理解、Agent决策的推理延迟与成本，尤其适配高并发场景下的小参数模型推理优化

  - 借鉴上下文绑定机制，在少样本规则学习场景（如电商新品规则适配、个性化推荐规则动态更新）中用循环记忆存储示例特征，避免推理时KV cache膨胀

  - 参考推理effort动态调整精度/成本的设计，在推荐排序、广告创意生成场景可根据流量优先级动态分配推理算力，平衡效果与成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有CoT推理依赖生成中间自然语言Token，推理成本、延迟随推理步骤线性增长；而隐式推理与上下文学习长期割裂，无法仅通过推理时的示例完成未知任务的规则学习，亟需兼顾上下文灵活性与低成本的推理架构。
### 方法关键点
- 基于BDH后Transformer架构设计双循环结构：循环记忆模块逐示例更新，存储上下文学习到的任务规则，避免KV cache随上下文长度膨胀；隐式工作空间迭代执行推理，无中间Token输出。
- 训练数据混合ARC-AGI-1、ConceptARC、RE-ARC等公开数据集与私有 curated ARC风格样本，叠加数据增强提升泛化性。
- 支持推理时动态调整隐式推理步数，可在精度与成本之间灵活做trade-off。
### 关键结果
- 150M参数配置在ARC-AGI-1公开测试集上达到29.5% pass@2，推理成本仅$0.0007/任务，比同精度的GPT 5.6 Luna低11倍，打破此前的成本-精度帕累托边界。
- 边界传播、复制等简单算子可完美外推至超出示例的复杂度，排序、嵌套规则存在明显能力边界，补充对应复杂度的示例可将深度5嵌套任务的准确率从79%提升至100%。

> 最值得记住的一句话：小参数模型通过循环隐式推理可实现远低于大模型CoT的推理成本，同时保留上下文学习的灵活适配能力，是高并发AI业务落地的重要技术方向。
