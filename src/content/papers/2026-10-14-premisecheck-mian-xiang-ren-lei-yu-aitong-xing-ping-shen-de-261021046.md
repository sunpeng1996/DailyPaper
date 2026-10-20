---
title: 'PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews'
title_zh: PremiseCheck：面向人类与AI同行评审的高效事实校验方法
authors:
- Dingjie Song
- Zhiling Yan
- Ziqian Zhang
- Yuxuan Zhang
- Lichao Sun
affiliations:
- Lehigh University
- University of British Columbia
- Vector Institute
arxiv_id: '2610.21046'
url: https://arxiv.org/abs/2610.21046
pdf_url: https://arxiv.org/pdf/2610.21046
published: '2026-10-14'
collected: '2026-10-20'
category: LLM
direction: LLM事实校验 · 成本延迟优化
tags:
- Fact-Checking
- LLM Efficiency
- Text Validation
- Benchmark
- Low-Cost Inference
one_liner: 提出LLM拆显式前提+轻量决策模型校验的评审事实校验框架，精度追平GPT-5.5成本减半
practical_value: '- 多隐含信息的文本校验场景可复用「LLM先拆显式原子断言+轻量模型逐句校验」架构，大幅降低大模型长文本调用开销，适合电商商品文案、广告话术的批量事实校验

  - 长文本（如商品详情页、用户长评价、Agent生成的服务回复）的事实一致性校验，可参考该拆分逻辑平衡精度与推理延迟

  - 业务侧构建自定义内容校验基准时，可参考ReviewFact的多域标注逻辑，同时纳入精度、成本、延迟三个核心业务指标做评估'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
投稿量激增导致同行评审压力陡增，人类/AI生成的评审意见常存在与论文内容不符的事实错误；现有方案要么是前沿大模型全量读取论文校验，成本延迟极高，要么是轻量决策模型直接校验，无法处理混合多个隐含断言的整段评论，精度不足。
### 方法关键点
两级校验架构：1）仅输入评论，调用LLM将其隐含的多个断言改写为独立显式前提，无需读取长文本论文；2）用低成本决策模型逐一对每个前提和论文内容做一致性校验，取最低匹配分作为整段评论的正确性结果。同时构建跨NLP、机器学习、自然科学三个领域的评审事实错误标注基准ReviewFact，同时评估精度、成本、延迟三个指标。
### 关键结果
- 全领域校验精度与GPT-5.5持平，成本仅为其50%
- NLP领域评审校验成本仅为GPT-5.5的25%，延迟降低50%以上
