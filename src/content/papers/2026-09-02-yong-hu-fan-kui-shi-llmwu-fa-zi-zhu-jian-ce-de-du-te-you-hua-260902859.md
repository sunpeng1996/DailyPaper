---
title: User Feedback Provides a Unique Signal that LLMs Can not Detect
title_zh: 用户反馈是LLM无法自主检测的独特优化信号
authors:
- Shachar Don-Yehiya
- Leshem Choshen
- Omri Abend
affiliations:
- The Hebrew University of Jerusalem
- IBM Research
- MIT
- MIT-IBM Watson AI Lab
arxiv_id: '2609.02859'
url: https://arxiv.org/abs/2609.02859
pdf_url: https://arxiv.org/pdf/2609.02859
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: LLM对齐 · 用户反馈利用
tags:
- User Feedback
- LLM Alignment
- LLM-as-Judge
- Evaluation Bias
- Model Improvement
one_liner: 揭示LLM评判者对反馈引导优化的系统性偏见，证明用户反馈可提升9%-32%问题解决率
practical_value: '- 做LLM导购/客服Agent优化时，不要完全依赖LLM-as-Judge的评估结果，要叠加用户反馈的问题解决率作为核心指标，避免误筛掉真正解决用户问题的响应

  - 小规模部署的Agent可优先用弱反馈信号（仅提示有问题/问题类型）优化，标注成本远低于全量标注，小模型可获得10%-17%的效果提升，性价比更高

  - 做生成式推荐的响应评估时，可拆分内容正确性和风格满意度两个维度打分，避免judge偏好流畅但事实错误的响应，适配电商场景信息准确的优先级

  - 业务若用小模型做Agent，接入用户反馈的收益远高于大模型，小模型问题解决率最高可提升32%，ROI更优'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
之前学界普遍认为自然交互中的用户反馈噪声大、难以有效利用，与业务端用户反馈是最直接优化信号的认知存在矛盾，需明确反馈的真实价值并定位过往负面结论的成因。

### 方法关键点
- 数据集构建：两类数据，①合成数据集：对正确响应做4类可控篡改（因果倒置、关键信息遗漏、实体替换、逻辑反转），生成3级强度的模拟反馈（告知修复方案、仅提示问题、仅告知有错）；②自然对话数据集：提取通用可复用反馈，过滤个性化主观内容。
- 对照实验：测试大小模型在有/无反馈下的错误修复效果，对比两种评估方式：目标问题解决率评估、通用LLM-as-Judge pairwise偏好评估。
- 偏差定位：筛选仅反馈组修复成功的样本，测试judge的选择准确率，分析偏差成因。

### 关键结果
- 问题解决率：加入反馈后，大模型修复率提升9%~16%，小模型提升27%~32%；最弱的仅告知有错的反馈，也能带来3%~10%的提升。
- 评估偏差：在反馈组修复成功、无反馈组失败的样本上，LLM judge正确选择率仅34%~54%，系统性偏好无反馈组的风格优化，忽略内容正确性。
- 关联失效模式：模型无法自主修复的问题，作为judge时也大概率无法识别正确修复结果。

### 核心结论
用户反馈是LLM权重中没有的独特信号，不要被LLM judge的风格偏好掩盖其真实优化价值。
