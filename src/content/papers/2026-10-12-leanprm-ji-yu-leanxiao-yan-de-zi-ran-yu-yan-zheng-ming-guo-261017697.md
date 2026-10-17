---
title: 'LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification'
title_zh: LeanPRM：基于Lean校验的自然语言证明过程监督框架
authors:
- Rodney Lafuente-Mercado
- Salman Rahman
- Jingyan Shen
- James Shiffer
- Saadia Gabriel
- Pavel Izmailov
affiliations:
- University of Texas at Austin
- University of California, Los Angeles
- New York University
arxiv_id: '2610.17697'
url: https://arxiv.org/abs/2610.17697
pdf_url: https://arxiv.org/pdf/2610.17697
published: '2026-10-12'
collected: '2026-10-17'
category: Reasoning
direction: 大模型推理 · 过程奖励模型自动标注
tags:
- Process Reward Model
- Lean
- Mathematical Reasoning
- Automated Annotation
- GRPO
one_liner: 基于Lean证明助手自动生成无人工标注步骤标签，训练的PRM性能超过人工标注的PRM800K
practical_value: '- 对于Agent推理链校验、推荐理由生成合规性校验等需要步骤级标注的场景，可复用「自动工具打标+过滤纯语法/格式错误」的低成本标注方案，替代高成本人工标注

  - 训练垂直场景奖励模型时，可借鉴其「步骤准确率+整体判定」的加权奖励设计，避免模型输出恒定标签的捷径行为

  - 对于无明确最终答案的开放生成任务（如长文案生成、复杂问题推理），可参考用形式化校验工具离线生成训练标签的思路，不依赖人工标注即可规模化扩量

  - 实验验证4B参数规模在这类校验任务上性价比最优，业务落地可优先尝试4B左右小模型微调垂直场景校验能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型已能生成高复杂度数学证明，但逐步骤校验成为落地瓶颈：传统过程奖励模型（PRM）训练依赖人工标注步骤级标签，成本极高；基于最终答案的自动标注方法不适用于无明确标准答案的开放证明任务；手动将自然语言证明转为形式化校验语言需要专家级投入，无法规模化。

### 方法关键点
- 两阶段无标注打标流程：第一阶段让模型盲写自然语言证明及对应Lean形式化步骤，全程不返回Lean校验反馈，保留模型真实推理错误；第二阶段用Lean校验形式化步骤，首个失败步骤前的所有步骤标为正确，失败步骤及后续所有步骤标为错误
- 噪音过滤机制：调用模型判断Lean报错属于数学错误还是纯语法错误，语法错误尝试一次修复后重校验，仅保留数学错误对应的负样本，剔除标签噪音
- 奖励设计：训练PRM时采用GRPO优化，奖励由70%步骤分类准确率+30%整体证明正确性判定组成，避免模型输出全对/全错的捷径答案
- 产出10634条带152K步骤级标签的无人工标注证明数据集，配套200条样本的LeanPRM-Bench基准测试集

### 关键实验
实验基于Qwen3系列模型训练，对比同配置下用人工标注的PRM800K训练的基线、初始基线模型、仅训练解题能力的基线：
- 4B参数模型在LeanPRM-Bench上步骤准确率达74.7%，较PRM800K基线高14.4个百分点，较初始模型高26.5个百分点；在4个外部测试集上3个性能领先
- 0.6B~8B全参数规模模型训练后效果均有提升，4B与8B模型性能接近，性价比最优
- Best-of-N选择场景下，LeanPRM训练的模型选对IMO级别证明的概率随N增大稳定提升，PRM800K基线效果接近随机选择

### 核心结论
形式化工具可离线生成无人工标注的高质量步骤级标签，训练出的PRM效果可超过同规模下基于人工标注训练的模型。
