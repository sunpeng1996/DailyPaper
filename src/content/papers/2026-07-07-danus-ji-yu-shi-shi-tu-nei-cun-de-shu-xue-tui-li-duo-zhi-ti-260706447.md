---
title: 'Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory'
title_zh: Danus：基于事实图内存的数学推理多智能体编排系统
authors:
- Jihao Liu
- Guoxiong Gao
- Zeming Sun
- Bin Wu
- Shurui Liu
- Jiedong Jiang
- Haocheng Ju
- Leheng Chen
- Ronnie Cheng
- Xiping Zhang
affiliations:
- 北京大学
- 京都大学
- 天津大学
- 斯坦福大学
- 西湖大学
arxiv_id: '2607.06447'
url: https://arxiv.org/abs/2607.06447
pdf_url: https://arxiv.org/pdf/2607.06447
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: Agent长链推理 · 共享内存设计
tags:
- MultiAgent
- Fact-Graph Memory
- Long-Horizon Reasoning
- Mathematical Reasoning
- Agent Orchestration
one_liner: 提出带共享事实图内存的多Agent编排框架，可完成研究级数学问题长链推理证明
practical_value: '- 多Agent分工架构可复用：主Agent做全局规划调度+Worker Agent做并行任务执行+独立校验模块做结果准入的三层架构，可直接迁移到电商推荐的多Agent召回/文案生成链路，解决并行任务冲突、结果不可靠问题

  - 共享事实图内存设计可借鉴：把验证通过的结构化产出（比如召回item特征、生成文案元信息）按依赖关系存为DAG，既支持多Agent并行读取复用，也支持错误结果的全链路级联撤回，适合长链路生成/推理任务

  - 任务编排思路可落地：主Agent定期同步全局状态、动态分配Worker任务的调度逻辑，可优化电商大促期间的多Agent算力分配，优先倾斜高潜力任务方向，提升整体资源利用率

  - 生成结果二次校验机制可复用：把结构化存储的结果重组成人类可读文本后，再走一遍校验链路的逻辑，可解决电商商品文案/营销话术生成时的信息失准问题，在可读性和准确性之间平衡'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM驱动的数学推理Agent已能解决部分公开研究问题，但多Agent并行探索时缺乏有效的全局状态管理与协调机制，容易出现中间结果冲突、错误传播、长链推理深度受限等问题，无法高效支撑研究级长周期数学证明任务。

### 方法关键点
- 三层Agent架构：主Agent（基于Claude Opus 4.8）负责全局规划、任务调度、状态汇总，支持对接人类专家或GPT-5.5-pro获取高阶策略；多Worker Agent（基于GPT-5.5）并行执行子任务探索，支持文献检索、子目标拆解、反例构造等能力；独立无状态验证器作为唯一正确性准入节点，负责校验所有待入库的数学命题与证明
- 共享事实图内存：采用DAG结构存储所有验证通过的事实，边记录逻辑依赖关系，仅允许验证通过的结果写入，支持错误事实的级联撤回，同时额外设置双层内存（Worker本地内存存执行日志、全局内存存探索死路/计划等中间信息）避免重复劳动
- 全流程闭环：从问题输入、并行探索、事实入库、动态调度到最终自动生成符合学术规范的证明论文，生成的论文需再次经过验证器校验确保内容与事实图一致

### 关键实验
在代数几何、奇点理论、组合数学等领域6个公开未解决的研究级数学问题上测试，对比baseline包括单Agent系统Rethlas、直接调用GPT-5.5-pro：所有问题直接调用GPT-5.5-pro均无有效输出；在最复杂的拟阵切分类问题上Rethlas三次尝试全部失败，Danus仅用5天就完成证明，生成的事实图包含3157条验证事实、最大依赖深度达54；所有案例仅需0-2次人类极简干预即可完成完整证明与论文输出。

### 最值得记住的一句话
多Agent系统的性能上限往往不取决于单模型能力，而取决于全局状态管理与任务编排的合理性，可靠的校验机制是长链推理正确性的核心支撑。
