---
title: 'Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science'
title_zh: 网络化智能：面向人机协同团队科研的主动共享上下文图
authors:
- Sutanay Choudhury
- Jeffrey J. Czajka
- Lummy M. O. Monteiro
- Erin Bredeweg
- Jason McDermott
- Katherine Wolf
- Alex Beliaev
- Josh Elmore
- Paul Piehowski
- Kylee Tate
affiliations:
- Pacific Northwest National Laboratory
arxiv_id: '2607.13220'
url: https://arxiv.org/abs/2607.13220
pdf_url: https://arxiv.org/pdf/2607.13220
published: '2026-07-14'
collected: '2026-07-16'
category: MultiAgent
direction: 多智体人机协同 · 上下文路由架构
tags:
- MultiAgent
- ContextRouting
- Human-AI-Collaboration
- GraphMemory
- Runtime
one_liner: 提出基于主动共享上下文图的Mycelium runtime，实现分布式人机科研团队的高价值上下文精准路由
practical_value: '- 跨角色协同场景可复用主动上下文图设计：将运营、算法、用户研究等不同角色/Agent的操作、结论按类型（证据/推理/行动）存入带溯源的有向图，避免信息孤岛，可直接用于大促跨部门运营协同、多Agent推荐策略迭代场景

  - 高价值信息路由机制可直接迁移：基于接收方当前任务的效用变化得分筛选待推送信息，而非全量同步，可用于推荐系统的多模块信号同步、Agent的上下文动态注入，大幅降低噪声干扰

  - 多Agent runtime工程实现可参考：基于MCP协议对接通用聊天客户端，沙箱动态生成执行工作流，自带错误重试，可复用在电商运营Agent、商品上新自动化审核、广告素材自动生成等场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前AI Agent多聚焦单任务推理或固定编排的多Agent协作，无法适配分布式跨角色团队的异步协作需求：不同角色的局部发现无法高效触达需要的参与方，知识传递依赖人工、效率极低；且单Agent无论如何扩容上下文窗口，都无法覆盖跨领域探索的广度，也无法整合不可合并的局部私有上下文（如专家隐性知识、机构数据权限限制）。
### 方法关键点
- 核心为主动上下文图（ACG）：节点为带类型的条目（数据集/观察/假设/发现/建议等），边记录溯源关系（generated_by/derived_from/supports等），所有写入强制绑定已有节点溯源，避免无根据信息。
- 三大核心能力：跨用户上下文路由（自动将新发现推送给受影响的参与方，保留不同角色的观点分歧而非强制合并）、持久化假设状态、溯源绑定的信息传播。
- 四大量化原语：严格溯源日志、空闲期主动补全数据缺口的bounded autonomy、基于效用得分的上下文路由（Pollination）、写入层强制溯源校验的持久化机制。
### 关键实验
在微生物多组学科研场景测试，3名不同领域专家与Mycelium异步协作，对比两个相同算力的单Claude Opus 4.8基线（带团队角色提示/不带）；Mycelium产出25个有效科研artifact，比单基线最高的18个提升38.9%，可直接用于实验的artifact达17个，比单基线最高的11个提升54.5%，覆盖加权得分2.62，比单基线最高的1.81提升44.7%，且产出artifact的平均特异性与单Agent相当，仅探索广度大幅提升。
### 核心结论
网络化智能是独立于模型扩容的第二增长曲线，仅通过精准路由高价值信息到决策节点，就能产生远超单模型的协作效能。
