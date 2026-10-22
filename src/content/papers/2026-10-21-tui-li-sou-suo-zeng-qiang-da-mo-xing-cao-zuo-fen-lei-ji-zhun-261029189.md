---
title: 'Reasoning-Search-Augmented LLMs: An Operational Taxonomy, Benchmark Analysis
  and Controlled Evidence Synthesis'
title_zh: 推理-搜索增强大模型：操作分类、基准分析与对照证据综述
authors:
- Biswas Poudel
- Nilson Chapagain
- Amit Kumar
- Xianshun Jiang
affiliations:
- Texas A&M University
- Texas A&M University–Corpus Christi
arxiv_id: '2610.29189'
url: https://arxiv.org/abs/2610.29189
pdf_url: https://arxiv.org/pdf/2610.29189
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 推理搜索增强框架选型
tags:
- RSA-LLM
- Reasoning
- Agentic RAG
- Taxonomy
- Benchmark
one_liner: 明确推理-搜索增强大模型的定义边界，提出四维分类体系，汇总同类方案的性能与效率增益
practical_value: '- 搭建电商导购/搜索Agent时，可复用RSA-LLM的三维准入条件判断系统是否属于自适应检索架构，避免将静态RAG误判为Agentic
  RAG

  - 优化搜索Agent成本-效果平衡时，可直接参考论文验证的组件增益：加入证据校验Judge模块可提升EM最高15.8pp，状态压缩可降低检索调用31.2%、token消耗44.1%

  - 评估Agentic RAG系统时，可参考论文提出的五类评价维度（答案质量/检索质量/grounding质量/控制效率/鲁棒性），避免只看最终准确率忽略 hallucination
  与检索效率问题

  - 长路径多步检索场景（如用户多轮商品找款），可优先尝试过程级RL奖励（信息增益、冗余惩罚）替代纯结果奖励，缓解稀疏信用分配问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM受限于静态参数知识、有限上下文窗口，传统静态RAG为一次性预处理流程，无法根据推理状态动态调整检索策略，易出现幻觉、证据利用不充分、检索冗余等问题；现有相关综述未明确自适应推理-搜索系统的边界，也缺乏统一的设计选型对比框架，不同研究的实验结果因变量混杂难以横向复用。
### 方法关键点
- 明确RSA-LLM三大准入条件：状态依赖的证据获取决策、带证据的外部交互、闭环证据集成，将静态RAG、固定多步检索等排除在核心范畴外
- 提出四维分类体系刻画设计空间：检索耦合方式（静态/自适应/有状态自适应）、控制器设计（单/多智能体、推理拓扑）、知识来源（开放Web/私有库/结构化存储）、grounding严格度（尽力/软/硬），将学习信号作为跨维度变量单独分析
- 建立基准的RSA-loop需求分级（低/中/高），仅纳入同研究内的对照消融结果，避免跨实验的模型、检索器、预算等变量混淆
### 关键结果
汇总13个核心RSA系统、15个基准的对照数据：检索token掩码可提升7B模型EM 8.8pp，过程级RL奖励可提升EM 2.45pp、F1 2.95pp，加入证据校验Judge模块可提升EM 15.8pp、F1 18.9pp，有状态证据压缩可降低 latency 17.7%、检索调用31.2%、输入token 44.1%，模块化规划+执行的BrowseMaster较基线提升准确率20.5pp。
> 最值得记住的一句话：自适应检索的核心价值是在预算约束下实现证据效用最大化，评估必须绑定搜索、token、延迟等成本指标做Pareto分析，不能孤立谈准确率
