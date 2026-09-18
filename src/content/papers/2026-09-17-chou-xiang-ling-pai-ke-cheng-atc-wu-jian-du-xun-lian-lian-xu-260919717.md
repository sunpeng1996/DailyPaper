---
title: 'Learn Your Own Thoughts: Abstract Token Curriculum'
title_zh: 抽象令牌课程（ATC）：无监督训练连续隐式思维链的学习框架
authors:
- Khashayar Gatmiry
- Avrajit Ghosh
- Parsa Mirtaheri
- Jason D. Lee
- Nika Haghtalab
- Emmanuel Abbe
- Peter Bartlett
affiliations:
- UC Berkeley
- UC San Diego
- EPFL
- Google DeepMind
arxiv_id: '2609.19717'
url: https://arxiv.org/abs/2609.19717
pdf_url: https://arxiv.org/pdf/2609.19717
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: LLM训练 · 隐式思维链学习
tags:
- Curriculum Learning
- Chain-of-Thought
- Continuous Representation
- Transformer
- Reasoning
one_liner: 无需显式思维链标注，通过课程学习让Transformer自发学习连续隐式思维链，提升复杂推理性能
practical_value: '- 电商/广告多步推理任务（如用户长序列意图拆解、复杂query理解）可复用ATC框架，无需人工标注中间推理步骤，仅按难度递进喂入数据+用连续隐式token存储中间状态，大幅降低标注成本

  - 训练长推理链模型时，可直接复用「截断backpropagation+课程回退」组合trick：截断反向传播最高降低73%显存占用，回退机制可修复前置阶段的性能退化，平衡训练效率和效果

  - 推荐/搜索/Agent任务中，可采用候选dropout trick避免模型学习复制候选的捷径，强制模型真正理解输入语义输出决策，提升泛化性'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有CoT技术需要显式标注推理步骤、人工设计任务专属草稿板，标注与设计成本高、泛化性差；直接在全难度任务上训练存在严重优化壁垒，无监督连续隐式CoT缺少高效的训练框架支撑。
### 方法关键点
- 分阶段课程设计：每个阶段逐步提升任务难度，同步增加连续隐式CoT令牌数量，仅监督最终答案，无需中间推理步骤标注
- 配套3个工程trick：1）候选dropout：随机隐藏部分训练样例的答案候选，避免模型学习复制候选的捷径；2）截断backpropagation：仅反向传播最近b个思维步的梯度，降低长推理链的显存占用；3）课程回退：阶段评估时检查所有前置阶段的准确率，出现退化则回退到最早失败的阶段重训
- 理论证明单层softmax attention场景下，梯度下降会自然让注意力集中到最近的CoT令牌，保障中间状态的有效传递
### 关键实验结果
- 奇偶校验任务：20个训练阶段后ATC准确率保持100%，无CoT的纯数据课程基线准确率降至50%（随机水平）
- 图可达性任务：ATC最终准确率99.9%，相比需要中间监督的SOTA方法Coconut，达到95%准确率的速度快2.6倍；搭配截断backpropagation+回退，仅损失2.4%准确率，显存占用降低73%、训练速度提升37%
- 8位加法任务：ATC准确率达99%，需要中间监督的Coconut方法准确率几乎为0
### 核心结论
仅需最终答案监督，通过难度递进的课程学习即可让Transformer自发形成有效的连续隐式思维链，无需人工设计中间推理结构
