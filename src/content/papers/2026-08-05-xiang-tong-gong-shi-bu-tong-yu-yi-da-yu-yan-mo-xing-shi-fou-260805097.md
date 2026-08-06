---
title: 'Same Formulas, Different Semantics: Do Language Models Follow Modal Logic
  Specifications?'
title_zh: 相同公式不同语义：大语言模型是否遵守模态逻辑规范？
authors:
- Réemi Andrieu
- Damien Sileo
affiliations:
- Univ. Lille
- Inria
- CNRS
- Centrale Lille
- CRIStAL
arxiv_id: '2608.05097'
url: https://arxiv.org/abs/2608.05097
pdf_url: https://arxiv.org/pdf/2608.05097
published: '2026-08-05'
collected: '2026-08-06'
category: Reasoning
direction: LLM 模态逻辑语义遵从性评估
tags:
- Modal Logic
- LLM Reasoning
- Reasoning Evaluation
- Semantic Compliance
- Contrastive Evaluation
one_liner: 构建语义可变的配对模态逻辑推理基准，验证推理模式可大幅提升LLM对指定语义的遵从度
practical_value: '- 做Agent决策/规则类业务校验时，可复用本文对照测试范式：固定逻辑形式仅切换约束条件，验证模型是否遵从输入约束而非用默认逻辑，避免合规、权限类场景出错

  - 电商导购、广告审核等需自定义规则的Agent场景，可强制开启高推理模式提升规则遵从度，本文验证开启后DeepSeek V4 Flash准确率从4.4%提升至88.1%

  - 规则类prompt优化可参考：优先明确写出关系定义而非仅用规则名称，不同模型对规则表示（自然语言/形式化语法）敏感度差异大，需针对性做适配测试'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM逻辑推理评估普遍默认固定语义体系，无法验证模型是否严格遵从显式指定的语义约束。而模态逻辑的推理有效性高度依赖框架、域等前置假设，在法律合规、多智能体权限管控、规则类业务决策等场景下，模型若忽略显式约束误用默认逻辑，会造成严重业务风险。

### 方法关键点
- 构造配对模态推理问题：固定前提和猜想内容，仅切换1项框架约束（如对称性/传递性）或域约束（如对象不可消失/不可新增），通过自动定理证明器给两个变体标注相反标签，避免问题形式本身泄露答案
- 构建平衡核心数据集：每个约束条件与正负标签的出现概率均等，仅靠记忆约束与标签的对应关系最多只能达到50%准确率，必须同时结合公式和约束才能获得更高分
- 采用严格配对准确率作为核心指标：要求同一配对问题的两个变体都答对才算正确，排除随机蒙对的情况

### 关键结果
在160条平衡核心数据集上测试5款主流LLM，直接prompt下4款模型准确率低于50%的条件仅用基线，仅Claude Sonnet 5达到65%；开启高推理模式后，DeepSeek V4 Flash的准确率从4.4%飙升至88.1%，GPT-5.6 Luna的框架类问题准确率从18.2%提升至63.7%。

**最值得记住的结论**：固定语义的推理基准会显著高估模型的鲁棒性，涉及规则约束的业务场景下，开启推理模式远比对prompt做表面优化更能提升模型对显式规范的遵从度。
