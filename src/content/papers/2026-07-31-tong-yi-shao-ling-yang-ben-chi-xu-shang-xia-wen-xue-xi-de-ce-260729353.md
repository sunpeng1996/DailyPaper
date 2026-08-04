---
title: Versatile On-device Adaptation at the Edge by Unifying Few-shot, Zero-shot,
  Continual, and In-context Learning
title_zh: 统一少/零样本/持续/上下文学习的灵活边缘端侧适配框架
authors:
- Douwe den Blanken
- Martin Lefebvre
- Charlotte Frenkel
arxiv_id: '2607.29353'
url: https://arxiv.org/abs/2607.29353
pdf_url: https://arxiv.org/pdf/2607.29353
published: '2026-07-31'
collected: '2026-08-04'
category: Training
direction: 端侧自适应 · 多学习范式统一
tags:
- On-device Learning
- Few-shot Learning
- Zero-shot Learning
- Continual Learning
- In-context Learning
- Edge AI
one_liner: 提出embedder-centric learning框架，统一4类学习场景，实现低功耗资源受限端侧自适应
practical_value: '- 端侧个性化推荐场景可复用ECL的embedder核心设计，无需云侧重训即可实现Few-shot用户偏好适配，降低隐私风险和响应延迟

  - 多学习范式统一的架构思路可迁移到端侧Agent，同一套框架支持冷启动Zero-shot推荐、持续用户兴趣更新、上下文实时调整三类需求

  - 低功耗端侧部署的优化经验可参考，适用于智能音箱、穿戴设备端的电商push文案、商品推荐的本地化适配'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前边缘智能设备多依赖固定预训练模型，端侧自适应仅支持单一学习场景，云侧重训存在延迟高、能耗大、隐私泄露风险，无法满足端侧实时个性化需求。
### 方法关键点
提出embedder-centric learning（ECL）框架，统一四类在线学习范式：Few-shot Learning实现即时定制、Continual Learning实现知识积累、Zero-shot Learning利用语义数据、In-context Learning适配分类外任务，可直接部署在资源受限的端侧硬件上。
### 关键结果
- Omniglot字符识别5-way 1-shot精度96.8%、32-way 1-shot精度83.3%，达Few-shot SOTA
- 关键词 spotting 持续学习200-way 5-shot精度71.8%，为首个硬件基线
- Zero-shot语音句子分类5-way精度60.6%、In-context Learning RegBench第500token精度46.2%，功耗仅微瓦到毫瓦级
