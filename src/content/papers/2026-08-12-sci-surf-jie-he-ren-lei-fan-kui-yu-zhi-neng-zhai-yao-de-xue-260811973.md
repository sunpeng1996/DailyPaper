---
title: 'Sci-Surf: Navigating Scientific Literature Discovery through Human Feedback
  and Intelligent Summarizatio'
title_zh: Sci-Surf：结合人类反馈与智能摘要的学术文献发现系统
authors:
- Fang Guo
- Qi Zhu
- Rongcan Pei
- Shuqi He
- Hui Chen
- Yue Zhang
affiliations:
- Zhejiang University
- Tongji University
- Google Cloud
- Westlake University
arxiv_id: '2608.11973'
url: https://arxiv.org/abs/2608.11973
pdf_url: https://arxiv.org/pdf/2608.11973
published: '2026-08-12'
collected: '2026-08-13'
category: RecSys
direction: 个性化内容推荐 · LLM用户画像
tags:
- Personalized Recommendation
- LLM User Profiling
- Multimodal Summarization
- User Feedback
- Information Retrieval
one_liner: 提出意图驱动的学术发现系统，融合反馈式LLM用户画像与多模态博客式论文摘要
practical_value: '- 可复用 verbalized 用户画像设计：用LLM从交互历史提取结构化的 persona、负向偏好、排序规则，替代纯向量画像提升重排精度，适合长周期兴趣稳定的推荐场景（如电商垂类用户、内容订阅）

  - 可复用离线批处理架构：将LLM摘要生成、重排等重计算逻辑放在每日离线批处理环节，在线仅分发结果，兼顾LLM能力落地与低延迟要求，适合非实时推荐（日更feed、订阅推送）

  - 多模态生成trick：优先用结构化HTML内容喂给LLM生成摘要，比PDF输入的严重幻觉率降低48.8%，电商商品种草文案等场景可参考优先用结构化属性输入

  - LLM4Rec验证方法：用盲评对比有无用户画像的推荐结果直接量化收益，可复用在各类LLM增强推荐的灰度验证环节'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
近年计算机科学年发文量从2000年的2万暴涨至2023年的12万，现有学术发现平台仅靠静态订阅或embedding相似度召回，仅提供短摘要，既无法精准捕捉用户动态细粒度兴趣，也难以支撑用户快速深度理解论文，存在推荐精准度低、内容消化成本高的双重痛点。

### 方法关键点
- 双阶段架构：Day0引导用户输入自然语言兴趣，用LLM生成初始结构化intent画像；Day1+每日跑离线批处理pipeline同步最新论文， decouple重计算与实时交互
- 内容处理：同时抓取论文HTML和PDF，解析为文本、图表、公式等结构化元素，预生成固定7模块的博客式多模态摘要，自动插入图表占位符
- 推荐链路：先用GritLM做向量召回，加3-5天新鲜度约束、去重、相似度阈值过滤；再用LLM基于用户verbalized画像和预生成摘要重排，输出每日Top5推荐
- 画像迭代：定期从用户点赞/点踩反馈中用LLM增量更新用户persona、负向约束、排序规则，迭代到重排prompt中保证稳定性

### 关键实验
- 离线召回：在LitSearch基准（597条学术查询+专家标注）上，GritLM的Recall@5达0.705、Recall@20达0.823，优于BM25、SPECTER、BGE-M3等基线
- 在线重排：15个真实用户盲评显示，加入verbalized用户画像后，推荐整体相关度从18.9%提升至29.3%，高度相关占比从0.5%提升至3.6%，月均偏好匹配度提升10.4%
- 摘要可信度：1000条测试样本中，基于HTML结构化输入的Gemini-2.5-Flash生成的摘要平均仅0.22个严重错误，幻觉率远低于Qwen系列模型

### 核心结论
把LLM的重计算逻辑全部移到离线批处理环节，用结构化verbalized用户画像而非纯向量做重排，是落地LLM4Rec兼顾效果、成本、用户体验的可行路径。
