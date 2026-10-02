---
title: 'Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents'
title_zh: RPG：无需更新模型权重的具身Agent引导式自提升框架
authors:
- Yen-Jen Wang
- Haozhe Jiang
- Shuying Deng
- Haoru Xue
- Weirui Ye
- Rocky Duan
- Nika Haghtalab
- S. Shankar Sastry
- Pieter Abbeel
- Haozhi Qi
affiliations:
- UC Berkeley
- Amazon FAR
- MIT
- University of Chicago
arxiv_id: '2610.02204'
url: https://arxiv.org/abs/2610.02204
pdf_url: https://arxiv.org/pdf/2610.02204
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 具身Agent · 无权重更新自提升
tags:
- EmbodiedAgent
- Self-Improvement
- SkillLibrary
- PromptOptimization
- Sim2Real
one_liner: 提出RPG三阶段具身Agent自提升框架，无需更新模型权重即可大幅提升任务成功率
practical_value: '- 可复用双Agent诊断逻辑：业务场景中可以拿全量后台真实数据（如电商全链路转化数据、广告曝光归因数据）作为「特权Agent」的输入，对比在线运行的业务Agent表现，定位策略缺陷，全程无需更新大模型权重，迭代成本远低于微调

  - 共享策略更新加跨场景校验门限：所有候选的技能库、prompt修改必须满足「整体指标提升+单场景指标降幅不超过预设阈值」，避免局部优化导致其他业务场景效果雪崩，可直接复用在多场景推荐、广告投放的策略迭代中

  - 模拟→灰度→全量的部署流程可复用：先在离线仿真环境/小流量灰度环境完成所有策略迭代，冻结系统后再上线全量环境，无需在线调优，大幅降低业务风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前具身Agent开发需大量人工投入完成技能开发、奖励设计、感知控制融合工作，基于LLM的机器人控制存在推理延迟高、执行鲁棒性差的问题，且直接微调模型权重成本高、可解释性弱、迭代风险大，亟需低成本的自提升方案。
### 方法关键点
- 三阶段RPG框架：Reconstruct阶段从离线操作数据集拆解核心能力，生成对应模拟练习任务；Practice阶段通过双Agent对比（仅用部署端观测的Runtime Agent + 可获取模拟器全状态的Privileged Agent）、失败轨迹视频分析诊断缺陷，迭代优化共享技能库与系统prompt，所有候选修改需通过「整体成功率提升+单任务降幅≤20pp」的跨任务校验才会保留；Go Real阶段将冻结系统做简单硬件校准后直接部署。
- 全程不更新模型权重，仅优化可解释的技能代码与系统prompt，迭代成本极低。
### 关键实验结果
- 模拟场景：22个操作任务上，15轮练习后成功率从首轮的28.6%提升至95.0%，远超ASPIRE（75.5%）、GPT-6 Astra Pro驱动的CaP-Agent0（60.0%）。
- 真实部署：3个物理任务共30次试验全部成功，额外5个零样本物理任务也可正常执行。
### 核心结论
对Agent系统的优化不一定需要调整模型权重，通过迭代高质量的共享技能库、系统prompt配合严格的跨场景校验，即可实现大幅效果提升，且成本更低、可解释性更强、上线风险更小。
