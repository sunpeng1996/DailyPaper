---
title: 'Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations'
title_zh: 基于互斥竞争解释集的开放式科学发现框架CONTRASTIVE Discovery
authors:
- Ziang Liu
- James J. Kim
- Yijia Dai
- Jennifer J. Sun
affiliations:
- Cornell University
arxiv_id: '2611.14514'
url: https://arxiv.org/abs/2611.14514
pdf_url: https://arxiv.org/pdf/2611.14514
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 开放式科学发现优化
tags:
- LLM Agent
- Scientific Discovery
- Bayesian Surprise
- MCTS
- Contrastive Evaluation
one_liner: 用MECE对比解释集替代单假设验证，相同实验预算下多解决67%科学问题
practical_value: '- 电商/广告AB实验场景下，验证假设时先构建MECE对比解释集（如优惠对转化率的影响：更高/无差异/更低），一次实验即可得到明确结论，减少实验轮次与预算浪费

  - 可将对比集评估逻辑无侵入叠加到现有Agent架构，既可以二次挖掘历史实验数据的隐性结论，也可以引导新实验搜索方向，提升单位实验的信息产出

  - 做LLM评估/策略效果离线验证时，用MECE选项集+信念分配的方式替代二元打分，减少评估歧义，大幅提升评估结果的信息量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent开放式科学发现普遍采用pointwise单假设验证逻辑，仅对比假设h与其补集¬h，当h被证伪时无法定位到具体成立的替代解释，相同实验预算下信息利用率极低，大量有效实验数据被浪费。
### 方法关键点
- 核心替换单假设为MECE（互斥且穷尽）对比解释集，覆盖同一科学问题的所有可能结论
- 用独立LLM作为信念elicitor，分别输出实验前后的解释集信念分布，采用熵缩放的KL散度（对比信念偏移）作为实验收益评分
- 当单条解释后验信念≥0.8时判定问题已解决，框架可无侵入叠加到现有Agent架构，支持历史数据二次评估、新实验搜索引导两种使用方式
### 关键结果
在材料科学、天文学、贷款歧视、社交行为等6个域的数据集测试，对比pointwise贝叶斯惊奇、novelty、feasibility三类基线，相同200次实验预算下：
1. 89%的高惊奇pointwise候选为被拒绝的假设，用对比集做事后评估无需新实验即可定位其中73%案例的具体替代解释
2. 对比集引导的搜索比pointwise惊奇基线多解决67%的科学问题，新增结论几乎全部来自原有方法仅能判定为拒绝的矫正型结论
3. 38位盲审专家对78%的已解决结论表示认同，对pointwise拒绝的案例，专家对框架输出的替代解释认同度达82%
### 核心结论
明确列出所有竞争解释的对比式验证，能让相同实验预算的信息产出提升60%以上，避免大量“只知错误不知正确结论”的无效实验
