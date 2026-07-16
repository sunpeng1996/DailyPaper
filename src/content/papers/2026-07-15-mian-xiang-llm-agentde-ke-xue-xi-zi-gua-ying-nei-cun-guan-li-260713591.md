---
title: 'Memory as a Controlled Process: Learned Adaptive Memory Management for LLM
  Agents'
title_zh: 面向LLM Agent的可学习自适应内存管理框架MEMCON
authors:
- Eric Hanchen Jiang
- Zhi Zhang
- Yuchen Wu
- Levina Li
- Dong Liu
- Xiao Liang
- Rui Sun
- Yubei Li
- Edward Sun
- Haozheng Luo
affiliations:
- University of California Los Angeles
- University of Washington
- Northwestern University
arxiv_id: '2607.13591'
url: https://arxiv.org/abs/2607.13591
pdf_url: https://arxiv.org/pdf/2607.13591
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: LLM Agent 自适应内存管理优化
tags:
- LLM Agent
- Memory Management
- Contextual Bandit
- UCB
- Adaptive Control
one_liner: 提出后端无关的轻量自适应内存控制框架MEMCON，无需额外LLM调用，同时提升任务成功率并降低token消耗
practical_value: '- 可给现有RAG/Agent内存模块加一层无额外LLM调用的轻量控制wrapper，无需修改底层存储即可获得自适应检索能力，同时降低token成本

  - 电商导购/客服Agent的记忆模块可复用这套UCB上下文老虎机策略，根据用户对话阶段、历史记忆规模动态选择检索top-k、是否复用历史成功话术模板，提升回复准确率

  - 生成式推荐的历史用户行为检索环节，可借鉴反向折扣信用分配机制，给更接近转化节点的检索操作更高权重，优化检索策略的在线学习效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent的内存访问多采用固定人工启发式规则，要么检索太激进浪费token、稀释prompt有效信息，要么太保守漏用历史经验，最优内存操作本身是上下文依赖的；而MemGPT这类让LLM本身做内存控制器的方案又会带来额外的LLM调用成本，亟需轻量无额外开销的自适应内存管理方案。

### 方法关键点
- 将内存管理建模为Memory MDP，状态融合任务进度（目标类型、执行阶段、是否卡壳等）和内存状态（存储规模、是否有可用成功计划、学习阶段），动作包含检索、计划注入、重检索、内存合并/遗忘、空操作等，附带top-k、检索跳数等参数
- 采用带UCB探索的轻量表上下文老虎机在线学习策略，无需预训练，无额外LLM调用，仅靠任务级二元反馈更新，搭配反向折扣信用分配（越接近任务结束的操作权重越高），几十轮任务即可收敛
- 实现为后端无关的薄wrapper，可兼容向量库、技能库、图内存等任意现有内存后端，无需修改底层存储逻辑

### 关键实验
在6个基准（3个交互决策类ALFWorld、PDDL、ScienceWorld，3个QA/工具类TriviaQA、WebWalkerQA、GAIA）、3个Agent框架、3个LLM backbone上测试，对比9个内存基线：任务成功率最高提升15.2个百分点，同时token消耗降低5~20%；在ALFWorld任务上用GPT-4.1-mini达到67.9%成功率，为所有参测内存方案最高。

**最值得记住的一句话**：Agent内存的效果不止取决于存了什么，更取决于能不能自适应地在正确的时机调取正确的内容。
