---
title: 'StudentSim: Training LLM-based Student Simulators'
title_zh: StudentSim：基于LLM的个性化学生模拟器训练框架
authors:
- Ke Yang
- Chenglong Wang
- Michel Galley
- Chandan Singh
- Jeevana Priya Inala
- ChengXiang Zhai
- Jianfeng Gao
affiliations:
- Microsoft Research
- University of Illinois Urbana-Champaign
arxiv_id: '2609.01591'
url: https://arxiv.org/abs/2609.01591
pdf_url: https://arxiv.org/pdf/2609.01591
published: '2026-08-31'
collected: '2026-09-02'
category: Agent
direction: Agent 个性化用户模拟器训练与评估
tags:
- User Simulator
- LLM Agent
- Two-stage Training
- LoRA
- Personalization
one_liner: 提出两阶段训练的StudentSim框架，让LLM学生模拟器同时具备高行为保真与高指导响应能力
practical_value: '- 可复用双维度用户模拟器评估思路：电商/推荐领域模拟用户对推荐/广告的反馈时，可同时定义「行为匹配度」（模拟偏好与真实用户一致度）和「策略响应度」（对促销/种草内容的反应符合度）两大指标，代替小流量测试降低试错成本

  - 两阶段训练范式解决稀疏用户数据问题：先全量用户数据预训练学习通用行为模式，再用单用户稀疏数据做LoRA微调得到个性化用户模拟器，可直接迁移到冷启动用户建模、个性化用户Agent训练场景

  - 个性化模拟器作为RL奖励源的思路可复用：用训练好的用户模拟器反馈优化推荐文案、促销策略，比通用LLM模拟的用户反馈更贴合真实用户，大幅提升策略优化效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI tutor优化依赖大量真实学生反馈，但真实反馈采集成本高、速度慢、数据稀疏。现有模拟器存在明显短板：状态追踪类模型行为保真度高但无法响应自然语言指导，prompted LLM能响应指导但难以复现特定学生的能力水平与行为特征，无法同时满足模拟器的核心要求。

### 方法关键点
- 定义双维度核心评估标准：行为保真度（F↑，模拟行为与真实学生行为的匹配度）、指导响应度（R↑，收到指导后行为向目标方向修正的程度）
- 两阶段训练框架：Stage 1用跨所有学生的公共数据预训练base模型，学习领域通用的学生行为模式、常见错误特征、指导响应逻辑；Stage 2用单学生稀疏数据做LoRA微调，得到个性化学生模拟器
- 配套标准化评估基准StudentSimEval，覆盖象棋、二语写作、数学3个领域共60名学生的公开学习数据，固定train/held-out拆分，统一评估指标，保证不同方法结果可比

### 关键结果
跨3个领域StudentSim均显著优于所有基线：象棋领域F=0.51、R=0.91，远超GPT-5.4的F=0.23、R=0.72，以及Maia2的F=0.45、R=0.27；二语写作、数学领域同样双指标领先。作为RL奖励源优化AI tutor时，比GPT-5.4作为奖励源的方案，专家评分的准确率高18.9%，指导质量高7.5%，个性化评分高62.4%。

**最值得记住的一句话**：个性化用户模拟器的核心价值是同时具备「与真实用户一致的行为基准」和「对干预的可响应性」，两者缺一不可，否则无法作为可靠的代理反馈源用于策略优化。
