---
title: 'MaxKernel: Agentic Kernel Generation for TPUs'
title_zh: MaxKernel：面向TPU的智能体内核生成框架
authors:
- Shangkun Wang
- Nina Cai
- Charles Hoong
- Julian Walker
- Gerson Kroiz
- George Vanica
- Deepak Patil
- Andi Gavrilescu
- Hassan Sipra
- Sethu Sankaran
affiliations:
- Google
- Google DeepMind
arxiv_id: '2609.04523'
url: https://arxiv.org/abs/2609.04523
pdf_url: https://arxiv.org/pdf/2609.04523
published: '2026-09-02'
collected: '2026-09-07'
category: Agent
direction: Agent 硬件内核自动优化
tags:
- MultiAgent
- Kernel Optimization
- TPU
- RAG
- Autonomous Search
one_liner: 多Agent框架支持三种编排模式生成TPU高性能内核，性能超过人类手调基线
practical_value: '- 多Agent任务拆分架构可复用：将复杂工程任务拆解为规划、实现、测试、调优、profiling专用子Agent，比单Agent稳定性提升显著，适合推荐/广告系统的特征工程、规则生成等落地场景

  - 三种编排模式的权衡思路可迁移：针对不同场景选择HITL（需人类把控的复杂业务规则）、单自动闭环（标准化任务快速迭代）、图搜索（需全局探索的优化问题），平衡可控性、迭代速度与优化效果

  - 闭环反馈+RAG的落地技巧：复杂领域任务不要使用纯零/少样本LLM，接入领域知识库RAG+实时工具反馈（如性能数据、错误日志），可大幅提升输出正确性，适合推荐系统策略生成、A/B实验分析等场景

  - 搜索优化的权衡经验：并行独立搜索适合需长迭代调试的复杂任务，束搜索适合优化空间清晰、反馈明确的任务，可直接复用在推荐系统超参数调优、召回策略搜索等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
定制高性能硬件内核需要深厚的底层硬件知识，人工开发成本极高；纯LLM零/少样本生成内核正确率极低，传统编译器优化又需要大量领域知识或昂贵的进化搜索，亟需高效的自动化内核生成方案。

### 方法关键点
- 模块化多Agent架构：拆分为规划、代码实现&修复、测试验证、自动调优、性能profiling 5个专用子Agent，各自负责单一子任务，降低单Agent复杂度
- 支持三种编排模式：1）人在回路模式，每个子Agent执行完返回控制权给人类，适合复杂内核的专家引导优化；2）自动闭环模式，迭代执行规划-生成-测试-调优-profiling全流程，无需人工干预；3）图基自动搜索模式，把内核设计空间建模为搜索图，支持并行搜索、束搜索等策略，避免局部最优
- 内置RAG知识库：存储硬件文档、框架手册等静态知识，避免全量塞入上下文窗口，且不引入人类手调内核代码，保证优化泛化性
- 自动闭环机制：固定测试套件避免奖励作弊，保留历史最优状态防止性能回退，错误自动回退到规划阶段重试

### 关键实验
在JaxBench的50个TPU内核任务+8个生产级真实模型内核上测试，对比Best-of-N零样本生成、人类手调内核基线：MaxKernel并行搜索模式在JaxBench上几何平均加速1.58×，8个生产级任务上几何平均加速2.32×，超过人类手调的2.02×，编译率和正确率均达100%；DeepSeek-V4稀疏注意力任务最高加速7.85×，Qwen3-Next训练步骤最高加速4.70×。

### 核心结论
复杂工程领域的Agent系统，通过任务拆分+工具反馈+分层搜索的设计，完全可以达到甚至超过领域专家的工作效果，同时大幅降低人力成本。
