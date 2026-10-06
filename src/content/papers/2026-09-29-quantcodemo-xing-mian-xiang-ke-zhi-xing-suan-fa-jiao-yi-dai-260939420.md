---
title: 'QuantCode Model: Specializing Language Models for Executable Algorithmic Trading
  Code'
title_zh: QuantCode模型：面向可执行算法交易代码生成的专业化大语言模型
authors:
- Alexey Chernysh
- Orkhan Ekhtibarov
- Dmitry Zmitrovich
arxiv_id: '2609.39420'
url: https://arxiv.org/abs/2609.39420
pdf_url: https://arxiv.org/pdf/2609.39420
published: '2026-09-29'
collected: '2026-10-06'
category: LLM
direction: LLM领域微调 · 可执行代码生成
tags:
- LLM Fine-tuning
- Domain Adaptation
- Code Generation
- Agent Capability
- Catastrophic Forgetting
one_liner: 采用领域预训练与执行验证SFT优化算法交易代码生成，解决工具调用能力退化问题
practical_value: '- 做领域专用LLM（如电商运营话术生成、广告文案生成、推荐策略规则代码生成）时，可复用「领域语料继续预训练+经过真实执行/落地验证的SFT」两阶段范式，比单一微调的效果提升更显著，尤其是单轮生成的准确率。

  - 领域微调完成后必须新增原有核心能力的留存校验环节，比如工具调用格式合规性、通用指令跟随能力，避免出现领域能力提升但Agent交互核心能力退化的问题，该问题在电商导购Agent、推荐系统交互Agent开发中极易被忽略。

  - 若出现工具调用能力退化，简单的权重合并无法恢复时，可采用少量结构化工具调用轨迹做针对性SFT，可快速恢复格式合规性，但需注意下游复杂任务的效果可能出现折损，需额外做效果对齐。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用大模型的通用代码生成能力优异，但面向算法交易这类强领域、强框架依赖的可执行代码生成场景时，频繁出现语法正确但无法运行、逻辑与需求不符的问题；现有评估多聚焦文本相似度、编译通过率，缺乏执行层面的端到端校验，同时领域微调容易引发原有核心能力（如工具调用）的灾难性遗忘，缺乏系统性的训练与评估方案。

### 方法关键点
- 两阶段训练：第一阶段用5~6B Token的量化交易领域GitHub代码做继续预训练，学习框架API、领域编程范式；第二阶段用800条经过执行验证的「自然语言策略→可运行Backtrader代码」对做SFT，对齐用户需求到代码的映射。
- 多层级评估：除单轮代码生成的编译、回测、交易生成、语义对齐4级校验外，新增最多10轮的Agent交互式修复评估、类似SWE-bench的仓库级代码修改任务评估。
- 能力恢复方案：针对领域微调后工具调用格式退化问题，对比权重合并、工具调用轨迹SFT两种恢复方案的效果。

### 关键结果
基于QuantCode-Bench 400个交易策略生成任务测试：Qwen3.6-35B-A3B经过两阶段训练后，单轮语义对齐通过率（Judge Pass）从27.8%提升至58.2%，回测成功率从46.0%提升至83.5%；Agent评估中首轮通过率从22.3%提升至58.3%，10轮修复后最终通过率从47.5%提升至79.5%。
单独继续预训练会提升首轮通过率，但会降低多轮修复后的最终成功率（从47.5%降至32.5%），核心原因是指令跟随能力退化。针对性工具调用SFT可恢复工具调用格式合规性，但仓库级任务解决率比原基线低7.4个百分点。

> 最值得记住的结论：领域专用代码生成模型要以执行环境中的行为作为训练和评估的核心标准，而非仅看文本输出本身，同时必须配套核心能力留存校验避免遗忘。
