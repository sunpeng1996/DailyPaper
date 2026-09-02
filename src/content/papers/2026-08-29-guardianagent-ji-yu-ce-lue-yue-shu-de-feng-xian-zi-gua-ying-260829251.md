---
title: 'GuardianAgent: Policy-Conditioned Risk-Adaptive Anonymization with Verified
  Adversarial Escalation'
title_zh: GuardianAgent：基于策略约束的风险自适应可验证匿名化框架
authors:
- Ruiyi Yang
- Gayathri Lihinikaduarachchi
- Rahat Masood
- Flora D. Salim
- Salil S. Kanhere
affiliations:
- School of Computer Science and Engineering, UNSW Sydney, Australia
arxiv_id: '2608.29251'
url: https://arxiv.org/abs/2608.29251
pdf_url: https://arxiv.org/pdf/2608.29251
published: '2026-08-29'
collected: '2026-09-02'
category: Agent
direction: Agent隐私保护 · 内容匿名化
tags:
- Agent
- Privacy Protection
- Risk Assessment
- Anonymization
- LLM System
one_liner: 提出多因子风险评分驱动的Agent自适应匿名化框架，兼顾隐私、效用与效率
practical_value: '- 构建Agent对外交互隐私防护体系时，可复用AMRSF多因子显式风险评分思路，不直接依赖LLM判风险，结合策略合规性、数据敏感度等硬规则降低误判

  - 可参考快慢路径架构：低不确定性的规则匹配走快路径，仅高风险/模糊场景调用LLM，兼顾业务效率与效果，适合高并发隐私脱敏场景

  - 内容匿名化分级设计可参考五级分层+对抗验证的思路，避免过度匿名化损失内容效用，可迁移到电商UGC、用户评论、个性化营销内容的隐私脱敏场景'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有web流量隐私防护仅做敏感片段检测，无法适配不同站点隐私策略、不同场景的风险等级，易出现过度匿名化损失效用，或匿名不足泄露隐私，全流程调用LLM的方案成本高、效率低。

### 方法关键点
1. 设计AMRSF多因子风险评分机制，融合策略违规概率、数据敏感度、接收方属性、用途合法性、上下文等维度显式计算风险，不依赖LLM直接打分；
2. 采用快慢路径架构，低不确定度的策略匹配走规则快路径，仅模糊场景调用LLM慢路径；
3. 基于可验证对抗猜测器实现五级匿名化分层，仅当原始文本可被攻击者合理推断时才升级匿名等级，避免过度脱敏。

### 关键结果
在法律文本、Reddit帖子、多格式PII记录三个基准数据集上均达到≥0.90的隐私保护得分，是现有基线中隐私-效用权衡最优的方案，更换基座模型仍保持鲁棒性，相同文本在不同接收方、用途等上下文下可自适应调整匿名策略。
