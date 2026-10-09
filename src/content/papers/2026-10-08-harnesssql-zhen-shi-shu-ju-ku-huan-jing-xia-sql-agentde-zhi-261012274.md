---
title: 'HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments'
title_zh: HarnessSQL：真实数据库环境下SQL Agent的执行框架原生训练方案
authors:
- Haolin Yang
- Jipeng Zhang
- Jian Xie
- Shuaishuai Gong
- Sirui Han
- Yike Guo
affiliations:
- Hong Kong University of Science and Technology
- Microsoft Research
- Tsinghua University
- University of Macau
arxiv_id: '2610.12274'
url: https://arxiv.org/abs/2610.12274
pdf_url: https://arxiv.org/pdf/2610.12274
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: SQL Agent 训练范式与交互优化
tags:
- Agent
- Tool-Use
- SFT
- RLHF
- Text-to-SQL
one_liner: 通过训练部署执行框架对齐、全轨迹SFT+执行奖励RL，大幅提升小参数SQL Agent交互执行准确率
practical_value: '- 所有工具调用类业务Agent（如电商商品库查询、用户行为归因SQL分析Agent）均可参考「训练-部署harness对齐」范式，避免仅训练静态输出、部署时加工具导致的性能暴跌

  - 交互类Agent的SFT优先选择全轨迹学习，不要拆分单轮对话样本，可大幅提升长周期决策一致性，适合电商客服、导购Agent训练

  - 小模型Agent训练可采用「全轨迹SFT冷启动+执行奖励RL优化」两阶段流程，效率比直接训练RL高3倍以上，适配业务端小模型落地降本需求

  - 针对特定业务场景定制极简工具集（如本工作将SQL工具压缩到4个），可显著降低小模型学习难度、提升工具调用准确率，适合业务Agent工具系统设计'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统Text-to-SQL模型仅训练静态问题到SQL的映射，而真实部署的SQL Agent需要和数据库多轮交互（查表、试执行、纠错），训练阶段未引入执行harness导致训练部署严重不匹配，小模型在复杂交互SQL任务上准确率极低。

### 方法关键点
- 构建隔离可执行的数据库沙箱环境，配套隐藏执行验证oracle，保证交互环境与部署完全一致
- 定制SQL专属极简交互harness，仅暴露4个核心工具（查表列表、查schema、执行SQL、提交结果），屏蔽无关能力降低学习复杂度
- 两阶段harness原生训练：先在harness内用专家模型生成验证通过的全交互轨迹做SFT，再用执行结果作为稀疏奖励做RL优化，仅对Agent生成的动作算损失，环境观测token全部mask

### 关键实验
在Spider 2.0-SQLite数据集上，对比32B参数传统Text-to-SQL模型、多Agent SQL系统，HarnessSQL将Qwen3-8B执行准确率从15.5%提升到45.2%，Qwen3-14B从22.2%提升到54.8%，效果是32B基线的3倍以上；跨域迁移到BIRD-Interact Mini、LiveSQLBench的效果也比基线高2-4倍。

### 核心结论
Agent的harness不是推理端的包装，而是训练阶段需要对齐的行为分布的一部分，训练和部署交互协议的对齐比单纯堆模型参数量更能提升小模型Agent性能。
