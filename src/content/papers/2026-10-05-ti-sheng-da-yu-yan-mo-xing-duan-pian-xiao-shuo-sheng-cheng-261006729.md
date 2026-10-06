---
title: Improving Diversity in LLM Short Story Generation
title_zh: 提升大语言模型短篇小说生成的多样性
authors:
- Zahra Solati Dehkordi
- Vasileios Lampos
affiliations:
- University College London, UK
- UCL Centre for Artificial Intelligence
- UCL Department of Computer Science
arxiv_id: '2610.06729'
url: https://arxiv.org/abs/2610.06729
pdf_url: https://arxiv.org/pdf/2610.06729
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: LLM生成优化 · 多样性提升
tags:
- LLM
- Diversity
- Post-training
- Reinforcement Learning
- Creative Generation
one_liner: 提出两阶段后训练框架DivLM，在保障生成质量的同时提升LLM短篇小说生成的多维度多样性
practical_value: '- 电商文案、商品卖点生成场景可复用两阶段后训练范式：先领域语料继续预训练+权重残差保指令跟随能力，再RL优化多样性，解决内容同质化问题

  - 多维度复合奖励函数设计思路可直接迁移：优化生成多样性的同时，约束内容质量、对齐度等业务指标，避免为了多样性损失效果

  - Agent营销方案、个性化话术生成等创意任务，可直接复用DivLM的多样性优化逻辑，提升输出差异化程度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM生成内容同质化问题突出，指令微调和RLHF等对齐流程会让输出分布向高奖励的典型内容收敛，无法满足短篇小说等创意生成场景的多维度差异化需求。
### 方法关键点
提出两阶段DivLM后训练框架：
1. 第一阶段在创意写作语料上做继续预训练，同时引入权重残差机制保留模型原有指令跟随能力，避免领域预训练后的通用能力退化
2. 第二阶段基于自定义复合奖励函数做RL优化，同时对体裁、语气、风格、命名实体4个维度的多样性做最大化，同时约束生成质量不下降
### 关键结果
在两个不同LLM系列上做验证，相比现有基线方法，多样性指标平均提升9%以上，同时完全保留指令跟随能力、整体生成质量与人写内容的相似度。
