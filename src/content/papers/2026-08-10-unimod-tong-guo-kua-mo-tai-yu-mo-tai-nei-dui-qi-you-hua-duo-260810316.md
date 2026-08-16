---
title: 'UniMod: Enhancing Multi-Modal Medical Diagnosis through Cross-Modality and
  Within-Modality Alignment'
title_zh: UniMod：通过跨模态与模态内对齐优化多模态医疗诊断
authors:
- Zijian Gu
- Weikai Lin
- Shuang Zhou
- Zihan Chen
- Song Wang
affiliations:
- University of Central Florida
- University of Rochester
- Harvard Medical School
- University of Virginia
arxiv_id: '2608.10316'
url: https://arxiv.org/abs/2608.10316
pdf_url: https://arxiv.org/pdf/2608.10316
published: '2026-08-10'
collected: '2026-08-16'
category: Multimodal
direction: 多模态学习 · 跨/模态内特征对齐
tags:
- Multimodal-Learning
- Representation-Alignment
- Shortcut-Learning
- Vision-Language
- Medical-AI
one_liner: 提出双对齐多模态训练框架UniMod，缓解多模态学习捷径效应，提升诊断精度
practical_value: '- 多模态电商推荐（图文商品/内容）可借鉴「单模态独立监督+多模态联合监督」训练范式，缓解简单模态（如文本标题）占主导、忽略图像特征的问题

  - 跨模态对齐策略可直接复用，实现图文特征空间统一，支撑多模态召回、排序等下游任务

  - 同标签样本的模态内有监督对比学习trick，可用于提升单模态特征判别性，优化用户/物品建模效果'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态学习（如图像+文本融合）在各领域落地广泛，但常规训练存在捷径学习问题：模型过度依赖易学习的模态特征，忽略难学习模态的有效信息，限制最终性能上限。

### 方法关键点
1. 同时对仅图像、仅文本、多模态三路输出做分类监督，强制每个模态都能独立提取有效判别特征；
2. 加入跨模态对齐实现不同模态间的知识迁移，缩小模态间特征分布差异；
3. 对同标签样本做模态内有监督对比对齐，增强单模态特征的判别性。

### 关键结果数字
- Harvard-Glaucoma数据集AUC达0.850，比OGM-GE、Gradient Blending高1.6-1.8%；
- CheXpert Plus数据集AUC达0.966，超上述基线5%以上；
- 无需修改架构即可适配5类多标签诊断任务，比CGGM平均AUC高0.097。
