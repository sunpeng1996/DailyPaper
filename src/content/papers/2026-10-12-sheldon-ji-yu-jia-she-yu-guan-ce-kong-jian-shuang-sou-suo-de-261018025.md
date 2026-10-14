---
title: 'SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces'
title_zh: SHELDON：基于假设与观测空间双搜索的科学推理框架
authors:
- Harshit Joshi
- Priyank Shethia
- Monica S. Lam
affiliations:
- Stanford University
arxiv_id: '2610.18025'
url: https://arxiv.org/abs/2610.18025
pdf_url: https://arxiv.org/pdf/2610.18025
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: Agent 科学推理双空间搜索优化
tags:
- Reasoning Agent
- Dual Space Search
- Scientific Discovery
- Test-time Scaling
- Hypothesis Exploration
one_liner: 提出假设与观测双空间联合探索的科学推理Agent框架，跨任务性能最高超基线26.7个点
practical_value: '- 电商/广告流量异常根因排查Agent可复用双空间设计：假设空间维护召回/排序/运营/外部竞争等候选根因，观测空间维护埋点、日志、业务指标等证据，避免排查局限于初始假设的局部区域，提升根因定位准确率

  - 生成式推荐策略迭代可引入跨假设对比分析机制：同时对多个候选策略（如不同Semantic ID生成规则、召回逻辑）的AB测试观测做交叉验证，避免陷入局部最优，发现更多创新策略组合

  - 通用Agent推理任务可复用假设状态管理机制：对暂时搁置的低优先级假设设置3轮冷却期，后续观测更新后可重新召回，兼顾推理效率与方案覆盖度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Test-time scaling的LLM推理方法大多将观测收集绑定到当前假设，仅做局部优化，容易遗漏假设空间外的未知区域，难以发现颠覆性新方案，在复杂推理、根因排查、优化探索类任务上性能受限。

### 方法关键点
- 双空间独立建模：分别维护假设空间（候选解决方案、根因、规则等）和观测空间（实验结果、日志、指标、证据等），两类空间通过支持/反驳/中立/未解决四类证据关系关联
- 四步迭代推理：循环执行「探索（扩展双空间边界、生成新候选）→ 单假设分析（逐个验证每个假设的证据）→ 跨假设对比分析（寻找能区分多个假设的观测）→ 利用（保留/搁置假设、迭代优化）」流程
- 容错状态管理：搁置的假设置3轮冷却期后可召回，新观测设临时状态，仅重复验证后的观测可用于反驳假设，避免误判

### 关键结果
在诊断、抽象推理、优化3大类共10个基准任务测试，对比ReAct、Codex、EvoX、GoS等基线：无显式打分函数任务上，DiagnosisArena准确率84%超最强基线6个点，ORCA-Bench根因定位准确率66.67%超基线26.67个点，ARC-AGI-2推理准确率59.17%超基线11.67个点；有打分函数任务上，QNN拓扑优化达到满分1.0，超基线0.15，分子优化任务3个指标超过库内最优参考，5项系统优化任务全部取得最优或并列最优性能；消融实验显示移除观测空间后性能最高下降14个点，生成的新方案数量最多是基线的4.5倍。

最值得记住的结论：把观测作为一等公民独立建模，而非仅作为当前假设的附属证据，能大幅提升Agent的探索广度和推理性能。
