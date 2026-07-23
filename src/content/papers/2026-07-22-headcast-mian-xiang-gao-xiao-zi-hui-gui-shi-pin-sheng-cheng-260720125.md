---
title: 'HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation'
title_zh: HeadCast：面向高效自回归视频生成的注意力头分流框架
authors:
- Jinliang Shen
- Lianghao Su
- Zheming Li
- Kang He
- ZiLiang Lai
- Yanbing Jiang
- Chengru Song
affiliations:
- Peking University
- KlingAI Research
arxiv_id: '2607.20125'
url: https://arxiv.org/abs/2607.20125
pdf_url: https://arxiv.org/pdf/2607.20125
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- Inference Acceleration
- Autoregressive Generation
- Attention Head
- Diffusion Model
one_liner: 训练免改、即插即用的自回归视频生成加速框架，通过分流注意力头降低KV cache开销并保障生成质量
practical_value: '- 面向商品短视频生成、Agent多轮流式回复等自回归生成类业务，可复用注意力头异质性分类思路，免训练实现推理加速且不降低生成效果

  - 高分辨率内容生成、长序列对话等KV cache膨胀严重的场景，可参考按头类型拆分KV缓存通路的设计，长时序依赖头保留全缓存、空间/局部依赖头固定缓存大小，平衡速度与一致性

  - 业务端上线推理优化方案时优先采用训练免改、即插即用的设计，规避重训成本，可快速适配已有预训练模型落地'
score: 6
source: arxiv-cs.CV
depth: abstract
---

## 动机
自回归（AR）视频扩散模型是长视频、流式视频生成的主流范式，但推理过程中KV cache持续膨胀导致注意力计算开销占比极高，高分辨率场景下每帧token数多，开销问题更突出；现有优化方案要么采用粗粒度缓存驱逐策略导致帧间闪烁、内容漂移，要么需要重新训练模型，落地成本高。
## 方法关键点
基于预训练AR模型注意力头存在稳定异质性行为的观测，提出免训练、即插即用的HeadCast框架：经过短时预热后，在最大噪声步做一次性分类，将所有注意力头划分为Sink、Dummy、Spatial、Global四类，将统一KV缓存拆分为对应头类型的专属通路；重点保留负责长时序一致性的Global头全量缓存，避免激进缓存驱逐导致的帧间漂移，Spatial类头采用固定大小网格缓存，分辨率越高缓存收益越大。
## 关键结果数字
在SOTA AR模型上实测，720P分辨率下推理加速最高1.62倍，1080P下最高1.95倍，VBench质量得分与全注意力模式持平，无明显帧间闪烁。
