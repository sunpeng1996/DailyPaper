---
title: 'ViewMind3D: Modular View-Aware Inference for Training-Free 3D-QA'
title_zh: ViewMind3D：面向免训练3D问答的模块化视角感知推理框架
authors:
- Ping-Kun Chiang
- Kun-Ru Wu
- Po-han Li
- Sandeep Chinchali
- Ufuk Topcu
- Yu-Chee Tseng
arxiv_id: '2607.28442'
url: https://arxiv.org/abs/2607.28442
pdf_url: https://arxiv.org/pdf/2607.28442
published: '2026-07-30'
collected: '2026-08-01'
category: Reasoning
direction: 多模态3D推理 · 免训练模块化架构
tags:
- 3D-QA
- VLM
- LLM
- Training-Free
- Modular Reasoning
one_liner: 提出免训练模块化3D-QA框架，编排通用LLM/VLM实现媲美微调方案的空间推理性能
practical_value: '- 做具身Agent电商导购（如VR逛店、3D商品咨询）时，可复用该四步模块化架构，无需标注3D数据即可快速搭建3D问答能力

  - 多模态业务任务可借鉴「问题驱动视角筛选→语义引导视觉定位→空间编码→分角色推理」的任务拆解范式，降低大模型微调成本

  - 空间感知类业务（如AR商品摆放推荐、线下到店导购路径规划）可复用BEV视角编码方法，提升空间推理准确率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D-QA方案依赖3D专属训练/微调，标注成本高、扩展性差，通用VLM缺乏显式3D推理能力，难以直接落地具身AI、机器人感知场景。

### 方法关键点
提出完全免训练的模块化3D空间推理框架，无需完整3D重建，将任务拆解为4个可解释组件：1）问题驱动的多视角选择；2）语言引导的visual grounding定位目标物体；3）通过BEV视角指示器编码空间上下文；4）基于角色分工的结构化答案生成，全程无需微调任何模型。

### 关键结果
在ScanQA、SQA3D基准上性能媲美现有免训练及微调3D-LLM，SQA3D整体准确率达50.8%，ScanQA的CIDEr得分达73.4，空间类问题性能提升尤为显著。
