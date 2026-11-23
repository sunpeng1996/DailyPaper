---
title: 'MemOnce: A Scalable Memory Architecture for Large Language Models'
title_zh: MemOnce：面向大语言模型的可扩展内存架构
authors:
- Chang Nie
- Chaoyou Fu
- Songlin Liu
- Yiqing Hu
- Caifeng Shan
affiliations:
- Nanjing University
- University of Science and Technology of China
arxiv_id: '2611.27973'
url: https://arxiv.org/abs/2611.27973
pdf_url: https://arxiv.org/pdf/2611.27973
published: '2026-11-19'
collected: '2026-11-23'
category: LLM
direction: LLM长上下文推理 · KV cache优化
tags:
- KV Cache
- Long Context
- Memory Architecture
- Inference Optimization
- Sparse Attention
one_liner: 通过内存编解码和单次稀疏注意力实现长上下文推理低时延高吞吐的LLM内存架构
practical_value: '- 电商多轮会话Agent场景可直接复用MemOnce的KV cache压缩方案，1M上下文下内存降1313×、prefill时延降6.9×，大幅降低长会话部署成本

  - 长文本商品详情/超长用户行为序列建模场景，可复用最终层隐藏态1/8比例压缩+跨层共享的trick，几乎无精度损失下降低存储开销

  - Agent记忆模块可替换原有RAG的reranker组件，MemOnce的记忆表征零样本迁移到检索任务超过BGE-M3等专用模型，简化记忆链路'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM落地多轮会话、长上下文Agent等持续交互场景时，标准Transformer的KV cache随上下文线性增长、计算复杂度平方级上升，线性时间架构又存在细粒度信息丢失问题，现有方案无法同时兼顾召回精度、推理效率和内存可控性。
### 方法关键点
- 内存编解码器：仅缓存最终层1/r（默认r=8）的尾部隐藏态作为紧凑内存表征，通过轻量层专属MLP动态解码为各层KV cache，实现Lr倍的跨层跨时间压缩
- 内存稀疏注意力：将内存池划分为短期窗口和长期池，针对当前输入仅做1次top-K（默认K=64）相关内存检索，路由索引跨所有层共享，实现常数级活跃内存占用
- 适配灵活：支持从头预训练，或冻结主干仅通过LoRA微调内存模块适配现有预训练LLM，无灾难性遗忘问题
### 关键结果
在4K~1M上下文的长内存基准上对比Qwen3.5、M+、Metis等基线，4B参数下1M上下文场景：内存状态缓存降低1313×，prefill latency降低6.9×，吞吐量提升3.5×，长上下文记忆任务平均性能超全上下文基线+5.77%；零样本迁移到检索任务，整体Recall@10和NDCG@10均超过BGE-M3、Qwen3-Embedding等专用模型。
**最值得记住的结论**：仅缓存最终层尾部隐藏态并单次检索解码的设计，在大幅降本提效的同时甚至能超过全上下文基线性能，打破了长上下文优化必然损失精度的固有认知。
