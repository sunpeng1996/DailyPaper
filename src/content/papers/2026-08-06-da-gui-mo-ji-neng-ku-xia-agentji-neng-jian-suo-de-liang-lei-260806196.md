---
title: Comparative Approaches to Agent Retrieval over Large Skill Libraries
title_zh: 大规模技能库下Agent技能检索的两类方法对比研究
authors:
- Indivara Kolluru
- Nathan Sportsman
affiliations:
- Praetorian
- Carnegie Mellon University
arxiv_id: '2608.06196'
url: https://arxiv.org/abs/2608.06196
pdf_url: https://arxiv.org/pdf/2608.06196
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 技能库检索方案优化
tags:
- Agent
- Skill Retrieval
- Knowledge Graph
- Hybrid Ranker
- Retrieval Evaluation
one_liner: 对比混合检索与知识图谱两类Agent技能检索方案，揭示图方案拓扑约束及评估偏差问题
practical_value: '- 搭建Agent技能检索系统优先选择BM25+稠密向量的混合检索方案，其hit@5可达73.5%，token成本仅为全量加载的1.2%，性价比远高于基于embedding邻域构建的知识图谱方案

  - 若要构建技能关联知识图谱，不要仅用embedding近邻作为边的候选池，需引入用户行为、技能依赖元数据等非embedding信号，才能突破拓扑约束带来的检索上限

  - 检索系统评估需规避使用作者构造的查询集，实验显示这类查询集会让hit@5虚高21~44个点，建议用无技能描述回显的真实用户查询作为评估基准'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agent依赖的技能库规模快速扩张，全量加载技能到上下文token成本极高（690个技能需46.9k token/次调用），且无法支持技能自动排序。行业普遍尝试用知识图谱优化技能检索，但缺乏和混合检索方案的头对头对比，同时检索评估的数据集偏差问题也未被量化。

### 方法关键点
- 两类对比方案：1）混合检索：BM25 lexical得分 + all-MiniLM-L6-v2稠密向量相似度融合的召回排序；2）类型化知识图谱：先取每个技能embedding top-8邻居作为候选，调用Claude Haiku生成8种带语义的关系边（含前置依赖、数据流、时序关系等），构建技能关联图谱。
- 边生成优化：仅对描述hash变更的技能增量生成边，增量成本仅$0.005/技能，全量690个技能生成1421条边仅需$2.7，同时做循环检测删除幻觉生成的环。

### 关键实验
数据集为690个内部技能，评估集包含117条无技能描述回显的真实查询，额外对比37条作者构造的查询集。核心结果：
1. 混合检索hit@5达73.5%，单次调用token成本仅560，较全量加载降低98.8%；
2. 相同token预算下，图谱方案hit@5比混合检索低11.2个点，LLM生成的边对比免费的embedding kNN无任何检索增益；
3. 作者构造的查询集会让hit@5虚高21~44个点，完全掩盖方案真实效果；
4. 98.6%的图谱边都落在混合检索已覆盖的候选范围内，73%混合检索漏召的查询在图谱中完全不可达。

### 核心结论
如果知识图谱的候选边完全来自检索所用embedding的近邻，它永远无法突破检索本身的覆盖上限，只能为边增加语义，不能扩展召回范围。
