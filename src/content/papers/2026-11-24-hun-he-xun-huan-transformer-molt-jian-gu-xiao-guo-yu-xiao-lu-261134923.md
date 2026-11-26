---
title: Mixture-of-Loops Transformer
title_zh: 混合循环Transformer (MoLT)：兼顾效果与效率的循环Transformer新架构
authors:
- Lianghui Zhu
- Shijie Wang
- Xinggang Wang
- Jinze Bai
- Bo Wang
- Xiang Bai
affiliations:
- Huazhong University of Science & Technology
- ByteDance Seed
- University of Toronto
arxiv_id: '2611.34923'
url: https://arxiv.org/abs/2611.34923
pdf_url: https://arxiv.org/pdf/2611.34923
published: '2026-11-24'
collected: '2026-11-26'
category: LLM
direction: LLM架构优化 · 循环Transformer效率提升
tags:
- Transformer
- Looped Transformer
- KV Cache
- MoE
- Efficient Inference
one_liner: 提出混合循环Transformer系列架构，通过KV跨循环复用打破传统循环Transformer的效率瓶颈
practical_value: '- 垂域小模型训练优化：推荐/Agent场景下的垂类小模型可复用loop forcing并行训练方法，在不增加参数规模的前提下，通过循环架构提升模型表达性，用1.4-1.7倍的token效率降低垂域预训练成本

  - 低延迟生成场景适配：生成式推荐、用户query理解等对延迟敏感的场景，可直接复用MoL-Hybrid解码方案，让循环Transformer的推理延迟降到和普通Transformer持平，同时保留循环架构的效果优势

  - KV缓存优化迁移：跨层跨循环KV选择性复用的设计思路，可直接迁移到生成式推荐的长序列用户行为建模中，降低KV cache占用与计算开销，提升长序列推荐的推理效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统循环Transformer通过复用共享层提升模型表达性，但仅依赖残差流传递跨循环信息，既会造成信息稀释降低表示质量，也存在同位置跨循环依赖，推理必须逐循环串行执行，延迟是普通Transformer的数倍，表达性与效率的tradeoff难以突破。

### 方法关键点
- 提出核心模块Mixture-of-Loops Attention (MoLA)，允许每一层同时对不同深度、不同循环的KV做注意力计算，用KV内存选择性复用替代传统单一残差流作为跨循环信息传递媒介
- 推出3款适配不同场景的架构变体：MoLT-R保留残差流+跨循环同位置KV读取，追求极致效果；MoLT-KV每次循环从embedding重启，仅读取前序循环的前缀KV，消除同位置跨循环依赖，支持单趟解码；U-MoLT采用编码器-解码器拆分架构，分离内存构造与预测输出，平衡效果与效率
- 配套loop forcing并行训练策略，所有循环并行训练对齐跨循环表示，支持推理时超过训练设定的循环长度；MoL-Hybrid解码结合并行prefill与单趟解码，完全抹平循环架构的推理延迟overhead

### 关键实验结果
400B token从零预训练对比baseline OLMo3：700M参数版本实现1.7倍token效率，10下游任务准确率提升2.5个百分点；3B MoE版本10域平均困惑度降低0.75，10任务准确率提升2.1个百分点；113M小模型推理端，MoL-Hybrid-2解码延迟为996.6ms，与普通单循环OLMo3的1000.6ms基本持平。

### 核心结论
循环Transformer的效率瓶颈本质是跨循环信息传递机制的缺陷，用KV内存选择性复用替代单一残差流，可同时兼顾表达性、训练效率与推理延迟。
