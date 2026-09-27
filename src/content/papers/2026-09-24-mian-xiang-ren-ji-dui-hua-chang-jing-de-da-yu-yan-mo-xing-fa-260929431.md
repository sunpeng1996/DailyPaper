---
title: Calibrating LLM Judges for Human and AI Conversations
title_zh: 面向人机对话场景的大语言模型评审校准方法
authors:
- Maike Züfle
- Patrícia Schmidtová
- Vilém Zouhar
- Shree Harsha Bokkahalli Satish
- Erica Cooper
- Shobhit Banga
- Vaibhav Nalawade
- Manmeet Kaur
- Jan Niehues
- Markus Müller
affiliations:
- Karlsruhe Institute of Technology
- Charles University
- ETH Zurich
- University of Edinburgh
- Voice Arena
arxiv_id: '2609.29431'
url: https://arxiv.org/abs/2609.29431
pdf_url: https://arxiv.org/pdf/2609.29431
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: LLM 对话评审校准与基准构建
tags:
- LLM Judge
- Calibration
- Conversational AI
- Evaluation Dataset
- Human-AI Dialogue
one_liner: 提出锚定数据集校准方法统一跨模型对话评审打分尺度，开源人机对话评测基准
practical_value: '- 电商智能客服、导购Agent的效果评估可复用「小锚数据集+µ/σ匹配」的校准方案，统一不同LLM评审的打分尺度，解决跨模型评测结果不可比问题

  - 对话类Agent评测优先选择pointwise打分方案，避免pairwise方案的长上下文超限、位置偏差问题，中小样本下评测效率更高

  - 自研对话Agent的效果benchmark可参考VOICEARENA数据集的构建方法，按任务实例做多组对比，兼顾任务完成度、拟人度两个核心维度'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
对话类AI（智能客服、语音助手等）的效果评估高度依赖人类标注，成本高且效率低，LLM评审是可规模化的替代方案，但现有LLM评审存在三大痛点：pointwise打分跨模型尺度不统一无法横向比较、pairwise对比受长上下文超限、位置偏差影响可靠性差、当前缺乏公开的人机对话评测基准验证评审效果。

### 方法关键点
- 提出锚定校准方案：从CANDOR人类对话数据集筛选32个代表性对话作为固定锚集，每个对话附带人类标注的对话成功率得分，任意新LLM评审只需先在该锚集输出原始打分，再通过仿射变换校准到人类打分的统一尺度，校准过程完全保留原始得分的排序相关性。
- 开源VOICEARENA GOAL数据集：包含200组任务导向人机对话（订票、改签两类场景），覆盖5类被测对象（4个SOTA对话模型+人类坐席），附带人类标注的任务完成度、拟人度两个维度的pairwise排序标注。

### 关键结果数字
- CANDOR数据集上的点wise打分最优模型（Phi-4多模态）和人类打分的Spearman ρ达0.32，高低分极端样本的pairwise准确率达93.6%，超过pairwise直接评审的91%。
- 32个锚集+Wasserstein仿射变换校准后，跨LLM评审得分分布与人类得分的Wasserstein距离降低70%以上，校准方案可零样本迁移到VOICEARENA人机对话场景，跨模型得分分布的Wasserstein距离降低3-10倍。
- VOICEARENA基准测试显示，当前SOTA LLM评审的pairwise准确率仅略高于时长基线（65%），远低于人类标注84%的一致性天花板。

最值得记住的结论：对话质量评测中，经过校准的pointwise LLM评审在效率、可靠性上均优于pairwise评审，小样本锚定校准是解决跨模型评测不可比问题的低成本可行方案。
