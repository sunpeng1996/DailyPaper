---
title: Accelerating Mixture of Block Attention via Dynamic Routing, KV-Centric Execution
  and Runtime Pipelining
title_zh: LightningMoBA：基于动态路由与KV调度的块混合注意力加速方案
authors:
- Yingqi Shi
- Junru Lu
- Yun Liu
- Di Yin
- Xing Sun
affiliations:
- Tencent Youtu Lab
arxiv_id: '2611.26268'
url: https://arxiv.org/abs/2611.26268
pdf_url: https://arxiv.org/pdf/2611.26268
published: '2026-11-18'
collected: '2026-11-20'
category: LLM
direction: 大语言模型 · 长上下文注意力加速
tags:
- MoBA
- KV cache
- Long Context LLM
- GPU Optimization
- Sparse Attention
one_liner: 提出LightningMoBA优化块混合注意力，同保留预算下实现1.2~1.6倍端到端生成加速且提升长上下文效果
practical_value: '- 长上下文Agent场景可直接复用动态阈值路由替换固定Top-k选KV块，大保留预算下路由效率最高提11倍，适配不同查询的上下文分布，减少无效计算

  - 电商搜推长用户行为序列建模用到块稀疏注意力时，可落地KV-centric执行策略，按KV块分组任务复用KV tile，实测注意力阶段 latency 降18%~34%

  - 部署长上下文LLM做商品文案生成、query理解时，可直接集成开源LightningMoBA kernel，Top16预算下拿到1.2~1.6倍端到端加速，还小幅提升长任务精度

  - 训练长上下文推荐领域预训练模型时，Top64预算下动态路由能提1.6倍训练吞吐量，训练损失几乎无劣化，大幅降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoBA方案采用固定Top-k选KV块，无法适配不同查询的分数分布，易保留弱相关块或丢弃高相关块；执行层采用查询中心调度，多个查询选到同一块KV时会重复加载，访存浪费严重，限制长上下文LLM的推理/训练效率。

### 方法关键点
- 动态阈值路由：替换固定Top-k，对每个查询的块得分设置相对最高得分的阈值，自适应保留符合相关性要求的KV块，无需排序，直接生成稀疏元数据，路由效率大幅提升
- KV中心执行：按（查询头，KV块）分组任务，同一块KV的所有查询请求合并处理，复用加载的KV tile；对高扇出块做感知拆分，限制单任务大小解决长尾调度问题
- 运行时流水线：针对Hopper架构优化，将TMA的KV传输、不规则查询采集和Tensor Core计算重叠，隐藏访存延迟

### 关键实验
基于RULER长上下文基准，对比基线为FlashMoBA，覆盖5个模型checkpoint（Qwen3-4B/235B/32B、Llama3.1-8B、内部GQA-30B）测试：1）同Top16保留预算下，端到端生成加速1.20~1.60×，平均RULER得分从74.42提升至75.28；2）Top32预算下设备路径加速2.16~2.56×，Top64下路由+CSC构造加速6.99~11.25×；3）训练场景下Qwen3-4B Top64预算实现1.602×训练吞吐量提升，训练损失几乎无差异。

> 最值得记住的一句话：块稀疏注意力的优化必须同时做路由策略和执行层的协同设计，才能在不损失精度的前提下拿到实质性能收益。
