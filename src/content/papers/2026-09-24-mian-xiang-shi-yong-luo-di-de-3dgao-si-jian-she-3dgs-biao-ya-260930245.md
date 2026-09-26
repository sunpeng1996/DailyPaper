---
title: Towards Practical Compression of 3D Gaussian Splatting
title_zh: 面向实用落地的3D高斯溅射（3DGS）表示压缩方法
authors:
- Pengpeng Yu
- Yueru Chen
- Fei Song
- Tai Qin
- Qi Zhang
- Jing Wang
- Yulan Guo
affiliations:
- 中山大学
- 鹏城实验室
- 国家广播电视总局广播科学研究院
- 北京大学深圳研究生院
arxiv_id: '2609.30245'
url: https://arxiv.org/abs/2609.30245
pdf_url: https://arxiv.org/pdf/2609.30245
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 3D场景表示 · 3DGS压缩优化
tags:
- 3DGS
- Compression
- Cross-platform Consistency
- Entropy Coding
- Novel View Synthesis
one_liner: 提出无空间聚合的COSA-GS，实现跨平台一致的SOTA 3DGS压缩
practical_value: '- 电商3D商品建模、AR试穿场景的3DGS存储优化，可复用anchor级因果上下文建模替代复杂空间聚合，降低编码训练复杂度

  - 跨端3D内容渲染场景，可借鉴量化感知训练+整数推理方案，保证熵解码跨平台比特级一致性，避免解码失败

  - 资源受限的端侧3D内容传输场景，可复用自适应高斯剪枝+率失真优化训练范式，平衡压缩率与渲染质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3DGS可实现高质量新视角合成，但存储开销极高；现有压缩方法依赖不规则3D表示的空间上下文建模，训练编码复杂度高，且浮点上下文推理存在跨平台数值不一致问题，易引发熵解码失败，落地性差。
### 方法关键点
1. 提出COSA-GS，通过anchor级因果因子分解构建无空间聚合的上下文，用anchor坐标导出的几何上下文建模紧凑可学习anchor隐向量，融合后得到属性编码的anchor上下文，上下文模型仅由线性变换和激活函数组成，架构极简
2. 采用带自适应高斯剪枝的率失真优化训练，进一步降低参数冗余
3. 设计上下文模型的量化感知训练与整数推理逻辑，实现熵解码符号跨平台比特级完全一致
### 关键结果
COSA-GS达到3DGS压缩领域SOTA性能，同时保留快速、稳定的跨平台解码能力，适配落地部署需求
