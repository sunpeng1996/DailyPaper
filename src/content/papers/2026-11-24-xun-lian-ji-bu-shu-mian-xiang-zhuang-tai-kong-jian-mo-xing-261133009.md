---
title: 'Train What You Run: Probabilistic Convolutions for Learning Token Compaction
  in State Space Models'
title_zh: 训练即部署：面向状态空间模型Token压缩的概率卷积方法
authors:
- Piotr Kubaty
- Mikhail Saladkou
- Jacek Tabor
- Łukasz Struski
affiliations:
- Jagiellonian University, Poland
- Warsaw University of Technology, Poland
arxiv_id: '2611.33009'
url: https://arxiv.org/abs/2611.33009
pdf_url: https://arxiv.org/pdf/2611.33009
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 大模型推理优化 · Token压缩训练
tags:
- Token Compaction
- State Space Model
- Mamba
- Probabilistic Convolution
- Inference Optimization
one_liner: 提出可微概率卷积算子ProbConv，解决状态空间模型Token压缩训练推理不一致问题
practical_value: '- 多模态电商搜推的视觉特征处理环节可接入ProbConv，在高Token压缩率下保留模型性能，降低推理时延

  - 用Mamba类状态空间模型做长序列用户行为建模时，可复用ProbConv训练逻辑，解决Token剪枝后邻域变化带来的训推不一致问题

  - 视频/直播内容推荐的帧选择场景，可直接用ProbConv替代零掩码训练方案，同等推理预算下提升预测精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
带局部卷积的序列模型（如Mamba）做Token压缩推理时，删除Token会改变局部卷积邻域关系，常规零掩码训练未适配推理时的邻域变化，导致训推不一致，高压缩率下性能掉点严重。
### 方法关键点
提出可微算子ProbConv，在独立Token保留决策下，计算保留位置激活前的精确期望卷积，算子对Token保留概率可微；训练阶段基于可微保留概率学习Token选择策略，推理阶段直接二值化输出保留Token，可1:1复现压缩后的Mamba block执行逻辑。
### 关键结果
强Token压缩场景下，ProbConv相对对照组的性能优势随压缩率提升扩大；在Cobra多模态框架中，同等推理预算下效果优于现有公开视觉语言剪枝方法；视频帧选择、语音帧丢弃任务中，性能优于匹配的零掩码训练方案。
