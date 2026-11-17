---
title: 'StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix'
title_zh: StaleBench：Agent记忆过期检索问题隔离基准及修复代价量化
authors:
- S M Mahbub Murshed
affiliations:
- Causal Dynamics Lab
arxiv_id: '2611.19752'
url: https://arxiv.org/abs/2611.19752
pdf_url: https://arxiv.org/pdf/2611.19752
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: Agent长时记忆时效性评估
tags:
- AgentMemory
- RetrievalBenchmark
- TemporalKnowledge
- StaleRetrieval
- LLMAgent
one_liner: 推出首个Agent记忆过期检索专用基准，提出contamination@k指标量化新旧冲突代价
practical_value: '- 做电商导购Agent/用户长期兴趣建模时，不要只依赖current@k评估记忆检索效果，必须新增contamination@k衡量上下文新旧冲突，无日期标注时冲突会导致LLM回答准确率最多掉65.6个点

  - 记忆写入的同事实检测不要直接用cosine相似度阈值，实体别名场景下准确率会降31.4个点，读写双路增加轻量字符trigram实体匹配，几乎无额外成本就能回收大部分损失

  - 不要盲目用时间重排这类'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent长时记忆评估要么测模型世界知识的时效性，要么测广义召回能力，没有单独隔离「已存储同一事实的新旧版本，相似度检索无法优先返回最新值」的核心故障；现有检索指标也无法准确反映策略的端到端效果，导致检索侧优化和下游任务收益脱节。

### 方法关键点
- 基于TempLAMA的Wikidata时态三元组构建892条真实更新事实流，时效性标签完全来自源数据的有效期，不依赖任何检索分数，避免评估污染
- 设置两个难度控制旋钮：`paraphrase_p`控制事实表述的改写程度，`alias_p`控制后续事实提及使用短别名的概率，模拟真实场景的实体指代多样性
- 新增`contamination@k`指标，衡量top-k检索结果中是否同时存在同一事实的新旧版本，弥补`current@k`仅关注首位结果的缺陷
- 覆盖三类主流记忆策略：全存储+相似度排序、全存储+时间感知重排序、写入时同事实检测+覆盖/失效的保留策略，同时测量检索指标和下游LLM reader的端到端准确率

### 关键结果
- 基线cosine全存储检索有53%的概率返回过期事实，时间重排能把`current@1`从0.464提升到0.925，但`contamination@5`仍高达0.974，无日期标注时qwen2.5:14b的回答准确率反而从0.558降到0.329
- 仅看`current@1`会有13/42的策略排序和实际reader准确率反转，`contamination@5`仅反转2次；两个首位结果完全相同的策略，仅上下文新旧冲突的差异就导致reader准确率最多相差65.6个点
- 读写双路加实体链接的对称键控策略，在全别名场景下`current@1`达0.831，`contamination@5`仅0.034，效果超过仅写入路径加完整别名表的方案

最值得记住的一句话：当前基于相似度的记忆检索指标严重高估端到端效果，忽略上下文新旧冲突的代价远高于提升检索首位准确率的收益
