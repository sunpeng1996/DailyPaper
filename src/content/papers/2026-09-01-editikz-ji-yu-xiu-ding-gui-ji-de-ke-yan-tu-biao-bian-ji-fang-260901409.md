---
title: 'EdiTikZ: Scientific Figure Editing from Revision Trajectories'
title_zh: EdiTikZ：基于修订轨迹的科研图表编辑方法
authors:
- Christian Greisinger
- Zhixue Zhao
- Steffen Eger
affiliations:
- University of Technology Nuremberg
- University of Sheffield
arxiv_id: '2609.01409'
url: https://arxiv.org/abs/2609.01409
pdf_url: https://arxiv.org/pdf/2609.01409
published: '2026-09-01'
collected: '2026-09-03'
category: Multimodal
direction: 多模态大模型 · 科研图表编辑
tags:
- VLM
- Scientific Editing
- TikZ
- Reinforcement Learning
- Dataset
- Fine-tuning
one_liner: 基于真实科研修订轨迹构建数据集，训练出性能赶超GPT-5.6-Sol的小参数TikZ图表编辑模型
practical_value: '- 可复用「从真实用户操作轨迹挖掘标注样本」的思路，替代高成本人工/合成标注，可直接用于电商主图/商详页生成、广告创意迭代等垂域的训练数据构造

  - 多任务联合训练+多维度互补RL奖励的范式可迁移，例如给创意生成Agent做微调时，可同时设置视觉还原度、修改指令符合度两个核心奖励信号

  - 小参数开源基座微调赶超闭源大模型的经验可复用，可大幅降低垂域编辑类Agent的部署与推理成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM在科研图表生成上表现优异，但出版级图表需要多轮迭代修改，当前编辑方法要么依赖昂贵的专有Agent系统，要么使用合成编辑数据做监督，泛化性差。
### 方法关键点
1. 挖掘arXiv、GitHub、TeX SE的真实修订数据，构建首个大规模真实修订来源的DaEdiTikZ数据集，包含391K TikZ编辑对、781K有向编辑指令
2. 构造790条人工精炼的测试基准DaEdiTikZ-Bench
3. 基于Qwen3.5训练4B/9B两款小参数模型，联合学习重建与编辑任务，再用渲染保真度、编辑适配度双奖励做RL微调
### 关键结果
9B模型自动评估优于所有测试基线；人工评估（9名标注员、4320次打分）效果超过GPT-5.6-Sol、与Gemini-3.1-Pro持平；分布外场景下，在2K序列长度区间仍与GPT-5.6-Sol竞争力相当。
