---
title: Who Chooses How Preferences Are Aggregated? Auditing Aggregation-Rule Authority
  in LLM-Based Group Recommendation
title_zh: LLM 群体推荐场景下的聚合规则权限审计研究
authors:
- Yuxuan Du
affiliations:
- Independent Researcher
arxiv_id: '2608.23966'
url: https://arxiv.org/abs/2608.23966
pdf_url: https://arxiv.org/pdf/2608.23966
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 群体推荐 · LLM决策权限控制
tags:
- Group Recommendation
- LLM4Rec
- Preference Aggregation
- Decision Authority
- Behavioral Audit
one_liner: 通过受控行为审计明确聚合规则权限分配对LLM群体推荐决策的作用机制
practical_value: '- 做多人场景（如家庭账号推荐、拼团选品、好友出行方案推荐）的LLM推荐系统时，可新增聚合权限配置逻辑：高冲突场景默认让用户选择聚合策略（如优先全员满意/优先总效用最高），减少决策争议

  - 对已明确授权LLM自主聚合的场景，可提前对齐不同模型的聚合偏好：比如测试发现Qwen更倾向ADD（总效用最大化）规则，可根据业务目标（如性价比优先/公平性优先）选择对应底座

  - 可复用论文的受控行为审计框架，针对不同业务场景的多用户推荐决策做合规性/偏好一致性校验，避免模型隐性决策带来的用户不满'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM越来越多用于多用户群体推荐场景，但现有研究多关注聚合规则的执行效果，忽略了「谁有权决定用哪种聚合规则」这个交互层面的核心问题——当不同聚合规则（如总效用最大化/最少痛苦原则）得出不同结果时，权限归属会直接影响最终决策的合理性与用户接受度。

### 方法关键点
- 定义3种权限条件：未明确指定权限、用户保留聚合规则选择权、用户将权限委托给模型
- 构造两类偏好数据集：1000条合成评分剖面、1000条从MovieLens 32M提取的真实用户评分剖面，其中60%为核心冲突剖面（ADD和LMS两种规则输出结果完全不同）
- 针对3款主流LLM（GPT-5.6 Sol、Claude Sonnet 5、Qwen 3.6 Plus）做单轮受控实验，对比不同权限下的决策承诺率、聚合结果分布

### 关键实验结果
- 用户保留权限时，3款模型在核心冲突场景的决策承诺率几乎为0，均会主动询问用户聚合策略偏好；用户委托权限时，3款模型的承诺率均达100%
- 所有模型在被明确要求执行ADD或LMS规则时准确率均为100%，但权限未明确/委托时，聚合结果差异极大：比如合成数据场景下GPT的ADD符合率达95.5%，Claude仅为43.9%
- 相同偏好剖面下，模型的聚合结果受场景表述（如餐厅/出行）影响，重复调用的结果变异率最高达24%

### 核心结论
授权LLM自主做群体推荐聚合，只是把决策权限交给模型，并不代表会得到符合业务预期的聚合结果，必须结合业务目标提前校验模型的聚合偏好。
