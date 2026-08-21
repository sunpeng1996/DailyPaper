---
title: Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization
  for Multimodal Sarcasm Detection
title_zh: 面向多模态反讽检测的动态门控跨模态融合与反讽感知正则方法
authors:
- Hao Guo
- Subin Huang
- Junjie Chen
- Zhifa Geng
- Sanmin Liu
- Chao Kong
affiliations:
- Anhui Polytechnic University
arxiv_id: '2608.19942'
url: https://arxiv.org/abs/2608.19942
pdf_url: https://arxiv.org/pdf/2608.19942
published: '2026-08-20'
collected: '2026-08-21'
category: Multimodal
direction: 多模态语义理解 · 反讽检测
tags:
- Multimodal Fusion
- Contrastive Learning
- Sarcasm Detection
- Gated Mechanism
- Cross-Modal Learning
one_liner: 提出结合动态门控跨模态融合与反讽感知对比正则的检测框架，性能优于现有基线
practical_value: '- 电商UGC内容审核、反讽差评识别等跨模态理解场景，可复用动态门控融合方法，自适应调整单模态特征权重，适配不同样本的模态贡献差异

  - 涉及语义冲突的识别任务（如虚假宣传检测、反向吐槽识别）可引入标签感知对比正则策略，对正负样本设置差异化跨模态对齐约束

  - 多模态模型训练时可加入单模态监督辅助目标，提升多模态表征鲁棒性，降低跨模态噪声干扰'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态反讽检测需识别内容字面义与上下文的隐含矛盾，现有方法采用固定融合策略，无法适配样本级模态贡献差异，且表面语义对齐易掩盖反讽样本的深层意图冲突，导致检测精度不足。

### 方法关键点
1. 双向门控交互模块做跨模态特征过滤，实例级自适应校准文本、视觉特征的贡献占比，再通过动态融合门生成鲁棒多模态表征；
2. 提出反讽感知对比正则（SaCR），对非反讽样本鼓励跨模态语义一致，对反讽样本抑制误导性的表面语义对齐；
3. 端到端多目标训练，联合优化多模态分类损失与单模态监督辅助损失。

### 关键结果
在MMSD、MMSD2.0两个公开多模态反讽检测数据集上，性能全面优于现有强基线模型。
