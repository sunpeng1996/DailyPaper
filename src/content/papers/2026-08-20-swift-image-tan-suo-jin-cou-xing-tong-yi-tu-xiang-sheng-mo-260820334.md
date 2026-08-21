---
title: 'Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation
  Models'
title_zh: Swift-Image：探索紧凑型统一图像生成模型的性能边界
authors:
- Taihang Hu
- Zhao Wang
- Zuan Gao
- Tao Liu
- Hao Yan
- Zhengze Xu
- Yuhang Yu
- Yongchao Du
- Xingjian Wang
- Jun Zheng
affiliations:
- Alibaba Group
arxiv_id: '2608.20334'
url: https://arxiv.org/abs/2608.20334
pdf_url: https://arxiv.org/pdf/2608.20334
published: '2026-08-20'
collected: '2026-08-21'
category: Multimodal
direction: 多模态 · 紧凑型统一图像生成编辑优化
tags:
- Image Generation
- DiT
- Model Compression
- Knowledge Distillation
- Reinforcement Learning
one_liner: 提出6B参数统一图像生成编辑模型Swift-Image，通过系统化训练工程实现同规模开源模型性能领先
practical_value: '- 多任务统一模型训练可复用「渐进式训练+多教师同策略蒸馏」方案，缓解不同任务目标互扰，可直接落地电商图文生成、商品素材编辑统一建模需求

  - 可借鉴Prompt Enhancer设计思路，将用户自由输入转换为生成模型适配的规范输入，降低普通商家的prompt使用门槛，适配电商低门槛AIGC工具开发

  - 小参数模型落地可参考「结构剪枝+少步蒸馏」方案，在几乎不损失效果的前提下压缩模型尺寸与推理耗时，适配端侧、边缘侧的AIGC服务部署'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前图像生成/编辑模型普遍参数量大、训练成本高，生成、编辑任务多拆分为独立模型，算力受限场景下小参数统一模型的性能上限尚未被充分挖掘。
### 方法关键点
- 采用6B单流DiT架构，配套渐进式训练pipeline，从宽语义覆盖逐步迭代到高分辨率、高质量、生成编辑统一监督
- 后训练采用并行专家RL+多教师同策略蒸馏，缓解异构目标互扰
- 新增Prompt Enhancer解耦高层推理和像素渲染，将用户请求转换为模型适配的视觉规范
- 部署阶段通过结构剪枝+少步蒸馏生成3B及低采样步速版本
### 关键结果
6B版本在同规模开源模型中综合性能领先，仅消耗243K GPU训练时；3B压缩版效果几乎无损，少步蒸馏版本采样步数大幅降低的同时编辑综合性能进一步提升。
