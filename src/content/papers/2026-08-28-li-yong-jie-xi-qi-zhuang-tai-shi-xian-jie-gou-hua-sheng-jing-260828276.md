---
title: 'Parser States Already Know: Structure-Conditioned KV Persistence for Structured
  Generation'
title_zh: 利用解析器状态实现结构化生成场景下的KV缓存持久化优化
authors:
- Linze Wu
- Xinrui Chen
affiliations:
- 中国科学院大学杭州高等研究院
arxiv_id: '2608.28276'
url: https://arxiv.org/abs/2608.28276
pdf_url: https://arxiv.org/pdf/2608.28276
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM推理优化 · KV cache结构化压缩
tags:
- KV cache
- Structured Generation
- Constrained Decoding
- LLM Inference
- Function Calling
one_liner: 复用约束解码的解析器状态指导KV缓存分配，大幅提升结构化生成任务的推理吞吐与准确率
practical_value: '- 做Agent工具调用/结构化输出场景的KV压缩时，可直接复用约束解码已有的解析器状态信号，不用额外计算注意力权重判断KV重要性，降低在线开销

  - 可借鉴「任务错误敏感度设保护底线+注意力失真分配剩余容量」的双指标策略，平衡准确率和KV压缩率，避免核心结构信息（如参数名、必填字段）被错误丢弃

  - 离线校准+在线查表的架构可直接复用在业务场景，用小批量业务数据完成校准后，在线仅做轻量lookup，几乎不增加推理延迟，适合高吞吐的电商推荐/广告Agent调用场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
结构化生成是LLM Agent输出JSON、SQL、函数调用的核心能力，单个字段错误就会导致下游任务失败；现有KV压缩方法仅依赖模型侧注意力、量化误差等信号，未利用约束解码过程中已有的解析器结构信息，存在模型侧KV敏感度与任务级结构风险不匹配的问题，容易丢弃对结构正确性至关重要的KV，导致压缩后准确率大幅下降。

### 方法关键点
- 提出PASK框架，将约束解码产生的解析器迁移转换为结构标签，结合Transformer层组划分，为每个（结构标签，层组）桶分配RELEASE/RETAIN-LOW/RETAIN-HIGH三种持久化策略
- 离线校准阶段用任务错误敏感度设置每个桶的最低保护优先级，再用注意力输出失真度排序剩余KV容量的分配优先级，生成查表规则
- 在线推理阶段仅需根据解析器状态查表得到KV持久化策略，无额外复杂度，同时支持预填阶段KV压缩的轻量化扩展

### 关键结果
实验在BFCL非实时、实时两个子集的8个子类别函数调用任务上开展，测试模型为Qwen3-4B、Qwen3-14B，对比Full KV、H2O、SnapKV等主流KV压缩方法：总KV预算0.33时，Qwen3-4B上平均准确率比最优基线高17.39个百分点；端到端推理吞吐最高提升2.2倍，TPOT最低降低3.3倍，峰值GPU内存仅为Full KV的0.53倍。

### 核心启示
约束解码过程中已经产生的解析器状态是免费且高质量的结构信号，直接复用即可大幅提升结构化生成场景的KV压缩效率与准确率。
