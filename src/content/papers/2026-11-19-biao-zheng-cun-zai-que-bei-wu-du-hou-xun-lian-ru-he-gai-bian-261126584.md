---
title: 'Represented but misread: Post-training changes how language models read out
  what they represent'
title_zh: 《表征存在却被误读：后训练如何改变大语言模型的表征读出机制》
authors:
- Jochen Laubrock
affiliations:
- University of Potsdam
arxiv_id: '2611.26584'
url: https://arxiv.org/abs/2611.26584
pdf_url: https://arxiv.org/pdf/2611.26584
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 大语言模型后训练可解释性研究
tags:
- Post-training
- Linear Probing
- Model Interpretability
- SFT
- Readout Mechanism
one_liner: 通过线性探针与模型输出对比，证明后训练主要改变LLM对已表征信息的读出逻辑而非表征内容
practical_value: '- 做LLM4Rec对齐时，不需要盲目增加SFT数据规模，可先通过探针验证所需信息（如用户偏好、item属性）是否已在base模型中表征，仅针对读出链路优化即可降低对齐成本

  - 线上LLM推理的bad case排查：如果模型输出与预期不符，可优先排查后训练阶段的读出逻辑偏差，而非直接认定预训练阶段缺乏对应知识，减少不必要的预训练增量迭代

  - 训练垂直领域Agent时，可通过少量标注数据校正特定任务的读出方向，无需全量微调：例如电商内容审核场景，仅需千级标注即可修正AI生成内容识别的输出偏差'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有研究普遍认为后训练仅改变LLM输出格式，不改变内部表征，但实际场景中频繁出现模型“知道但不说对”的问题（如无法识别自身生成的AI文本），需明确后训练对表征与读出链路的差异化影响，为LLM对齐优化、可解释性分析提供依据。

### 方法关键点
- 选取6款开源base模型及其对应后训版本（含SFT、DPO等全阶段checkpoint），覆盖4B~12B参数规模
- 采用信号检测论分离模型回答的敏感度与判定阈值，对比线性探针（从隐层表征解码目标属性）与模型实际输出的效果差异
- 引入模型拼接、激活补丁、定向steering等可解释性干预手段，定位后训练影响发生的网络层与prompt位置

### 关键结果
- 数据集：德语AI/人类文本分类任务（聊天、新闻、教科书摘要三类私有corpus）+ 公开否定陈述真值判断数据集
- 基线：词n-gram分类器、字符n-gram分类器、输入embedding探针
- 核心数字：① 所有模型的隐层探针均可有效解码文本属性，中位数d'达1.35~3.70，与词n-gram分类器效果相当；② 后训练平均降低模型回答敏感度Δd'=-0.34，部分模型输出甚至出现逆序（d'<0）；③ 仅加入2000条标注的SFT数据即可定向校正读出方向，对表征的影响可忽略。

**最值得记住的一句话**：大语言模型“不知道”的问题往往远少于“说不对”的问题，后训练对齐的核心是优化表征读出逻辑，而非反复注入已存在的知识。
