---
title: 'Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents'
title_zh: JITMEM：面向LLM Agent的任务自适应读时内存架构
authors:
- Yefan Zhou
- Yang Li
- Zeyu Leo Liu
- Semih Yavuz
- Shafiq Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2609.27334'
url: https://arxiv.org/abs/2609.27334
pdf_url: https://arxiv.org/pdf/2609.27334
published: '2026-09-22'
collected: '2026-09-24'
category: Agent
direction: Agent 任务自适应内存优化
tags:
- LLM Agent
- Memory Management
- GRPO
- Task Adaptation
- Read-time Curation
one_liner: 将LLM Agent内存整理从写时延后至读时，大幅提升多场景任务成功率与执行效率
practical_value: '- 电商导购/智能客服Agent可直接复用该架构：仅存储成功执行的原始历史轨迹，读时结合当前用户请求动态蒸馏适配经验，避免写时蒸馏的不可逆信息损失，适配多场景用户需求

  - 训练环节可借鉴GRPO即时奖励范式：仅针对Curator模块单独训练，无需关联未来任务解决长程信用分配问题，训练流程更简单；训练好的Curator可跨不同Executor模型迁移，降低迭代成本

  - 工程落地可显著降本：实测该架构可降低Executor输入Token量50%+、执行步骤28%以上，大幅减少大模型调用成本，适配高流量的电商搜索、推荐导购、客服等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent内存系统普遍采用写时蒸馏逻辑，任务完成后即把执行轨迹提炼为固定的经验、技能或反思，后续通过相似性检索调用。但写时蒸馏无法预知未来任务需求，会不可逆地丢失潜在有用信息；同时训练写时蒸馏模块需要解决长程信用分配问题（存储内容的价值要到未来被调用时才能验证），训练复杂度高、效果不稳定。

### 方法关键点
- 存储层仅保留完整原始轨迹，不做任何写时蒸馏，仅通过LLM-as-judge过滤任务执行成功的轨迹存入内存库，降低检索噪声
- 读时收到当前任务后，先通过BM25检索Top-K相关历史轨迹，再由独立Curator模块结合当前任务，将原始轨迹蒸馏为紧凑的任务自适应Payload，输入给冻结的Executor执行
- Curator采用GRPO训练：同个任务下生成多组候选Payload，以Executor的即时任务成功率作为奖励信号更新参数，无需延迟奖励或人工任务分组，训练流程极简

### 关键实验
在ALFWorld（具身任务）、WebShop（电商购物任务）、τ2-bench（客服工具调用任务）三个基准测试，对比无内存Agent、ReasoningBank、SkillOS等主流写时内存方案：RL训练后的JITMEM较最强基线分别提升16.2、16.3、3.9个绝对成功率点；零样本未训练的Curator也可打平甚至超过多数写时方案；同时可降低Executor输入Token量50.3%~56.3%，执行步骤减少28.4%~31.4%。

### 核心结论
Agent内存的价值不只取决于存储了什么内容，更取决于何时、针对什么任务来整理这些内容。
