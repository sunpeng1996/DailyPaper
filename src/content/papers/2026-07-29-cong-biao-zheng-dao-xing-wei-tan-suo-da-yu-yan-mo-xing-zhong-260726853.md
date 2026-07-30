---
title: 'From Representations to Behaviors: Exploring the Person-Situation-Behavior
  Triad in LLMs'
title_zh: 《从表征到行为：探索大语言模型中的人-情境-行为三元组》
authors:
- Ruikang Zhang
- Shuo Wang
- Qi Su
affiliations:
- Peking University
- Beijing Institute of Technology
arxiv_id: '2607.26853'
url: https://arxiv.org/abs/2607.26853
pdf_url: https://arxiv.org/pdf/2607.26853
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: LLM内部表征 · 人格特质建模
tags:
- LLM
- Sparse Autoencoder
- Personality Representation
- Internal Activation
- Behavior Modeling
one_liner: 基于人格三元框架构建LLM类人格表征发现、控制与验证体系，证实LLM存在可控的关联情境与行为的类人格特征
practical_value: '- 可复用SAE稀疏分解方法提取LLM内部用户/人格类表征，替代显式prompt注入实现更稳定的Agent人设控制，适合电商客服、导购Agent的人设对齐

  - 跨情境的特征干预方法可用于生成式推荐的个性化响应微调，在不同推荐场景下保持用户偏好一致性，减少人设漂移问题

  - 类人格特征的收益权衡结论可指导社交场景内容推送、商品推荐的策略制定，匹配不同特质用户的内容/商品偏好'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM人格相关研究仅聚焦prompt条件触发的外部输出表现，缺乏对内部人格相关表征的存在性、跨情境表达规律、表征到行为映射关系的机制性验证。
### 方法关键点
1. 适配Funder人格三元框架，将LLM分析维度划分为内部人格表征（Person）、特质响应触发上下文（Situation）、社交任务响应模式（Behavior）；
2. 基于同情境下的对比行为对，通过SAE分解提取人格特质两极对应的稀疏内部特征，从行为影响、token级激活模式、paraphrase鲁棒性三个维度验证特征相关性；
3. 对识别到的特征做干预，验证跨场景特质表达一致性，再迁移到社交智能任务完成行为级校验。
### 关键结果
证实LLM内部存在可控的类人格表征，特征干预可实现跨多样场景的双向特质偏移且不降低响应有效性，干预后行为变化的收益权衡模式完全匹配人类人格研究结论。
