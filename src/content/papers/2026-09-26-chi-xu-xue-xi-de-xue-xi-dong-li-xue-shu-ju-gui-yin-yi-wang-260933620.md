---
title: 'Learning Dynamics of Continual Learning: A Unified View of Data Attribution,
  Forgetting, and Plasticity Loss'
title_zh: 持续学习的学习动力学：数据归因、遗忘与可塑性损失的统一视角
authors:
- Yi Ren
- Wenlong Deng
- Guanzhe Hong
- Clare Lyle
- Yarin Gal
affiliations:
- OATML
- University of Oxford
- UBC
- Google DeepMind
arxiv_id: '2609.33620'
url: https://arxiv.org/abs/2609.33620
pdf_url: https://arxiv.org/pdf/2609.33620
published: '2026-09-26'
collected: '2026-10-01'
category: Training
direction: LLM持续学习 · 训练动力学
tags:
- Continual Learning
- Learning Dynamics
- LLM Fine-tuning
- Catastrophic Forgetting
- Plasticity Loss
one_liner: 推导token与层级的更新-行为交互分解，统一解释持续学习的数据归因、遗忘、可塑性损失机制
practical_value: '- 做LLM持续微调（如商品文案生成、推荐话术迭代）时，可计算token能量Eu过滤高能量更新（阈值1.5-1.8），缓解旧知识（原有推荐规则、商品属性记忆）遗忘，几乎不影响新任务效果

  - 不同业务场景的微调（如导购对话、商品搜索query理解）可采用差异化响应格式（指令后缀、输出结构），减少多任务微调时的语义侵蚀，避免旧业务效果下降

  - 长时间持续微调后若新任务适配速度变慢，可检测readout传输得分RD，下降明显时重置readout层参数，能快速恢复模型可塑性，避免全量重训成本

  - 做Agent经验筛选时，可使用文中的CH1+CH2交互得分正向排序候选经验，用5%的训练数据就能达到接近全量微调的效果，大幅降低多轮迭代的训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
部署后的LLM需要持续迭代适配新业务数据（如电商新增品类、活动规则、用户反馈），但现有研究将数据选择、遗忘抑制、可塑性保持作为独立问题解决，缺乏统一机理分析，且梯度归因类方法计算成本过高，无法落地到LLM规模的业务微调场景。
### 方法关键点
- 推导token级更新-行为交互的一阶近似，将单个token学习对其他token预测的影响拆分为两个前向可计算通道：CH1是词汇空间直接交互，CH2是通过共享readout和残差流的语义扩散交互
- 揭示遗忘的两种独立机制：碰撞（少量高能量更新引发的集中冲突）、侵蚀（大量弱负向交互累积的缓慢漂移），分别对应不同缓解策略
- 提出readout传输得分RD，量化模型对未来任务的学习能力，得分下降直接对应可塑性损失，可通过重置readout层快速恢复
### 关键实验结果
- 跨语言经验检索任务上，CH1+CH2相比仅用CH1，MMLU检索准确率从0.488提升到0.625，GSM8K从0.445提升到0.600
- 数据选择实验中，用交互得分筛选5%的训练数据，相比随机选择，Qwen2.5-1.5B上GSM8K准确率从0.610提升到0.636，优于LESS等基线方法
- 长周期训练后OOD任务的RD得分下降20%-40%，重置readout层可恢复70%以上的新任务适配速度，RD退化程度和重置收益的Spearman相关系数达0.83
### 核心结论
持续学习中数据选择、遗忘、可塑性损失本质是同一个更新-行为交互过程的不同阶段，可通过前向可计算的轻量指标实现低成本的全流程管控
