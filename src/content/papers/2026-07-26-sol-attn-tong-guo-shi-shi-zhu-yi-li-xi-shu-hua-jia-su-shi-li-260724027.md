---
title: 'Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention
  Sparsification'
title_zh: Sol-Attn：通过实时注意力稀疏化加速视频生成推理
authors:
- Haopeng Li
- Yitong Li
- Junsong Chen
- Tian Ye
- Haozhe Liu
- Jincheng Yu
- Duomin Wang
- Ruihua Zhang
- Zeke Xie
- Enze Xie
affiliations:
- NVIDIA
arxiv_id: '2607.24027'
url: https://arxiv.org/abs/2607.24027
pdf_url: https://arxiv.org/pdf/2607.24027
published: '2026-07-26'
collected: '2026-07-29'
category: LLM
direction: 大模型推理优化 · 注意力稀疏化
tags:
- Sparse Attention
- Inference Acceleration
- Diffusion Transformer
- Video Generation
- Training Free
one_liner: 提出免训练动态稀疏注意力方法Sol-Attn，视频生成端到端提速2.1倍且无视觉质量损失
practical_value: '- 电商短视频/营销主图等生成式内容推理场景可直接复用免训练动态稀疏注意力思路，无需finetune即可降低推理延迟、提升服务吞吐

  - 用户长行为序列建模、多轮Agent上下文推理等长序列attention瓶颈场景，可借鉴在线softmax动态阈值选块+未选块分数复用设计，平衡精度与速度

  - 生成类业务推理链路优化可参考Sol-Attn与其他加速技术组合的思路，叠加后可实现更高的端到端提速比'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Diffusion Transformer是高保真视频生成的核心组件，但长token序列下attention计算成为推理主要瓶颈；现有免训练动态稀疏注意力方法存在两大缺陷：一是路由计算开销高，固定/动态预算的块选择都需要生成完整代理分数映射；二是直接丢弃未选块导致高稀疏度下精度损失严重。
### 方法关键点
Sol-Attn是免训练的在线稀疏注意力方案，核心是带代理分数复用的实时块阈值策略：在单轮在线softmax计算过程中通过块代理分数与阈值对比筛选关键块，无需实例化完整代理映射即可实现动态可控的块预算，同时直接复用未选块的代理分数近似其贡献，统一动态路由、稀疏计算、近似校正三个步骤。
### 关键结果
视频生成端到端提速2.1倍，视频编辑提速2.3倍，完全保留原始视觉质量；与其他加速技术结合后，视频生成端到端最高可实现5倍提速。
