---
title: 'SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution
  and Runtime Feedback'
title_zh: SkillDRE：基于预执行与运行时反馈的Agent技能双阶段红队演化
authors:
- Pengyu Zhu
- Jingyi Yang
- Yi Liu
- Li Sun
- Sen Su
affiliations:
- Beijing University of Posts and Telecommunications
- North China Electric Power University
- Chongqing University of Posts and Telecommunications
arxiv_id: '2609.32400'
url: https://arxiv.org/abs/2609.32400
pdf_url: https://arxiv.org/pdf/2609.32400
published: '2026-09-25'
collected: '2026-09-29'
category: Agent
direction: Agent 恶意技能演化红队测试框架
tags:
- Agent
- Red Teaming
- Skill Evolution
- Runtime Defense
- Pre-execution Scanning
one_liner: 提出双阶段闭环反馈的Agent恶意技能演化框架，攻击成功率超最强基线40.3%且检测率为0
practical_value: '- 做Agent业务安全防御可参考双阶段检测的互补性，不要只做单阶段静态扫描或运行时拦截，必须联合校验避免被绕过

  - 做Agent技能正向迭代（如电商客服技能升级、推荐Agent策略优化）可复用该双阶段闭环：先做预执行合规校验，再用运行时反馈迭代，同时保留原有核心功能，降低线上风险

  - 做自身Agent系统红队测试的团队，可直接复用SkillDRE的攻击目标构造、校验规则生成逻辑，自动化挖掘技能漏洞，降低人工成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能自迭代机制可用于正向能力升级，也能被攻击者用来演化难检测、高成功率的恶意技能。但单靠预执行扫描或单靠运行时防御都存在明显漏洞：通过扫描的技能可能在运行时被拦截，修复运行时问题的版本又会触发扫描告警，现有攻击方法无法同时绕过两层防御且保留原有良性功能。

### 方法关键点
1. 初始化阶段自动生成与任务绑定的固定恶意目标和可验证判定规则，迭代过程中目标保持不变，保证优化方向一致
2. 双阶段闭环设计：第一阶段预执行演化用SkillScan反馈迭代修改技能包，直到风险分降为0；第二阶段运行时演化用SkillSonar拦截结果和攻击判定结果修改技能，修改后返回第一阶段重新过扫描，循环直到攻击成功或预算耗尽
3. 风险分按严重程度加权（高/中/低风险权重10000/1000/10），优先消除高风险告警，同时要求迭代过程保留技能原有良性功能接口

### 关键实验结果
在SkillsBench的94个任务、249个技能上测试，跨4个主流大模型，对比SkillJect、SkillHarm基线：平均攻击成功率45.28%，比最强基线高40.3个百分点；最终恶意技能SkillScan检测率为0，且良性任务准确率仅平均下降0.15个百分点，部分模型甚至有所提升；消融实验显示双阶段闭环比单阶段扫描的攻击成功率高12.05%，比单阶段运行时迭代的检测率低79.92%。

### 核心结论
单独评估预执行或运行时任意一个阶段的防御能力，都会遗漏实际存在的攻击风险，必须联合评估两层防御的协同效果
