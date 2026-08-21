---
title: 'ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language
  Models'
title_zh: ConceptGuard：大语言模型上下文敏感遗忘能力评测基准
authors:
- Sahil Kale
- Ian Harris
affiliations:
- Pune Institute of Computer Technology
- University of California, Irvine
arxiv_id: '2608.20338'
url: https://arxiv.org/abs/2608.20338
pdf_url: https://arxiv.org/pdf/2608.20338
published: '2026-08-20'
collected: '2026-08-21'
category: Eval
direction: LLM安全 · 机器遗忘评测
tags:
- LLM Unlearning
- Benchmark
- Context Sensitivity
- Model Safety
- Dual-use Concept
one_liner: 提出基于两用概念的LLM上下文敏感遗忘评测基准，验证现有方法的概念场景区分缺陷
practical_value: '- 电商Agent/合规大模型的内容安全评测可复用「同一概念+善恶意图配对」的框架，比如针对优惠券、退款等高频场景，构造恶意薅羊毛/正常咨询的配对样本，评估模型的场景区分能力，避免一刀切屏蔽正常请求

  - 对业务大模型做unlearning优化（如删除侵权商品介绍、违规引流话术）时，可优先选择SimNPO、RMU作为 baseline，二者的遗忘效果与业务效用的tradeoff显著优于梯度上升等传统方法

  - 内容风控模型迭代可引入CtxtSep指标，衡量模型对同一主题下风险内容与正常内容的区分度，替代单纯的准确率指标，降低正常商品/内容的误杀率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM unlearning评测基准采用独立的遗忘/保留集，仅评估孤立事实的删除效果，无法覆盖真实安全场景中「同一概念兼具善恶两种用途」的核心需求（如网络安全知识既可用于防护也可用于攻击），导致评测结果与实际安全表现存在显著偏差。
### 方法关键点
- 提出**dual-use concept**框架：遗忘集存储同一概念的有害用法，保留集存储同一概念的良性用法，两组样本完全互补而非独立
- 构建包含5166条配对样本的ConceptGuard基准，覆盖68个两用概念（网络安全、社会工程等），配套对应查询集
- 设计三层评测指标：遗忘质量（有害内容回忆度、HarmScore）、模型效用（良性内容保留度、HelpScore）、上下文区分度CtxtSep（同一概念下良性得分与有害得分的加权差）
### 关键结果
在Qwen-2.5-3B-Instruct、Llama-3.1-8B-Instruct上测试4种主流unlearning方法：梯度上升、SimNPO、RMU、UNDIAL。
- 梯度上升遗忘效果最优，但模型效用最高下降76%，属于过抑制
- SimNPO、RMU的遗忘-效用tradeoff最优，CtxtSep最高较基线提升73%，但仅达0.38，远未满足安全需求
- 不同概念的unlearning效果方差极大，社交行为类概念的区分一致性远低于技术类概念
### 核心结论
LLM安全unlearning的核心不是删除孤立事实，而是对同一概念的不同使用意图做精准区分。
