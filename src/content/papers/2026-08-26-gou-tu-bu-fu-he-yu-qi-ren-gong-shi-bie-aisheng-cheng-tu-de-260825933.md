---
title: 'When Composition Doesn''t Add Up: Humans Identifying Defects in AI-Generated
  Images'
title_zh: 构图不符合预期：人工识别AI生成图像的缺陷
authors:
- Ruoqi Hu
- Chulin Zhao
- Jiashuo Chang
- Ramon Ruiz-Dolz
- Hanhe Lin
affiliations:
- Dundee International Institute of Central South University, Central South University,
  China
- Faculty of Science, Engineering and Business, University of Dundee, United Kingdom
arxiv_id: '2608.25933'
url: https://arxiv.org/abs/2608.25933
pdf_url: https://arxiv.org/pdf/2608.25933
published: '2026-08-26'
collected: '2026-08-27'
category: Multimodal
direction: 多模态 · 生成图像质量评估与优化
tags:
- Text-to-Image
- Image Quality Assessment
- Dataset
- Defect Detection
- Generative AI
one_liner: 构建开源标注数据集CO-AID，支持AI生成图缺陷预测与文生图模型优化
practical_value: '- 电商广告AI图生成场景可复用CO-AID的缺陷标注体系，筛除构图错误的商品宣传图，降低人工审核成本

  - 可基于该数据集微调T2I模型的构图对齐能力，提升多主体、多属性提示词的生成准确率，适配电商多商品组合海报生成需求

  - 生成式内容推荐链路可接入基于CO-AID训练的缺陷预测模型作为内容质检环节，拦截不合格的AI生成物料'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前SOTA文生图（T2I）模型处理含多实体、多属性等复杂构图要求的提示词时，存在系统性缺陷，缺乏统一的构图类缺陷标注数据集支撑缺陷检测与生成优化。
### 方法关键点
1. 人工筛选人物、手部、物体、场景4类共651张含复杂构图特征的参考图，基于ChatGPT生成提示词后人工调整得到强调查构图因素的输入prompt
2. 输入3款主流T2I模型生成图像，组织29名参与者对每张图做多标签缺陷类型、位置标注，构建CO-AID数据集
### 关键结果
基于CO-AID训练的深度模型可同时实现AI生成图缺陷预测与文生图生成效果优化，数据集已完全开源。
