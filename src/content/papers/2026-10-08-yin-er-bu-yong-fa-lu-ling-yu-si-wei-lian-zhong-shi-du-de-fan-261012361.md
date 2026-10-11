---
title: 'Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought
  Faithfulness'
title_zh: 引而不用：法律领域思维链忠实度的反事实审计
authors:
- Saisab Sadhu
- Shreeyans Arora
- Pratinav Seth
affiliations:
- Lexsi Labs
arxiv_id: '2610.12361'
url: https://arxiv.org/abs/2610.12361
pdf_url: https://arxiv.org/pdf/2610.12361
published: '2026-10-08'
collected: '2026-10-11'
category: Eval
direction: 大语言模型 · 思维链忠实度评估
tags:
- Chain-of-Thought
- Faithfulness
- Counterfactual Evaluation
- LLM Auditing
- Legal NLP
one_liner: 通过反事实替换验证法律大模型法条引用多为事后合理化 不构成判决的因果依据
practical_value: '- 针对Agent输出带规则引用（如电商合规条款、平台规则）的场景，可复用反事实替换法验证引用是否真实影响输出，避免事后合理化带来的合规风险

  - 垂直领域LoRA微调效果验证不能仅看表面准确率、引用召回率，需增加因果性校验环节，避免模型学会「凑引用」而非真正遵循规则

  - 高风险场景（如营销合规话术生成、售后理赔Agent）的LLM评估需加入对抗隐指令测试，量化模型抗干扰能力，降低恶意诱导下的违规概率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前高风险场景下LLM生成CoT时会引用规则/法条证明决策合理性，但该引用是否为决策的真实因果依据未得到验证，存在合规风险
### 方法关键点
固定案件事实，反事实替换模型判决中引用的法条为无关内容，从隐状态解码判决变化；覆盖7个8B-70B开源模型、4个法律推理基准，新增对抗隐指令红队测试
### 关键结果
- 模型法条引用准确率达66.7%-100%，但替换法条后判决变更率仅0.0%-76.7%，不同基准差异极大
- 参数规模提升、垂直领域LoRA微调均无法缩小引用准确率与判决敏感度的差距
- 对抗隐指令遵从率达73.3%-96.4%，远高于判决对法条变更的敏感度
