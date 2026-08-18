---
title: 'Topological Attribution Distance (TAD): Revealing Segment-Level RAG Influence
  on LLM Output Geometry for Incident Log Analysis'
title_zh: 拓扑归因距离(TAD)：面向事件日志分析的片段级RAG影响归因方法
authors:
- Reza Fayyazi
- Michael Zuzak
- Shanchieh Jay Yang
affiliations:
- Rochester Institute of Technology
- Gonzaga University
arxiv_id: '2608.16775'
url: https://arxiv.org/abs/2608.16775
pdf_url: https://arxiv.org/pdf/2608.16775
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG归因 · 检索片段贡献追溯
tags:
- RAG
- Attribution
- LLM
- Topological Data Analysis
- Provenance Tracking
one_liner: 提出基于拓扑几何的TAD方法，可精准追溯RAG系统中对LLM输出影响最大的检索片段
practical_value: '- RAG溯源场景可复用「片段消融+输出嵌入拓扑变化匹配」的思路，解决高相似度召回源的贡献区分问题，适用于电商客服RAG、商品咨询回答归因等场景

  - Agent决策链路可嵌入TAD类几何归因方法，快速定位触发决策的关键召回片段，降低决策错误后的排查成本

  - 生成式推荐的RAG归因可借鉴该思路，追溯推荐文案生成的触发商品/用户行为片段，提升生成结果可解释性'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前Agent与RAG结合的落地场景（如网络安全事件分析）亟需可信赖的生成结果溯源能力，现有归因方法无法有效区分高度相似的召回源（如同源事件日志），缺乏对召回证据与生成响应间全局几何关系的捕捉，难以支撑可靠的证据校验。
### 方法关键点
提出拓扑归因距离TAD，基于拓扑学原理刻画LLM输出的全局几何特征，通过片段级消融实验比对移除某段召回日志前后LLM输出嵌入空间的几何变化量，量化单段召回日志对最终输出的贡献度，无需修改模型结构或新增训练成本。
### 关键结果
在真实网络攻击事件日志分析场景下，TAD可自适应精准定位对LLM输出影响最大的归因日志，为Agent工作流提供可解释、可验证的生成溯源能力，可有效区分高相似度召回源的贡献差异。
