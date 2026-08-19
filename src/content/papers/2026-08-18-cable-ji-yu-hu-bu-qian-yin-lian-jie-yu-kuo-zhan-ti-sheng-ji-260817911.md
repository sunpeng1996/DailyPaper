---
title: 'CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based
  Linking and Expansion'
title_zh: CABLE：基于互补前因链接与扩展提升记忆检索覆盖范围
authors:
- Zheling Tan
- Jin Gao
- Dequan Wang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.17911'
url: https://arxiv.org/abs/2608.17911
pdf_url: https://arxiv.org/pdf/2608.17911
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 长时记忆检索增强
tags:
- Long-Term-Memory
- Retrieval-Augmentation
- LLM-Agent
- Memory-Graph
- Semantic-Retrieval
one_liner: 提出可插拔的CABLE记忆增强模块，通过互补前因链接扩展语义检索的有效覆盖范围
practical_value: '- 做用户长时兴趣召回的推荐系统可复用CABLE的互补链接思路：给新用户行为生成前因导向查询，减去语义匹配已召回的结果，仅保留互补兴趣关联，避免召回冗余，提升跨会话兴趣召回准确率

  - 工程上可直接将CABLE作为可插拔组件集成到现有记忆系统（如Mem0、A-MEM），仅在记忆写入时做一次性链接生成与校验，检索阶段无额外LLM调用，性能开销可控，适合高并发的电商Agent客服、个性化推荐场景

  - 针对多会话用户偏好挖掘、跨行为链路归因（如用户下单前置动机挖掘），可复用类型条件的前因查询生成模板，针对事件/观点/计划/状态变更四类记忆分别生成检索query，提升隐性关联召回率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent长时记忆依赖语义相似度检索，仅能召回和查询语义接近的记忆，容易遗漏语义距离远但存在因果/前因关联的历史信息；现有记忆图的链接多基于语义重叠，和直接召回结果高度冗余，无法在有限上下文预算下扩展检索有效覆盖范围。

### 方法关键点
- 记忆写入阶段：先对新记忆做类型分类（事件/观点/计划/状态变更），针对不同类型生成2~3个前因导向查询，分别检索得到前因候选集，再减去与新记忆直接语义匹配的候选集，仅保留互补候选，经LLM校验确认是有效前因（因果/动机/背景）后，存入稀疏有向记忆图
- 检索阶段：先运行宿主系统的标准语义检索得到初始结果，对相似度高于阈值的高置信种子做1跳图扩展，按关联种子的相似度总和打分，过滤冗余后替换初始结果中低排名条目，全程无额外LLM调用

### 关键实验
在LoCoMo、MA-LongMemEval两个长时对话记忆基准上，集成到A-MEM、SimpleMem、Mem0g三个主流记忆系统，适配Qwen3.5-27B、DeepSeek-chat、GPT-4o-mini多个底座，所有场景下LLM judge打分均提升：A-MEM+Qwen3.5在MA-LongMemEval上提升6个百分点，在LoCoMo开放域问题上提升6.24个百分点，多会话、用户偏好类问题增益最高。

### 最值得记住的一句话
记忆图的核心价值不是构建完整的关系模型，而是在有限上下文预算下，提供宿主检索无法覆盖的互补关联证据。
