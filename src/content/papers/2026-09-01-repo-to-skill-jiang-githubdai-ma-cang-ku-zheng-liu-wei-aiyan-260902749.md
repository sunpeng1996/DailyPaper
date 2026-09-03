---
title: 'Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills'
title_zh: Repo-To-Skill：将GitHub代码仓库蒸馏为AI研究Agent可复用技能
authors:
- Jianlyu Chen
- Yuyang Hu
- Hongjin Qian
- Jiawei Liu
- Wenqing Wei
- Xiaolong Chen
- Defu Lian
- Zhicheng Dou
- Chaozhuo Li
- Qiwei Ye
affiliations:
- Beijing Academy of Artificial Intelligence
- University of Science and Technology of China
- Renmin University of China
- Hong Kong Polytechnic University
arxiv_id: '2609.02749'
url: https://arxiv.org/abs/2609.02749
pdf_url: https://arxiv.org/pdf/2609.02749
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: Agent 技能蒸馏与复用优化
tags:
- Agent Skill
- Skill Distillation
- ML Research Agent
- Operational Knowledge
- Knowledge Distillation
one_liner: 提出双模式技能蒸馏的DisCo Agent，构建5000+验证技能的AREX库，提升ML研究Agent性能
practical_value: '- 可直接复用双模式技能蒸馏架构：离线预蒸馏业务常用工具库/算法repo为通用技能，任务触发时蒸馏定制化技能，大幅降低Agent重复试错成本，例如电商推荐Agent常用的召回/排序算法库、A/B测试工具可提前蒸馏，无需每次任务都摸索API用法

  - 技能三层结构+渐进式披露设计可直接落地：既避免全量技能占用过多上下文窗口，又保障技能可直接执行，可解决业务Agent调用工具、执行复杂流程不稳定的问题

  - 技能入库强制验证机制可复用：所有技能必须经过用例验证、错误修复后才能入库，避免错误知识误导Agent，例如推荐业务的特征工程、模型训练技能可提前用小流量数据验证，减少线上故障风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自主ML研究Agent仅依赖LLM backbone与编排harness，缺失领域操作知识层，只能通过试错探索完成任务，大量浪费执行预算，且跨任务无法复用经验；公开论文、代码库等知识面向人类编写，体量过大无法直接作为上下文加载，需转化为Agent可直接调用的紧凑、可验证技能形式。
### 方法关键点
- 提出DisCo技能驱动的研究Agent，支持两种互补蒸馏模式：任务无关蒸馏提前批量处理通用代码库/论文生成长期可复用技能，任务导向蒸馏按需为特定任务生成定制技能
- 技能采用三层结构：`SKILL.md`作为知识接口说明适用场景、使用流程，`references/`为按需加载的参考资料，`scripts/`为可直接调用的执行脚本；单来源技能组织为技能图，支持渐进式披露减少上下文占用
- 所有技能入库前必须经过多轮验证修复，附带验证记录与未解决缺口说明；构建的AREX-Skill库从1000个热门ML repo蒸馏出5000+验证技能，按20个领域178个能力族分类，通过路由供Agent按需调用
### 关键实验结果
固定GPT-5.5 backbone、Codex harness与执行预算不变，仅对比有无技能的Agent性能：MLE-bench得分提升134.3%，PaperBench提升34.4%，FrontierCS提升9.2%，PassNet提升14.0%，高难度任务下增益更显著。
### 核心结论
Agent的harness决定「怎么执行任务」，而蒸馏得到的操作知识层决定「执行任务时知道什么」，不改变模型和编排的前提下，可复用的验证技能就能带来大幅性能提升。
