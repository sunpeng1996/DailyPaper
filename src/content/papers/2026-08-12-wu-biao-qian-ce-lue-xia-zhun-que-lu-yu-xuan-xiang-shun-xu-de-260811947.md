---
title: Accuracy and Order Sensitivity Diverge Under Label-Free Strategies
title_zh: 无标签策略下准确率与选项顺序敏感性的分化现象研究
authors:
- Karl Hanna
- Chen Feng
affiliations:
- Queen’s University Belfast
arxiv_id: '2608.11947'
url: https://arxiv.org/abs/2608.11947
pdf_url: https://arxiv.org/pdf/2608.11947
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: LLM评测 · MCQ去偏方法验证
tags:
- LLM Evaluation
- Multiple Choice Question
- Debiasing
- Prompt Engineering
- Order Sensitivity
one_liner: 验证两类MCQ无标签去偏策略无法稳定提精度，定位性能瓶颈为选项隐藏环节
practical_value: '- 做LLM MCQ类评测（如Agent技能评测、电商导购意图分类）时，不要盲目采用无标签去偏策略，可优先尝试低成本cyclic
  permutation提升评测准确率

  - 落地生成-匹配类任务（如RAG答案匹配、用户Query到候选商品匹配）时，不要刻意隐藏候选集，完整暴露候选+LLM匹配的方案效果更稳定

  - LLM评测去偏效果验证不能仅看整体准确率，需同步监控顺序敏感性指标，避免出现准确率提升但去偏失效的问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
MCQ是LLM主流自动评测范式，但得分混淆模型真实知识与选项顺序敏感性，现有去偏策略要么调用成本高（全排列需k!次调用），要么需要logit访问权限，无标签提示式去偏的真实效果缺乏系统验证。
### 方法关键点
测试两类无标签去偏策略：1）generation-then-matching 范式，先生成答案再匹配候选；2）孤立对每个选项打分，天然无位置偏置。同时对策略做全链路拆解，对比循环排列选项、两阶段提示等方案的去偏效果与精度表现。
### 关键结果
两类无标签去偏策略均无法稳定提升准确率；性能瓶颈来自隐藏选项的操作，而非后续匹配步骤；仅完整暴露所有选项+LLM匹配的配置能稳定追平基线；完全消除位置偏置也不能稳定带来精度收益，反而cyclic permutation通常可提升准确率；召回不平衡、单题顺序敏感性指标均无法验证两阶段提示的可靠去偏效果。
