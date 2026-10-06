---
title: 'The Extender: A Log-Structured Transformer'
title_zh: Extender：低持久化注意力内存开销的日志结构Transformer架构
authors:
- Jakob Eriksson
affiliations:
- University of Illinois Chicago
arxiv_id: '2609.32759'
url: https://arxiv.org/abs/2609.32759
pdf_url: https://arxiv.org/pdf/2609.32759
published: '2026-09-25'
collected: '2026-10-06'
category: LLM
direction: LLM架构优化 · KV cache内存压缩
tags:
- Transformer
- KV cache
- Long Context
- Memory Optimization
- Inference Acceleration
one_liner: 拆分残差流与注意力输入通道，924M参数下持久化KV缓存降低104倍且长上下文效果更优
practical_value: '- 可借鉴双通道拆分思路：在电商个性化Agent的LLM推理模块中，将会话上下文KV存储与下一轮回复预测的残差流拆分，用极小维度的extension存储注意力所需特征，大幅降低多轮会话的持久化内存开销，支持单GPU同时服务更多用户会话

  - 可复用ephemeral KV cache设计：在长文案生成、长用户行为序列召回的LLM推理场景中，仅持久化极小的x*缓存，KV临时缓存按需从x*重投影生成，会话间隙释放临时缓存，进一步降低峰值内存占用，且兼容GQA、量化等现有优化手段

  - 长上下文优化结论可复用：在需要处理用户超长浏览/搜索历史的生成式推荐场景中，Extender在同等参数量下长上下文效果优于标准Transformer，可直接替换底层基座降低推理成本同时提升长序列建模精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
标准Transformer的KV缓存内存随模型宽度、层数、上下文长度线性增长，大模型单轮会话持久化KV缓存可达上百GB，严重限制长上下文场景的部署效率；且残差流同时承载下一词预测和层间特征传递功能，存在特征竞争问题。

### 方法关键点
- 设计双通道架构：保留传统残差流h专用于下一词预测，新增日志结构的扩展通道x，每层仅向x追加32维极小extension向量εℓ，注意力的KV投影仅从x读取输入，Q投影同时读取h与x
- 统一全局x*缓存：所有层共享全量扩展后的x*缓存，替代每层独立的KV缓存，持久化内存开销仅与εℓ维度、层数、上下文长度相关
- 引入临时KV缓存：推理时按需从x*重投影生成当前层所需KV，会话间隙可释放临时缓存，重投影成本可通过GQA等优化大幅降低

### 关键结果
短上下文基于DCLM CORE数据集、长上下文基于RULER数据集评测，对比基线为同等参数量的Llama风格标准Transformer：199M~924M参数量下短上下文效果与基线持平，924M参数下长上下文RULER平均分显著优于基线，持久化注意力内存开销仅为MHA的1/104；兼容GQA优化，813M参数的GQA版Extender效果仍优于920M标准Transformer。

### 最值得记住的一句话
仅需每层输出32维的注意力专用特征，即可在不损失短上下文效果的前提下，实现百倍级的持久化KV缓存压缩，同时提升长上下文建模能力。
