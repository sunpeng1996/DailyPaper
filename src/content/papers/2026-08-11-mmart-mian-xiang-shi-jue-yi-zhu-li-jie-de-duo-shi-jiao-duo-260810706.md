---
title: MMArt A Multi-Perspective Multimodal Dataset for Visual Art Understanding
title_zh: MMArt：面向视觉艺术理解的多视角多模态数据集
authors:
- Shuai Wang
- Wangyuan Ding
- Yixian Shen
- Jia-Hong Huang
- Stevan Rudinac
- Monika Kackovic
- Nachoem Wijnberg
- Marcel Worring
affiliations:
- University of Amsterdam
- Amazon AGI
- University of Johannesburg
arxiv_id: '2608.10706'
url: https://arxiv.org/abs/2608.10706
pdf_url: https://arxiv.org/pdf/2608.10706
published: '2026-08-11'
collected: '2026-08-16'
category: Multimodal
direction: 多模态艺术理解 · 多视角标注数据集
tags:
- Multimodal Dataset
- Vision-Language Model
- Art Understanding
- Multi-perspective Annotation
- Cross-modal Retrieval
one_liner: 构建7万余幅画作的多视角多模态艺术数据集，验证多视角信息的任务互补性
practical_value: '- 跨模态电商商品检索/生成场景可复用多视角标注思路：给商品标注内容、风格、场景、背景四类属性，匹配不同下游任务需求

  - 多模态召回阶段可参考任务不对称性结论：搜索召回优先匹配叙事类特征，图生图/风格迁移优先匹配形式类特征，提升任务表现

  - 商品caption生成场景可借鉴分视角标注再融合方案：兼顾不同用户信息需求，提升文案覆盖度与转化效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视觉语言模型艺术理解能力浅层，仅能描述表面内容，无法完成深度形式分析、历史解读、情感刻画；现有艺术数据集均为单视角标注，缺乏同一作品的多维度同步标注，限制模型能力上限。
### 方法关键点
构建MMArt大规模多视角多模态数据集，覆盖74234幅WikiArt画作，每幅作品包含叙事、形式、情感、历史四类独立标注+统一融合caption，标注由专业多模态模型生成+人工校验，通过多轮质量评估保证标注有效性。
### 关键结果数字
1. 多视角编码信息完全独立，单一视角无法覆盖所有任务；
2. 跨模态检索任务中叙事类描述R@1达44.0%，形式类描述R@1仅7.8%；
3. 图像重建任务中形式类描述最优保留构图风格，历史类描述携带最强情感信号，是两类任务中最不可替代的视角。
