---
title: 'CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs'
title_zh: CoVeR：面向VLM多视角3D推理的基于覆盖度的Token剪枝方法
authors:
- Nhat-Tan Bui
- Varshini Elangovan
- Arun Reddy Anugu
- Sreyas Mohan
- Wei Ye
- Dilin Wang
- JQ Huang
- Rakesh Ranjan
- Aviral Chharia
- Fernando De la Torre
affiliations:
- Carnegie Mellon University
- Meta Reality Labs
arxiv_id: '2609.08345'
url: https://arxiv.org/abs/2609.08345
pdf_url: https://arxiv.org/pdf/2609.08345
published: '2026-09-07'
collected: '2026-09-09'
category: Multimodal
direction: 多模态大模型 · Token剪枝优化
tags:
- Token Pruning
- VLM
- Multi-View 3D
- 3D Reasoning
- Inference Optimization
one_liner: 提出无训练纯规则的空间覆盖式视觉Token剪枝方法，在多视角3D推理任务上超现有SOTA
practical_value: '- 电商3D商品展示、多视角商品图理解场景可复用空间覆盖式剪枝逻辑，在不损失语义准确性的前提下降低VLM推理时延

  - 无训练纯规则的剪枝思路可直接作为plug-and-play模块接入现有多模态内容理解链路，无需额外fine-tune成本

  - 跨模型通用的剪枝框架设计可迁移至多帧短视频、多视角实拍内容等多模态处理场景，降低算力消耗'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
将3D场景表达为多视角图像可复用2D VLM预训练先验、规避3D标注稀缺问题，但会生成数千个冗余视觉Token，算力成本随视角数量线性上涨；现有剪枝方法要么保留大量近重复Token导致场景覆盖不全，要么无法严格控制Token预算、存在性能饱和瓶颈。
### 方法关键点
提出无训练、纯规则的CoVeR剪枝策略，仅基于Token空间坐标筛选能够覆盖全场景的Token，无需额外学习信号；可严格控制单场景Token预算，同时避免近重复Token选择、突破体素化方法的性能饱和瓶颈，支持即插即用接入各类VLM。
### 关键结果
在3个3D推理基准上全面超越此前SOTA，跨4种VLM验证通用性；仅保留8%视觉Token时即可维持93.5%的全Token性能，平均领先现有SOTA 3.9个百分点。
