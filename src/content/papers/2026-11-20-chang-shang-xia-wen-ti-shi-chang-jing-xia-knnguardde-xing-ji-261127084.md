---
title: Auditing and Adapting kNNGuard for Long-Context Prompts
title_zh: 长上下文提示场景下kNNGuard的性能审计与免训练适配
authors:
- Niccolò Ronchetti
arxiv_id: '2611.27084'
url: https://arxiv.org/abs/2611.27084
pdf_url: https://arxiv.org/pdf/2611.27084
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM安全护栏 · 长上下文适配
tags:
- kNNGuard
- Long-Context
- Guardrail
- RAG
- Hallucination-Detection
one_liner: 通过三种免训练优化大幅提升长上下文场景下kNNGuard的审核与幻觉检测性能
practical_value: '- 做电商导购/客服Agent安全审核时，可直接复用长度路由双参考库设计，无额外latency，仅需按输入token长度路由匹配长短参考库即可提升长文本（用户长咨询、长商品详情）审核准确率

  - 长文本RAG场景（电商商品知识库问答、广告素材合规审核）可复用跨步窗口Top-2均值聚合方法，无需额外LLM推理，仅从prefill阶段提取固定步长的中间token隐状态即可缓解长上下文信号稀释问题

  - RAG幻觉检测场景直接弃用静态文本embedding的kNN分支，仅保留LLM隐态的kNNGuard LE分支即可避免无效分支拉低整体检测效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有免训练LLM护栏kNNGuard在短输入（≤256 tokens）下表现优异，但在长上下文（>1000 tokens）场景（长文档审核、RAG问答等）性能骤降到接近随机水平；而当前生产级护栏多依赖微调大模型，存在latency高、策略迭代成本高的问题，亟需适配长上下文的免训练护栏方案。

### 方法关键点
- 长度路由双参考库：分别构建短（≤256 tokens）、长（>512 tokens）两个独立参考库，推理时先统计输入token数直接路由到匹配库，无额外开销，避免隐态长度偏移导致的匹配失效
- 长上下文embedding替换：将默认的MiniLM（仅支持256 tokens）替换为Qwen3-Embedding-0.6B（支持32768 tokens），消除长文本截断问题
- 跨步窗口池化：LLM激活分支从prefill阶段提取每256个token位置的中间隐态分别打分，embedding分支将长文本切为256 token重叠窗口分别编码，最终用Top-2均值聚合所有窗口得分，缓解长文本单向量信号稀释问题

### 关键结果
在内容安全审核Aegis-2.0数据集上：长上下文场景下，优化后的kNNGuard LE AUROC从0.554提升到0.828（+0.274），融合版kNNGuard FE AUROC从0.721提升到0.886（+0.164），无额外latency。
在RAG幻觉检测HaluBench数据集上：中等长度（257-1000 tokens）场景下kNNGuard LE AUROC恢复到0.853，静态embedding分支在所有长度下均接近随机水平（0.46-0.56 AUROC），融合反而拉低效果。

### 核心结论
免训练隐态护栏适配长上下文的核心是消除参考库与输入的长度分布偏移，同时避免长文本单向量压缩导致的局部信号丢失。
