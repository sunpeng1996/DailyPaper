---
title: Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation
title_zh: 基于跨执行环境适配的检索增强Agent技能优化框架
authors:
- Jaewon Chu
- Ji Soo Lee
- Jihwan Park
- Dohwan Ko
- Jeehye Na
- Seunghun Lee
- Taehoon Lee
- Minseo Yoon
- Minseok Joo
- Yunyang Xiong
affiliations:
- Korea University
- KAIST
- Meta AI
arxiv_id: '2609.38024'
url: https://arxiv.org/abs/2609.38024
pdf_url: https://arxiv.org/pdf/2609.38024
published: '2026-09-28'
collected: '2026-10-02'
category: Agent
direction: Agent技能优化 · 检索增强+跨环境适配
tags:
- Agent Skill
- RAG
- Cross-Harness Adaptation
- Skill Retrieval
- Prompt Optimization
one_liner: 提出检索增强Agent技能优化框架RASO，结合跨环境适配复用外部技能库知识降本提效
practical_value: '- 技能库复用场景可引入分段检索+跨环境适配机制：不要直接复用外部prompt/技能，先做细粒度段级检索，再通过LLM把外部知识改写为符合当前业务（如电商导购、搜索Agent）工具链、规则的可执行步骤，避免引入不兼容逻辑

  - Agent冷启动阶段可参考RASI思路：无需先跑大量业务rollout，基于任务描述+现有公开技能库做检索适配，生成初始技能，大幅降低冷启动成本，实测比直接LLM生成初始技能平均提升5%+效果

  - 技能迭代优化阶段可接入RASU流程：每次Agent执行失败后，先基于错误日志生成检索query，从外部技能库找对应解决方案，适配后更新现有技能，比仅靠自身反馈迭代效率提升明显

  - 检索参数可参考实验结论：单query取Top5检索段的性价比最高，超过5容易引入噪声；哪怕只用1%的外部技能库也能拿到明显效果，小体量业务也可快速落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能优化完全依赖自身rollout迭代，成本极高，且完全浪费了公开平台上已有的数百万跨领域、跨执行环境的技能知识；直接检索复用外部技能又会遇到执行环境（harness）不匹配、领域不兼容的问题，反而可能降低效果，SpreadsheetBench场景下92.9%的检索到的技能都来自不同执行环境，直接复用完全不可行。

### 方法关键点
- 两阶段RASO框架：包含无需rollout的检索增强技能初始化（RASI）、基于执行反馈的检索增强技能更新（RASU）两个模块
- 核心设计Cross-Harness Adaptation：对检索到的段级技能片段，剥离源领域、源环境的特定逻辑，重写为符合目标任务、目标执行环境的可执行Lesson，避免不兼容问题
- 流程设计：RASI基于任务+环境描述生成检索query，检索适配后直接生成初始技能；RASU基于失败rollout的文本梯度生成query，检索适配后迭代更新技能，仅接受验证集效果提升的更新

### 关键结果
在OfficeQA、SpreadsheetBench、ALFWorld、WebShop四个Agent基准，GPT-5.6-Luna、Qwen-3.5-9B两个模型上验证：
- RASI初始技能比LLM直接生成的初始技能最高提升10.73pp（WebShop+Qwen-3.5-9B），无需任何rollout
- 完整RASO框架比当前最优SkillOpt基线最高提升11.30pp（WebShop+Qwen-3.5-9B），且API成本更低、rollout数更少
- 消融实验显示：Cross-Harness Adaptation可带来最高7.74pp的效果提升，Top5检索段性价比最高，仅用1%的外部技能库即可拿到明显增益

**最值得记住的一句话**：外部公开技能库是Agent技能优化的低成本增量增益来源，只要做好跨环境适配，哪怕是完全不同领域的技能也能迁移到目标任务带来效果提升。
