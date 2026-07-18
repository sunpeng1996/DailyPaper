---
title: On Locality and Length Generalization in Visual Reasoning
title_zh: 视觉推理中的局部性与长度泛化能力研究
authors:
- Pulkit Madan
- Sanjay Haresh
- Reza Ebrahimi
- Sunny Panchal
- Apratim Bhattacharyya
- Roland Memisevic
affiliations:
- Qualcomm AI Research
arxiv_id: '2607.09061'
url: https://arxiv.org/abs/2607.09061
pdf_url: https://arxiv.org/pdf/2607.09061
published: '2026-07-09'
collected: '2026-07-18'
category: Reasoning
direction: 视觉推理 · 长度泛化能力优化
tags:
- Visual Reasoning
- Length Generalization
- Local Attention
- Compositional Generalization
- Recurrent Vision Policy
one_liner: 提出基于严格局部感知的循环视觉策略，解决全局CV模型长度泛化失效问题
practical_value: '- 多模态商品理解/生成式推荐场景可替换全局注意力为Local Attention循环策略，提升长商品列表、复杂组合推荐的泛化鲁棒性

  - 多模态Agent的视觉交互模块加入局部感知约束，避免模型依赖训练分布全局捷径，提升陌生场景推理准确率

  - 训练跨域多模态召回模型时，引入Local Attention设计可降低对域内全局特征的依赖，减少跨域效果衰减'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有主流CV模型采用全局一次性输入范式，易学习训练分布内的全局捷径，当任务长度、复杂度提升时泛化能力大幅下降，类人局部序列式视觉处理的实际计算价值尚未被验证。
### 方法关键点
受LLM Length Generalization相关研究启发，设计一系列需要聚合图像全图局部信息的简单视觉推理任务，对比全局视觉模型与基于严格局部感知的循环视觉策略在任务上的泛化表现。
### 关键结果
全局视觉模型普遍存在任务长度/复杂度泛化失效问题；基于严格局部感知的循环视觉策略可完全缓解该类失效，证明Local Attention是实现鲁棒组合泛化的核心被忽略要件。
