---
title: LLM Judges Can Be Too Generous When There Is No Reference Answer
title_zh: 无参考答案场景下LLM评审模型普遍存在打分过宽问题
authors:
- Chalamalasetti Kranti
- Sowmya Vajjala
arxiv_id: '2607.12885'
url: https://arxiv.org/abs/2607.12885
pdf_url: https://arxiv.org/pdf/2607.12885
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: LLM自动评估 · 无参考场景校准
tags:
- LLM Judge
- Automatic Evaluation
- Reference-free Evaluation
- Evaluation Calibration
- Human Alignment
one_liner: 揭示无参考答案场景下LLM评审易过誉错误答案的问题，给出校准实施蓝图
practical_value: '- 做生成式推荐文案、智能Agent回复的无参考自动评估时，需先拿带参考答案的小样本校准LLM评审的打分阈值，避免误判劣质输出

  - 评估RAG问答结果、搜索Query改写效果时，优先在Prompt中加入参考答案，可使LLM评审决策准确率最高提升85%，更好对齐人工判断

  - 多语言跨境电商场景的内容合规/质量评估，可直接复用两阶段校准流程（校验评审模型任务认知、参考敏感度实验）快速落地评估体系'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前无参考答案的开放场景下，LLM评审被广泛用于生成内容、模型回复的自动评估，但缺乏对其评估可靠性的系统性验证，易导致评估结果失真。
### 方法关键点
采用两阶段实验框架验证LLM评审能力：1）校准实验：验证评审模型对待评估任务的认知能力；2）敏感度实验：验证参考答案的存在、在Prompt中的位置对评审结果的影响，覆盖3种语言场景，同步对比人工标注结果。
### 关键结果
1. 无参考答案时，LLM评审普遍给错误答案过高评分；
2. Prompt中加入参考答案后，LLM评审的对错决策翻转比例最高可达85%，且该翻转整体与人工判断对齐；
3. 验证有效的两阶段校准流程可作为LLM评审落地无参考场景前的标准校验步骤。
