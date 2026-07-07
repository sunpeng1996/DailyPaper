---
title: KVpop -- Key-Value Cache Compression with Predictive Online Pruning
title_zh: KVpop：基于预测式在线剪枝的KV缓存压缩方法
authors:
- Lukas Hauzenberger
- Niklas Schmidinger
- Anamaria-Roberta Hartl
- David Stap
- Thomas Schmied
- Sebastian Böck
- Günter Klambauer
- Sepp Hochreiter
affiliations:
- NXAI
- Johannes Kepler University Linz
arxiv_id: '2607.05061'
url: https://arxiv.org/abs/2607.05061
pdf_url: https://arxiv.org/pdf/2607.05061
published: '2026-07-05'
collected: '2026-07-07'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- LLM inference
- model compression
- long context
- pruning
one_liner: 基于未来注意力监督的学习式KV缓存剪枝方法，高压缩比下几乎无损保留LLM长上下文性能
practical_value: '- 业务侧部署长上下文LLM服务（如商品解读、多轮对话推荐Agent）时，可复用KVpop的固定预算缓存设计，75%-88%压缩比下仅损失2%-5%推理质量，大幅降低单卡显存占用、提升服务并发

  - 未来注意力监督思路可迁移到推荐系统用户行为序列剪枝：用未来点击/转化信号作为监督，淘汰长期无用的历史行为特征，压缩序列建模内存开销

  - 延迟打分设计可复用：对缓存/序列元素不要在插入时做留存决策，等待N步后用近邻上下文再判断，大幅提升决策准确率，可用于用户会话特征留存判断场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
KV cache随上下文长度线性增长是LLM长上下文推理的核心瓶颈，现有驱逐方法多依赖静态启发式规则或代理打分，无法准确预测token未来的注意力价值，上下文相关性变化时容易误删关键token，导致推理质量大幅下降。

### 方法关键点
- 分三类固定缓存区：永久保留sink初始token、w长度的最近滑动窗口token、k个学习选择的长程token，单头总缓存预算固定为s+w+k，内存占用完全可控
- 训练时用转置注意力计算未来注意力目标作为监督信号：无需生成密集S×S注意力矩阵，复用注意力核返回的LSE归一化值即可计算token离开滑动窗口后的未来注意力权重，无推理额外开销
- 支持延迟状态打分：token进入缓存时不立刻打分，等到离开滑动窗口即将进入淘汰池时，用mLSTM状态累积的近未来上下文信息计算重要性，决策更精准
- 边界感知损失优化：仅在缓存淘汰边界处对新进入淘汰池的token和当前最低分保留token做pairwise损失，训练效率更高

### 关键实验
在AIME、HMMT数学推理数据集上测试，对比StreamLLM、TOVA、DMS等主流KV缓存压缩基线：Qwen3-4B在75%压缩比下保留98%全注意力性能，88%压缩比下保留97%性能；Qwen3-8B在88%压缩比下性能几乎无损，同时长上下文解码latency比DMS更低，显存占用稳定不随生成长度线性增长。

**最值得记住的一句话**：学习式KV缓存压缩的核心是用未来真实效用信号替代静态启发式规则，在固定内存预算下可以实现几乎无损的长上下文推理性能。
