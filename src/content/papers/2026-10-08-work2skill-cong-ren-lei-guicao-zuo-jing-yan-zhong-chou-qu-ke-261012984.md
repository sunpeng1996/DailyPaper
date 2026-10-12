---
title: 'Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction'
title_zh: Work2Skill：从人类GUI操作经验中抽取可复用Agent技能
authors:
- Yuqi Huang
- Hui Li
- Yifei Cao
- Zikun Cai
- Tianci Xie
- Yangfan Gao
- Pinxue Guo
- Chaoyun Zhang
- Bingxuan Li
- Rui Zheng
affiliations:
- 上海交通大学
- 复旦大学
- 南洋理工大学
- 浙江大学
- 上海启智之峰有限公司
arxiv_id: '2610.12984'
url: https://arxiv.org/abs/2610.12984
pdf_url: https://arxiv.org/pdf/2610.12984
published: '2026-10-08'
collected: '2026-10-12'
category: Agent
direction: Agent 可复用GUI技能抽取优化
tags:
- GUI Agent
- Skill Induction
- Multimodal Alignment
- Human Demonstration
- Agentic Workflow
one_liner: 提出多模态对齐的GUI操作采集框架与主动式技能诱导方法，提升GUI Agent任务成功率与泛用性
practical_value: '- 电商运营/客服自动化Agent开发中，可复用WorkRecorder的多模态对齐思路，同步采集员工操作录屏、键鼠事件、前端DOM数据（对应论文AX树），避免纯视觉解析GUI的歧义，低成本沉淀标准化操作SOP

  - 技能抽取环节可借鉴主动式证据探查设计：无需强制一次性加载全量操作记录，让Agent根据当前技能草稿的缺失信息主动回溯对应时段的录屏/事件/DOM数据，既降低context压力，又提升技能的泛用性

  - 生成可复用技能时，要求明确保留步骤依赖、完成校验规则、异常处理逻辑，而非仅输出线性操作序列，可直接迁移到电商退货、退款、改地址等高频标准化场景的Agent开发'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent难以处理需要领域隐含知识的工作流（如企业内部报销、电商后台运营操作），无法从模糊用户指令中获取未明示的操作规则；人类GUI操作演示是最直接的经验来源，但现有方案要么依赖纯视觉解析歧义高，要么固定流程抽取易丢失上下文，生成的技能可复用性差。

### 方法关键点
- WorkRecorder采集工具：同步对齐录屏、键鼠事件、可访问性树（AX）三类数据，为操作语义解析提供结构化+多模态证据，解决纯视觉解析的歧义问题
- WorkDemo-350数据集：包含350条经过成功校验的桌面GUI操作演示，覆盖64个MyPCBench任务、286个OSWorld任务，所有数据带时间戳对齐，为技能诱导提供统一基准
- 主动式技能诱导流程：Agent交替执行证据探查、技能编写、迭代修订，按需调取对应时段的多模态数据，无需一次性加载全量记录，最终输出包含操作规则、步骤依赖、完成校验的可复用技能

### 关键实验
跨4个主流执行模型（GPT-5.5、Opus-4.8、Qwen3.5-35B、Qwen3.5-9B）测试，对比No Skill、ShowUI-Aloha、Demo2Tutorial基线：相对No Skill，MyPCBench任务得分提升4.67~10.54分，OSWorld任务得分提升3.11~7.50分；技能可直接迁移到同应用的参数修改类任务，相对基线仍有3.93~8.64分的得分提升，同时支持跨执行模型复用。

### 核心结论
从人类操作演示中抽取可复用技能时，多模态证据对齐+按需主动探查的效果远优于固定流程的纯文本/纯视觉抽取方案，生成的技能可跨任务、跨模型复用
