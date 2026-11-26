---
title: What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware
  Reanalysis of SkillsBench
title_zh: SkillsBench基准源码审计与技能增益度量的噪声感知重分析
authors:
- Haozhe Zhang
- Zhen Long
affiliations:
- Trine University
- National University of Singapore
arxiv_id: '2611.33943'
url: https://arxiv.org/abs/2611.33943
pdf_url: https://arxiv.org/pdf/2611.33943
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent技能评估 · 基准审计
tags:
- Agent Skills
- Benchmark Audit
- Evaluation Methodology
- Regression to the Mean
- Statistical Reanalysis
one_liner: 通过源码审计与统计重分析纠正SkillsBench基准关于技能损伤和门控效果的错误结论
practical_value: '- 做Agent技能效果评估时，需将所有评分规则明确写入任务prompt，避免评分信息仅在技能中披露导致增益度量失真

  - 验证技能门控/路由策略时，不能仅依赖离线log replay的结果，需额外做标签打乱空检验和独立held-out集测试，规避回归均值与数据泄漏带来的假增益

  - 不要基于少量测试样本的负结果直接判定技能有害，需做多重检验校正的显著性验证，排除采样噪声干扰'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
SkillsBench是首个面向Agent技能的大规模评估基准，此前其报告的16.6pp平均技能增益、13个任务技能负提升结论被广泛用作技能淘汰、压缩、路由优化的决策依据，但该基准的度量逻辑、负增益真实性从未被系统校验，直接复用结论会导致大量无效算法迭代。
### 方法关键点
- 源码级审计全量任务的prompt、评分脚本、技能包、执行框架，定位评估偏差来源
- 基于7554条公开运行记录构建1421组(配置,任务)配对单元，采用置换检验做多检验校正的显著性验证，排除采样噪声干扰
- 设计三类评估协议：离线log replay、标签打乱空检验、独立held-out测试，交叉验证技能门控策略的真实效果
### 关键结果数字
- 审计发现3个任务的评分规则仅在技能中披露，贡献总增益的18%，该类任务平均技能增益达74.6pp；4个任务存在占位符技能目录，某执行框架默认注入48个内置技能导致对照组不纯
- 统计重分析显示，经FDR校正后26个任务有显著正增益，无任务存在显著负增益；观测到的169个负增益单元远低于零技能效应下的噪声预期值（302-353个）
- 看似能提升2-3pp的基线门控策略，在标签打乱无真实技能效应时仍能获得4-7pp增益，在独立held-out测试中无统计显著提升
### 核心结论
任何基于少量样本的技能增益/损伤结论都要做显著性校验和空检验，离线replay的效果很大概率是回归均值和数据泄漏带来的假象。
