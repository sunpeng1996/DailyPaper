---
title: 'GenPage: Towards End-to-End Generative Homepage Construction at Netflix'
title_zh: GenPage：Netflix 端到端生成式首页构建方案
authors:
- Lequn Wang
- Jiangwei Pan
- Fengdi Che
- Linas Baltrunas
affiliations:
- Netflix
- University of Alberta
arxiv_id: '2606.31031'
url: https://arxiv.org/abs/2606.31031
pdf_url: https://arxiv.org/pdf/2606.31031
published: '2026-06-30'
collected: '2026-07-01'
category: GenRec
direction: 生成式推荐 · 端到端首页生成
tags:
- Generative Recommendation
- End-to-End RecSys
- LLM4Rec
- Reinforcement Learning
- A-B Testing
one_liner: 用单Transformer替代多阶段推荐栈，端到端生成结构化首页，在线涨核心指标0.24%、降延迟20%
practical_value: '- 可复用自定义领域Tokenizer设计：将用户行为、实体、页面结构ID映射为单Token，既缩短序列长度降低推理延迟，又方便后续通过约束解码快速实现业务规则管控

  - 训练流程可直接借鉴「预训练+WBC后训练」的低门槛落地方案：预训练学历史优质分发的分布，后训练用加权二分类对齐业务目标，比RL落地复杂度低很多，可快速拿到指标收益

  - 工程落地Trick直接复用：多节奏增量训练（周级全量训练+日级增量更新）兼顾模型新鲜度和训练成本；语义嵌入融合（ID Embedding+内容语义Embedding）解决新品冷启动；混合行解码（行头部核心Token自回归生成、剩余实体单次前向选TopK）进一步压缩推理延迟

  - 资源投入优先级参考：当前工业场景下，丰富Prompt上下文（新增特征、优化Token化方式）的收益远高于单纯堆模型参数量，初期迭代优先做Prompt优化而非盲目扩模型规模'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统首页推荐依赖多阶段流水线（召回、排序、重排、模块组装），各阶段目标对齐成本高、特征工程冗余、维护复杂度高，且无法做全局页面级优化，难以兼顾内容多样性、模块注意力分配等全局业务诉求。
### 方法关键点
- 数据表示：自定义领域Tokenizer，将用户上下文（行为、属性、请求信息）、首页结构化内容（行、实体）统一编码为离散Token序列，每个实体/行对应单Token，大幅压缩序列长度
- 训练范式：采用「预训练+后训练」两阶段流程：先基于历史优质高互动首页做Next Token Prediction预训练，学习首页生成的基础分布；后训练支持两种方案：**WBC（加权二分类）** 基于用户反馈给每个Token标注正负标签与权重，优化交叉熵损失，落地门槛低；**RL** 基于页面级总Reward做全局优化，可捕获行/实体间的交互效应
- 工程适配：落地配套多节奏增量训练（周级全量+日级更新）保模型新鲜度、语义嵌入融合解决新品冷启动、约束解码强控业务规则、混合行解码降推理延迟
### 关键结果
基于Netflix内部生产数据，对比高度优化的成熟多阶段生产推荐栈：WBC版本在线A/B测核心用户engagement指标提升+0.24%（p<0.001），端到端服务延迟降低20%；离线实验显示，丰富Prompt上下文带来的WBC损失下降（6.9%）是模型从120M扩至900M参数收益（1.3%）的5倍以上；RL后训练未加入多样性目标的前提下，页面内容多样性仍可大幅提升。
### 核心结论
工业级生成式推荐场景下，上下文信息的质量与丰富度对效果的影响远大于模型参数量，优先优化Prompt的投入产出比更高
