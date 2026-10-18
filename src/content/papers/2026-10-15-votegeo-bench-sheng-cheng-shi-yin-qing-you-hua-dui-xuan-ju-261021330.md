---
title: 'VoteGEO-Bench: Measuring the Impact of Generative Engine Optimization on Electoral
  Visibility'
title_zh: VoteGEO-Bench：生成式引擎优化对选举曝光影响的评测基准
authors:
- Shiqi Zhang
- Xiaokui Xiao
affiliations:
- National University of Singapore
arxiv_id: '2610.21330'
url: https://arxiv.org/abs/2610.21330
pdf_url: https://arxiv.org/pdf/2610.21330
published: '2026-10-15'
collected: '2026-10-18'
category: Eval
direction: 选举场景GEO效果评测基准构建
tags:
- Generative Engine Optimization
- Benchmark
- LLM Evaluation
- Content Visibility
- Election LLM
one_liner: 推出覆盖美日选举场景的VoteGEO-Bench基准，评测11种GEO改写策略的内容曝光提升效果
practical_value: '- 做生成式搜索/AI导购内容优化时，必须明确绑定待提升曝光的目标（如商品/品牌），无目标的内容改写几乎无法提升曝光

  - 内容改写提升曝光优先级：优化页面组织结构>通过论证强化核心观点>补充佐证材料>调整措辞，可直接复用在电商商品页、种草文案的GEO优化流程

  - 用户显式偏好（如明确标注的品牌/品类偏好）对内容曝光的影响远大于单条内容改写的效果，个性化生成式推荐优先复用显式偏好信号'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
LLM已成为公众获取选举等公共信息的核心渠道，但外部网页内容如何影响LLM生成结果的曝光、GEO（生成式引擎优化）的实际效果缺乏标准化评测框架，选举场景下的GEO操纵风险尚未被系统验证。
### 方法关键点
构建VoteGEO-Bench开源基准，覆盖2024美国大选、2026日本众议院选举场景，整合选举相关Query、历史网页、选民画像三类数据，评测4大类共11种GEO改写策略的曝光提升效果。
### 关键结果
1. 生成引擎引用来源中62%来自低成本自有/开放平台，近30%网页的曝光可持续3天以上；
2. 无指定目标的改写仅不足5%的概率提升目标曝光，指定目标的改写曝光提升概率达32%；
3. 优化页面结构、论证强化观点两类策略的增益是补充证据/改措辞策略的2.3倍，两类最优策略在所有美国选民画像下均保持正向增益；
4. 用户显式党派身份带来的曝光基线差距是单网页改写增益的2.1倍。
