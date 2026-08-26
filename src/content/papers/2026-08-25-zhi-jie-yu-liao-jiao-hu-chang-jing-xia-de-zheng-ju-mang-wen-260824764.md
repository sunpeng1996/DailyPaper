---
title: 'Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with
  AtlasNav'
title_zh: 直接语料交互场景下的证据盲问题与持久导航框架AtlasNav
authors:
- Hongyu Guo
- Zhiyu Zheng
- Zhao Cao
arxiv_id: '2608.24764'
url: https://arxiv.org/abs/2608.24764
pdf_url: https://arxiv.org/pdf/2608.24764
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 直接语料交互导航优化
tags:
- Agent
- DCI
- RAG
- Navigation
- Evidence Blindness
one_liner: 提出证据盲问题诊断框架与持久多视图语料导航框架AtlasNav，显著降低DCI场景推理成本、提升准确率
practical_value: '- 搭建企业级RAG/Agent知识库时，可离线构建Topic/Identity/Episode/Relation四视图语料地图，复用全局结构避免每次查询重建探索空间，实测能降低30%+在线推理成本

  - 异构多源的电商商品/评论/客服知识库场景，可复用「多视图语义检索+BM25+加权RRF融合」的路由逻辑，平衡语义匹配和 lexical 检索，降低多跳证据查找的证据盲问题

  - 做Agent性能诊断时，可借鉴证据盲四阶段（Construction/Surface/Open/Locate）评估法，比单纯看最终准确率更容易定位检索/交互链路的瓶颈'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Direct Corpus Interaction（DCI）模式下Agent虽能直接访问全量语料，但有限交互预算下会出现证据可达但不可用的静默失效（证据盲），现有动态工作区方法每次查询都要重建交互空间，效率低且容易错过多跳证据链，导致性能上限不足。

### 方法关键点
- 形式化证据盲的四阶段漏斗：Construction（语料存在证据）→Surface（证据文档出现在Agent观测）→Open（文档内容进入模型上下文）→Locate（关键决策片段进入上下文），并构建片段级Qrel标注体系实现可量化诊断
- 离线构建多视图Corpus Atlas：对每份文档提取Topic/Identity/Episode/Relation四个语义视图，通过多路社区检测生成持久层级结构，全局仅构建一次、所有查询复用，不裁剪原始语料
- 在线自适应导航：查询侧为四个语义视图+BM25分配动态权重，用加权Reciprocal Rank Fusion（RRF）融合多路排序结果，引导Agent优先访问高优先级区域，保留原生DCI全语料访问能力

### 关键结果
- 在BrowseComp-Plus数据集上，对比SOTA动态工作区方法DR-DCI，用DeepSeek-V4-Flash backbone时严格准确率达92.05%（提升7.47个点），在线推理成本降低30.21%；四视图设计降低全阶段证据盲率，Locate阶段证据完全缺失率从24.46%降至11.45%
- 10K-1M语料规模的PhantomWiki数据集上，AtlasNav在各规模下都保持最低证据盲率和最高准确率，1M规模下准确率比DR-DCI高24个点
- 企业知识基准EnterpriseRAG-Bench上，AtlasNav整体得分73.72，效果超过原生OpenAI File Search等基线

> 最值得记住的结论：Agentic search的瓶颈不仅是证据是否可达，更是语料的表示方式能不能让有限的交互转化为有效的导航。
