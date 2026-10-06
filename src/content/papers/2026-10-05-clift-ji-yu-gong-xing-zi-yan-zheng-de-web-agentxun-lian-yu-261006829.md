---
title: 'CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling'
title_zh: CLIFT：基于共形自验证的Web Agent训练与测试阶段性能提升框架
authors:
- Yifan Zhang
- Yutong Dai
- Viraj Prabhu
- Zhiyuan Hu
- Ran Xu
- Zeyuan Chen
affiliations:
- Salesforce AI Research
arxiv_id: '2610.06829'
url: https://arxiv.org/abs/2610.06829
pdf_url: https://arxiv.org/pdf/2610.06829
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Web Agent 共形自验证训练与推理优化
tags:
- Web Agent
- Conformal Prediction
- GRPO
- Trajectory Selection
- RL
one_liner: 基于共形校准的可复用验证库，同时优化Web Agent训练RL奖励与测试轨迹选择效果
practical_value: '- 电商导购/广告投放Agent的RL训练可复用「全局/域名/路径分层共形校准的验证问题库」，替代高成本LLM judge生成step级奖励，降低训练成本

  - 搜索/导购Agent推理阶段可复用保守多数投票的轨迹选择逻辑，仅用预训练验证库打分选最优路径，无需调用外部judge，保证性能无劣化的同时降低推理延迟

  - 跨场景Agent迁移无需重新训练，仅需改写验证库的URL适配规则、重校准lift权重即可快速落地，大幅降低跨品类/业务的迁移成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Web Agent的RL训练面临反馈瓶颈：二元成功信号过于稀疏，无法支撑有效credit assignment；调用前沿LLM judge提供稠密奖励成本过高，且部署阶段无法依赖外部judge，昂贵的judge反馈价值无法复用。

### 方法关键点
- 构建带URL作用域、极性标签的验证问题库，通过Mondrian-ACI共形跟踪器按「全局/域名/URL路径」三层校准每个问题的信任权重，仅保留与judge打分高度对齐的高置信验证信号
- 训练阶段：将验证库得分非负叠加到judge奖励上，结合URL分层归一化优势做GRPO更新，不会拉低原有judge奖励基线，有效解决奖励稀疏问题
- 测试阶段：冻结验证库，生成贪心轨迹+多组多样性重试轨迹，通过保守多数投票规则选最优轨迹，无需调用外部judge，保证性能不低于贪心基线
- 验证库支持跨模型、跨场景迁移，仅需重校准权重即可适配新环境

### 关键实验
在三个主流Web Agent基准上验证效果：WebArena Infinity(WAI)上，开源Gemma-4 31B+CLIFT+CTS成功率达74.6%，超过原SOTA基线70.1%；VisualWebArena(VWA)上，训练得到的验证库直接迁移给GPT-5.5，成功率达53.7%，超过原SOTA 52.9%；Online Mind2Web(OM2W)零样本迁移场景下，GPT-5.5搭配CTS的成功率提升11.3pp至61.0%。

### 核心结论
单次轨迹奖励仅能被消耗一次，而经过共形校准的可复用验证库可以被审计、重校准、跨场景迁移，将昂贵的judge反馈价值从训练延伸到部署全链路。
