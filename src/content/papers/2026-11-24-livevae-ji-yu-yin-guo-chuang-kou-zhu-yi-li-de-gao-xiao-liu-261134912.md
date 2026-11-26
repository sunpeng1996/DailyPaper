---
title: 'LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE'
title_zh: LiveVAE：基于因果窗口注意力的高效流式视频VAE
authors:
- Jiachen An
- Sijie Zhao
- Le Li
- Hongyu Liu
- Zhiyuan Li
- Tianyu Yang
- Xiaoyu Kong
- Xunliang Cai
- Yong Zhang
- Chi-Man Pun
affiliations:
- GVC Lab, Great Bay University
- Meituan
- The Hong Kong University of Science and Technology
- University of Macau
arxiv_id: '2611.34912'
url: https://arxiv.org/abs/2611.34912
pdf_url: https://arxiv.org/pdf/2611.34912
published: '2026-11-24'
collected: '2026-11-26'
category: Multimodal
direction: 多模态生成 · 流式视频VAE优化
tags:
- VAE
- Causal Attention
- KV Cache
- Video Generation
- Model Acceleration
one_liner: 提出基于因果窗口注意力的流式视频VAE，大幅提升编解码速度且可直接替换原有VAE
practical_value: '- 业务中若涉及商品短视频/直播切片等多模态内容生成场景，可复用因果窗口注意力+边界可控KV cache的方案，降低VAE编解码延迟，适配流式生成需求

  - 自研模型替换第三方预训练组件时，可参考解耦蒸馏+联合微调的策略，保证原有隐空间兼容，无需重构下游生成链路

  - 做生成类模型性能优化前，可先分析预训练模型的有效感受野，裁剪冗余全局建模逻辑，兼顾速度与生成效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前视频扩散模型的核心延迟瓶颈集中在VAE环节，现有VAE加速方案多仅优化解码，依赖重卷积或全帧注意力，编码成本过高，无法支撑流式条件生成、实时视频编辑等交互场景。
### 方法关键点
1. 分析预训练视频VAE的有效感受野，发现编解码patch几乎仅依赖时空邻域信息，无需全局时空建模
2. 基于因果窗口注意力构建流式编解码器，降低单帧计算量，且流式推理时temporal KV cache大小可控
3. 采用解耦编解码器蒸馏+联合微调的训练策略，保留预训练隐空间，可作为原有VAE的直接替换组件
### 关键结果
在MiniMax-H3上，编码速度较官方VAE提升5.2~6.2倍、解码速度提升3.0~3.3倍，PSNR更高；结合专属推理基建后加速比达13.4倍，几乎无质量损失
