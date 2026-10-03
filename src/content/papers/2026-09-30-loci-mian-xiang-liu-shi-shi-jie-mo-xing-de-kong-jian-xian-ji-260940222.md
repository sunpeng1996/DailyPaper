---
title: 'LOCI: Spatial Linear Memory for Streaming World Models'
title_zh: LOCI：面向流式世界模型的空间线性记忆架构
authors:
- Ji Xia
- Tingting Liao
- Xuezhi Liang
- Hao Li
- Guangyi Liu
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Pinscreen
arxiv_id: '2609.40222'
url: https://arxiv.org/abs/2609.40222
pdf_url: https://arxiv.org/pdf/2609.40222
published: '2026-09-30'
collected: '2026-10-03'
category: LLM
direction: 流式世界模型 · 混合记忆架构优化
tags:
- World Model
- KV Cache
- Linear Attention
- Memory Optimization
- Streaming
one_liner: 提出混合KV缓存与几何感知循环线性注意力的流式世界模型架构，降内存同时提升重访内容复现精度
practical_value: '- 混合KV缓存+固定尺寸循环记忆的架构可直接复用在长序列推荐场景，用户长行为序列建模时既能降低峰值内存，又能保留历史行为的细粒度信息

  - 几何感知的记忆寻址逻辑可迁移到多模态Agent的空间场景记忆模块，提升重访场景的内容召回准确率

  - 流式长序列恒定内存的处理方案可用于电商直播/长视频的实时内容理解与推荐场景，降低服务端部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型的记忆方案存在明显缺陷：KV缓存随视频长度持续增长，内存占用不可控；循环内存将历史压缩为固定尺寸状态，无法直接访问单条历史观测，导致相机重访已观测区域时内容复现精度低。
### 方法关键点
1. 采用混合空间记忆架构，一半Transformer块保留全量历史KV缓存存储细粒度视觉信息；
2. 另一半块仅处理当前数据块，补充引入结合相机投影几何的循环线性注意力记忆，将视角信息融入记忆寻址与存储逻辑；
3. 循环记忆输出传入后续KV缓存块，为查询提供累积场景上下文。
### 关键结果
在MIND记忆基准与外采轨迹数据集上，重访内容复现精度优于基线世界模型与同配置全softmax模型；全历史场景下峰值内存较全softmax降低约30%；边界KV约束下，长视频流式处理可维持恒定内存，同内存预算下精度优于全softmax。
