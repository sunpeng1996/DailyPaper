---
title: 'Community Notes Across Platforms: Evaluating the Feasibility of Re-using Crowd-sourced
  Context Notes'
title_zh: 跨平台社区笔记：众包上下文注释的复用可行性评估
authors:
- Nishka Arora
- Yann Issam Aouidef
- Ashish Goel
affiliations:
- Stanford University, Department of Management Science and Engineering
arxiv_id: '2611.33546'
url: https://arxiv.org/abs/2611.33546
pdf_url: https://arxiv.org/pdf/2611.33546
published: '2026-11-24'
collected: '2026-11-28'
category: Eval
direction: 内容治理 · 跨平台众包注释复用
tags:
- Crowdsourced_Fact_Checking
- Community_Notes
- Cross_Platform_Governance
- Content_Moderation
- Matching_Pipeline
one_liner: 验证跨平台众包事实核查笔记复用可行性，实现三阶段匹配管道精度72.6%
practical_value: '- 电商虚假宣传、不实评论的众包审核场景可复用跨场景标注思路，同一违规话术在多直播间/多商品页出现时直接挂载已审核标签，减少重复人力投入

  - 内容推荐的风险内容治理环节可复用三阶段匹配架构，先召回疑似重复风险内容再做细粒度校验，平衡治理精度与算力成本

  - UGC内容众包贡献复用场景可参考时序分析方法，优先挂载已验证有效的历史标注，大幅缩短风险内容的治理响应时效'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
众包事实核查系统生成、评级有效注释需要大量贡献者投入，但现有注释通常仅对生成时的对应帖子、平台生效，同类误导性内容跨平台重复出现时会造成大量重复劳动，生效时效也无法保障。
### 方法关键点
1. 构建X平台一周内社区笔记关联的340条声明+Bluesky平台候选匹配帖子的人工标注数据集；
2. 设计三阶段匹配管道，实时检索Bluesky流中的重复声明，判断现有社区笔记是否适用；
3. 开发Crossnote原型系统实现跨平台注释自动挂载。
### 关键结果
140/340条声明在Bluesky有至少一次重复出现，复用空间充足；三阶段管道在留出流评估中精度72.6%，已知正样本端到端召回70.1%；大部分匹配注释在目标帖子发布时已处于有效状态，即使目标帖子先发，注释复用的生效速度也比原平台首次生成注释更快。
