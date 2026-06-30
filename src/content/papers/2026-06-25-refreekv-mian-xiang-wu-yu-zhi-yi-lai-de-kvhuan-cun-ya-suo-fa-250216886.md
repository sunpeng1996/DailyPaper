---
title: 'ReFreeKV: Towards Threshold-Free KV Cache Compression'
title_zh: ReFreeKV：面向无阈值依赖的KV缓存压缩方法
authors:
- Xuanfan Ni
- Liyan Xu
- Chenyang Lyu
- Longyue Wang
- Mo Yu
- Lemao Liu
- Fandong Meng
- Jie Zhou
- Piji Li
affiliations:
- Nanjing University of Aeronautics and Astronautics
- WeChat AI, Tencent
- Fudan University
- Independent Researcher
arxiv_id: '2502.16886'
url: https://arxiv.org/abs/2502.16886
pdf_url: https://arxiv.org/pdf/2502.16886
published: '2026-06-25'
collected: '2026-06-30'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- LLM inference
- compression
- memory optimization
one_liner: 提出无输入依赖阈值的自适应KV缓存压缩，兼顾内存节省和性能稳定性
practical_value: '- 业务部署LLM推理（如电商Agent、搜索问答）时，可直接复用1%通用阈值，无需针对不同任务调缓存预算，降低部署调优成本

  - 工程改造成本低，可复用位置排序+Uni-Metric终止的轻量设计，额外剪枝延迟可忽略，适配现有vLLM等推理引擎

  - 自动为复杂任务（如多步推理、长文档问答）分配更高缓存预算，对混合输入场景鲁棒性远好于固定阈值方法，避免复杂任务掉点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有KV cache压缩方法均依赖输入/任务特定的缓存预算阈值，同一固定阈值在不同任务上性能波动极大：比如20%固定预算在长文档数据集能保持性能，但在GSM8K推理任务上性能掉点超过70%。真实业务场景多为开放域混合输入，无法提前分域调优阈值，极易出现大幅性能退化，该问题此前未得到有效解决。

### 方法关键点
- 两阶段轻量设计，仅在prefill后执行一次剪枝，不增加解码阶段开销：第一阶段基于位置先验排序，保留前m个初始位置+逆序保留剩余位置，利用注意力汇和近期token更重要的特性，排序开销极低；
- 提出输入不敏感的Uni-Metric停止准则：基于最后一行注意力向量的Frobenius范数变化判断剪枝停止点，使用固定1%的通用阈值，无需针对输入调参；
- 工程优化：保留LLM前两层完整KV缓存，避免底层注意力分布均匀导致的重要token误剪，全程用PyTorch并行算子实现，无顺序循环开销，支持批量处理，适配vLLM分页缓存机制。

### 关键实验结果
在13个跨域数据集（覆盖推理、阅读理解、摘要、编码），对比5种主流KV压缩方法，测试多个尺寸主流LLM：Llama3-8B下平均压缩36.3%KV缓存，平均性能略超全缓存0.12%；Qwen2.5-7B下平均压缩24%，性能超全缓存2.63%；Mistral-7B压缩13%，性能仅下降1.5%；额外剪枝延迟仅0.03-0.15秒，整体推理吞吐量提升10%-20%。

最值得记住的一句话：固定1%的范数阈值就能跨模型跨任务保持近全缓存性能，无需针对业务场景调缓存预算
