---
title: 'SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale'
title_zh: SkillSeek：面向市场级规模的Agent技能检索方案
authors:
- Guanqun Yang
- Wenlong Zhang
- Tian Shi
- Ping Wang
affiliations:
- Stevens Institute of Technology
- Independent Researcher
arxiv_id: '2609.38822'
url: https://arxiv.org/abs/2609.38822
pdf_url: https://arxiv.org/pdf/2609.38822
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent 技能检索成本与效果优化
tags:
- Skill Retrieval
- Two-stage IR
- LLM Agent
- MCP
- Cost Optimization
one_liner: 开源两阶段确定性Agent技能检索器，效果追平LLM介导方案，单轮成本降近一半
practical_value: '- 架构选型参考：业务中Agent技能/工具检索场景优先用确定性IR方案做基线，万级以内技能库纯BM25就够用，万级以上用BGE双编码器+小参数量cross-encoder的两阶段架构，可替代昂贵的LLM在环检索，降本50%以上。

  - 索引优化Trick：不要把技能/工具的完整文档塞进索引，仅索引名称、描述+离线生成的结构化标签（如核心操作、适配场景），加全量正文会引入噪声导致效果下降2~3%。

  - 参数调优经验：召回阶段返回top20候选给重排器即可，更深的召回池会引入干扰降低效果；最终给Agent返回top3~5个技能就覆盖几乎全部收益，更多候选只会干扰Agent决策。

  - 成本分层思路：先跑确定性IR方案覆盖90%以上常见场景，仅在确定性方案效果不达标的长尾场景再启用LLM介导的query改写、候选融合逻辑，平衡效果与成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前开源Agent技能库总量已突破23万条，技能选择替代技能编写成为新瓶颈；现有主流方案将LLM放在检索环内做query改写、候选筛选，每次任务都消耗大量LLM token，成本极高，且加载过多技能还会导致Agent任务通过率下降。

### 方法关键点
- 两阶段确定性检索架构：第一阶段用BGE-base bi-encoder召回top20候选，第二阶段用bge-reranker-v2-m3 cross-encoder重排后返回top5技能；
- 索引优化：仅索引技能名称、描述+LLM离线生成的4个Tool-REX结构化标签（文件类型、主操作、两个次操作），不索引技能完整正文避免噪声；
- 对外暴露MCP服务，所有兼容MCP的Agent框架可无缝接入，无需修改源码。

### 关键实验
基于89任务的SkillsBench基准测试，覆盖192条精标技能库、3.4万条市场级技能库两个场景，对比基线为Liu等人2026提出的LLM介导检索方案：
- 3个测试场景下纯BM25的通过率就超过LLM介导方案，剩余3.4万技能库+Qwen3.5的场景下，SkillSeek用0.6B参数量的Qwen重排器做到和LLM介导方案相同的0.442通过率；
- 单轮任务总成本从LLM方案的$51.30降到$27.54，和无技能基线的$27.41几乎持平。

### 最值得记住的一句话
Agent技能检索场景下，标准确定性IR方案是性价比远高于LLM在环检索的默认选择，仅在确定性方案失效时才需要启用LLM介导方案。
