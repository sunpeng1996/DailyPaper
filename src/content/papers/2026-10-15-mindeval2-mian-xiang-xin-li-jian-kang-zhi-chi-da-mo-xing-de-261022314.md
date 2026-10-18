---
title: 'MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language
  Models in Mental Health Support'
title_zh: MindEval2：面向心理健康支持大模型的临床级评估框架
authors:
- John Mendonça
- Daniel Tschernutter
- José Pombal
- Areti Vassilopoulos
- Catarina Botelho
- Ignacio Sarasua
- Maya D'Eon
- Nuno Guerreiro
- Ricardo Rei
affiliations:
- Sword Health
- NVIDIA
- Instituto Superior Técnico
- Yale University
arxiv_id: '2610.22314'
url: https://arxiv.org/abs/2610.22314
pdf_url: https://arxiv.org/pdf/2610.22314
published: '2026-10-15'
collected: '2026-10-18'
category: Eval
direction: LLM垂直场景评估 · 心理健康领域
tags:
- LLM-Evaluation
- Mental-Health
- Synthetic-User
- Multi-turn-Interaction
- LLM-as-Judge
one_liner: 提出融合临床级评分规则与高拟真患者模拟器的心理健康场景LLM评估框架
practical_value: '- 搭建垂直场景Agent（如电商导购、客服Agent）评估体系时，可参考与领域专家共建可操作评分细则的思路，替代模糊的主观评分规则，提升评估结果的业务对齐度

  - 构建仿真测试用户时，可复用「固定用户画像+动态会话场景+轮间记忆更新+工具调用」的架构，提升模拟用户的真实度，覆盖更复杂的测试case

  - 多轮交互Agent评估可加入纵向记忆校验维度，用来测试长会话下的一致性、长期任务完成能力，适配电商长周期导购、售后等场景'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前心理健康场景LLM评估存在两大痛点：一是模拟患者过于主动、自我反思度不符合真实用户特征；二是LLM-as-judge采用的李克特量表规则不透明，评估结果实用价值低。
### 方法关键点
框架包含两大核心组件：
1.  MHQR评分规则：与心理学博士共建，将响应质量拆解为明确可执行的评估标准，可解释性和落地性远优于现有评估体系
2.  MindSim患者模拟器：结合固定患者画像、动态会话场景、工具调用能力、轮次间可更新的记忆模块，支持多轮、长周期的高拟真交互。
### 关键结果数字
测试18款闭源/开源大模型发现，头部模型已基本解决表层质量、边界合规问题，**引导校准是所有模型的核心失效模式，贡献了大部分质量缺口**。
