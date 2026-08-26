---
title: Constrained Entity Selection under Partial Knowledge for LLM-Based Knowledge
  Graph QA
title_zh: 面向LLM知识图谱问答的部分知识约束实体选择方法
authors:
- Emanuel Kitzelmann
affiliations:
- Brandenburg University of Applied Sciences
arxiv_id: '2608.24824'
url: https://arxiv.org/abs/2608.24824
pdf_url: https://arxiv.org/pdf/2608.24824
published: '2026-08-25'
collected: '2026-08-26'
category: Reasoning
direction: LLM知识图谱问答 · 约束推理优化
tags:
- KGQA
- Constrained Entity Selection
- Three-Valued Semantics
- Knowledge Graph
- Symbolic Verification
one_liner: CES-PK框架采用三值约束语义过滤KGQA候选答案，在保召回的同时提升精度
practical_value: '- 电商客服Agent、商品咨询等KGQA场景，可复用三值约束语义（满足/违反/未知）过滤LLM生成的候选答案，避免因商品/商家KG不完备导致的误召回错误

  - 推荐系统候选池粗筛阶段，可借鉴轻量符号约束校验思路，无需生成复杂SPARQL查询，仅用从用户Query/偏好提取的约束过滤无效候选，平衡精度和工程实现成本

  - Agent调用结构化知识库（商品库、活动规则库等）的结果校验环节，可复用CES-PK框架逻辑，对LLM生成的候选结果二次校验，同时保留约束未知的候选避免损失召回'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM-based KGQA方案存在两类缺陷：一类依赖语义解析生成SPARQL等可执行查询，实际场景中因KG schema复杂、数据不完备鲁棒性极差；另一类直接基于LLM推理生成答案，缺乏形式化正确性保障，极易出现答案与KG事实不匹配的grounding错误。
### 方法关键点
1. CES-PK问题范式下，先由LLM生成候选答案，再用从问句提取的轻量符号约束做校验，无需构造复杂可执行逻辑表达式，工程落地门槛低
2. 针对KG不完备的开放世界假设，采用三值约束语义（满足/违反/未知），仅过滤明确违反约束的候选，保留约束状态未知的候选避免误拒
3. 满足约束的结果可作为符号特征用于后续候选排序，进一步提升排序准确性
### 关键结果
在Hetionet生物医学KG上测试，通过类型、关系、排除约束过滤可显著提升候选答案精度，同时100%保留召回率，有效降低KGQA的错误输出概率。
