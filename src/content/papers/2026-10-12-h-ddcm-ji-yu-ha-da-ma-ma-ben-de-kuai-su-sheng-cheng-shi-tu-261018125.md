---
title: 'H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression'
title_zh: H-DDCM：基于哈达玛码本的快速生成式图像与视频压缩
authors:
- Or Ronai
- Vladimir Kulikov
- Tomer Michaeli
affiliations:
- Technion – Israel Institute of Technology
arxiv_id: '2610.18125'
url: https://arxiv.org/abs/2610.18125
pdf_url: https://arxiv.org/pdf/2610.18125
published: '2026-10-12'
collected: '2026-10-17'
category: Other
direction: 生成式音视频压缩 · 码本优化
tags:
- Generative Compression
- Hadamard Transform
- Codebook Optimization
- KV Cache
- Diffusion Model
one_liner: 提出基于哈达玛码本的H-DDCM框架，大幅降低免训练生成式图像视频压缩的存储计算开销
practical_value: '- 码本优化思路可迁移到生成式推荐的Semantic ID编码场景，用哈达玛变换替代密集高斯码本，大幅降低内存与计算开销

  - 无表字典编码方案可复用在电商素材/短视频低码率压缩场景，显著降低存储与传输成本

  - 复用重建结果更新KV cache前缀的技巧，可迁移到长序列生成推荐/Agent会话场景，零额外开销保留上下文'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于码本的免训练扩散压缩方案依赖密集高斯码本，存储、计算开销高，对大隐空间维度的生成器扩展性差，组合编码代价随维度上涨显著。
### 方法关键点
1. 用隐式随机哈达玛字典替换高斯码本，借助快速沃尔什-哈达玛变换实现O(d log d)计算、O(d)内存开销，无需实例化全维字典；
2. 提出无表字典序编码方案，适配大维度下的组合编码需求；
3. 视频场景设计流式压缩方案，定期将已重建帧重编码为新KV cache前缀，零额外比特开销保留跨片段时序上下文。
### 关键结果
图像视频基准测试中率失真感知表现与现有SOTA持平，码本相关存储计算开销大幅降低，单GPU即可实现接近实时的长视频生成式压缩。
