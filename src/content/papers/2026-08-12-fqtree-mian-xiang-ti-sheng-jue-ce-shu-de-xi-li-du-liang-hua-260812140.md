---
title: 'FQTree: Fine-grained Quantization and Hardware Generation of Boosted Decision
  Trees'
title_zh: FQTree：面向提升决策树的细粒度量化与硬件自动生成
authors:
- Zhiqiang Que
- Chang Sun
- Haiyang Wang
- Dinesh Pamunuwa
- Roshan Weerasekera
- Qijia Tang
- Bakhtiar Zadeh
- Wayne Luk
- Maria Spiropulu
affiliations:
- University of Bristol
- California Institute of Technology
- Imperial College London
arxiv_id: '2608.12140'
url: https://arxiv.org/abs/2608.12140
pdf_url: https://arxiv.org/pdf/2608.12140
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: BDT量化优化 · 硬件自动部署
tags:
- BDT
- Quantization
- FPGA
- Quantization-Aware Training
- Hardware Deployment
one_liner: 提出BDT细粒度量化感知训练算法FQTree与自动硬件生成框架QXGB，降低FPGA部署成本且精度持平或更优
practical_value: '- 电商/广告实时排序场景的XGBoost/LightGBM类BDT模型，可复用FQTree的细粒度叶节点量化方案，在精度无损前提下压缩模型体积、降低推理延迟

  - 可借鉴量化感知融入boosting的训练流程：训练时将量化误差纳入迭代，让后续树适配已量化部分的误差，避免事后量化的精度掉点

  - 有FPGA/端侧部署BDT需求的业务（如端侧推荐、边缘广告推理），可直接复用QXGB框架的自动硬件生成流，降低定制开发成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
BDT是低延迟场景（搜索推荐实时排序、风控等）的主流模型，但现有FPGA部署方案多采用统一或手动调优的定点格式，难以平衡硬件成本与推理精度。
### 方法关键点
1. 设计硬件友好的叶值量化方案：采用全局量化步长+单树偏移，实现紧凑非负整数叶节点表示，结合裁剪、偏置折叠降低数据通路开销
2. 量化操作融入boosting训练流程，后续训练的树自适应已量化集成模型的误差，大幅降低量化带来的精度损失
3. 配套QXGB编译器流，可将训练完成的量化模型自动生成低延迟FPGA实现
### 关键结果
在JSC、MNIST、NID数据集上，相比现有SOTA FPGA BDT实现，LUT资源占用降低26%~57%，同时精度持平甚至更优
