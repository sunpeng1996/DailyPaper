---
title: 'Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative
  Policy Optimization for LLM'
title_zh: 面向LLM推理上下文敏感幻觉的步级自洽GRPO优化算法
authors:
- Xiaomeng Hu
- Jiaqi Hu
- Hao Chen
- Qi Zhang
- Zhanming Shen
- Wentao Ye
- Junbo Zhao
affiliations:
- Zhejiang University
arxiv_id: '2607.18915'
url: https://arxiv.org/abs/2607.18915
pdf_url: https://arxiv.org/pdf/2607.18915
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: LLM训练优化 · 推理幻觉缓解
tags:
- GRPO
- Hallucination
- Reasoning
- Policy Optimization
- RLHF
one_liner: 提出无外部知识依赖的SSC-GRPO，缓解LLM多步推理中的上下文敏感事实幻觉
practical_value: '- 电商/导购Agent做多轮推理、属性匹配时，可复用SSC-GRPO的步级自洽奖励机制，无需接入外部知识库即可减少「模型本身知道正确属性但受上下文干扰输出错误」的问题，降低推理幻觉率

  - 生成式推荐构建用户需求推理链时，可直接复用跨rollout的步级一致性打分方法，实现无标注的推理步骤质量校验，替代部分人工标注成本

  - 现有基于GRPO的LLM微调流程可直接加入步级优势重加权trick，仅需少量代码修改即可提升推理类任务（如商品参数计算、优惠规则推导）的准确率，不需要额外引入监督信号'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM多步推理能力提升的同时，长推理链中的幻觉很难检测，其中占比近70%的上下文敏感事实幻觉尤为突出：模型本身具备对应知识，只是受推理上下文干扰产生错误，现有检测方法大多依赖外部知识库，成本高、场景适配难度大。

### 方法关键点
- 复用GRPO多rollout采样的天然特性，无需额外采样即可计算步级自洽性，无需引入外部知识源
- 用模型自身做NLI判断，对比同组其他rollout的推理步骤，给每个步骤打一致度得分，正确rollout的匹配权重更高
- 把GRPO的轨迹级优势按步级得分重加权，保持总优势不变，优先优化一致性低的错误步骤

### 关键实验
在Qwen3-4B、Llama3-8B系列模型上训练，对比GRPO、FSPO等基线，数学推理+幻觉评测平均得分分别超基线1.8%、1.01%、1.5%，上下文敏感幻觉占比从22.76%下降到16.9%，训练过程中推理步骤一致性持续提升。

最值得记住的结论：多步推理中大部分幻觉不是模型没有知识，而是上下文干扰导致的，利用自洽性做步级奖励，不需要外部知识就能有效缓解这类问题
