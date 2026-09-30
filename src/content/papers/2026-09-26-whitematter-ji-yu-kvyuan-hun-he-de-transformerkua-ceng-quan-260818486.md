---
title: 'WhiteMatter: All-to-All Cross-Layer Connections via KV Source Mixing'
title_zh: WhiteMatter：基于KV源混合的Transformer跨层全连接架构
authors:
- Wenbo Zhang
- Xiang Ren
affiliations:
- University of Southern California
arxiv_id: '2608.18486'
url: https://arxiv.org/abs/2608.18486
pdf_url: https://arxiv.org/pdf/2608.18486
published: '2026-09-26'
collected: '2026-09-30'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- Transformer Optimization
- Decoding Efficiency
- Cross-layer Connection
- Inference Acceleration
one_liner: 提出动态跨层KV混合架构与循环迭代策略，降低KV缓存同时提升模型性能与预填充速度
practical_value: '- 电商Agent长会话推理、长商品文案生成场景可直接复用跨层KV共享方案，半缓存配置下KV缓存占用降低39.4%，生成质量不降反升，适配低显存服务器/边缘端部署需求

  - 长Query理解、多轮对话历史处理的预填充阶段，可替换原有Jacobi迭代为循环Gauss-Seidel迭代，预填充速度提升12.5倍，显著降低搜索推荐系统中LLM模块的首包响应延迟

  - 生成式推荐的LLM4Rec模块可复用动态KV混合思路，将不同深度层的用户/物品语义表征按需融合，无需扩增模型层数即可获得等效于层数提升50%的性能收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer推理阶段KV缓存占比高，且每层只能读取同深度历史token的KV，无法复用已计算的跨层表征，导致显存占用高、模型容量利用率低；现有跨层KV共享方案存在表征压缩瓶颈，且并行训练/预填充迭代收敛速度慢，难以适配Agent、长文本生成、生成式推荐等低延迟高吞吐需求场景。

### 方法关键点
- 跨层KV池设计：对每个token的所有层隐状态，通过动态路由学习混合权重，生成k个共享KV通道，每层固定读取对应通道，KV缓存大小仅为原生Transformer的k/L
- 因果解码优化：采用严格因果注意力，当前token仅访问历史token的跨层KV，解码阶段仅需1次层栈+1次池化计算，吞吐与原生Transformer持平
- 循环Gauss-Seidel迭代：将token按步长划分为多组，组内并行计算、组间串行更新，单轮迭代即可实现信息跨token传播，解决跨层依赖导致的训练/预填充并行度低问题

### 关键结果
在FineWeb-Edu数据集上训练，对比原生Transformer、LCKV、FusedKV等基线：
- 同参数量下，半缓存WhiteMatter（k=L/2）在1.3B规模上perplexity降低4.3%，零样本任务平均得分提升1.76个百分点，解码峰值显存降低39.4%，吞吐与原生持平
- 全缓存WhiteMatter性能等效于层数增加50%的原生Transformer，预填充阶段循环迭代相比Jacobi迭代提速12.5倍

### 核心结论
跨层表征动态共享+细粒度分组迭代的组合，可在几乎不损失推理吞吐的前提下，同时实现KV缓存降本与模型性能提升，是LLM部署优化的高性价比方向
