---
title: 'DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration'
title_zh: DataMagic：基于声明式多智能体编排的自动化数据视频生成系统
authors:
- Yupeng Xie
- Zhenyang Wang
- Liangwei Wang
- Jiayi Zhu
- Zhouan Shen
- Yuyu Luo
affiliations:
- 香港科技大学（广州）
arxiv_id: '2609.33403'
url: https://arxiv.org/abs/2609.33403
pdf_url: https://arxiv.org/pdf/2609.33403
published: '2026-09-26'
collected: '2026-10-02'
category: MultiAgent
direction: 多智能体协作 · 声明式中间表示设计
tags:
- MultiAgent
- DeclarativeSpecification
- Orchestration
- LLM4Workflow
- InteractiveSystem
one_liner: 提出声明式中间表示+生成后编排多智能体 pipeline，端到端生成高准确率数据视频
practical_value: '- 「生成-编排」两阶段多智能体架构可直接复用：先并行生成多维度候选物料，再全局选排优化整体逻辑，解决顺序生成的逻辑断层、内容冗余问题，适合电商营销文案/商品短视频/数据看板报告等多片段内容生成场景

  - 声明式中间表示设计思路可迁移：将跨模态内容（文本/视觉/动画/音频）的依赖关系、触发逻辑用语义绑定而非硬编码ID/时间戳，大幅降低多模态内容生成的同步错误率，适合电商带货短视频的口播、画面、高亮动效自动对齐场景

  - 分角色任务拆解+模块化设计支持人工在环局部修改，无需全量重生成，匹配业务侧对AIGC内容可控可编辑的落地需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
数据视频是融合动态图表、语音旁白、同步动画的高效数据叙事载体，在电商业务复盘、营销报告、用户增长分析等场景应用广泛，但传统生产需要跨领域专业能力，周期长成本高；现有工具要么只能生成静态图表、无法处理多场景叙事，要么端到端生成存在数据幻觉、音画不同步问题，无法同时保障数据准确性、叙事连贯性和全流程自动化。

### 方法关键点
- 设计声明式中间表示 **DVSPEC**：以场景为核心单元组织视频内容，通过数据驱动的语义引用绑定视觉元素与底层数据，用旁白索引触发替代绝对时间戳，自动实现音画同步，保障数据可溯源
- 提出「Generate-then-Orchestrate」两阶段多智能体策略：第一阶段并行生成覆盖多分析维度的候选场景池；第二阶段全局选择符合查询需求的场景并排序，基于上下文生成连贯旁白，绑定旁白提到的数据实体与对应高亮动画，实现全局叙事连贯
- 支持画布操作、脚本编辑、自然语言命令三种交互模式，仅局部修改对应DVSPEC字段即可更新内容，无需全量重生成

### 关键结果
在109个真实业务样本上测试，对比GPT-5等SOTA大模型端到端生成方案，基于Claude-Sonnet-4的DataMagic将生成成功率从48.62%~86.24%提升至98.17%，视频质量评分从2.13/5提升至3.89/5（+83%），其中动画、叙事维度提升最显著；用户研究显示相比直接调用大模型的工作流，任务耗时降低79.7%，认知负荷大幅下降。

> 最值得记住的结论：端到端跨模态生成的核心瓶颈不在单模型能力，而在于合理的中间表示设计与任务拆解编排，用结构化约束替代大模型黑盒生成可同时提升准确率、可控性和鲁棒性。
