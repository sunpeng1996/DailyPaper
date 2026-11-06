---
title: 'Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse
  Attention'
title_zh: 多层索引器：DeepSeek稀疏注意力的选择与注意力并行优化
authors:
- Serdarcan Dilbaz
- Arjun Krishna
- Kiran Kamble
- Daniel M. Bikel
affiliations:
- Writer AI Research, Writer, Inc.
arxiv_id: '2611.03768'
url: https://arxiv.org/abs/2611.03768
pdf_url: https://arxiv.org/pdf/2611.03768
published: '2026-11-01'
collected: '2026-11-06'
category: LLM
direction: 长上下文LLM推理 · 稀疏注意力优化
tags:
- Sparse-Attention
- Long-Context
- Inference-Optimization
- DeepSeek
- GLM-5
one_liner: 无需重训改权重，通过并行索引与注意力计算提升DSA架构长上下文LLM解码速度
practical_value: '- 业务中使用DeepSeek/GLM-5做长上下文RAG、电商导购Agent的团队，可直接集成MLI+IndexCache，无需重训即可获得最高14.5%的解码吞吐提升，精度损失在2pp以内完全可用

  - 跨层候选集复用的思路可迁移到推荐系统链路：上层召回输出的top-k候选集可直接复用给下层粗排，减少重复特征计算与候选检索开销

  - 工程上可借鉴多CUDA流并行技巧：将无强依赖的旁支计算（如用户兴趣检索、冷启动候选打分）和主路径排序计算并行，零算法改动提升链路吞吐'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
DeepSeek-V3.2、GLM-5等生产级长上下文LLM采用的DeepSeek Sparse Attention（DSA）架构中，每层前置的轻量索引器扫描全量KV cache选择top-k token是解码延迟的核心瓶颈；相邻层索引选择的token重合度高达26%~42%，存在显著跨层冗余，现有IndexCache方案仅通过减少索引器数量优化，未解决索引扫描与注意力串行执行的依赖问题，长上下文下优化空间有限。

### 方法关键点
- 提出Multi-layer Indexer（MLI）：让第ℓ层注意力直接复用前一层索引器的token选择结果，本层索引器与本层注意力在多CUDA流上并行执行，无需重训、无需新增权重，可直接嵌入SGLang生产解码图，输出选择结果和原生DSA完全一致
- 可与IndexCache无缝组合：IndexCache负责降低索引器执行次数，MLI负责隐藏剩余索引器的扫描延迟，两者优化效果相乘
- 可选融合解码核进一步加速DeepSeek-V3.2，仅微调占参0.5%的索引器参数即可恢复极端索引压缩下的效果损失。

### 关键实验
在10K~195K上下文长度下测试DeepSeek-V3.2、GLM-5，对比基线为原生DSA、纯IndexCache：
- 相同索引保留率下，MLI+IndexCache比纯IndexCache解码速度最高提升14.5%（DeepSeek-V3.2，保留率1/2）、9.8%（GLM-5，保留率1/2）
- 128K上下文下，MLI+IndexCache在1/4保留率时吞吐达原生模型的1.32倍，优于IndexCache在1/8保留率的1.28倍，同时选择新鲜度高一倍
- LongBench、RULER等长上下文 benchmark 得分仅比IndexCache低2个百分点以内，无显著效果损失。

### 核心结论
稀疏注意力优化的两个核心杠杆是减少索引执行次数、缩短索引等待时间，两者组合可实现几乎无精度损失的长上下文解码加速。
