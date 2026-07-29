---
title: Localized Adaptation Reveals Distinct Learning Signatures in Transformers
title_zh: Transformer分层局部适配呈现差异化学习特征
authors:
- Rebecca Ramnauth
- Brian Scassellati
affiliations:
- Yale University
arxiv_id: '2607.25663'
url: https://arxiv.org/abs/2607.25663
pdf_url: https://arxiv.org/pdf/2607.25663
published: '2026-07-28'
collected: '2026-07-29'
category: Training
direction: 大模型参数高效微调 · LoRA层选择
tags:
- LoRA
- Parameter-Efficient Fine-Tuning
- Transformer
- Model Adaptation
- Model Editing
one_liner: 揭示五类学习目标的分层LoRA适配规律，可控平衡适配的获取、泛化与边界性
practical_value: '- 业务LoRA微调可按目标类型选适配层：新增商品/行业术语（词汇绑定）选早期层，更新商品/商家事实信息选晚期层，优化推荐/客服策略规则选中层，平衡效果、泛化能力与规则边界性

  - 对适配溢出容忍度低的场景（如电商合规话术、Agent安全规则适配），优先用局部层LoRA替代全栈微调，大幅降低对原有能力的干扰，同时提升适配的边界性避免误触发

  - 做新任务适配前可先执行小规模分层LoRA sweep，快速定位最优适配层组合，无需盲目全栈微调，既节省训练成本，又能针对性优化适配的核心指标'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Transformer适配普遍采用全栈更新模式，即使是窄范围的目标调整也会分布在全模型深度，容易导致新更新与原有能力纠缠，无法可控平衡适配的三大核心诉求：目标行为获取、跨场景泛化、适用场景边界性，且不同学习目标的最优适配位置缺乏系统性落地指导。
### 方法关键点
- 构建覆盖5类典型学习目标的可控评测基准：词汇绑定、事实关联、行为策略、因果映射、流程推理，每类目标分别从三个维度评测：获取（分布内+paraphrase准确率）、泛化（跨场景迁移准确率）、边界性（负例下不触发准确率）
- 控制变量实验设计：以Llama-3.1-8B为base模型，分别在早期、中期、后期层和全栈部署相同单层rank的LoRA，预先校准每类目标的最优训练样本量消除任务难度干扰，补充参数匹配对照、跨5类主流开源模型验证规律鲁棒性
### 关键结果数字
- 词汇绑定：早期层适配获取率97.2%接近全栈的99.7%，边界性比全栈高28.3pp，但泛化比全栈低44.3pp
- 事实关联：局部适配中晚期层最优，获取率52.1%、泛化率63.1%，比早期层高19.7pp、42.7pp，边界性比全栈高23.8pp
- 行为策略：晚期层负责动作获取（比中层高5.1pp），中层负责策略边界控制（比晚期层高21.6pp），两类能力可解耦适配
- 因果、流程推理：局部适配中中层最优，泛化率比早期层高12.9pp、28.7pp，三类指标平衡最优
- 核心规律在5类主流开源模型上方向一致性达80%以上，目标类型解释25%的适配效果差异，模型架构解释34%
### 核心结论
适配层位置是控制大模型学习内容、泛化范围、边界性的核心设计变量，而非无关的工程实现细节
