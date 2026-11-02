---
title: 'Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought'
title_zh: 分步查询：无需访问教师模型思维链的推理蒸馏方法
authors:
- Dicong Yu
- Wenhua Wang
- Tian Wang
affiliations:
- Institute of AI and Future Network, Beijing Normal University
arxiv_id: '2610.41769'
url: https://arxiv.org/abs/2610.41769
pdf_url: https://arxiv.org/pdf/2610.41769
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 大模型推理蒸馏 · 黑盒教师分步查询
tags:
- Reasoning Distillation
- Chain-of-Thought
- Black-box LLM
- Supervised Fine-Tuning
- Stepwise Query
one_liner: 通过黑盒大模型分步独立查询生成细粒度推理监督数据，高效蒸馏小模型推理能力
practical_value: '- 业务侧小模型推理能力蒸馏可复用分步查询协议：先让黑盒大模型输出简洁步骤，再针对每一步独立查询要求推导、校验、纠错，无需访问大模型内部CoT即可生成高质量SFT训练数据

  - 训练推理类小模型（如电商规则计算、推荐理由生成、客诉归因）时，无需完全过滤最终答案错误的样本，只要中间步骤有效仍可加入训练集，可提升泛化性

  - 可复用SEIG指标评估推理样本的局部价值，无需大模型logit，仅需文本和校验标签即可筛选高价值训练样本，降低标注/数据生成成本

  - 推理步骤拆解到合理粒度即可，递归拆分为子步骤收益极低，可避免浪费大模型调用成本，控制数据生成ROI'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
黑盒大模型推理蒸馏场景下，现有方案仅能获取教师模型的最终答案和简略解答，无法拿到完整中间推理轨迹，导致蒸馏监督信号质量差，小模型推理能力提升受限；已有推理补全方案容易出现事后合理化、遗漏边界情况的问题，无法支撑高质量蒸馏。

### 方法关键点
- 分步查询协议：先让黑盒教师输出问题候选答案和简略步骤列表，再针对每个步骤单独发起独立查询，提示词要求教师从原始问题独立推导该步骤、校验有效性、补全遗漏场景、纠正初始候选错误，每个查询共用初始上下文，不传递其他步骤的扩展结果
- 组装校验流程：将各步骤扩展结果按顺序拼接，校验一致性、完整性、有效性，修正初始答案错误后生成SFT样本，输入仅保留原始问题，输出为完整推理链+最终答案
- SEIG诊断指标：计算冻结小模型在分步解释和全局CoT解释下正确完成单步推理的概率对数比，无需教师模型logit或内部轨迹，即可量化单步推理监督信号的价值

### 关键结果
在2个黑盒教师（DeepSeek-V4-Pro、GLM-5.2）、2个学生模型（Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct）、4个基准（GSM8K、MATH-500、HumanEval、LiveCodeBench）的16组对比中，14组优于3个SOTA基线，相对未蒸馏基线最高提升16.3个百分点；验证了带有效中间步骤的错误答案样本可提升效果0.6~1.5个百分点，递归拆分子步骤收益可忽略。

最值得记住的结论：推理蒸馏的核心是中间步骤的局部有效性而非最终答案正确性，合理粒度的分步查询是低成本获取高质量推理监督信号的有效方案。
