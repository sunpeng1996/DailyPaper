---
title: The Disconnect Between Better Descriptive Reasoning Trace Quality and Recommendation
  Effectiveness
title_zh: 生成式推荐中描述性推理轨迹质量与推荐效果的脱节现象研究
authors:
- Gustavo Penha
- Juan Elenter
- Claudia Hauff
- Hugues Bouchard
- Paul Bennett
- Mounia Lalmas
affiliations:
- Spotify
arxiv_id: '2608.23154'
url: https://arxiv.org/abs/2608.23154
pdf_url: https://arxiv.org/pdf/2608.23154
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · 推理轨迹效果验证
tags:
- Generative Recommendation
- Semantic ID
- Chain-of-Thought
- Reasoning Trace
- Alignment Tax
one_liner: 通过2×2对照实验证实生成式推荐中推理轨迹质量提升不必然转化为传统离线推荐效果增益
practical_value: '- 不要盲目给生成式推荐加CoT推理：标准SFT+仅准确率奖励的训练范式下，加推理会使Title表示的R@10下降11%-20%，SID表示下降0%-5%，上线前必须做小流量验证

  - 若需加推理优先优化奖励函数：采用包含准确率、轨迹质量、推荐相关性的复合LLM-judge奖励，可使SID表示在2个商品域的R@10超无推理基线3.2%/2.9%，ROI远高于做多任务SID对齐

  - 生产场景可做推理+无推理两路候选融合：Spotify千万级曲库场景下，两路结果融合后HR@30提升2.8%，可释放推理的互补价值

  - 可解释性优先场景选Title做item表示：生成的推理轨迹groundedness比未对齐SID高157%，若要抵消效果损失需搭配复合奖励优化'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐领域普遍通过添加显式CoT推理轨迹提升可解释性和预期效果，但Semantic ID的对齐成本高，且没有研究验证推理轨迹质量的提升是否真能转化为推荐效果增益，存在认知偏差。

### 方法关键点
- 2×2因子对照设计：控制item表示（SID/Title）、是否加推理两个变量，共用Qwen3-1.7B backbone和相同数据拆分，隔离变量影响
- 三阶段训练流程：1）无推理LoRA SFT基线训练；2）暖启动后用GPT生成的教师轨迹做全参数SFT，item token损失权重设为推理token的20倍避免任务偏移；3）GRPO RL优化，分别测试仅前缀匹配奖励、复合LLM-judge奖励两种配置
- 新增全对齐对照组：复现SIDReasoner的8任务对齐流程，验证对齐成本对推理效果的影响
- 多维度评价体系：同时测传统离线Recall@k/nDCG@k、LLM judge打分的6维度推理轨迹质量、推荐相关性

### 关键结果数字
- 标准SFT+仅准确率奖励下，加推理使Title组R@10下降11%-20%，SID组下降0%-5%，推理轨迹质量更高的Title组效果损失更大
- 8任务全对齐SID的推理轨迹总分比未对齐SID高58%、比Title高5%，但R@10反而比无推理基线下降17%-23%
- 采用复合LLM-judge奖励后，SID组在Office/Industrial两个商品域的R@10分别提升3.2%/2.9%，超过无推理基线
- 生产级千万级曲库场景下，加推理不改变离线核心指标，但两路候选融合后HR@30提升2.8%

最值得记住的结论：提升描述性推理轨迹质量本身不足以稳定提升传统离线推荐效果，优化目标和评价指标的影响远大于轨迹本身的语义质量。
