---
title: 'PhiZero: A World Model Built Around Physical Language'
title_zh: PhiZero：基于物理语言构建的世界模型
authors:
- Shuyao Shang
- Yuqi Wang
- Ruopeng Gao
- Xu Chen
- Tieniu Tan
- Lue Fan
- Zhaoxiang Zhang
affiliations:
- NLPR, Institute of Automation, Chinese Academy of Sciences (CASIA)
arxiv_id: '2607.28624'
url: https://arxiv.org/abs/2607.28624
pdf_url: https://arxiv.org/pdf/2607.28624
published: '2026-07-29'
collected: '2026-08-01'
category: Multimodal
direction: 多模态世界建模 · 物理语言表征
tags:
- World Model
- Physical Language
- Video Generation
- Self-supervised Learning
- Discrete Representation
one_liner: 通过自监督从视频中学习离散物理语言表征，采用先推理后渲染范式实现物理一致的世界建模
practical_value: '- 离散语义表征的先推理后生成范式可迁移到短视频生成、商品3D动态展示场景，降低高维像素空间直接预测的误差

  - 自监督学习跨模态抽象表征的思路可复用在用户行为序列语义化建模，提升推荐系统序列预测鲁棒性

  - 零样本动作迁移方案可借鉴到虚拟数字人带货场景的动作自动生成，降低内容制作成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有物理世界模型直接在像素空间预测未来视频，高维视觉预测器隐式建模世界动态，物理一致性差，无法支持显式推理。
### 方法关键点
1. 参考人类从视觉经验抽象预测结构、用自然语言组织显式推理的机制，通过自监督从野生视频中学习紧凑离散的物理语言表征，作为世界状态转移的中间表示
2. 采用**先推理后渲染**两阶段范式：先将未来世界演化推理为物理语言序列，再将推断的转移渲染为视频
### 关键结果
在多个生成与理解基准上验证了其建模物理一致世界演化的能力，同时支持三大下游场景：真实交互世界建模、细粒度动作条件仿真、零样本动作迁移
