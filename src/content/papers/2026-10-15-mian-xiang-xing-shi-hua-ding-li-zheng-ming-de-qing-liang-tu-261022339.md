---
title: Lean Graph Search for Formal Theorem Proving
title_zh: 面向形式化定理证明的轻量图搜索方法LeanGraphSearch
authors:
- Yihan Xu
- Jia-Chen Gu
- Junyi Zhang
- Di Wu
- Haikang Deng
- Po-Nien Kung
- Kai-Wei Chang
- Amit Sahai
- Wei Wang
- Nanyun Peng
affiliations:
- University of California, Los Angeles
arxiv_id: '2610.22339'
url: https://arxiv.org/abs/2610.22339
pdf_url: https://arxiv.org/pdf/2610.22339
published: '2026-10-15'
collected: '2026-10-18'
category: Reasoning
direction: 形式化定理证明 · 依赖图多跳检索
tags:
- Graph Retrieval
- Multi-hop Search
- Reranking
- Dependency Graph
- Theorem Proving
one_liner: 基于依赖图多跳检索相关引理，提升形式化定理证明的检索和端到端通过率
practical_value: '- 推荐召回场景可借鉴多跳依赖图拓展思路：对语义匹配召回的候选，沿用户行为/知识图谱依赖链传播相关性，扩充低语义相似但高关联的长尾候选，提升召回覆盖率

  - 排序模块可复用「语义初召回→图传播扩召回→原query重排」三段式架构，平衡相关性和召回广度，适合小众/冷启动内容的分发优化

  - Agent任务的工具/知识库检索可引入依赖图关联推理，降低对纯语义匹配的依赖，减少prompt工程复杂度，提升任务链路准确率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有形式化定理证明的引理检索系统仅做单跳语义匹配，未利用声明间的多跳依赖关系，容易漏掉语义不相似但多次出现在相关证明中的支撑引理，限制检索召回率和端到端证明通过率。

### 方法关键点
1. 基于Mathlib的前置依赖构建声明关联图，将每个声明链接到其依赖的前提节点；
2. 先做语义初召回得到高相关种子节点，用图排序算法沿依赖链传播相关性，扩充多跳候选集；
3. 结合原始查询对扩充后的候选做重排输出。

### 关键结果
检索任务上，比最强基线LeanSearch v2在MathlibQR召回率最高提升12%，MathlibMPR的完整证明路径覆盖率提升3.7%；端到端定理证明任务上，比原生证明器在8/16/32轮反射时通过率最高提升40%，比LeanSearch v2最高提升10%，准确率-成本效率更优。
