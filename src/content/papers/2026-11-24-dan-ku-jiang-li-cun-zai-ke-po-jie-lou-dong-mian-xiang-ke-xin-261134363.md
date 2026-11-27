---
title: 'Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy
  Text-to-SQL RL'
title_zh: 单库奖励存在可破解漏洞：面向可信Text-to-SQL RL的反事实执行
authors:
- Shreshth Rai
- Rishii Kumar Singh
- Aksh Aggarwal
affiliations:
- Artificial Intelligence and Machine Learning Society (AIMS-DTU)
- Delhi Technological University, New Delhi, India
arxiv_id: '2611.34363'
url: https://arxiv.org/abs/2611.34363
pdf_url: https://arxiv.org/pdf/2611.34363
published: '2026-11-24'
collected: '2026-11-27'
category: Agent
direction: Text-to-SQL Agent 奖励机制优化
tags:
- Text-to-SQL
- Reinforcement Learning
- Reward Mechanism
- Counterfactual Reasoning
- Agent
one_liner: 提出反事实数据库奖励方案，大幅降低Text-to-SQL强化学习的奖励作弊率
practical_value: '- 开发电商数智问答、库存对账类SQL Agent时，可复用反事实多库校验逻辑，避免查询偶然正确导致的业务决策错误

  - RL训练奖励设计可参考多采样校验思路，降低单样本评估的奖励信号噪声，提升模型鲁棒性

  - 做RL相关的效果对比实验时必须采用多seed验证，单seed结果存在正负反转可能，不可作为上线依据'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Text-to-SQL Agent的RL训练通常以单数据库执行结果与参考匹配作为奖励依据，错误查询可能因数据分布巧合命中正确结果，导致奖励作弊，模型学习到错误逻辑。
### 方法关键点
设计反事实数据库（CF）奖励机制：代码生成若干隐藏的数据库副本，将生成SQL在所有副本上执行；严格版奖励仅当所有副本结果匹配时给全分，平均版奖励按匹配占比给分。
### 关键结果
1302个合成审计问题上，严格版CF奖励将错误查询得全分比例从29.5%降至16.8%，奖励作弊率从54.1%降至1.9%，不误拒2847个正确查询；3.35B模型GRPO训练中，平均版CF奖励在Spider数据集精度提升1.6pts，单seed实验结论存在正负反转风险不可靠。
