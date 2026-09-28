---
title: 'FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation
  Gap in Representation Autoencoders'
title_zh: FuseReg：正则化层融合缓解表征自编码器的重建-生成差距
authors:
- Hongyang Du
- Yunfei Xie
- Junjie Ye
- Jiawei Yang
- Xiaoyan Cong
- Haodong Zhang
- Yongchao Huang
- Haiyu Wu
- Zongxia Li
- Shihang Gui
affiliations:
- USC PSI Lab
- Brown University
- Rice University
- University of Aberdeen
- University of Notre Dame
arxiv_id: '2609.31620'
url: https://arxiv.org/abs/2609.31620
pdf_url: https://arxiv.org/pdf/2609.31620
published: '2026-09-24'
collected: '2026-09-28'
category: Training
direction: 表征自编码器训练 · 层融合正则优化
tags:
- Autoencoder
- Layer Fusion
- Regularization
- Diffusion Model
- Representation Learning
one_liner: 提出FuseReg正则策略，通过随机层子集训练缓解表征自编码器的重建-生成差距
practical_value: '- 多模态召回/生成场景中，可复用随机层子集训练思路替代固定启发式层融合，平衡细节保留与生成效果

  - 预训练大模型下游微调时，可引入跨层敏感度惩罚正则，无需修改预训练权重即可缩小不同任务性能gap

  - 多任务共享特征提取器的推荐系统，可借鉴层融合鲁棒性训练思路，用单解码器适配不同层级特征输入，降低部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
表征自编码器（RAE）复用预训练视觉编码器特征作为生成与重建的隐空间，需选择编码器层做融合，但浅层特征像素细节保留能力优、深层特征生成指标更高，固定启发式层融合会耦合对信息需求不同的两个阶段，存在显著的重建-生成性能gap。
### 方法关键点
提出FuseReg正则方法，用随机编码器层子集训练替代启发式特征选择，通过子集采样显式惩罚跨层不一致敏感度，全程无需修改预训练编码器权重。
### 关键结果
- ImageNet-256数据集下基于DINOv3-L编码器，单FuseReg解码器无需重训即可适配全量、稀疏、单层融合输入，PSNR高于固定融合的专用解码器
- 仅替换解码器即可使RAEv2 DiT-XL生成器的无引导gFID降低27%
- 联合正则扩散训练阶段，DiT-Base的无引导gFID降低29%
