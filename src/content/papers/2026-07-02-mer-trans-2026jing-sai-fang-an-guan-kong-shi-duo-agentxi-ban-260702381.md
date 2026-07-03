---
title: 'HULAT2 at MER-TRANS 2026: Governed Multi-Agent Simplification for Spanish
  Easy-to-Read Generation'
title_zh: MER-TRANS 2026竞赛方案：管控式多Agent西班牙语易读文本生成
authors:
- Lourdes Moreno
- Paloma Martínez
- Marco Antonio Sanchez-Escudero
- Miguel Domínguez-Gómez
affiliations:
- Universidad Carlos III de Madrid
arxiv_id: '2607.02381'
url: https://arxiv.org/abs/2607.02381
pdf_url: https://arxiv.org/pdf/2607.02381
published: '2026-07-02'
collected: '2026-07-03'
category: MultiAgent
direction: 多智体 · 可控文本生成
tags:
- Multi-Agent
- LangGraph
- Text Simplification
- LoRA
- ECA Routing
one_liner: 提出信号引导的LangGraph多Agent易读生成架构，SARI较线性基线提升14.39%
practical_value: '- 可复用LangGraph+ECA规则的多Agent路由架构：多模型并行生成差异化候选+多维度无参考质量信号打分+规则路由选优/合并/重试，适合电商商品文案简化、下沉市场/老年用户专属内容生成、合规文案易读化改造等场景

  - 垂直小语种业务优化参考：领域LoRA微调小模型搭配通用大模型并行生成，兼顾推理成本、领域适配性与生成质量，可直接迁移至跨境电商小语种商品详情页、营销文案生成场景

  - 生成质量管控参考：将语义保真、事实一致性等业务硬约束设为最高优先级拦截规则，可读性、词汇难度等设为可调软优化指标，可避免生成内容偏离业务核心要求

  - 领域词表落地校准提示：直接引入领域词汇替换/解释模块可能降低自动指标得分，需结合下游用户实际阅读体验、业务合规要求做权衡校准，不要盲目为加功能而加功能'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
易读文本生成是认知障碍人群、低识字率群体、非母语用户获取公共信息、商业内容的核心支撑，传统LLM生成易读文本常出现信息遗漏、事实篡改、术语使用不当等问题，现有BLEU、SARI等自动指标无法覆盖可读性、语义保真、事实一致性等多维度质量要求，亟需可控、可追溯的生成架构平衡易读性与信息准确性。

### 方法关键点
- 核心架构基于LangGraph实现有状态多Agent工作流，包含预分析、并行生成、候选评估、ECA规则路由、受控编辑、最终校验6个核心模块，全流程决策可追溯，无人工干预
- 并行生成设置3路差异化策略：Gemini 2.5 Flash生成优先保义的Plain Language候选、RigoChat-7B-v2生成优先句法拆分的简化候选、Gemini 2.5 Flash生成符合CEFR A2级要求的易读候选，覆盖不同简化力度
- 质量评估采用5类无参考内部信号：语义与事实保真（数字/日期/否定词保留校验）、可读性、句法清晰度、词汇简单度、生成鲁棒性，无需参考文本即可完成路由决策
- 基线方案采用LoRA微调的RigoChat-7B-v2单模型，搭配生成-评估-重试线性流程做对照

### 关键实验
在MER-TRANS 2026西班牙语易读生成赛道测试，对比3种方案：无词汇增强的多Agent方案(RUN1)、增加词汇Agent的多Agent方案(RUN2)、LoRA微调单模型基线(RUN3)。核心结果：RUN1 SARI达44.05，较RUN3提升5.54分（相对提升14.39%），在19支参赛队伍中排名第6；RUN2 SARI为43.10，略低于RUN1，说明直接引入词汇增强未提升参考类指标，需结合场景校准后使用。

### 核心结论
高源文本重叠度与高语义相似度不等于文本简化效果好，必须结合语义保真、可读性、句法简化等多维度信号做综合评估。
