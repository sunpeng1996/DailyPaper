---
title: 'Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP'
title_zh: 强制输出字母会抑制LLM拒绝：来自WMDP的机制性证据
authors:
- Stepan Epifantsev
- Anna Antipova
- Oleg Chernikov
- Leon Strelkov
- Alexey Dontsov
affiliations:
- Independent Researcher
- HSE University
- ITMO University
- AIRI
arxiv_id: '2611.08639'
url: https://arxiv.org/abs/2611.08639
pdf_url: https://arxiv.org/pdf/2611.08639
published: '2026-11-05'
collected: '2026-11-09'
category: Eval
direction: LLM安全评估 · 格式偏差机制分析
tags:
- LLM Safety
- Evaluation Bias
- MCQ Evaluation
- Model Interpretability
- WMDP
one_liner: 从机制层面解释MCQ格式为何抑制LLM拒绝，证明其仅衡量知识而非安全能力
practical_value: '- 做LLM驱动的Agent、推荐话术合规性评测时，不要完全依赖MCQ类选择题评估，必须补充开放场景测试，否则会严重低估违规输出风险

  - 在需要LLM输出结构化选项的场景（如用户偏好收集、召回类目标签选择、多候选排序），可添加「仅输出对应字母/编号」的指令，能大幅降低无关回复（拒绝、冗余解释）占比，提升输出稳定性

  - 做LLM对齐优化时，需覆盖强制输出结构化内容的场景，避免恶意用户通过选择题格式绕过安全限制，比如防止电商客服场景下用户套取违规商品信息的攻击'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM安全评估大量采用MCQ（选择题）格式，此前已有研究发现MCQ会显著降低模型拒绝率，但缺乏机制层面的解释，导致安全评分可能严重高估模型实际安全能力，误导高风险场景的评估决策。

### 方法关键点
- 基于WMDP大规模危险品知识基准，构造匹配的开放问答(OE)和MCQ两组Prompt，对比两类格式下的模型行为与内部激活差异
- 采用tuned lens追踪层间token概率的动态变化，用refusal direction分析激活与拒绝通路的几何相似度，通过注意力头消融实验验证通路的因果关系
- 覆盖Llama-3.1-8B-Instruct、Qwen3-8B两个主流8B参数指令微调模型

### 关键结果
- OE下60%以上请求会被拒绝的问题，MCQ下拒绝率几乎为0，且MCQ答题准确率与OE拒绝率无统计学显著相关性
- MCQ格式下模型在中层（Llama 15~18层、Qwen 22~25层）就快速锁定答案字母，而OE格式下拒绝信号从第11层开始逐步累积
- MCQ激活与拒绝方向的余弦相似度仅为OE的1/3，接近 benign 样本的激活水平
- 消融Llama中负责MCQ答案选择的Top10注意力头后，正确字母概率从0.77降至0.64，拒绝概率从0.007升至0.05

### 核心结论
MCQ格式的安全评分仅衡量知识检索能力，完全无法反映模型在开放场景下的拒绝安全机制是否生效
