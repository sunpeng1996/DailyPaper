---
title: 'SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use'
title_zh: SkillCoach：面向Agent技能使用的自演化评估与增强框架
authors:
- Jiayin Zhu
- Kelong Mao
- Yudong Guo
- Dengbo He
- Sulong Xu
- Simiu Gu
- Yutao Yue
affiliations:
- HKUST(GZ)
- JD.COM
- JITRI
arxiv_id: '2607.01874'
url: https://arxiv.org/abs/2607.01874
pdf_url: https://arxiv.org/pdf/2607.01874
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: Agent技能使用评估与性能优化
tags:
- Agent
- Skill Evaluation
- Self-Evolving Rubric
- Process Supervision
- SFT
one_liner: 构建四维度自演化评估量表，区分Agent技能使用过程质量与偶然成功，支撑训练数据筛选
practical_value: '- 企业内部Agent技能库落地可直接复用四维度（选择/遵循/组合/反思）评估框架，替代纯结果验收，避免Agent靠试错蒙对结果但流程不可复用、不合规的问题

  - 做Agent SFT训练时，可借鉴rubric过滤方案，仅保留同时满足结果正确+过程合规的轨迹做训练数据，效果显著优于纯过验轨迹训练，文中Qwen9B模型准确率较纯结果过滤SFT提升14pp

  - 技能库规模扩容时，可基于文中的降解/崩溃边界指标设定安全阈值，普通开源模型在20+高相似度干扰技能时就会出现明显选择退化，需提前加前置召回过滤层'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能评估大多仅看最终任务成功率，无法区分偶然试错通过和合规使用技能的可复用轨迹；随着企业技能库规模扩大、重叠技能增多，纯结果导向的评估和训练会引入大量brittle行为，无法保障Agent执行的稳定性和合规性。

### 方法关键点
- 定义四维度Agent技能使用元能力：`skill selection`（选对黄金技能、避开干扰技能）、`skill following`（严格执行技能定义的关键步骤）、`skill composition`（多技能按依赖顺序正确编排）、`skill-grounded reflection`（提交前按技能要求完成结果校验）
- 自演化量表框架：从技能文档、任务说明生成初始rubric，通过真实执行轨迹自动校准补全评分规则，经过验证门限迭代出最优评估量表
- 训练数据过滤：仅保留同时通过外部验证器、且rubric得分≥0.95的高质量轨迹用于SFT训练

### 关键实验
数据集为从SkillsBench筛选的28个强技能依赖任务，每个任务搭配5个干扰技能模拟企业真实技能库场景；对比基线为仅用结果过滤的SFT，Qwen3.5-9B用演化后rubric过滤的SFT准确率达32%，较纯结果SFT的18%提升14pp，较原始基线的14%提升18pp；rubric演化后黄金关键点覆盖率从71.56%提升到83.70%，轨迹过滤一致性从82%提升到96%。

最值得记住：可靠的Agent技能使用不能依赖偶然的任务成功，必须通过过程合规性保障可复用性。
