---
title: 'Don''t Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask
  Exploration and Transition-aware Memory'
title_zh: BATON：基于智能体子任务探索与转换感知记忆的长程机器人操作方法
authors:
- Bingxin Xu
- Yuzhang Shang
- Emilio Ferrara
affiliations:
- University of Southern California
- University of Central Florida
arxiv_id: '2608.16889'
url: https://arxiv.org/abs/2608.16889
pdf_url: https://arxiv.org/pdf/2608.16889
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 长程机器人操作 · LLM智能体编排
tags:
- Long-Horizon Manipulation
- LLM Agent
- VLA
- Transition-aware Memory
- Subtask Exploration
one_liner: 提出零参数更新的LLM智能体框架BATON，解决长程机器人操作探索成本高、子任务衔接失效问题
practical_value: '- 长链路业务任务（如电商全链路转化优化、多轮个性化推荐、用户生命周期运营）可复用子任务拆分探索思路，将探索成本从子任务数的指数级降为线性加和，同时实现故障环节的精准定位，避免全链路重试浪费资源

  - 多模块Agent协作架构可直接复用三类转换感知记忆设计：调用前校验（如调用RAG/召回模块前先校验Query/上下文是否合规）、跨模块状态复位（如推荐链路每个节点输出后校验是否符合下游输入要求，不符合则补全修正）、前瞻约束（如上游召回阶段提前考虑下游排序、投放、合规的约束，筛选适配的候选集）

  - 无法微调大模型参数的业务场景可参考其零参数更新思路，纯靠自然语言记忆库和校验逻辑即可提升全链路成功率，所有经验可审计、可跨任务复用'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长程机器人操作需要串联多个接触密集型子任务，现有VLA模型单独子任务表现优异但串联后错误累积、子任务衔接无约束导致整体成功率极低；现有基于LLM编码智能体的方案采用全任务探索，成本随子任务数量指数级增长，且失败后无法定位故障环节，子任务之间没有转换条件约束导致前后执行结果不兼容。

### 方法关键点
1. 分层子任务探索：先将长任务拆分为独立子任务，每个子任务单独做短程探索，成功后存入记忆库，再逐层向外拼接验证子任务对，探索成本从T^K降至T·K，失败可精准定位到具体子任务或衔接边界
2. 三类转换感知记忆设计：① 调用转换：子任务内调用VLA前，验证智能体确认场景满足进入条件，不满足则重调；② 交接转换：跨子任务前，验证智能体复位场景满足下一个子任务的初始状态要求，消除前序残留干扰；③ 前瞻转换：调度智能体根据后续子任务要求，选择当前子任务的执行策略，确保当前结果可被下游继承
3. 全程无参数更新，所有经验以自然语言形式存入记忆库，可审计、可复用

### 关键实验
在千步级长程操作基准RoboMemArena上对比10个SOTA基线，BATON平均任务成功率（TSR）达57.7%，累计成功率（CSR）达78.8%，较当前SOTA分别提升11.6%和14.9%，甚至超过带真实记忆的Oracle基线。

### 核心结论
长程任务的核心瓶颈往往不是单个模块的能力不足，而是模块之间的转换衔接没有被显式设计和校验。
