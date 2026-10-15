---
title: 'TreeFlex: Agents Navigating Their Own Search Trees'
title_zh: TreeFlex：支持自主导航搜索树的长 horizon 智能 Agent 框架
authors:
- Dongzhuo Li
- Fangzhou Cheng
- Weiwei Li
- Kevin Han
- Haixu Ma
- Zhongchang Sun
- Ruiyi Li
- Serena Li
- Xiangjun Fan
- Lizhu Zhang
affiliations:
- Meta AI
arxiv_id: '2610.20334'
url: https://arxiv.org/abs/2610.20334
pdf_url: https://arxiv.org/pdf/2610.20334
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 长任务推理搜索树优化
tags:
- LLM Agent
- Tree Search
- GRPO
- Long-horizon Reasoning
- RL
one_liner: 双角色单LLM实现自主决策搜索树，搭配树感知GRPO训练，长任务表现大幅领先ReAct等基线
practical_value: '- 可复用双角色LLM设计，将全局路径规划（Reflection）和单分支执行（Execution）拆分，解决长会话Agent上下文冗余问题，适合电商导购Agent、用户深度意图挖掘等场景

  - 树感知GRPO训练思路可迁移，把多分支搜索的完整路径作为一个rollout计算奖励，不需要复杂树形注意力，降低Agent RL训练成本

  - 中间节点checkpoint+摘要的存储方案，可复用在搜索推荐多路径召回试错场景，比如query改写的多分支探索，可回溯旧节点重新生成，避免无效历史占用上下文'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统ReAct风格Agent将所有历史存储在单一线性上下文，长任务下废弃分支、无效信息挤占有限上下文容量，导致推理效率下降；现有LLM树搜索方法依赖人工设计的DFS/BFS/MCTS规则，无法根据任务进展动态调整搜索策略，且多分支结构难以适配端到端RL训练。

### 方法关键点
- 单LLM双角色设计：Reflection角色全局查看所有节点的短摘要，自主决策要回溯/扩展的节点及对应执行指令；Execution角色仅加载目标节点的路径上下文，调用工具完成指令后生成新checkpoint节点或提交方案，返回Reflection审核。
- 树感知GRPO训练：将完整搜索树作为一个rollout，每个模型输出仅用其生成时的上下文训练，结合任务最终奖励+过程惩罚（工具调用错误、超出指令范围等），无需额外设计树形注意力掩码。
- 无固定搜索规则：Agent自主决定加深当前分支、回溯旧节点、验证方案或停止，无需人工指定遍历逻辑。

### 关键实验
- 深度研究任务（BrowseComp-Plus数据集）：4B模型RL训练后，TreeFlex准确率达48.8%，超flat ReAct（41.5%）、FoldAgent（42.8%），Pass@8领先两个基线约10个百分点。
- SWE-bench Verified代码任务：9B模型训练后，TreeFlex任务解决率达54.9%，超FoldAgent（43.3%）11.6个百分点。

### 核心结论
让Agent自主管理搜索树的分支选择和回溯，比人工预设搜索规则+上下文压缩的方案，在长复杂任务上的性能提升更显著。
