---
title: Scalable Neural Video Representation Compression
title_zh: 可扩展神经视频表征压缩算法
authors:
- Tianhao Peng
- Ho Man Kwan
- Fan Zhang
- Shan Liu
- David Bull
affiliations:
- University of Bristol, UK
- Tencent Media Lab, Palo Alto, USA
arxiv_id: '2609.04273'
url: https://arxiv.org/abs/2609.04273
pdf_url: https://arxiv.org/pdf/2609.04273
published: '2026-09-02'
collected: '2026-09-08'
category: Other
direction: 神经视频编码 · 可扩展压缩
tags:
- SVC
- INR
- Video Compression
- Neural Codec
- Scalable Coding
one_liner: 提出S-NVRC可扩展INR视频编码方案，单码流支持比特率与解码复杂度灵活调优，性能优于主流标准编码
practical_value: '- 电商短视频/直播转码场景可参考分层编码思路，针对不同终端算力、网络条件下发对应档位码流，平衡播放流畅度与画质体验

  - 短视频素材存储场景可借鉴INR单次编码多码率输出的设计，减少多分辨率、多码率转码版本的存储冗余，降低存储成本

  - 广告视频端侧播放优化可参考嵌套网络层前缀的设计，根据端侧算力动态调整解码复杂度，降低设备功耗、减少播放卡顿'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于INR的可扩展视频编码方案通过新增网络层实现分层，比特率与解码复杂度强耦合，性能显著弱于成熟传统编码标准，无法适配多元终端算力与网络波动场景。
### 方法关键点
提出S-NVRC可扩展INR视频编码框架，采用特征网格粗到细前缀实现比特率缩放，嵌套网络层前缀实现解码复杂度缩放，单次编码即可生成单个嵌入码流，支持比特率、解码复杂度的独立/联合细粒度调节。
### 关键结果
在UVG数据集上，S-NVRC BD-rate相比SHM 12.4降低43.7%，相比多层VTM-20.0降低5.6%，同时覆盖宽范围的比特率与解码复杂度档位，灵活性远超现有方案。
