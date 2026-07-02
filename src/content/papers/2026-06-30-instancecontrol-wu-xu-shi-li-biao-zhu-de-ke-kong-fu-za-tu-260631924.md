---
title: 'InstanceControl: Controllable Complex Image Generation without Instance Labeling'
title_zh: InstanceControl：无需实例标注的可控复杂图像生成
authors:
- Xiaoyu Liu
- Huan Wang
- Fan Li
- Zhixin Wang
- Jiaqi Xu
- Ming Liu
- Wangmeng Zuo
affiliations:
- 哈尔滨工业大学
- 华为诺亚方舟实验室
arxiv_id: '2606.31924'
url: https://arxiv.org/abs/2606.31924
pdf_url: https://arxiv.org/pdf/2606.31924
published: '2026-06-30'
collected: '2026-07-02'
category: Multimodal
direction: 多模态可控图像生成
tags:
- Controllable Generation
- VLM
- Instance Alignment
- Mask Refinement
- Image Generation
one_liner: 提出无需手动实例标注的多实例可控生成方法，解决复杂场景实例属性混淆问题
practical_value: '- 电商多商品组合场景图/营销图生成可直接复用该方案，无需人工标注实例位置，大幅降低素材生产的标注成本

  - 自适应掩码动态精炼的trick可迁移到现有ControlNet等可控生成管线，优化多商品同框生成时的属性错乱问题

  - 可落地到AI商拍的自定义布局生成需求，用户输入文本描述的多商品布局即可直接生成符合要求的商品图'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有ControlNet等可控图像生成方法在多实例复杂场景下易出现实例属性混淆，现有优化方案依赖手动实例标注，人力成本极高，无法规模化落地。
### 方法关键点
1. 利用VLM自动建立文本prompt中实例描述与视觉条件的实例级对应关系，完全免除人工标注需求
2. VLM同步完成两个任务：解析prompt中的实例描述、基于输入视觉条件预测对应实例掩码
3. 新增自适应掩码精炼策略，在图像生成过程中动态修正带噪声的预测掩码，提升对齐准确率
### 关键结果
实验效果全面超越现有SOTA方法，在复杂多实例场景下实现更高的生成保真度与更精准的实例级控制
