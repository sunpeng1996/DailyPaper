---
title: 'PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking'
title_zh: PAR：面向状态追踪任务长度泛化的进度对齐循环机制
authors:
- Pan Wang
- Yihao Hu
- Guangyuan Dong
- Yitong Lin
- Hang Wang
- Zimi Liu
- Zhihao Wen
- Jianshe Li
- Jiang-Ming Yang
- Wei Wu
affiliations:
- Ant International
- National University of Singapore
arxiv_id: '2610.27628'
url: https://arxiv.org/abs/2610.27628
pdf_url: https://arxiv.org/pdf/2610.27628
published: '2026-10-19'
collected: '2026-10-21'
category: LLM
direction: 循环LLM · 长度泛化优化
tags:
- LoopedLLM
- LengthGeneralization
- StateTracking
- Recurrence
- LLMReasoning
one_liner: 提出进度对齐循环PAR，结合状态归一化锚定，使循环LLM在状态追踪任务实现16倍训练长度泛化
practical_value: '- 电商/推荐的长序列用户兴趣建模、多步交互Agent状态维护场景，可复用RMS状态归一化锚定技巧，防止多步迭代时状态漂移，提升长序列泛化能力

  - 多步推理Agent的自主停机设计，可复用「6 of 8」滑动窗口确认机制，无需新增参数仅靠现有输出头训练完成信号，平衡停机及时性和鲁棒性

  - 无中间标注的序列任务训练，可复用前缀自蒸馏方法，用短前缀的最终答案作为长序列中间步骤的监督信号，降低标注成本

  - 生成式推荐的超长用户行为序列建模，可参考深度-长度对应设计，让循环迭代次数与用户行为步数对齐，提升建模精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
循环大模型可通过测试时增加迭代次数提升推理能力，但现有方案未明确每次迭代的进度目标，且循环状态随迭代漂移，在需要多步连续更新的状态追踪场景下长度泛化能力极差，甚至不如显式CoT。
### 方法关键点
- 架构改造：将预训练LLM拆分为前缀层、权重共享循环核心层、后缀层，每次迭代拼接输入特征与上一轮状态输入核心层计算
- 进度对齐监督：第k次迭代的预测目标对齐前k步操作后的真实状态，建立迭代次数与任务步数的一一对应关系
- RMS状态锚定：每次迭代后将所有token状态归一化到首次迭代的RMS范数，防止多轮迭代后状态漂移
- 无标注适配：前缀自蒸馏，用EMA教师模型在短前缀上的预测结果作为长序列中间步骤的监督信号，无需中间标注
- 自主停机：复用后缀层输出头训练完成信号，采用「6 of 8」滑动窗口确认规则，无需提前知道任务长度即可自动停止迭代
### 关键结果
在swap-S5状态追踪任务上，Qwen2.5-0.5B仅用最多32步训练数据，在512步（16倍训练长度）测试时全状态准确率达95.5%，远高于RLT的55.7%和显式CoT的0.8%；移除归一化锚定后外推倍数从16×降至2.2×以下，移除进度对齐目标后外推倍数最多仅8×；无中间标注时前缀自蒸馏也能实现16×外推，256步准确率达85%。
### 核心结论
循环大模型的每一次迭代必须有明确的任务进度定义，同时保持状态表示的稳定性，才能将额外的迭代次数转化为更长序列的处理能力。
