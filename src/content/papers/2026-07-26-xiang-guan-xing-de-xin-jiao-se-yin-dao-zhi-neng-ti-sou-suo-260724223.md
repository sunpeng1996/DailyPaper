---
title: 'A New Role for Relevance: Guiding Corpus Interaction in Agentic Search'
title_zh: 相关性的新角色：引导智能体搜索的语料交互过程
authors:
- Jiangnan Li
- Yuqing Li
- Mo Yu
- Jinchao Zhang
- Jie Zhou
affiliations:
- Tencent
- IIE-CAS
arxiv_id: '2607.24223'
url: https://arxiv.org/abs/2607.24223
pdf_url: https://arxiv.org/pdf/2607.24223
published: '2026-07-26'
collected: '2026-07-29'
category: Agent
direction: Agent 智能搜索效率优化
tags:
- Agentic Search
- Relevance Estimation
- Corpus Interaction
- RAG
- Efficiency Optimization
one_liner: 提出相关性感知的RARG搜索智能体，将相关性作为语料交互执行先验，提升搜索精度与效率
practical_value: '- 电商导购/商品检索Agent可复用RARG粗到细引导架构：先通过embedding召回限定搜索范围，改造grep命令强制按召回顺序遍历，降低无效工具调用成本

  - 多轮检索场景可引入入口点初始化：将top-N相关段落提前喂给LLM作为探索起点，减少冷启动阶段的无效检索次数

  - 检索结果截断场景可增加match-level rerank：结合全局查询意图和本地关键词匹配目标做细粒度重排，避免截断丢失低排名文档中的高价值信息

  - 工具调用侧可做规则化改造：无需修改LLM逻辑，仅给rg命令加-j1参数强制单线程按召回顺序返回结果，工程落地成本极低'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有检索智能体要么仅用相关性筛选top-k内容，无法定位、组合、验证复杂问题所需证据；要么采用无相关性引导的直接语料交互（DCI），有效线索出现晚、收敛速度慢，且相关性仅用于构造搜索空间，未直接引导交互过程，大语料下成本剧增。
### 方法关键点
- 提出RARG三级粗到细相关性引导框架：
  1. 文档级：用embedding召回生成排序后的文档范围文件，改造rg命令添加-j1参数强制单线程按召回顺序扫描，优先遍历高相关文档
  2. 入口初始化（RARG+）：召回top相关段落作为初始探索锚点，减少冷启动无效搜索
  3. 匹配级重排（RARG++）：结合全局查询意图和本地rg关键词构造重排query，对匹配片段重排，让低排名文档的高价值片段优先被LLM观测到
- 仅保留Bash、Read、embed_recall三类工具，架构轻量易落地
### 关键实验
- 数据集：BrowseComp-Plus（100K/1M文档问答）、BRIGHT（4个领域推理型检索）
- 对比基线：DCI、RISE、专用检索智能体NeMo等
- 核心结果：100K文档BC+数据集上，RARG++用GPT-5.4-mini达到84%准确率，比RISE/DCI高6pp，工具调用量减少46%；1M文档场景下准确率79%，比RISE-BM25高10pp；BRIGHT数据集上RARG+平均nDCG@10达53.36，超过NeMo的52.89
### 核心结论
相关性不应只是检索的内容筛选标准，更应作为语料交互的执行先验，从遍历顺序、观察优先级等维度全程引导智能体探索，大幅提升收敛效率。
