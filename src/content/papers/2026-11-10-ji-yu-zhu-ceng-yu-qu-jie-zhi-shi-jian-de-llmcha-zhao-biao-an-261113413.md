---
title: Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines
title_zh: 基于逐层预取截止时间的LLM查找表分层存储方案
authors:
- Wen Huang
- Jack Liu
affiliations:
- Microsoft
- Independent Researcher
arxiv_id: '2611.13413'
url: https://arxiv.org/abs/2611.13413
pdf_url: https://arxiv.org/pdf/2611.13413
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: LLM推理服务 · 内存优化与分层存储
tags:
- LLM serving
- memory tiering
- Engram
- NVMe
- RDMA
- SGLang
one_liner: SlackTier分层存储方案可将LLM大查找表下沉到NVMe/RDMA，性能损失<1.4%时节省84%主机内存
practical_value: '- 电商/Agent场景用DeepSeek-V4、Qwen3.8等带大查找表的LLM服务，可直接复用SlackTier方案，将深层查找表下沉到NVMe，节省的内存扩容KV
  cache，可提升30%+服务吞吐量

  - 查找表GPU缓存优先分配给浅层（窗口短的层），无需全量缓存深层表，1GB小GPU缓存即可覆盖74%的Agent场景查找请求，效果远优于静态热数据集缓存

  - 带n-gram类输入索引查找表的模型，所有查找可在step启动时全部发起，与前序层计算重叠，几乎无额外 overhead'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
DeepSeek-V4.1等新架构LLM引入的Engram、PLE类大尺寸查找表（总容量可达203GB）占服务进程主机内存的85%以上，挤占KV cache空间，限制服务吞吐量；直接将表下沉到NVMe会导致6~7%的解码延迟上升，传统静态热数据缓存仅能将 overhead 降至4.9%，优化效果有限。

### 方法关键点
- 定义逐层预取窗口：查找表所在层的前序层计算总时长即为该层查找的可容忍延迟，DeepSeek-V4.1层1窗口仅0.3ms，层14窗口达9.3ms，差值超30倍
- 分层规则：查找表可下沉到读取延迟小于对应层窗口的存储介质，无需全量存于DRAM；GPU缓存优先分配给窗口更短的浅层，而非命中率相近的深层
- SlackTier嵌入SGLang的decode CUDA graph流，step启动时优先提交浅层查找请求，层内去重，读路径与原生gather结果位精确一致，无需修改模型定义

### 关键结果
基于OpenHands Agent轨迹、WildChat多轮对话 workload 测试，对比原生SGLang DRAM存表基线：
- 两层查找表全放4块NVMe，搭配1GB GPU缓存均分，解码性能仅下降0.7%（Agent）/1.7%（Chat），主机内存从212GiB降至34GiB
- 节省的内存扩容主机KV cache，在KV受限的Agent场景下，中位数吞吐量提升36%，p90首包时间从38s降至24s
- 通过RDMA从远端节点读表无需缓存，性能与DRAM存表几乎一致，单份表可同时服务2个实例

### 核心结论
对于输入token索引的确定性查找表，按其所在层的预取窗口做分层存储，优化效率远高于单纯依赖热数据缓存的方案
