---
title: 'Many Solutions, One Answer: Search Order Shapes the Default Solutions of Language
  Models'
title_zh: 搜索顺序决定大语言模型多解约束问题的默认输出解
authors:
- Qinhan Hou
- Jing Tang
affiliations:
- University of Helsinki
arxiv_id: '2611.25916'
url: https://arxiv.org/abs/2611.25916
pdf_url: https://arxiv.org/pdf/2611.25916
published: '2026-11-19'
collected: '2026-11-20'
category: Reasoning
direction: 大语言模型多解推理 · 输出多样性优化
tags:
- LLM Reasoning
- Output Diversity
- Constraint Satisfaction
- Search Heuristic
- Prompt Engineering
one_liner: 揭示LLM多解问题输出同质化的类搜索机制，提出仅调整prompt顺序即可低成本提升输出多样性
practical_value: '- Agent做多约束路径规划、商品组合推荐这类多解任务时，可通过随机化问题中属性、候选项的呈现顺序，在几乎不损失有效性的前提下提升输出多样性，解决同质化问题

  - 当需要引导LLM输出指定可行解时，不需要微调，直接在prompt中显式指定变量/候选值的遍历顺序，即可让输出偏移到目标解，适用场景如定向推荐、合规文案生成

  - 不要依赖「要求LLM随机选择」的prompt指令来提升多样性，实测效果远不如随机化呈现顺序，还可能损失输出有效性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多解推理任务中LLM输出高度同质化，难以区分是模型无法生成其他解，还是仅偏好默认解，限制了规划、创意生成、推荐等需要多样输出的场景落地，且同质化背后的行为机制尚不明确。

### 方法关键点
- 数据集：两类已知全解集的约束推理任务，符号分配任务（2~6个可行解）、ZebraLogic多解变体（2~4个可行解），所有解可验证、可定向触发
- 测试模型：4个跨家族开源LLM（Qwen3-1.7B、Olmo-3.1-32B、gpt-oss-20B/120B）
- 对比策略：验证名称顺序、最小剩余候选（MRV）启发式对默认解的预测效果，测试随机化呈现顺序、指定搜索顺序、随机选择指令、调高等温四种干预的效果

### 关键结果
- 多解任务中默认解占比远超均匀采样预期，不同模型的默认解重合度达63%~95%
- 95%以上的低频次解可通过追加约束线索触发，说明模型并非无法生成其他解，仅存在输出偏好
- 基于MRV的类搜索规则预测默认解的准确率比名称顺序高26~40个百分点
- 随机化问题呈现顺序可提升符号任务输出广度28~39个百分点，ZebraLogic任务提升11~26个百分点，有效性损失不超过4个百分点，效果远优于随机选择指令（广度提升<2个百分点）

**最值得记住的一句话**：LLM在多解任务上的同质化输出并非能力限制，而是类搜索的遍历顺序偏好导致，仅通过prompt层面的顺序调整即可低成本提升输出多样性。
