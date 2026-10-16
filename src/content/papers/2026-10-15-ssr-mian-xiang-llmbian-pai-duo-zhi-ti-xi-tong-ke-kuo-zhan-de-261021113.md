---
title: 'SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated
  Multi-Agent Systems'
title_zh: SSR：面向LLM编排多智体系统可扩展Agent发现的结构信号检索器
authors:
- Giancarlo Maldonado Cárdenas
- Carlos A. Astudillo
- Nelson L. S. da Fonseca
affiliations:
- Institute of Computing, State University of Campinas, Brazil
arxiv_id: '2610.21113'
url: https://arxiv.org/abs/2610.21113
pdf_url: https://arxiv.org/pdf/2610.21113
published: '2026-10-15'
collected: '2026-10-16'
category: MultiAgent
direction: 多智体系统 · Agent发现检索优化
tags:
- Multi-Agent
- Agent Discovery
- Retrieval
- Inverted Index
- LLM Orchestration
one_liner: 提出无训练的结构信号检索器SSR，大幅降低多Agent系统Agent发现的LLM上下文开销与延迟
practical_value: '- 电商多Agent业务（智能客服、营销Agent编排）可直接复用SSR的预检索架构，用固定预算K控制送入LLM的Agent候选数，避免上下文随Agent库膨胀，降低推理成本与延迟

  - 若系统有结构化的Agent/工具描述卡片，可直接复用SSR的IDF加权结构信号匹配+倒排索引方案，无需训练、可解释，上线成本低，效果与BM25相当

  - K值选择可参考文中方法：选最小的K，使得各规模下召回率比最优值低不超过0.02，平衡上下文开销和检索覆盖率

  - 当前用全量Agent送入LLM选择的方案，先加一层轻量候选预检索（SSR/BM25均可），就能拿到90%以上的成本延迟收益，无需直接上复杂向量检索'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大规模多Agent生态中，全量Agent卡片送入LLM编排的方案会导致上下文随Agent库线性增长，推高推理成本、延迟，还容易触发上下文窗口超限；现有工具/Agent检索方案未明确解耦检索层和LLM上下文约束，大多需要训练、可解释性差。

### 方法关键点
- 定义候选上下文可扩展性问题，解耦全库检索和送入LLM的候选池，用固定最大候选数K控制LLM输入大小
- 检索器SSR完全无训练、可解释：从Agent卡片的能力相关字段提取1/2元词作为结构信号，用IDF加权计算匹配得分
- 构建倒排信号索引(ISI)，仅对和查询有共享信号的Agent打分，大幅降低检索计算量
- 候选按得分排序后取Top K送入LLM做最终选择，得分可回溯到具体匹配的信号

### 关键实验结果
- 数据集：自研SSR-AgentBench（1000个Agent卡片，250个查询）、适配MS MARCO数据集，基线为全量编排、BM25
- 1000个Agent规模下，SSR相比全量编排减少98.8%的LLM输入token，降低70.9%的端到端延迟
- MS MARCO上ISI减少96.8%的打分样本，检索速度提升74.2倍；端到端效果和BM25无统计显著差异
- 5000个Agent规模下全量编排完全不可用，SSR仍稳定运行

### 核心结论
多Agent系统中，只要加一层轻量候选预检索，就能用极小的效果损失，换取极大的成本、延迟、可靠性收益，不需要一开始就上复杂的检索方案
