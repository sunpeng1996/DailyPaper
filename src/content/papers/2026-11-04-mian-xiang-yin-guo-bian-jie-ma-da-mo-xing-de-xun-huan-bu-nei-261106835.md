---
title: 'LooM: Loop-Invariant Memory for Causal Encoder-Decoder Language Models'
title_zh: 面向因果编解码大模型的循环不变内存LooM优化方法
authors:
- Lele Yang
- Muxi Diao
- Zhonghao Yan
- Jiankang Chen
- Bin Wen
- Tingting Gao
- Wentao Zhang
- Kongming Liang
- Zhanyu Ma
- Weiran Xu
affiliations:
- 北京邮电大学
- 北京大学
- 中关村研究院
- Kling Team
arxiv_id: '2611.06835'
url: https://arxiv.org/abs/2611.06835
pdf_url: https://arxiv.org/pdf/2611.06835
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM推理优化 · KV缓存 循环Transformer
tags:
- KV cache
- Looped Transformer
- Causal Encoder-Decoder
- Inference Optimization
- Adaptive Compute
one_liner: 实现循环Transformer KV缓存不随循环数增长 单无路由checkpoint支持3-21层推理预算
practical_value: '- 可复用publish-once KV缓存机制到电商场景LLM服务（生成式推荐文案、Agent推理等），循环推理时不新增KV条目，显著降低显存开销，无需大规模修改模型结构

  - 借鉴Random-Depth训练策略，训练单模型支持多档推理预算，高峰时用低预算（少循环）保证吞吐，低峰时用高预算（多循环）提升效果，无需部署多套模型

  - 因果编解码架构的分层循环设计可迁移到生成式推荐定制LLM开发：用户/物品特征编码仅跑一次，仅循环生成侧只读层平衡输出质量和推理速度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Looped Transformer通过复用同参数层提升有效深度、不新增参数量，但三大痛点限制落地：KV缓存随循环次数线性增长，显存占用高；计算调整粒度粗，仅能按整个层块调整；训练后难以切换循环次数，需额外路由或停机策略，适配成本高。

### 方法关键点
- 基于因果编解码（CED）架构，仅循环解码器第一层后的只读层：编码器+第一层解码器每个token仅执行一次，写入全局内存，后续循环只读不写
- 设计publish-once规则：每个解码器层仅首次访问token时写入本地KV缓存，后续循环仅更新当前token隐藏态，不新增KV条目，缓存大小与循环次数完全无关
- 训练采用Random-Depth策略：每次更新随机采样推理预算与对应层循环次数，模型自动适配所有预算；推理时每个预算选验证最优静态路径，无需额外路由模块
- 每个只读层可独立循环0~4次，覆盖3~21层执行的全量预算，调整粒度细到单层级

### 关键结果
基于204M参数CED backbone，在5B tokens FineWeb-Edu数据上训练，对比单通baseline：
- 21层循环时，测试交叉熵低0.020 nats，零样本任务平均准确率高0.79个点，LAMBADA困惑度从180.4降至134.4，128token prompt下缓存仅364.1KiB，和3层循环时完全一致
- 11层循环时效果即超过单通baseline，相比固定21层循环的模型，latency降低33.3%，FLOPs减少28.2%
- 64K长上下文场景下，PG19困惑度比单通baseline低0.0068 nats，检索任务准确率高6个百分点

### 核心结论
在因果编解码架构下，仅循环只读层+KV首次写入机制，可在不增加显存开销的前提下，让单模型自适应多档推理预算，实现效果和成本的灵活权衡。
