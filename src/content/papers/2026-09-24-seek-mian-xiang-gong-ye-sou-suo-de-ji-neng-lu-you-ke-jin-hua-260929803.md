---
title: 'SEEK: Skill-Routed Evaluation with Evolvable Knowledge for Industrial Search'
title_zh: SEEK：面向工业搜索的技能路由可进化知识评价框架
authors:
- Zhongxin Huang
- Songyang Li
- Renzhe Zhou
- Feiran Zhu
- Chenglei Dai
- Zhen Xiao
- Xuanping Li
- Jingwei Zhuo
affiliations:
- Peking University
- Kuaishou Technology
arxiv_id: '2609.29803'
url: https://arxiv.org/abs/2609.29803
pdf_url: https://arxiv.org/pdf/2609.29803
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: 搜索自动评价 · 技能路由
tags:
- LLM-as-a-Judge
- Search-Evaluation
- Skill-Routing
- Listwise-Evaluation
- Evolvable-Knowledge
one_liner: 提出技能-能力分离的页级搜索评价框架，无需重训模型即可快速迭代评价标准
practical_value: '- 搜索/推荐自动评价可复用「技能路由+外部化技能库」架构，把动态变化的评价规则（如电商合规、内容质量标准）做成结构化技能，无需频繁重训评价模型，大幅降低规则迭代成本

  - Listwise评价任务训练可借鉴「两阶段对齐策略」：先用强Teacher模型蒸馏结构化推理轨迹做SFT，再用分层奖励（任务级+技能诊断级+冲突惩罚）做RL对齐，显著提升小模型评价准确率

  - 评价规则迭代可复用「重播门控更新机制」：新规则上线前必须同时在新案例集、历史回放集验证，保证新增规则不退化历史效果，避免规则迭代的负向波动

  - 工业级大流量搜索评价可参考该部署方案：8B小模型+技能路由的架构，评价准确率超过多轮人工审核，还能实现40倍以上效率提升，适合大规模离线A/B实验的效果评估'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业搜索系统迭代高度依赖质量评价，传统人工评估成本高、周期长，无法覆盖长尾流量与高频迭代需求；现有LLM自动评价要么将全量规则塞进单Prompt导致上下文冗余、规则冲突，要么通过SFT把规则内化进模型，迭代规则就得重训，成本高周期长；且大多方法聚焦item级相关性，缺少页级整体质量评估与故障归因能力，无法满足工业场景多维度、动态迭代的评价需求。

### 方法关键点
- 采用能力-知识分离架构，将多维度评价规则外化为结构化技能库，每个技能包含路由描述（触发条件）和操作指引（评价规则、证据要求、归因逻辑）
- 轻量化技能路由为每个query-结果页对匹配3-4个相关技能，避免全量规则注入带来的干扰
- 两阶段训练对齐：先用大模型Teacher蒸馏结构化推理轨迹，监督训练路由和评估器；再用DAPO强化学习，基于分层奖励（页级标签准确率+技能诊断质量+逻辑一致性惩罚）对齐人类偏好
- 可进化技能库：将线上错误分为路由/技能/执行三类，仅针对重复出现的技能类错误做局部规则更新，经历史回放集验证不退化后上线，无需重训模型

### 关键实验
在快手16.9万条标注短视频搜索query-页面对数据集上，基于Qwen3-8B实现的SEEK，三分类页级评价Macro-F1达0.6555，比同参SFT+GRPO基线高1.37个点；权威、异质性维度归因召回分别提升8.59、7.21个点；线上部署后评价准确率达0.842，超过多轮人工审核的0.83，效率是外包人工的40.6倍；仅更新技能库即可获得与模型重训95%以上的适配收益，历史效果退化仅0.08%。

### 核心结论
工业场景的LLM自动评价系统，将动态易变的业务规则外化为可独立迭代的外部知识，比把规则内化进模型参数的方案，综合迭代效率、稳定性、成本优势更显著
