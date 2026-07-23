---
title: 'Computational Humor with Multimodal LLMs: Methods, Datasets, Evaluation, and
  Challenges'
title_zh: 多模态大模型计算幽默研究综述：方法、数据集、评估与挑战
authors:
- Tuo Liang
- Zhe Hu
- Disheng Liu
- Jing Li
- Yu Yin
affiliations:
- Case Western Reserve University
- The Hong Kong Polytechnic University
arxiv_id: '2607.19011'
url: https://arxiv.org/abs/2607.19011
pdf_url: https://arxiv.org/pdf/2607.19011
published: '2026-07-20'
collected: '2026-07-23'
category: Multimodal
direction: 多模态大模型 · 计算幽默研究综述
tags:
- MLLM
- Computational Humor
- Survey
- Multimodal Alignment
- Evaluation
one_liner: 系统梳理多模态幽默研究脉络、基准与建模范式，指明领域现存瓶颈与演进方向
practical_value: '- 电商趣味营销、广告创意生成场景可复用多模态幽默的受控生成范式，提升素材吸引力

  - 社交内容推荐、梗图理解场景可借鉴多模态幽默识别的模态对齐+evidence grounding方案提升准确率

  - 内容风控场景可参考该领域评估设计思路，规避检测shortcut，提升隐含讽刺/低俗幽默识别效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
梗图、漫画、卡通等多模态幽默内容的语义依赖非字面表达、共有文化知识与沟通意图，现有MLLM对这类隐含语义的处理能力存在明显短板，领域缺乏系统性的研究梳理。
### 方法关键点
以能力为核心搭建三层研究框架：识别、解释与推理、生成，对比此前幽默、讽刺与通用MLLM综述的差异，梳理领域从任务专属融合模型到基于多模态对齐、evidence grounding、受控生成的大模型方案的演进路径，整合基准设计、评估协议、建模范式的相关研究。
### 关键结果
明确当前领域四大核心瓶颈：易存在shortcut的评估体系、文化与叙事覆盖范围有限、evidence grounding能力薄弱、安全与版权归属问题未解决。
