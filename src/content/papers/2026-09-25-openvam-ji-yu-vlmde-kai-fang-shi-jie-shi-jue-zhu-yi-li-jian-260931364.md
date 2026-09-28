---
title: 'OpenVAM: Open-World Visual Attention Modeling with VLMs'
title_zh: OpenVAM：基于VLM的开放世界视觉注意力建模框架
authors:
- Kiana Hooshanfar
- Amirhossein Kazerouni
- Alireza Hosseini
- Michael Brudno
- Babak Taati
affiliations:
- University of Tehran
- University of Toronto
- Vector Institute
- University Health Network
arxiv_id: '2609.31364'
url: https://arxiv.org/abs/2609.31364
pdf_url: https://arxiv.org/pdf/2609.31364
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态视觉注意力预测与可解释性优化
tags:
- VLM
- Visual Attention
- Saliency Prediction
- Cross-domain Robustness
- Explainable AI
one_liner: 提出解耦对齐的多模态视觉注意力框架，同时实现跨域鲁棒显著性预测与可解释归因
practical_value: '- 电商商品图、首页/活动页UI优化场景可直接复用跨域鲁棒显著性检测能力，定位用户视觉焦点元素，指导素材排版、卖点露出位置设计

  - 解耦但对齐的双分支架构可迁移至多模态推荐、广告素材评估任务：保留原有视觉主干的精度能力，新增语义归因分支解释预测原因，无需扰动原有上线模型

  - 三阶段参数高效适配训练策略可复用，在不损害原有任务效果的前提下，低成本为模型新增解释性输出能力，降低训练与上线改造成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉注意力模型仅输出稠密显著性图，无法将注意力峰值关联到场景离散元素、也无法解释注意力驱动原因，且跨自然图像、商业素材、UI/web布局等场景的域迁移鲁棒性差，无法满足商材分析、UI优化等落地需求。
### 方法关键点
1. 采用解耦对齐架构：独立稠密视觉通路保障空间精准的显著性定位，指令跟随VLM语义头基于输入图像+数据类型prompt输出 grounded 的「是什么/为什么」解释
2. 三阶段训练策略：通过parameter-efficient adaptation逐步引入语言对齐能力，全程不扰动显著性分支的原有定位先验
3. 配套可扩展的多域显著性推理标注生成pipeline，支撑模型训练与系统性评估
### 关键结果
跨多域数据集实验验证，OpenVAM显著提升域迁移鲁棒性，同时可生成与图像对齐的可解释归因，让显著性预测具备直接落地的行动指导价值
