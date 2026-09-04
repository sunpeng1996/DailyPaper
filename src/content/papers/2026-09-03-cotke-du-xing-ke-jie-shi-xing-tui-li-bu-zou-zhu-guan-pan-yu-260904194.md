---
title: 'Legibility is Not Interpretability: Comparing Judged and Actual Importance
  in Chain-Of-Thought Reasoning'
title_zh: CoT可读性≠可解释性：推理步骤主观判断与实际重要性对比
authors:
- Kevin Du
- Alexander Hoyle
- Laura Ruis
- Acyr Locatelli
affiliations:
- ETH Zürich
- MIT
- Cohere
arxiv_id: '2609.04194'
url: https://arxiv.org/abs/2609.04194
pdf_url: https://arxiv.org/pdf/2609.04194
published: '2026-09-03'
collected: '2026-09-04'
category: Reasoning
direction: CoT推理可解释性 · 步骤重要性量化
tags:
- Chain-of-Thought
- Interpretability
- Reinforcement Learning
- LLM-as-Judge
- Process Reward Modeling
one_liner: 用RL优势值量化CoT步骤真实重要性，证实LLM法官难以从文本识别正确响应的关键步骤
practical_value: '- 做Agent推理链路优化时，不要仅依赖LLM judge标注CoT步骤优劣，尤其是正确响应的核心步骤很难从文本识别，可引入少量蒙特卡洛rollout测试步骤真实价值

  - 训练Process Reward Model（PRM）时，可参考advantage量化方法标注样本，错误响应的关键步骤易识别，可优先用这部分数据微调PRM降低标注成本

  - 电商导购Agent的CoT优化中，对用户query响应链路的步骤重要性评估可复用本文的PELT changepoint检测方法，降低多步骤假设检验的假阳性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大量工作默认CoT的可读性等同于可解释性，依赖LLM法官诊断推理错误、开展过程奖励建模，但从未验证CoT文本是否真的编码了步骤对最终结果的真实贡献，这会导致PRM训练、推理链路优化等工作的底层假设存在偏差。

### 方法关键点
- 将CoT步骤的重要性定义为RL领域的advantage：加入该步骤后，模型获得目标奖励（最终答案正确/与原响应答案一致）的期望变化值，通过蒙特卡洛rollout采样估计
- 用PELT changepoint检测算法识别重要步骤：将步骤价值序列建模为分段常数，仅优势值变化超过0.1且统计置信度≥95%的步骤才被标记为核心贡献步骤
- 分组对比零样本LLM法官和微调后critic模型的步骤重要性识别能力，按最终响应正确/错误拆分评估

### 关键结果数字
实验覆盖GSM8K、MATH500、AIME等6个数学推理数据集，测试Qwen3 1.7B到32B全规模模型：零样本LLM法官识别重要步骤的PR-AUC比噪声上限低9倍；微调后的critic在错误响应上PR-AUC达0.28~0.30，接近一半噪声上限，在正确响应上仅0.065~0.10，仅达噪声上限的10%~20%；正确响应中仅1%~5%的步骤是真正的核心贡献步骤。

**最值得记住的一句话**：CoT的可读性不等于可解释性，不要过度从文本表面解读推理步骤的实际作用，尤其是正确响应的核心贡献步骤几乎无法从文本直接识别。
