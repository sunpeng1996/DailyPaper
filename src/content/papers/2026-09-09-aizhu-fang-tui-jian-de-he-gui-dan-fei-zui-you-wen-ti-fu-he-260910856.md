---
title: 'Following the Preference, Missing the Optimum: Compliance Without Optimization
  in AI Housing Recommendation'
title_zh: AI住房推荐的合规但非最优问题：符合偏好却遗漏最优选项
authors:
- Hsuan Lo
affiliations:
- Harvard University
- Independent Researcher
arxiv_id: '2609.10856'
url: https://arxiv.org/abs/2609.10856
pdf_url: https://arxiv.org/pdf/2609.10856
published: '2026-09-09'
collected: '2026-09-11'
category: RecSys
direction: LLM推荐 · 约束合规与优化审计
tags:
- LLM
- Recommender System
- Algorithmic Audit
- Pareto Optimization
- Fairness
one_liner: 通过带地面真值的审计，发现LLM住房推荐符合约束但39%推荐被帕累托占优，无显著身份歧视
practical_value: '- 评估生成式推荐效果时，除约束合规率、相关性/点击率外，新增Pareto占优率、最优选项价差等量化用户实际收益损失的指标，避免仅用自洽的评估指标高估系统价值

  - 多约束推荐场景下，可采用「规则预过滤约束满足候选集+LLM排序」的混合架构，直接将硬约束违规率降为0，且不会引入额外身份偏差

  - Pareto占优率可作为生成式推荐的线上可观测诊断指标，无需依赖用户反馈就能快速发现排序劣化问题，适合电商、租房等约束明确的推荐场景

  - LLM在多候选集下的排序优化能力不会随模型规格/价格提升而变好，不要盲目堆大模型参数解决排序优化问题，可配合轻量精排模型补全短板'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM住房推荐审计要么聚焦种族转向等公平性问题，要么仅评估点击率等 engagement 指标，无枚举库存作为地面真值量化用户因系统遗漏更优选项产生的实际可度量损失，也无法验证身份歧视带来的实际成本。
### 方法关键点
- 面向纽约150个合成租客场景，每个场景构建120套真实房源候选池，包含40套满足租金、卧室数、通勤时间硬约束的房源，且覆盖该场景全量Pareto最优房源
- 定义无效用假设的严格Pareto占优规则：推荐房源被占优当且仅当同候选池内存在另一套房源租金更低、通勤更短、卧室数不少于该房源
- 测试OpenAI、Anthropic共3款覆盖45倍价格区间的模型，累计9945次API调用，以随机抽样作为效果baseline
### 关键结果
- 约束合规率达98.2%，远高于随机抽样的33.4%；但39.0%的推荐房源被严格占优，占优房源中位数便宜$900/月、通勤短3.5分钟，租金表现劣于随机抽样（比最优高$498/月 vs 随机的$261/月）
- 模型可准确响应偏好调整：单句偏好修改可使中位推荐租金按预期变动$646/月，但即使明确给出优先级指令，推荐租金仍比同池最便宜的5套合格房源高$606/月，prompt优化无显著效果
- 候选集规模越大优化能力越差：10个候选集时最便宜房源召回率93.7%，80个候选集时降至53.5%
- 48组身份对比中47组经校正后无显著差异，未观测到统计显著的身份导向歧视
### 核心结论
LLM推荐当前存在「合规不优化」的共性问题：可严格执行用户明确约束，但不会在约束范围内做Pareto最优选择，且该问题不随模型规格、价格提升而改善
