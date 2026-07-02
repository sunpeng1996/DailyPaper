---
title: 'Learning to Compose: Revisiting Proxy Task Design for Zero-Shot Composed Image
  Retrieval'
title_zh: 学习组合：面向零样本组合图像检索的代理任务重设计
authors:
- Jingjing Zhang
- Lei Zhang
- Zheren Fu
- Zhendong Mao
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.00374'
url: https://arxiv.org/abs/2607.00374
pdf_url: https://arxiv.org/pdf/2607.00374
published: '2026-07-01'
collected: '2026-07-02'
category: Multimodal
direction: 多模态检索 · 零样本组合图像检索
tags:
- Zero-Shot CIR
- Proxy Task
- Multimodal Retrieval
- Contrastive Learning
- Vision-Language Model
one_liner: 提出两阶段可学习组合的FoCo框架，无需三元组标注即可实现零样本组合图像检索SOTA
practical_value: '- 电商多模态以图搜图场景可复用两阶段组合逻辑：先基于用户文本修改指令定位参考图需调整区域，再生成目标检索特征，提升搜索准确率

  - 零样本多模态任务训练可参考双代理任务设计，无需昂贵三元组标注即可实现跨模态特征的可学习融合，降低标注成本

  - 多模态检索训练时加入跨实例对比损失，可规避捷径学习问题，显著提升细粒度语义修改场景下的模型泛化性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
零样本组合图像检索（ZS-CIR）可规避监督CIR所需的昂贵<参考图+修改文本+目标图>三元组标注，但现有方法的组合逻辑为预定义（如伪词注入、线性特征运算），组合函数不可学习，无法适配多样细粒度的语义修改需求。
### 方法关键点
提出FoCo框架，将组合过程拆解为两个协同代理任务：1）文本锚定视觉聚合：基于局部文本语义引导，选择性筛选参考图中与修改相关的视觉内容；2）上下文感知语义补全：结合场景上下文将聚合后的视觉内容转换为统一的组合表征；双任务联合跨实例对比目标训练，避免捷径组合策略，提升语义多样性。
### 关键结果
在4个ZS-CIR基准数据集上取得SOTA性能，泛化性显著优于现有基线方案。
