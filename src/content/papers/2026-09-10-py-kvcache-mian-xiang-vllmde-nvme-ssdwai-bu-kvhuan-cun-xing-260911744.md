---
title: 'Building py-kvcache: A Performance Characterization of External KV Caching
  for vLLM with NVMe SSDs'
title_zh: py-kvcache：面向vLLM的NVMe SSD外部KV缓存性能表征与实现
authors:
- Joseph Kanichai
- Tiziano De Matteis
- Animesh Trivedi
affiliations:
- Vrije Universiteit Amsterdam
- IBM Research Zurich
arxiv_id: '2609.11744'
url: https://arxiv.org/abs/2609.11744
pdf_url: https://arxiv.org/pdf/2609.11744
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM推理优化 · 外部KV缓存
tags:
- KV cache
- vLLM
- NVMe SSD
- LLM inference
- TTFT optimization
one_liner: 设计适配vLLM的外部KV缓存py-kvcache，量化跨层缓存收益临界点，性能优于LMCache
practical_value: '- 部署LLM驱动的电商导购Agent、长文档RAG服务时，若长上下文请求占比高、GPU显存不足，可接入py-kvcache用NVMe
  SSD做外部缓存，80k token场景下TTFT比LMCache低50%

  - 不要无脑开启外部KV缓存，需先基于自身硬件（GPU算力、SSD带宽）和业务请求特征（前缀长度、复用率）测算盈亏平衡点，低于阈值时GPU重算比加载缓存更快，比如H100上大部分短请求无需开启外部缓存

  - KV缓存优化优先做调度层面的预加载：给排队中的请求提前读取KV数据，把磁盘I/O移出TTFT关键路径，仅该优化即可带来34%的TTFT提升，收益高于单纯堆SSD带宽

  - 自研vLLM KV缓存扩展时，优先用KV Offload API而非旧的KV Transfer API，配合大粒度块传输、限制中间staging内存，可减少不必要的拷贝开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM请求的KV缓存容量随token数线性增长，极易耗尽GPU显存，通过NVMe SSD等介质实现的外部KV缓存可大幅扩展缓存容量，但现有方案默认所有前缀命中均走缓存路径，未考虑短前缀、高算力GPU场景下，加载缓存的I/O+传输开销反而高于GPU重算成本，且I/O路径未和调度、计算重叠，TTFT优化效果不达预期。

### 方法关键点
- 基于vLLM KV Offload API实现py-kvcache，采用分层文件系统存储KV块，无需额外组件即可跨多vLLM实例共享缓存
- 基于io_uring实现异步直接I/O，显式限制中间staging内存上限，避免无意义的内存拷贝与数据放大
- 新增调度感知预加载机制，请求排队阶段即启动磁盘读取，与已有计算任务重叠，将磁盘I/O移出TTFT关键路径
- 新增缓存准入策略，实测当前硬件、workload下的盈亏平衡点，低于阈值的前缀直接绕过外部缓存，由GPU重算

### 关键结果
基于Llama 3.2 3B、Qwen3 4B测试，对比LMCache、原生vLLM KV Offload，覆盖合成长文档、LongBench、SCBench、Bailian生产trace：80k token场景下，纯磁盘读取模式py-kvcache比LMCache快2.0×，其中预加载贡献1.34×的性能提升；三级缓存（GPU+CPU+磁盘）模式下比LMCache快1.23×，与原生vLLM KV Offload性能差距仅约4%；H100高算力GPU场景下，大部分生产请求前缀长度低于盈亏平衡点，仅靠GPU本地缓存即可满足需求，开启外部缓存无收益。

**最值得记住的一句话**：外部KV缓存不是通用性能优化，其收益由硬件配置、workload前缀特征共同决定，必须先测算盈亏平衡点再开启，调度层面的I/O预加载优化收益远高于单纯提升存储带宽。
