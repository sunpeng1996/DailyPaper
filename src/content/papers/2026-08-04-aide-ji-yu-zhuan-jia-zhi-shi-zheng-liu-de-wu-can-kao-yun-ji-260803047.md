---
title: 'AIDE: Automated Instruction via Distilled Expertise for Reference-Free Motor
  Skill Coaching'
title_zh: AIDE：基于专家知识蒸馏的无参考运动技能自动指导框架
authors:
- Yoshiki Ito
affiliations:
- Hitachi, Ltd.
- Research & Development Group, Hitachi, Ltd.
arxiv_id: '2608.03047'
url: https://arxiv.org/abs/2608.03047
pdf_url: https://arxiv.org/pdf/2608.03047
published: '2026-08-04'
collected: '2026-08-09'
category: Other
direction: 无参考运动技能自动反馈生成
tags:
- Knowledge Distillation
- LLM
- Feedback Generation
- Pose Estimation
- Reference-Free
one_liner: 通过师生蒸馏架构实现训练仅用专家参考、推理仅输入学习者姿态生成指导反馈
practical_value: '- 师生蒸馏架构可复用：训练阶段用高成本专家/全量特征数据训练教师模型，推理阶段仅用易获取的用户/物品特征生成结果，大幅降低推理成本，适合电商个性化文案、推荐理由生成场景

  - 专家差异编码转无参考辅助token生成的思路，可迁移到无监督的用户行为差距分析、个性化改进建议生成任务

  - LLM-based自动评估方法可复用在文本类生成结果的批量指标校验，替代部分人工标注，降低测评成本'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有运动技能自然语言指导反馈生成方法在训练、推理阶段均依赖专家演示数据，部署门槛高，且专家教练资源稀缺、成本高昂，难以规模化落地。
### 方法关键点
1. 采用师生蒸馏架构，仅训练阶段使用专家参考数据
2. 教师模型基于配对的学习者-专家姿态数据，通过冻住的LLM生成学习者专属token与学习者-专家差异编码token
3. 学生模型继承教师编码器与权重初始化，新增辅助模块仅输入学习者姿态序列生成补充token，替代显式专家对比步骤，推理阶段无需任何专家数据
### 关键结果
在ExpertAF数据集上，AIDE多数指标优于无参考基线，效果与训练、推理双阶段都依赖专家数据的方法相当，LLM自动评估结果与上述结论一致。
