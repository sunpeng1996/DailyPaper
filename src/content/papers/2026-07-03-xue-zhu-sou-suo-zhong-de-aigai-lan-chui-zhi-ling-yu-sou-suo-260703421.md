---
title: 'AI Overviews in Academic Search: Evaluating AI-generated Summaries of Search
  Results in a Domain-specific Search Engine'
title_zh: 学术搜索中的AI概览：垂直领域搜索引擎搜索结果AI生成摘要评估
authors:
- Kevin Schott
- Kanishka Silva
- Ingo Frommholz
- Philipp Mayr
- Dagmar Kern
- Daniel Hienert
affiliations:
- GESIS – Leibniz Institute for the Social Sciences, Germany
- Modul University Vienna, Austria
arxiv_id: '2607.03421'
url: https://arxiv.org/abs/2607.03421
pdf_url: https://arxiv.org/pdf/2607.03421
published: '2026-07-03'
collected: '2026-07-07'
category: Eval
direction: 垂直学术搜索 · AI生成SERP摘要评估与落地
tags:
- Multi-document Summarization
- User Study
- Search Engine
- Error Taxonomy
- Academic Search
- Evaluation
one_liner: 构建学术搜索SERP层AI摘要错误分类与落地保障框架，通过用户研究验证其场景化辅助价值
practical_value: '- 做垂直搜索（如电商商品搜、行业知识库搜）的SERP层AI摘要功能时，可复用本文的6类错误分类框架做输出质量校验，提前拦截幻觉、信息遗漏等问题

  - 上线AI摘要前可参考本文的5项落地保障策略，结合用户分群（如专业用户/普通用户）灰度放量，避免当作通用功能全量上线

  - 可基于信息觅食理论设计AI摘要的信息密度，帮助用户快速做结果初筛，降低query重写次数、提升搜索转化效率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
学术搜索场景下用户评估SERP结果相关性的成本极高，目前缺少对垂直领域搜索SERP层AI生成摘要的系统性评估与落地指导。

### 方法关键点
针对10条query的TOP5搜索结果，分别用商业/开源通用大模型生成摘要，人工标注后构建6大类错误分类框架，提炼出5项学术场景落地保障规则；随后开展30人组内对照用户研究，对比有无AI摘要的搜索界面的用户行为与主观反馈。

### 关键结果数字
主观指标上AI摘要在工作负荷、有用性、满意度、决策信心上均有正向趋势但未达统计显著，探索性分析显示用户心理负担、挫败感均呈下降趋势；行为指标上用户极少展开完整摘要，结果点击量、query重写次数均有小幅下降。结论显示AI摘要是场景与用户依赖的辅助功能，而非通用提升方案。
