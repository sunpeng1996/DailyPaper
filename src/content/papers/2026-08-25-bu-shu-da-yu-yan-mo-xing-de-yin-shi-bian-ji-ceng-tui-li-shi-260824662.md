---
title: 'The Invisible Editorial Layer: Formalizing Undisclosed Inference-Time Steering,
  Probability Placement, and the Attribution Problem in Deployed Language Models'
title_zh: 部署大语言模型的隐式编辑层：推理时干预、概率投放与归因问题
authors:
- Augusto Camargo
affiliations:
- Bluecore Consulting, São Paulo, Brazil
arxiv_id: '2608.24662'
url: https://arxiv.org/abs/2608.24662
pdf_url: https://arxiv.org/pdf/2608.24662
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: LLM 推理时干预与合规治理
tags:
- LLM
- Inference Steering
- Probability Placement
- AI Governance
- Advertising Primitive
one_liner: 形式化LLM部署层推理时隐式干预机制，提出归因问题、概率投放原语与透明度治理框架
practical_value: '- 电商广告可借鉴Probability Placement思路，在生成式导购/搜索推荐的LLM推理logit层微调品类/商品的生成概率，替代硬广植入降低用户反感

  - 生成式推荐系统的归因审计可参考推理归因问题框架，区分模型权重、prompt、推理层干预三类因素对生成结果的影响，优化迭代效率

  - 出海业务的生成式AI应用需关注推理策略透明度要求，适配EU AI Act、DSA等监管规则，避免合规风险'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM评估默认其行为仅由权重、训练数据、对齐策略、用户prompt决定，忽视了token采样前推理管道对输出概率分布的系统性修改，这类未公开干预的治理、经济价值长期被低估。

### 方法关键点
明确「模型≠部署系统」的核心事实，定义三类核心框架：
1. 推理归因问题：有限可观测性下，模型行为偏差无法单独因果归因于权重本身
2. Probability Placement：无需显式植入产品，仅通过系统性偏移生成概率实现商业影响的广告原语
3. 推理策略透明度：要求部署层干预可审计、可披露的治理原则

### 关键结论
三类框架完全适配欧盟AI法案第5条、欧盟数字服务法案、FTC广告监管规则，将LLM治理核心从「模型编码了什么」转向「谁控制模型到用户间的概率分布」
