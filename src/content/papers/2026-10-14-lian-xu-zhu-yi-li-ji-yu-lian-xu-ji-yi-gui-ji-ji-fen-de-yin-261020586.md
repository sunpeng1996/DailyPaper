---
title: Continuum Attention
title_zh: 连续注意力：基于连续记忆轨迹积分的因果Transformer注意力算子
authors:
- Afshin Khadangi
affiliations:
- University of Luxembourg
arxiv_id: '2610.20586'
url: https://arxiv.org/abs/2610.20586
pdf_url: https://arxiv.org/pdf/2610.20586
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: LLM基础算子 · 注意力机制优化
tags:
- Attention
- Transformer
- CausalLM
- Continuous Integration
- GPU Implementation
one_liner: 将离散KV查找替换为连续记忆轨迹积分，实现无额外参数量的更优因果注意力算子
practical_value: '- 做LLM4Rec/生成式推荐时，可直接替换原有软注意力为固定温度版Continuum Attention，无需增加参数量即可提升用户行为序列、候选集序列的建模效果

  - 上下文长度≤512的短序列场景（如个性化push文案生成、短序列用户召回排序）下，CA训练速度与软注意力相当，架构改动成本极低

  - 连续KV插值的设计思路可迁移到RAG记忆检索模块，对相邻相关记忆段做插值融合，减少检索结果跳变，提升对话Agent的回复连贯性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统Transformer软注意力仅对离散KV点做加权聚合，没有利用相邻token语义的连续性，限制序列建模效果，过往连续注意力方案难以直接嵌入标准Transformer架构落地。

### 方法关键点
- 相邻KV向量通过分段线性插值构造连续记忆轨迹，首尾补0.5token的常数扩展段保证权重均匀性
- 每个query生成沿轨迹的指数相关密度，通过0/1/2阶指数矩的闭式解直接计算积分结果，无需数值积分
- 支持解析求导，可直接替换标准因果Transformer的注意力层，时间复杂度与原生软注意力一致为O(T²dh)，支持GPU并行实现
- 固定温度版本无额外训练参数，可直接与同配置软注意力对标

### 关键实验
在TinyStories字节级语言建模任务上测试6层5M参数Transformer：固定温度0.3的CA版本在上下文长度192时验证NLL比软注意力低0.02nats/byte，上下文512时低0.048nats/byte，5组种子实验全部获胜；512长度下独立验证集仍领先0.0457nats/byte，95%置信区间不包含零；192长度下训练速度与软注意力相当，512长度下训练慢7.3%、推理慢39%。

### 核心结论
固定温度的连续注意力不需要额外参数量就能稳定优于同配置软注意力，短上下文场景下可直接落地替换。
