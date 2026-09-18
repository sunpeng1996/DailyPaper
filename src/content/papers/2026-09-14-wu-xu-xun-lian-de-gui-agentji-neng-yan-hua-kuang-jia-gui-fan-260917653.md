---
title: 'Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents'
title_zh: 无需训练的GUI Agent技能演化框架EvoSkill-GUI：反思-修订-复用循环
authors:
- Bofan Chen
- Boxuan Zhang
- Fei Tang
- Zhengxi Lu
- Yong Du
- Tongbo Chen
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
- University of Electronic Science and Technology of China
arxiv_id: '2609.17653'
url: https://arxiv.org/abs/2609.17653
pdf_url: https://arxiv.org/pdf/2609.17653
published: '2026-09-14'
collected: '2026-09-18'
category: Agent
direction: Agent 技能自演化优化
tags:
- GUI Agent
- Skill Evolution
- Training-free
- Self-evolution
- Skill Reuse
one_liner: 提出训练无关的EvoSkill-GUI框架，通过结构化技能包和自演化循环提升GUI Agent执行成功率
practical_value: '- 可将业务Agent的操作技能从单文本prompt改造为结构化多文件包，拆分元数据、执行计划、兜底策略、故障恢复规则，定向迭代无需重写全量prompt，适配电商商家后台自动化、广告投放操作等Agent场景

  - 复用同一backbone做信息隔离的故障诊断，无需额外部署大模型即可从失败轨迹生成修订方案，大幅降低Agent自演化的部署成本，适合低算力预算的业务场景

  - 技能召回可放弃全文匹配，改用结构化元数据（意图、适用场景、平台）加权检索，准确率从8%提升至100%，可直接迁移到Agent技能库的召回模块

  - 业务场景下控制技能迭代在3轮以内即可平衡效果与成本，额外迭代的收益不足1%，避免无意义的多轮推理消耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent的技能多为静态单文本，遇到弹窗、控件移位、加载延迟等动态界面时极易失效；且技能无法从执行失败中迭代，要么需重新训练，要么依赖外部反思模块成本高、耦合弱，失败经验无法沉淀为可复用资产。

### 方法关键点
- 结构化技能包设计：每个技能拆分为检索元数据、执行计划、兜底定位策略、故障恢复规则、accessibility工具、失败案例多个独立文件，通过受限工具接口仅可修改对应模块，避免全局篡改
- 反思-修订-复用三环逻辑：执行阶段支持即时修正局部适配问题，失败后用同一backbone做信息隔离的诊断（仅可见执行轨迹与指令，无法获取原技能与执行思考，避免路径依赖），再定向修改对应技能文件，验证通过后存入技能库
- 元数据检索机制：基于意图、适用APP、平台、关键词等元数据加权召回，避免全文匹配的语义错配问题

### 关键结果
在MobileWorld、AndroidWorld、OSWorld三个跨平台GUI基准上，无需任何训练即可给所有基线模型带来稳定提升，最大涨幅分别为+16.2%、+6.0%、+10.5%；结构化技能包比单文件技能成功率高2.85%，元数据检索准确率100% vs 全文匹配的8%，3轮迭代后效果基本饱和，在相同token消耗下比pass@3基线高6.7个百分点。

最值得记住的结论：无需训练也无需额外部署大模型，只要给Agent做结构化技能拆分和信息隔离的自诊断，就能靠执行反馈持续提升任务成功率。
