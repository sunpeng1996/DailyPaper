---
title: 'EfficientSkill: Learning Skills for Token-Efficient Multi-Turn Agents'
title_zh: EfficientSkill：面向多轮Agent的Token高效技能学习框架
authors:
- Deep Shah
- Sanket Badhe
- Nehal Kathrotia
- Priyanka Tiwari
affiliations:
- Google LLC
- Purdue University
arxiv_id: '2611.19823'
url: https://arxiv.org/abs/2611.19823
pdf_url: https://arxiv.org/pdf/2611.19823
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: 多轮Agent · Token效率优化
tags:
- Agent
- Multi-Turn Agent
- Token Efficiency
- Prompt Optimization
- Skill Learning
one_liner: 提出两阶段技能优化框架，先保障准确率再做精度约束压缩，降低多轮Agent Token消耗同时提精度
practical_value: '- 先跑通再优化：搭建业务Agent时，先放开Token约束完成准确率达标，再用≥90%基线精度的约束做Prompt剪枝，避免早期成本约束压制任务探索效果

  - 通用逻辑剥离：把Agent常用的校验、计算、接口调用逻辑封装成工作区工具函数，无需在Prompt里重复写代码片段，既降输入Token又减少执行错误

  - Token约束做正则：给多轮Agent加输出Token上限，可减少无效循环、冗余推理步骤，不仅降推理成本，还能缓解多轮漂移问题，甚至提升离线准确率

  - 按基座适配优化：不同基座的Agent输出习惯、错误模式差异大，切换基座时重新跑带精度约束的剪枝流程，成本和精度收益更显著'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多轮Agent技能优化仅关注准确率，反复针对边缘 case 打补丁会导致Prompt臃肿、Token开销随轮次指数上涨，还容易让Agent陷入无效重试、多轮漂移问题；若一开始就增加Token约束，又会压制对陌生任务的探索，导致准确率无法收敛。此前的静态Prompt压缩方案仅能减少输入Token，无法缩短Agent运行时的推理、动作输出Token，解决不了核心成本问题。

### 方法关键点
- 两阶段优化：Phase1 无Token约束，仅修复失败调优技能准确率，得到达标基线技能A*；Phase2 从A*热启动，在≥0.9*A*准确率的硬约束下做剪枝，目标最小化输出Token。
- 技能拆分表示：将技能拆分为Prompt内的自然语言指令I、工作区可执行工具函数T两部分，重复使用的代码逻辑移到T，完全不占用Prompt Token，仅在I中保留函数调用签名。
- 剪枝规则：验证集准确率达标前提下，输出Token下降≥5%或帕累托更优则更新技能，同时强制校验工具函数语法合法性。

### 关键实验
在MATH-500、ALFWORLD、SPREADSHEETBENCH三个基准，覆盖4款不同量级模型对比基线EVOSKILL：12组配置中11组输出Token下降，最高降幅80%；所有基准平均准确率均提升，其中SPREADSHEETBENCH上Gemini 3.8 Flash、Grok 4.1 Fast准确率分别上涨14.3、17.5个百分点；全场景服务成本下降，无KV缓存时降幅25%~67%，开全前缀KV缓存时降幅31%~75%。

### 核心结论
先学会把事做对，再学会把事做省，优化Token效率不会牺牲准确率，反而可作为正则提升技能泛化性。
