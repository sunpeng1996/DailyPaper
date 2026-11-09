---
title: 'From LoRA to Language: Recovering Skill Documents from Adapters'
title_zh: 从LoRA适配器中逆向恢复Agent技能文档的技术研究
authors:
- Saranya Dintakurthy Swadha
- Pavan C Shekar
- Arpit Jain
- Aswanth Krishnan
affiliations:
- QpiAI, Bengaluru, India
arxiv_id: '2611.09454'
url: https://arxiv.org/abs/2611.09454
pdf_url: https://arxiv.org/pdf/2611.09454
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent技能 · LoRA逆向与跨模型迁移
tags:
- LoRA
- Agent Skills
- Adapter Interpretation
- Cross-model Transfer
- Instruction Recovery
one_liner: 提出两种LoRA逆向方案，可恢复39%-93%技能指令，支持跨模型迁移
practical_value: '- 电商Agent私有技能若用LoRA部署，可复用Executing Writer方案逆向为可审计文本，解决黑盒LoRA的合规审查、规则迭代需求，避免每次调整规则都重训LoRA

  - 跨模型迁移技能时无需重复训练LoRA，可将已训LoRA逆向为通用技能文档，直接适配无法加载LoRA的公有云API大模型，降低跨基座适配成本

  - 可复用「对比基座/适配模型行为差异生成规则」的思路，挖掘黑盒推荐排序、广告投放模型的隐式规则，输出可解释的运营优化规则

  - 业务训练用于存储技能的LoRA时优先选择rank≥32，兼顾存储成本、技能效果和可恢复率，rank64时恢复率接近上限'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Agent技能文档编译为LoRA后可大幅节省推理上下文、降低部署成本，但成为无法读取、编辑、审计、跨模型迁移的黑盒，现有LoRA解析方法仅能预测属性标签，无法还原完整可用的技能文档，无法满足业务合规、跨基座适配的需求。

### 方法关键点
- 按训练目标划分三类LoRA：文档拟合类（训练时以文档为输出目标）、行为拟合类（仅对齐技能带来的输出行为，无文档训练目标）、背诵类（触发后直接输出完整文档）
- 提出**Executing Writer**：在冻结的基座+目标LoRA上额外训练一个rank16的轻量Writer适配器，直接让适配后的模型输出技能文档
- 针对行为拟合类LoRA，提出无训练的执行Agent：对比基座与适配模型在任务实例上的行为差异，自动归纳生成技能文档

### 关键实验
测试集覆盖37个自建技能、41个SkillsBench公开技能、ALFWorld交互任务数据集，对比静态权重编码、关键词检索等基线方案：背诵类LoRA（rank64）的文档恢复率达90%-93%，文档拟合类可恢复39%-44%的关键指令，还原的文档可保留85%-91%的原技能任务收益；行为拟合类LoRA用执行Agent方案可恢复58%-71%的ALFWorld任务收益，生成的文档可直接跨模型迁移，将Llama-3.1-8B的任务准确率从5%提升至55%。

### 核心结论
仅通过静态权重解析LoRA仅能获取1bit左右的有效信息，运行LoRA观察行为是还原技能的核心有效路径。
