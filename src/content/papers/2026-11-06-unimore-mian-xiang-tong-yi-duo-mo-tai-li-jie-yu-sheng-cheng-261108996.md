---
title: 'UniMore: Fine-Grained Supervision for Unified Understanding and Generation'
title_zh: UniMore：面向统一多模态理解与生成的细粒度监督
authors:
- Haoyue Bai
- Yinyi Luo
- Yicheng He
- Qingsong Wen
- Sharon Li
- Jindong Wang
affiliations:
- William & Mary
- Carnegie Mellon University
- University of Illinois Urbana-Champaign
- Squirrel Ai Learning
- University of Wisconsin–Madison
arxiv_id: '2611.08996'
url: https://arxiv.org/abs/2611.08996
pdf_url: https://arxiv.org/pdf/2611.08996
published: '2026-11-06'
collected: '2026-11-09'
category: Multimodal
direction: 统一多模态模型 · 细粒度后训练
tags:
- Multimodal
- Unified Model
- Post-training
- Fine-grained Supervision
- Image-Text Pair
one_liner: 通过双路细粒度后训练优化统一多模态模型，不改动推理流程同时提升双向任务精度
practical_value: '- 商品多模态理解场景可复用细粒度负样本构造方法：通过篡改/省略商品属性生成难负例，提升文案生成、商品打标的属性准确率

  - 统一多模态模型后训练可采用双路独立优化+参数合并的方案，无需修改推理逻辑即可同时提升图文生成和理解能力，降低落地改造成本

  - 商品图生成场景可引入短语-局部裁剪块的配对监督，避免生成图属性与文案描述不符的问题，提升AI商拍的输出合格率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有统一多模态预训练模型存在特异性损失问题：生成图像易出现对象属性错误，图文理解输出的描述缺乏区分性细节，缺少面向双向任务的细粒度监督方案。
### 方法关键点
1. 后训练阶段从图文对的细粒度内容衍生双路互补任务，无需改动模型结构：生成路用对应短语监督局部裁剪块的预测，匹配条件和视觉目标的范围；理解路在全图条件下拟合正样本caption，同时对篡改/省略细节的负样本caption做排序。
2. 双路独立优化后将参数更新合并为单一模型，推理流程完全不变。
### 关键结果
在多个多模态理解、生成基准测试上均取得稳定精度提升
