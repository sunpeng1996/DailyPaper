---
title: Scalable Behaviour Cloning on Browser Using via Skill Distillation
title_zh: 基于技能蒸馏的可扩展浏览器行为克隆框架BrowserBC
authors:
- Kaisen Yang
- Zheng Jiang
- Yuzhao Peng
- Houde Qian
- Boshi Zhang
- Youjie Zheng
- Shijin Hong
- Qingle Liu
- Ruoyu Han
- Bohan Lyu
affiliations:
- Tsinghua University
- Einsia.AI
- Navers Lab
arxiv_id: '2606.32014'
url: https://arxiv.org/abs/2606.32014
pdf_url: https://arxiv.org/pdf/2606.32014
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 浏览器Agent · 行为克隆 技能蒸馏
tags:
- Browser Agent
- Behavior Cloning
- Skill Distillation
- Skill Library
- LLM Agent
one_liner: 将人类浏览器交互轨迹蒸馏为可复用自然语言技能库，大幅提升浏览器Agent任务成功率
practical_value: '- 轨迹转技能范式可迁移到电商导购Agent：将用户/运营的平台操作轨迹蒸馏为标准化技能卡，覆盖加购、下单、售后咨询等通用流程，大幅减少Agent试错成本

  - 技能蒸馏+大小模型解耦架构可降低业务部署成本：用大模型离线蒸馏通用技能，小模型在线检索技能执行，兼顾效果与推理成本

  - 技能图谱组织方式可复用：按依赖、特化关系构建技能图谱，避免冗余膨胀，提升检索准确率，适合多场景Agent的经验沉淀与复用

  - 电商复杂交互任务可直接复用技能卡设计：包含前置条件、执行步骤、终止判断、故障恢复的结构化技能卡，稳定性远优于纯prompt提示'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有浏览器Agent核心瓶颈并非底层操作能力，而是不完全信息下的决策能力：Agent仅能观测当前页面，对网站全局结构、可靠路径、终止信号缺乏先验，只能依赖试错探索效率极低；人类浏览器交互轨迹隐含大量决策先验，但原始轨迹噪声大、与页面状态强耦合，无法直接复用。

### 方法关键点
- 行为证据抽象：清洗原始轨迹，过滤无效操作，分段提取包含上下文、行为、反馈、结果的结构化证据单元，去除坐标、DOM选择器等非可迁移信息
- 技能蒸馏：将证据单元蒸馏为固定字段的结构化自然语言技能卡，包含意图、适用范围、前置条件、执行步骤、里程碑、终止信号、故障恢复等，仅保留通用流程知识
- 技能库构建：将候选技能合并、特化，组织为技能图谱，节点为技能，边编码依赖、特化等关系，避免技能冗余膨胀
- 技能条件执行：推理时通过语义匹配检索相关技能插入Agent上下文，Agent结合实时页面状态落地执行

### 关键实验
在三类基准测试：①自托管网站基准WebArena-Hard（258个任务），对比无技能基线成功率从60.5%提升到81.4%，绝对提升20.9个百分点，平均交互步骤减少27.3%；②真实生产网站基准ClawBench（152个任务），成功率从32.9%提升到68.4%，绝对提升35.5个百分点；③验证大小模型解耦效果：用Claude Sonnet蒸馏的技能可让小模型成功率达到77%，接近大模型基线的80%。

### 核心结论
浏览器Agent的可扩展性不来自人工设计的任务，而来自互联网用户已经沉淀的集体交互技能，蒸馏通用流程知识的泛化性远优于直接复现底层操作。
