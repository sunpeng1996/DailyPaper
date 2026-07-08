---
title: Streaming Neural Speech Codecs through Time-Invariant Representations
title_zh: 基于时间不变表征的流式神经语音编解码器
authors:
- Kélian Estève
- Salima Mhdaffar
- Mickael Rouvier
- Richard Dufour
- Yannick Estève
affiliations:
- LIA, Avignon University, France
- LS2N, Nantes University, France
arxiv_id: '2607.05250'
url: https://arxiv.org/abs/2607.05250
pdf_url: https://arxiv.org/pdf/2607.05250
published: '2026-07-06'
collected: '2026-07-08'
category: Other
direction: 流式神经语音编解码 · 时间不变表征
tags:
- Neural Speech Codec
- Streaming Inference
- Time-Invariant Representation
- Low-Latency Processing
- Speech Generation
one_liner: 提出Dual-TIRE多层时间不变表征提取架构，实现无显著性能损失的低延迟流式神经语音编解码
practical_value: '- 电商语音交互Agent（智能导购、直播数字人）可复用跨文件采样策略，提升说话人/环境特征提取鲁棒性

  - 实时语音生成场景（实时客服语音回复、直播实时配音）可参考660ms分块流式推理方案，在基本不损失音质的前提下降低端到端延迟

  - 多模态生成式推荐的语音输出模块，可借鉴Dual-TIRE分层特征提取思路，分离语音内容与身份/环境属性，提升生成语音的说话人相似度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
神经语音编解码器是语音生成、多模态大模型的核心中间组件，现有方案帧级建模信息冗余高，难以适配低延迟流式推理需求。
### 方法关键点
1. 通过探测任务分析时间不变表征提取（TIRE）模块的信息属性，发现编码器中间层可捕捉互补的说话人、环境信息且几乎不含语言学内容
2. 验证跨文件采样的训练策略可显著提升不变表征的鲁棒性
3. 提出Dual-TIRE多层架构，利用不同编码器层的表征互补性优化性能
4. 采用660ms逐块处理的流式推理方案
### 关键结果
流式推理下语音重建性能无显著下降，语音重建质量、说话人相似度均优于基线TiCodec
