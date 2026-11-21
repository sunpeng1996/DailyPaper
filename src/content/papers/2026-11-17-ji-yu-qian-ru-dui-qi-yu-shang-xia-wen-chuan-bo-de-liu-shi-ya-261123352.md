---
title: Streaming Generative Video Compression with Embedding Alignment and In-Context
  Propagation
title_zh: 基于嵌入对齐与上下文传播的流式生成式视频压缩
authors:
- Zhitao Wang
- Hengyu Man
- Han Liu
- Wenrui Li
- Debin Zhao
- Xiaopeng Fan
affiliations:
- Harbin Institute of Technology
- Harbin Institute of Technology Suzhou Research Institute
- Peng Cheng Laboratory
arxiv_id: '2611.23352'
url: https://arxiv.org/abs/2611.23352
pdf_url: https://arxiv.org/pdf/2611.23352
published: '2026-11-17'
collected: '2026-11-21'
category: Other
direction: 生成式视频压缩 · KV缓存复用
tags:
- Diffusion Transformer
- KV Cache
- Embedding Alignment
- Generative Compression
- Video Compression
one_liner: 提出流式生成式视频压缩框架SGVC，通过嵌入对齐与跨帧KV复用实现低延迟高画质压缩
practical_value: '- 跨帧复用KV cache的上下文传播思路，可直接迁移到流式生成式推荐、多轮对话Agent场景，显著降低长序列生成的推理延迟与算力开销

  - 嵌入对齐的训练trick，可复用在RAG、LLM4Rec等场景，弥合业务侧自定义特征与预训练LLM原生输入嵌入的分布差异，提升生成效果

  - 绕开预训练大模型内置高开销解码器、新增轻量映射头的架构设计，可用于优化基于LLM的生成式推荐、商品文案生成任务的推理速度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
超低码率下视频压缩感知画质保留难度大，现有基于预训练视频DiT的生成式压缩方案存在两大痛点：一是依赖计算开销极高的VAE解码器重建帧，二是多帧联合优化利用时序特性会引入额外缓冲延迟，无法支持流式场景。
### 方法关键点
1. 提出流式生成式视频压缩框架SGVC，将预训练latent视频DiT适配为因果像素域优化器，直接将上下文像素Codec的解码特征投影到DiT输入嵌入空间
2. 新增嵌入对齐训练策略，对齐Codec输出投影嵌入与原帧提取的DiT原生输入嵌入，弥合分布gap
3. 新增轻量重建头直接将DiT隐状态映射到像素域，绕开预训练VAE解码器降低推理开销
4. 提出上下文传播机制，跨帧复用逐层KV状态，无需clip级缓冲即可提升时序一致性
### 关键结果
DISTS指标下相比S²VC平均BD-rate降低71.97%，率感知性能达到SOTA水平
