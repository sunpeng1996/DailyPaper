---
title: What Do Tabular Foundation Models Compute In Context? In-Situ Representation
  Refinement through Attention-Gated Updates
title_zh: 表格基础模型上下文计算机制：基于注意力门控更新的原位表征优化
authors:
- Tian Zhou
- Beverly Jin
- Linxiao Yang
- Xue Wang
- Wenwei Wang
- Bingqing Peng
- Mengni Ye
- Jinjie Gu
- Liang Sun
affiliations:
- Ant Group
- Independent Researcher
arxiv_id: '2609.27679'
url: https://arxiv.org/abs/2609.27679
pdf_url: https://arxiv.org/pdf/2609.27679
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: 表格大模型 · 上下文学习优化
tags:
- Tabular Foundation Model
- In-Context Learning
- Attention Gating
- Low-Rank Feature Interaction
- Representation Refinement
one_liner: 提出无FFN的注意力门控上下文学习框架RefineICL，大幅提升表格基础模型的任务适配性能
practical_value: '- 推荐/广告场景的小样本冷启动任务可借鉴注意力门控原位表征更新思路，无需微调模型即可快速适配新类目、新用户群的预测需求

  - 线上高并发推理场景可复用无FFN的低秩特征交互架构，在效果无损的前提下降低60%左右的推理峰值内存占用

  - 小样本表格预测类任务可引入留一法正则化目标优化上下文学习能力，降低对新任务标注数据量的要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有表格基础模型的上下文学习计算范式不清晰，每张新表格对应独立监督任务，亟需无需微调参数即可快速适配新任务的通用能力。
### 方法关键点
提出原位表征优化范式，通过支持集标签引导当前episode的表征更新，无需修改模型参数即可迁移到无标注查询样本；基于正则化留一法目标推导支持集校正与查询扩展项，拆分注意力读取与状态依赖缩放逻辑，设计无FFN的RefineICL上下文堆叠架构，融合低秩特征交互与类型化记忆模块。
### 关键结果
- RefineICL-L24在AMLB29数据集上OVR-AUC达0.93836，准确率达0.87173
- TabArena 38数据集上Elo得分达1644.8，较同设置下的TabPFN-3高31.4
- L8层结构下，对比带FFN的版本推理峰值内存低60.2%，效果无一致性损失
