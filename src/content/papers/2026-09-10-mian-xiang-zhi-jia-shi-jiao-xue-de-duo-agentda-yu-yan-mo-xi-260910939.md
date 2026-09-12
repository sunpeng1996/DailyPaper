---
title: Evaluating Scaffolding-Oriented Multi-Agent Large Language Model System for
  Clinical Interview Training
title_zh: 面向支架式教学的多Agent大语言模型系统临床问诊训练效果评估
authors:
- Luming Yang
- Haoxian Liu
- Siqing Li
- Rong Jia
- Yue Xiao
- Guanhua Chen
- Li Lu
affiliations:
- The Ohio State University
- The Hong Kong University of Science and Technology
- Southern University of Science and Technology
- Johns Hopkins University
- Guangzhou Medical University
arxiv_id: '2609.10939'
url: https://arxiv.org/abs/2609.10939
pdf_url: https://arxiv.org/pdf/2609.10939
published: '2026-09-10'
collected: '2026-09-12'
category: MultiAgent
direction: 多Agent协作 · 教学场景模拟训练系统
tags:
- MultiAgent
- LLM
- AgentCollaboration
- EducationalApplication
- Evaluation
one_liner: 提出三角色多Agent临床问诊训练平台，验证其可提升医学生沟通共情等实操能力
practical_value: '- 多Agent分角色分工架构可直接复用：可迁移搭建电商客服/直播销售话术训练平台，分别设置用户模拟Agent、导师Agent、评估Agent，大幅降低人工带教成本

  - Agent输出约束规则可借鉴：导师Agent仅输出引导提示、不直接给出标准答案，评估Agent仅反馈过程问题、不透露总分的设计，可用于AI导购、推荐话术的实时反馈场景，避免使用者过度依赖标准答案

  - 多Agent系统效果评估方法可复用：采用无Agent干预的纯场景考核衡量最终收益，排除AI辅助带来的效果虚高，可用于评估智能推荐话术、Agent客服的实际业务价值'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统临床标准化病人（SP）训练资源消耗高、难规模化，单一案例式学习无法还原实时问诊的沟通要求，难以训练医学生在不确定性下的安全连贯问诊能力。
### 方法关键点
设计支架式教学导向的三角色多Agent AI-SP训练平台：
1. 患者Agent负责模拟真实患者对话交互
2. 导师Agent输出苏格拉底式引导提示，不直接泄露诊断信息
3. 轮次级评估Agent实时监控问诊进度，不提前披露最终总分
### 关键结果数字
100名医学生的随机对照实验显示：相较于结构化信息披露对照组，多Agent组最终考核得分更高，其中沟通能力、共情表达、病史采集行为的提升最显著，两组最终诊断准确率无统计学差异。同时公开了多专家标注的问诊转录、过程评估、OSCE评分数据集。
