---
title: 'Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation'
title_zh: Rubric-CEPR：基于奖励验证自蒸馏的自进化图像编辑框架
authors:
- Ritesh Thawkar
- Shubham Patle
- Shravan Venkatraman
- Rao Muhammad Anwer
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Aalto University
arxiv_id: '2610.12469'
url: https://arxiv.org/abs/2610.12469
pdf_url: https://arxiv.org/pdf/2610.12469
published: '2026-10-08'
collected: '2026-10-09'
category: Other
direction: 自进化图像编辑 · 自蒸馏奖励验证
tags:
- Image Editing
- Self-Distillation
- Reward Verification
- Self-Evolution
- LoRA
one_liner: 提出无需人工标注与外部奖励的自进化图像编辑框架Rubric-CEPR，通过自蒸馏提升编辑效果
practical_value: '- 可复用分层rubric校验逻辑，对电商生成的商品主图、营销素材做多维度校验（编辑完成度、原始信息保留度），减少错误内容上线

  - 自蒸馏+轻量适配器训练思路可迁移到垂域生成模型迭代，无需额外人工标注即可基于历史优质生成样本优化现有生成器

  - Planner自动生成结构化指令的设计可借鉴到电商素材生成的prompt自动工程，基于现有商品图自动生成合规编辑指令，降低运营成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有指令引导图像编辑模型迭代依赖人工标注对或外部奖励模型，标注成本高，且易出现输出逼真但未完成编辑要求、篡改需保留内容的失效问题。
### 方法关键点
1. 提出Rubric-CEPR自进化框架，无需人工标注/外部训练阶段奖励模型，仅基于模型自身生成样本完成迭代
2. 三层架构：Planner从无标注图像生成结构化编辑指令，Editor生成多候选编辑结果，冻结Critic基于编辑器内部特征做编辑实现、旧状态移除、内容保留三类校验，通过非补偿门控淘汰不合格样本
3. 筛选最优样本通过轻量适配器训练蒸馏进编辑器，可循环迭代
### 关键结果
在Qwen-Image-Edit基准上，ImgEdit评分从4.36提升至4.60（+5.5%），物体隔离任务增益达24.9%，可迁移到GEdit-Bench等数据集；相同流程也使Step1X-Edit的ImgEdit评分提升7.8%
