---
title: 'Semantic Action Graph: A Shared Representation for Agent Grounding and Human
  Interpretation of Sports Highlights'
title_zh: 语义动作图：用于Agent落地与体育高光人工解读的共享表示
authors:
- Tica Lin
- Deepak Chandran
- Gauri Jagatap
- Chen Chen
- Andrea Fanelli
- David Gunawan
- Josh Kimball
affiliations:
- Dolby Laboratories
- XPENG
arxiv_id: '2609.20768'
url: https://arxiv.org/abs/2609.20768
pdf_url: https://arxiv.org/pdf/2609.20768
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent落地 · 语义图共享表示
tags:
- Semantic Graph
- Agent Grounding
- Shared Representation
- Highlight Generation
- Human-AI Interaction
one_liner: 提出轻量语义动作图schema，同时支撑Agent体育高光生成与用户交互检索调整
practical_value: '- 多角色共享语义schema设计思路可迁移到电商Agent场景：用统一的<商品/用户/行为/时效>节点+边结构，同时支撑Agent召回排序推理，以及用户可解释的偏好调整（如直接筛选「降价+近7天上新」节点）

  - 闭环词汇+可定位原始数据的语义表示设计，可解决生成式推荐结果不可追溯问题：给每个语义节点绑定原始物料ID/行为埋点ID，既降低Agent幻觉，也方便业务排查badcase

  - 人机共融推荐pipeline可复用：Agent生成逻辑与前端交互共用同一份语义图数据，省去多套表示的对齐成本，支持用户直接调整语义条件实现个性化推荐'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
生成式Agent生成视频高光时多依赖非结构化或帧级表示，输出结果难追溯验证，也无法支撑用户灵活调整个性化偏好。

### 方法关键点
1. 提出轻量领域语义动作图schema：将体育赛事拆解为表演者、动作、接收方、时刻、状态5类节点，通过角色、时序、结果3类边连接，具备事件序列连通、共享闭环词汇、帧可寻址三大核心特性，同时适配Agent推理与人类交互需求；
2. 落地SportSAGE系统，四模块高光生成Agent pipeline与前端可视化交互界面复用同一份语义图数据，免去多表示对齐成本。

### 关键结果数字
12名足球粉丝用户调研显示，用户对生成的高光片段与叙事质量满意度高，100%会使用图界面完成赛事高光的搜索、导航、解读操作，验证了统一可读schema同时支撑Agent落地与人工交互的可行性。
