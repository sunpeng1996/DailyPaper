---
title: 'Content Depth Matters in Short-Video Recommendation: Rethinking the Attention
  Economy'
title_zh: 短视频推荐中的内容深度重要性研究：对注意力经济的反思
authors:
- Liwei Deng
- Jing Jiang
- Zhiwei Li
- Yang Wang
- Guodong Long
affiliations:
- University of Technology Sydney
- Australian Department of Health, Disability and Ageing
arxiv_id: '2608.13990'
url: https://arxiv.org/abs/2608.13990
pdf_url: https://arxiv.org/pdf/2608.13990
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 短视频推荐 · 内容质量评估
tags:
- Short-video Recommendation
- Content Quality
- Evaluation Metric
- Recommendation Benchmark
- User Well-being
one_liner: 提出内容深度量化指标CDS与评估基准SCOPE-Bench，揭示现有推荐系统对浅内容的偏好
practical_value: '- 7级CDS内容深度评分框架可直接迁移到电商短视频/直播/种草内容的质量分层，用于区分引流型娱乐内容和高价值知识类内容，做分层流量分配

  - 列表级LCDS指标可直接加入推荐排序多目标优化，在保证观看时长/转化的前提下平衡内容健康度，降低用户长期流失风险

  - 「小批量人工标注黄金集→筛选高对齐LLM→批量标注」的内容标注 workflow 可复用，大幅降低内容质量标注的人工成本

  - 现有纯engagement优化的推荐系统内容深度接近随机的结论可直接指导业务迭代：新增内容质量目标不会显著降低现有engagement指标天花板'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前短视频推荐系统均以点击、观看时长等engagement指标为核心优化目标，天然偏好能在几秒内抓取用户注意力的浅内容，长期暴露于此类内容会损害用户的持续注意力与心理健康，全球已有多个国家出台青少年短视频使用限制，但此前缺乏可量化的内容深度评估标准，无法将内容深度纳入推荐系统的优化与评估体系。

### 方法关键点
- 基于认知心理学双加工理论、布鲁姆认知分类、SOLO分类理论，设计7级ContentDepthScore(CDS)指标，从Level 0（仅情绪刺激）到Level 6（可跨场景迁移的通用模型构建），对应不同层级的认知加工深度
- 构建SCOPE-Bench评估基准：基于开源15万条短视频数据集，覆盖1万用户、100万条交互，采用「小批量人工标注黄金集→筛选与人类判断对齐度最优的LLM→批量生成全量CDS标注」的流程，兼顾标注效率与人类对齐度
- 提出列表级LCDS指标，支持平均加权、位置曝光加权等多种聚合方式，可直接用于推荐Top-K列表的内容深度评估

### 关键结果
在SCOPE-Bench上测试13个主流推荐算法（包括ID类BPR、LightGCN，多模态类VBPR、FITMM等），所有算法的Recall@20最高达3.82%，远高于随机基线的0.08%，但内容深度得分A-LCDS@20仅6.22%-8.12%，和随机基线的6.59%-6.9%几乎持平，证明现有推荐系统的engagement与内容深度完全解耦。

> 核心结论：纯注意力经济导向的推荐系统内容深度表现几乎和随机推荐无差异，优化内容深度目标不会显著冲击现有engagement指标的天花板
