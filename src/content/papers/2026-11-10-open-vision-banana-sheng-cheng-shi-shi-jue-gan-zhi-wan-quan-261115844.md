---
title: 'Open Vision Banana: A Fully Open Recipe for Generative Visual Perception'
title_zh: Open Vision Banana：生成式视觉感知完全开源实现方案
authors:
- Arpit Jadon
- Valentinos Pariza
- Jona Ruthardt
- Ryousuke Yamada
- A. Sophia Koepke
- Andrei Bursuc
- Yuki M. Asano
affiliations:
- Fundamental AI Lab, University of Technology Nuremberg
- DLR
- AIST
- University of Tübingen, Tübingen AI Center
- valeo.ai
arxiv_id: '2611.15844'
url: https://arxiv.org/abs/2611.15844
pdf_url: https://arxiv.org/pdf/2611.15844
published: '2026-11-10'
collected: '2026-11-14'
category: Multimodal
direction: 多模态生成·视觉感知系统开源实现
tags:
- Generative Vision
- Multi-task Perception
- Open Source
- Image Editing
- Zero-shot Perception
one_liner: 开源将预训练图像生成器转换为统一多任务感知系统的可复现全流程与配套资源
practical_value: '- 可复用legend ensembling测试时增强思路：针对多模态生成任务的不稳定输出（如商品属性识别、图文匹配），用多prompt模板生成结果后投票融合，无需重训即可提效

  - 多任务微调时需验证设计选择的组合效果：避免单个优化点组合后反而掉点，适合电商多目标（点击/转化/停留）微调场景的调优参考

  - 预训练生成模型可复用为感知模块：无需重新训练专用视觉模型，可快速搭建商品分割、属性识别、图文生成一体化的多模态推荐Agent能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
原Vision Banana框架将视觉任务转为条件图像编辑实现多任务感知，但未开源任何数据、权重、代码及实现细节，无法复现和落地。

### 方法关键点
1. 基于开源4B/9B参数量预训练图像生成器，用公开数据集的2.1M-3.8M训练对微调，识别出影响泛化性的核心设计：颜色编码、prompt设计、参数适配、任务平衡，明确单个优化点组合可能存在负向作用
2. 提出测试时增强方法legend ensembling：用多类-色映射模板生成分割结果后多数投票融合，修正颜色-类别绑定不稳定问题

### 关键结果
- 零-shot版本Cityscapes mIoU达73.9，超出原Vision Banana 4个点，性能媲美SOTA仿射不变深度估计器
- 非零-shot版本在参考/推理分割任务上与原Vision Banana差距小于5个mIoU点
- legend ensembling无需重训即可将Cityscapes mIoU提升最高8.7点、COCO目标分割mIoU提升最高15.0点
