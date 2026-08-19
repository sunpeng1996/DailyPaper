---
title: 'Demystifying Agent Skills: Why They Work-Until They Don''t'
title_zh: 拆解Agent技能机制：生效逻辑与失效边界研究
authors:
- Zhiyuan Jiang
- Fangrui Huang
- Hanwen Xing
- Xander Wu
- Yipeng Gao
- Rui Cao
- Mengdi Wang
- Shilong Liu
- Yijiang Li
affiliations:
- Princeton University
- UC San Diego
- Stanford University
- University of Southern California
- Johns Hopkins University
arxiv_id: '2608.14036'
url: https://arxiv.org/abs/2608.14036
pdf_url: https://arxiv.org/pdf/2608.14036
published: '2026-08-13'
collected: '2026-08-19'
category: Agent
direction: Agent 技能机制与效能评估
tags:
- Agent
- Skill
- Procedural Memory
- Retrieval
- Evaluation
one_liner: 通过受控对比实验拆解Agent技能的生效逻辑与失效边界，明确其核心价值为流程锚定
practical_value: '- 搭建Agent技能库时优先沉淀流程类操作（如促销活动配置、投放参数校验流程）而非零散事实知识，技能核心价值是降低执行层错误，而非补全信息差

  - 技能检索环节不需要过度追求召回ground-truth的精度，相关技能的组合使用也可支撑任务完成，可降低检索模块设计压力，优先保障覆盖度而非精确匹配

  - 技能蒸馏时必须保留轨迹的成功/失败标注，引入失败轨迹时若无标注会大幅降低技能效果，可复用论文的对比蒸馏方法从执行日志中批量提炼有效技能

  - 技能库规模超过20后检索精度会大幅下降，电商场景可按业务域（如直播运营、广告投放、客服售后）分库存储，避免跨域干扰降低检索准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能的评估仅关注整体任务成功率，无法解释技能什么时候有用、为什么生效、哪里会失效，导致技能设计依赖启发式迭代，缺乏系统化指导，难以落地到复杂业务场景。

### 方法关键点
- 设计控制变量对比实验，固定源轨迹分别蒸馏为Workflow Memory和标准化Skill，对比不同表征形式的效果差异
- 对8135条实验记录做标准化处理，对240条采样轨迹做开放式编码，构建包含3大类12种模式的技能使用分类体系
- 从表征、结果标注、跨框架鲁棒性、检索难度四个维度，拆分技能生效全链路的影响因素

### 关键结果
在Terminal-Bench、SkillsBench两个基准上测试，对比Raw、Workflow Memory、Skill三组基线：
- 技能比Workflow Memory的匹配对比成功率高6.06个百分点
- 65.7%的技能生效来自procedural anchoring，仅4.5%来自explicit knowledge injection
- 技能库规模从5扩容到100时，实际使用精度从29.6%降到3.3%，但下游任务成功率基本稳定

### 核心结论
技能的核心价值是作为流程锚定稳定Agent执行动作，而非注入缺失的事实知识，精确召回ground-truth技能既不充分也不必要。
