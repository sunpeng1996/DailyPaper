---
title: 'E-GenRM: Generative Reward Modeling for Open-Ended E-Commerce Shopping Agents'
title_zh: 面向开放式电商购物Agent的生成式奖励模型E-GenRM
authors:
- Ying Sun
- Qiuyu Zhao
- Xiao Wang
- Xiyu Zhao
- Gege Shi
- Zenghui Sun
- Jinsong Lan
- Haihong Tang
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba
- Technische Universität Wien
arxiv_id: '2611.03008'
url: https://arxiv.org/abs/2611.03008
pdf_url: https://arxiv.org/pdf/2611.03008
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: 购物Agent · 生成式奖励建模
tags:
- Generative Reward Model
- E-commerce Agent
- GRPO
- Preference Modeling
- Active Retrieval
one_liner: 基于真实用户行为训练的电商专属生成式奖励模型 大幅提升购物Agent线上业务指标
practical_value: '- 数据构造侧可复用「全平台用户行为从购买节点反向推导购物轨迹+偏好标注」的方案，无需局限于Agent现有交互日志，解决现有数据分布窄、覆盖场景有限的问题

  - 奖励模型训练可直接复用三阶段框架：先SFT学习生成带证据的评估链，再用GRPO结合最终偏好奖励+准则级事实反馈优化，最后加入个性化难负例训练提升偏好敏感度

  - 可复用主动检索扩展模块设计，给奖励模型加低调用率的电商信息检索能力，仅在上下文缺决策证据时召回，在不显著增加 latency 的前提下提升奖励准确率

  - 购物Agent对齐阶段可优先选用领域专属生成式RM替代通用LLM-as-a-Judge，线上实测能同时提升用户满意度和降低P99延迟'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有电商购物Agent的奖励建模存在两大核心瓶颈：一是已有Agent交互日志受限于当前Agent能力边界，用户仅会提出当前能力可响应的请求，导致训练数据分布狭窄，无法支撑开放场景下的能力迭代；二是传统标量奖励无法实现细粒度信用分配，稀疏、带噪声的反馈难以区分满足显式要求但匹配用户隐性偏好差异的响应，大幅限制Agent优化效果。

### 方法关键点
- 数据层：基于全平台120+种用户行为，从购买节点反向推导跨会话长周期购物轨迹，自动构造带偏好标注的多轮交互候选对，生成有证据支撑的评估链作为训练数据，突破现有Agent交互数据的分布限制
- 训练层：三阶段训练框架：1）SFT阶段学习生成包含动态加权评估准则、准则级打分、证据依据、最终偏好的完整评估链；2）GRPO优化阶段，奖励同时覆盖最终偏好正确性和每个准则判断的事实一致性，实现细粒度监督；3）个性化难负例训练阶段，加入满足显式要求但隐性偏好不同的候选对，提升模型对用户隐性偏好的敏感度
- 扩展层：新增主动检索模块，仅当上下文缺失决策必要证据时，召回商品百科、用户评论等电商信息，在低调用率下提升评估准确率

### 关键结果
- 自建E-GenRM-Bench上，27B版本带主动检索的E-GenRM偏好准确率达87.40%，超出最强基线6.97个百分点
- 淘宝线上14天A/B测试显示，经E-GenRM后训练的购物Agent，有效购物协助率提升1.39pp，用户满意度提升2.33pp，P99 latency下降17.88%

### 核心结论
电商Agent的奖励建模不能仅依赖现有Agent交互数据，从全平台真实用户行为推导评估标准，才能支撑开放场景下的能力迭代
