---
title: 'PhantomEnvironments: Training LLM Agents in Fictional Worlds'
title_zh: PhantomEnvironments：在虚构世界中训练LLM搜索Agent
authors:
- Anmol Kabra
- Swathi Saravana Selvam
- Albert Gong
- Chao Wan
- Christian Belardi
- Dongyoung Go
- Katie Z. Luo
- Kilian Q. Weinberger
affiliations:
- Cornell University
- Stanford University
arxiv_id: '2609.40221'
url: https://arxiv.org/abs/2609.40221
pdf_url: https://arxiv.org/pdf/2609.40221
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: LLM搜索Agent 虚构环境RL训练
tags:
- LLM Agent
- Reinforcement Learning
- Synthetic Environment
- Multi-hop Search
- Transfer Learning
one_liner: 通过纯规则生成的零成本虚构环境RL训练，LLM搜索Agent可高效迁移到真实世界多跳搜索任务
practical_value: '- 训练多跳搜索类Agent时，可自行构建纯规则生成的合成训练环境，零边际成本，可规避人工标注成本、LLM生成的幻觉与基准污染问题，能迫使模型学习通用的query拆解、检索、知识组合能力，而非依赖事实记忆，适合电商场景复杂用户搜索query的Agent能力训练

  - 设计训练环境无需盲目叠加复杂度：线性多跳任务已能贡献大部分迁移收益，仅当业务存在大量比较类query时可补充对应训练任务，约束类任务容易让模型学会逐字匹配query的捷径，反而损害泛化性，需谨慎引入

  - 小参数LLM经该类合成环境RL训练后性能可追平10倍参数的base模型，业务中可通过「小模型+针对性合成训练」的方案降低搜索Agent部署成本，适配电商场景低成本、高并发的部署需求'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM搜索Agent的RL训练长期受环境瓶颈限制：人工标注环境成本高、锚定固定知识快照，LLM生成环境存在 hallucination、基准污染、API成本高、能力上限由生成模型决定的问题，行业急需低成本、可验证、泛化性强的训练环境方案。

### 方法关键点
- 基于PhantomWiki构建纯规则生成的虚构世界环境PhantomEnvs，生成流程无人工、无LLM参与，零边际成本，可自由控制世界大小、问题跳数、难度等参数
- 环境包含模板生成的虚构人物关系文档、多跳问题，答案可通过Prolog精确验证，完全不含真实世界事实，迫使模型学习通用的「问题拆解→检索→知识组合」搜索能力，而非记忆事实
- 采用GRPO算法做RL fine-tuning，仅基于最终答案的F1值给reward，训练时屏蔽环境返回的检索结果梯度

### 关键结果
- 训练后模型在2018版维基百科基准（HotpotQA、2WikiMultihopQA等）上F1平均提升1.7倍，在更新更难的跨域基准（SynthWorlds、FRAMES）上平均提升2.2倍，Llama-3.2-3B在SynthWorlds-SM上F1提升达7.1倍
- 和真实世界NQ+HotpotQA训练数据对比，域内基准上真实数据略优，但跨域/新基准上PhantomEnvs训练的模型表现更好，且完全消除了模型依赖预训练记忆的知识优势（KA gap降为0）
- 消融实验显示线性多跳任务贡献了大部分迁移收益，增加比较任务可针对性提升真实世界比较类query效果，增加约束任务反而会因奖励捷径损害泛化性

### 核心结论
不含任何真实事实的纯规则虚构环境，完全可以训练出能迁移到真实世界的通用搜索Agent，且成本远低于人工或LLM生成的训练方案
