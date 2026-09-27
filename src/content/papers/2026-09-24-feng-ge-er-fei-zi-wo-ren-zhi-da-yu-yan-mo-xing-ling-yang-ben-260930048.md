---
title: 'Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large
  Language Models'
title_zh: 风格而非自我认知：大语言模型零样本代码归因依赖表面特征
authors:
- Ehsan Barkhordar
- Surendrabikram Thapa
affiliations:
- Koç University
- Virginia Tech
arxiv_id: '2609.30048'
url: https://arxiv.org/abs/2609.30048
pdf_url: https://arxiv.org/pdf/2609.30048
published: '2026-09-24'
collected: '2026-09-27'
category: LLM
direction: 大模型可解释性 · 代码归因分析
tags:
- LLM
- Code Attribution
- Zero-Shot
- Model Evaluation
- Surface Cue
one_liner: 揭示LLM零样本代码归因并非靠自我识别，而是依赖代码长度、注释等表面风格特征
practical_value: '- 用LLM做文案/内容质量评估、A/B测试裁判时，需先对生成内容做归一化，去掉格式、长度、注释等表面特征，避免自偏好偏差

  - 多Agent协作需要跨模型校验输出时，不要依赖LLM原生归因能力，需额外引入规则或轻量化分类器做生成溯源，防止合谋风险

  - 评估模型归因类任务时不要仅用原始准确率，需同步上报balanced accuracy、启发式基线，规避模型固有肯定/否定偏置对结论的干扰'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
大模型作为裁判、校验器的落地场景快速增多，若模型能识别自身生成内容，会引发自偏好、多模型合谋等风险，现有研究对大模型零样本代码归因的底层逻辑尚不明确。
### 方法关键点
12款主流LLM在MBPP、HumanEval、DS-1000三个代码数据集生成答案，设计4类归因任务：成对选择自身输出、单样本判断是否自身输出、指定模型输出归因、盲测质量；额外测试去掉注释、类型提示、变量名等表面特征后的归因效果。
### 关键结果数字
单样本归因任务15组模型-基准组合的balanced accuracy仅49~58%，接近随机水平；成对归因任务准确率与自身生成代码更长的概率相关系数r=0.93；去掉表面特征后12组重测结果中有10组归因准确率降至随机水平，Claude Haiku的自偏好完全消失。
