---
title: 'MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off'
title_zh: MemoryCPT：面向性价比优化的端到端智能体记忆框架
authors:
- Songxin Lei
- Kun Ouyang
- Weilin Ruan
- Yuqian Wu
- Zhijiang Guo
- Yushi Sun
- Fugee Tsung
affiliations:
- 香港科技大学
- 腾讯光子工作室群
- 香港科技大学（广州）
- 香港中文大学
arxiv_id: '2608.04843'
url: https://arxiv.org/abs/2608.04843
pdf_url: https://arxiv.org/pdf/2608.04843
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 长会话记忆性价比优化
tags:
- AgentMemory
- LoRA
- GRPO
- RRF
- CostPerformance
one_liner: 提出两阶段可训练长会话记忆管道，通过蒸馏与GRPO优化实现记忆质量与推理成本的最优权衡
practical_value: '- 可直接复用离线蒸馏+在线检索压缩的两阶段记忆架构，离线处理长周期用户会话/交互历史，成本摊销到多轮查询，适配电商复访用户个性化推荐、智能客服Agent等场景

  - 成本感知的GRPO奖励设计可直接迁移，将token成本加权加入优化目标，避免人工在准确率和推理成本之间做阈值取舍，适合大流量LLM业务的成本控制

  - RRF融合稠密+稀疏检索的配置可直接复用：episodic记忆取top20、semantic记忆取top50、平滑系数k_rrf=60，无需额外调参

  - QPC（单位成本质量）指标可引入业务评估体系，替代仅看准确率的传统指标，更贴合LLM落地的ROI核算需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长horizon LLM Agent需处理跨多轮、多会话的交互历史，现有记忆系统要么依赖人工规则、多次LLM调用导致推理成本高企，要么过度压缩丢失关键证据，无法在回答质量和成本之间找到最优平衡，缺乏端到端可训练的性价比优化框架。
### 方法关键点
- 两阶段端到端架构：离线Query-agnostic Distillation（QAD）阶段，基于教师模型的显式推理轨迹做SFT，训练LoRA-A将会话分段、事件生成/合并、语义提取的模块化记忆构建能力蒸馏进小模型，输出结构化episodic+semantic记忆库，成本摊销到后续所有查询；
- 在线Query-aware Retrieval and Summarization（QAR）阶段，先通过RRF融合稠密+稀疏检索结果做粗筛，再用GRPO训练LoRA-B生成查询感知细摘要，奖励加权平衡回答F1和token消耗，下游QA模型全程冻结，默认奖励系数α=0.8时性价比最优；
- 提出QPC（Quality per Cost）指标，量化单位推理成本的回答质量，统一评估记忆系统的性价比。
### 关键实验
在LoCoMo、LongMemEval两个长会话记忆基准测试，对比BudgetMem、MemoryOS等5个主流基线，采用Qwen2.5-7B作为记忆模块基座时，LoCoMo测试集上F1达0.479、单query成本仅3.46（USD×10^4），相比最优基线BudgetMem，F1相对提升28%、推理成本降低7倍、QPC提升9倍。
### 核心结论
长周期Agent记忆系统的核心评价标准应该是单位成本产出的有效智能，而非单纯的准确率。
