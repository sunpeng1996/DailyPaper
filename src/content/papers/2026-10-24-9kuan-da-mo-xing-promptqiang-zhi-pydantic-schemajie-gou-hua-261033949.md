---
title: Why Does Structured Output Fail? An Empirical Study of Prompt-Enforced Pydantic
  Schemas Across Nine LLMs
title_zh: 9款大模型Prompt强制Pydantic Schema结构化输出失败原因实证研究
authors:
- Amit Verma
affiliations:
- Independent Researcher, Phoenix, AZ, USA
arxiv_id: '2610.33949'
url: https://arxiv.org/abs/2610.33949
pdf_url: https://arxiv.org/pdf/2610.33949
published: '2026-10-24'
collected: '2026-10-27'
category: LLM
direction: LLM结构化输出 · Pydantic校验失败分析
tags:
- Structured Output
- Pydantic Schema
- Failure Taxonomy
- Prompt Engineering
- LLM Validation
one_liner: 构建LLM结构化输出细粒度失败分类体系，给出prompt校验范式下4条工程实践指导
practical_value: '- 搭建LLM结构化输出管线时，先对返回结果做markdown fence剥离再校验，实测仅48%的带围栏JSON剥离后可通过校验，剩余隐藏的长度/格式违规需单独处理，能大幅降低重试成本，适用于Agent工具调用、推荐结果结构化解析等场景

  - 定义Schema时将长度限制和正则规则分开写，避免长度溢出被归为正则匹配失败导致误优化，同时先通过小流量采样统计字段输出长度再设置合理阈值，减少不必要的长度违规，适合电商商品属性抽取、用户标签生成等场景

  - 构建重试逻辑时，不要直接返回原生Pydantic解析错误，要基于剥离围栏后的校验结果构造反馈提示，实测32.2%的重试反馈仅提示解析错误但实际隐藏了更深层的违规，优化后可提升重试成功率

  - 评估结构化输出效果时不要只看单一通过率，要按失败类别统计分布，相同通过率下不同模型/提示的失败模式差异极大，针对性优化效率远高于盲目调prompt'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM结构化输出管线普遍只用单一通过率评估效果，无法区分不同失败原因的差异；原生结构化输出模式不支持自定义跨字段约束，prompt+事后校验的范式仍是跨厂商部署的主流，但现有评估方式无法指导针对性优化，导致重试成本高、管线稳定性差，是Agent、生成式推荐等场景的共性痛点。

### 方法关键点
- 设计细粒度结构化输出失败分类体系，分2阶段判定：先基于原始输出识别markdown围栏、前置散文、Schema镜像3类格式错误，再基于Pydantic错误映射正则匹配、长度限制、枚举违规等7类Schema错误，优先级规则确保格式错误不掩盖底层违规
- 覆盖OpenAI、Anthropic共9款模型的18种配置，在HotpotQA、FinanceBench两个数据集上累计采集3997次生成尝试，所有失败样本都经确定性分类器打标，部分样本经人工校验分类逻辑一致性

### 关键实验结果
整体尝试失败率28.2%，60.5%的失败为markdown围栏格式问题，仅48%的围栏输出剥离后可通过校验，剩余52%隐藏长度或正则违规；同类模型在相同通过率下失败模式完全不同，如gpt-4o、gpt-4o-mini、Claude Sonnet 4.6通过率均在13~16%区间，但主导失败类别分别为Schema镜像、正则违规、长度违规；提升字段长度上限后，对应长度违规完全消失，失败主导类别切换为正则违规；提示词优化减少围栏问题时，表观长度违规率上升本质是原本隐藏的长度违规被暴露，不是新增问题。

### 核心结论
单一结构化输出通过率对工程优化几乎没有指导价值，只有拆解到具体失败类别、同时暴露格式错误和底层Schema违规，才能针对性提升管线稳定性。
