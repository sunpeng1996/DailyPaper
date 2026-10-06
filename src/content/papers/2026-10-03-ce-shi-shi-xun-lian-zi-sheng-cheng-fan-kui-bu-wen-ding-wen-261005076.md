---
title: 'Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition
  of Long-Horizon Adaptation'
title_zh: 测试时训练自生成反馈不稳定问题：长程适配的因果分解
authors:
- Cheng Luo
- Bing Li
- Bernard Ghanem
affiliations:
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2610.05076'
url: https://arxiv.org/abs/2610.05076
pdf_url: https://arxiv.org/pdf/2610.05076
published: '2026-10-03'
collected: '2026-10-06'
category: LLM
direction: LLM 测试时训练稳定性优化
tags:
- Test-Time Training
- Self-Generated Feedback
- Causal Decomposition
- LLM Adaptation
- Agent Robustness
one_liner: 通过因果分解定位自生成反馈导致测试时训练退化路径，提出校验机制大幅降低性能损失
practical_value: '- 长时运行的电商导购Agent、用户长序列建模场景不要直接用模型自生成内容做测试时训练数据，避免累积性能退化

  - 必须用自生成内容做在线适配时，可引入Settlement机制：更新权重前用独立真实业务数据（如真实用户query、点击样本）校验，仅性能不下降才保留更新

  - 测试时训练的自反馈退化可通过定期插入真实数据打断缓解，每3-4轮自生成内容后插入1轮真实数据训练，可减少60%以上性能损失

  - 不要用参数更新幅度、生成内容多样性判断测试时训练更新是否安全，独立真实数据校验是唯一可靠依据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Test-Time Training (TTT) 是长上下文LLM、长时运行Agent的核心能力，可在推理阶段更新权重存储超出KV cache窗口的信息，降低长序列的计算开销。但当模型用自生成输出作为训练数据时会形成闭环反馈，长周期运行后会出现真实数据预测性能下降的问题，现有工作未明确退化的因果路径，也缺乏可落地的缓解方案。

### 方法关键点
- 设计三组因果对照实验定位退化路径：Fixed Generation采用冻结模型生成所有训练数据，切断更新对未来训练样本的影响；Recorded Replay使用固定的退化生成文本训练，分离注意力读取损失和权重更新的持久损失；配对单步更新对比，验证单步更新对源样本和独立真实样本的性能影响差异。
- 提出Settlement更新校验机制：每次生成候选权重更新后，在独立真实文本上验证性能，仅当性能不下降时才保留更新，无需依赖生成样本的标签。

### 关键实验
实验覆盖125M/760M/3B TTT-E2E模型、Qwen3-4B模型，数据集包括PG-19书籍语料、WebShop、ALFWorld Agent任务，基线为Writes Off（仅读取生成内容不更新权重）。闭环自生成训练在125M/760M/3B模型上分别带来3.01/6.00/0.40 nats的真实文本NLL损失上升；Fixed Generation可消除98%以上的性能损失；Settlement机制将125M/760M模型的最终NLL差距降至0.07/-0.02 nats，同时保留真实数据训练的收益，在WebShop任务上将Exact Success从0.1053提升至0.1853。

### 核心结论
测试时训练的更新是否有益，只能通过独立真实数据的性能校验判断，源数据拟合度、参数更新幅度、生成内容多样性都不能作为可靠依据。
