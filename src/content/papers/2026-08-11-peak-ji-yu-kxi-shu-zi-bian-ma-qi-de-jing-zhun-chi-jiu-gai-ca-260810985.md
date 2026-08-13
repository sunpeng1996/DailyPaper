---
title: 'PEAK: Precise and Persistent Concept Erasure via k-Sparse Autoencoders'
title_zh: PEAK：基于k稀疏自编码器的精准持久概念擦除框架
authors:
- Man Jiang
- Ouxiang Li
- Weibao Xue
- Zhenhua Tang
- Yuan Wang
- Shuo Wang
- Yanbin Hao
affiliations:
- Hefei University of Technology
- University of Science and Technology of China
- University of Macau
arxiv_id: '2608.10985'
url: https://arxiv.org/abs/2608.10985
pdf_url: https://arxiv.org/pdf/2608.10985
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态模型安全 · 概念擦除
tags:
- Concept Erasure
- k-Sparse Autoencoder
- Diffusion Model
- T2I Generation
- Model Safety
one_liner: 基于k稀疏自编码器定位概念特征，实现扩散模型无推理开销的鲁棒概念擦除
practical_value: '- 可复用kSAE稀疏特征定位思路，擦除电商AIGC营销素材生成模型中的侵权IP、违规内容概念，规避合规风险

  - 特征引导的参数优化方案直接将擦除能力嵌入模型参数，无推理额外开销，适配高并发的电商图生图落地场景

  - 目标/非目标prompt对比筛选特征的方法可迁移到推荐系统敏感用户兴趣的定向屏蔽场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文生图扩散模型的概念擦除方法无法同时满足精准性与持久性：概念表征定位不准易引发非目标语义干扰，擦除不彻底则可被对抗恢复，难以适配版权、合规类场景要求。
### 方法关键点
1. 训练k-Sparse Autoencoders对扩散去噪网络的内部激活做分解，将稠密表征转换为可解释的稀疏特征
2. 对比目标、非目标prompt触发的稀疏激活，结合激活强度与频率两个维度，筛选得到紧凑的目标专属特征集
3. 基于定位的特征做参数优化，选择性抑制目标相关激活，同时保留非目标表征与原模型能力，擦除能力直接嵌入模型参数，无需推理侧额外干预，可抵御对抗攻击
### 关键结果
I2P基准上NudeNet违规内容检测数从582降至6，平均攻击成功率从96.52%降至5.63%；MS-COCO数据集上KID接近0，通用生成质量几乎无损失。
