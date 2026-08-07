---
title: 'CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework
  for Multispectral Object Detection'
title_zh: CFGPNet：基于交叉注意力的融合梯度编程多光谱目标检测网络框架
authors:
- Nima Hatami
- Karim Faez
- Saeed Sharifian
- Hamidreza Amindavar
affiliations:
- Department of Electrical Engineering, Amirkabir University of Technology, Tehran,
  Iran
arxiv_id: '2608.06205'
url: https://arxiv.org/abs/2608.06205
pdf_url: https://arxiv.org/pdf/2608.06205
published: '2026-08-06'
collected: '2026-08-07'
category: Other
direction: 多模态目标检测 · 跨模态特征融合
tags:
- Multimodal
- Cross-Modal Fusion
- Object Detection
- Attention Mechanism
- Reparameterization
one_liner: 提出兼顾精度与效率的多光谱目标检测框架，解决跨模态交互不足、融合不稳定、算力开销高问题
practical_value: '- 跨模态高效交叉注意力CrossCEA模块可复用至多模态商品/内容的召回排序场景，降低不同模态（图文/短视频/属性）特征的冗余传输，提升跨模态交互效率

  - RepViT风格重参数化块的backbone优化思路，可用于多模态理解模型的端侧/轻量化落地，平衡推理效率与特征表达能力，适配直播/短视频实时内容理解需求

  - 可编程梯度辅助分支的训练优化方法，可迁移至多模态推荐模型训练，解决跨模态特征分布差异导致的训练不稳定、梯度消失问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有RGB-T多光谱目标检测存在三类痛点：跨模态交互不足、模态分布差异导致融合不稳定、重注意力架构算力开销高，无法兼顾低光/恶劣天气等复杂场景的检测精度与部署效率。
### 方法关键点
1. 采用带RepViT重参数化块的改进GELAN backbone，兼顾特征表达能力与计算效率；
2. 引入CrossCEA高效交叉注意力模块，增强可见光/红外分支的跨模态交互，减少冗余信息传输；
3. 提出ASAF注意力选择聚合融合网络，结合稠密特征聚合与选择性注意力生成高判别性融合特征；
4. 加入可编程梯度辅助分支，优化梯度传递与训练效果。
### 关键结果
在FLIR、M3FD等5个公开多光谱基准集上实现SOTA性能，其中FLIR数据集mAP50达80.7%，M3FD达89.9%，LLVIP达97.8%，三个模型尺度均实现优异的精度-效率权衡。
