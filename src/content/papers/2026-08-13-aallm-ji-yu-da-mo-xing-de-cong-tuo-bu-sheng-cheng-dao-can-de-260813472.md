---
title: 'AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation
  to Sizing Using Large Language Models'
title_zh: AaLLM：基于大模型的从拓扑生成到参数调优的端到端模拟电路设计框架
authors:
- Mohammed Ayman Habib
- Rylan Hart
- Morteza Fayazi
affiliations:
- University of Utah
arxiv_id: '2608.13472'
url: https://arxiv.org/abs/2608.13472
pdf_url: https://arxiv.org/pdf/2608.13472
published: '2026-08-13'
collected: '2026-08-15'
category: MultiAgent
direction: 多Agent协作 · 垂直领域LLM落地
tags:
- MultiAgent
- RAG
- Vertical LLM
- Feedback Loop
- Workflow Optimization
one_liner: 提出集成自动RAG、三Agent反馈机制的端到端模拟电路设计工作流，显著降低迭代耗时与调用次数
practical_value: '- 可复用「设计器-批评者-仲裁者」三角色Agent架构，解决生成-校验类任务的迭代冗余问题，适合广告文案生成、商品卖点优化等闭环场景

  - 垂直领域LLM落地时可参考自动从公开文献、行业手册构建RAG知识库的方案，大幅降低手动整理领域知识的成本

  - 多阶段决策系统中引入独立仲裁角色，可有效平衡生成质量与迭代效率，适配推荐系统召回-排序-重排多阶段结果仲裁场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
模拟电路设计高度依赖专家经验，现有LLM方案仅覆盖单点任务、需手动录入领域知识易出现幻觉、迭代效率低、难以生成创新拓扑，效果受限。

### 方法关键点
1. 自动从学术论文、专业教材构建领域知识库，搭配RAG注入专业知识，减少手动整理工作量；
2. 三Agent反馈架构：Designer负责生成电路参数，Critic校验参数合理性，Evaluator仲裁两方意见，减少无效迭代；
3. 微调Seq2Seq模型学习传统拓扑连接规则，重组生成创新合法拓扑。

### 关键结果
生成的创新拓扑品质因数（FoM）最高比已知拓扑高3倍；推理阶段SPICE调用次数比SOTA多Agent pipeline低3~4.5倍；整体耗时比现有方案降低40倍
