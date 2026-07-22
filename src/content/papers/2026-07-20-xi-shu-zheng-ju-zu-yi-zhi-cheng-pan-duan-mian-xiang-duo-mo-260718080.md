---
title: 'Sparse Evidence Can Suffice: Agentic Evidence Seeking for Multimodal Video
  Misinformation Detection'
title_zh: 稀疏证据足以支撑判断：面向多模态视频虚假信息检测的智能体证据检索框架
authors:
- Haochen Zhao
- Yongxiu Xu
- Xinkui Lin
- Dong Xie
- Jiarui Lu
- Yuqi Qian
- Yubin Wang
- Hongbo Xu
- Gaopeng Gou
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
- Baidu
arxiv_id: '2607.18080'
url: https://arxiv.org/abs/2607.18080
pdf_url: https://arxiv.org/pdf/2607.18080
published: '2026-07-20'
collected: '2026-07-22'
category: Agent
direction: 多模态Agent · 稀疏证据主动检索
tags:
- Agent
- Multimodal
- Reinforcement Learning
- GRPO
- Misinformation Detection
one_liner: 提出主动选择稀疏多模态证据的SIEVE框架，在多个视频虚假信息检测基准上实现SOTA性能
practical_value: '- 可复用「证据获取+校验解耦」的Agent范式到电商短视频合规审核、商品卖点真实性校验场景，将长视频拆分为时间槽+多模态通道，由Agent主动选取关键证据，避免全量处理冗余内容，大幅降低推理算力消耗

  - 四阶段训练流程可直接迁移到所有预算约束下的Agent决策任务：先通过强基座生成教师轨迹做SFT，再用GRPO做RL优化，奖励同时覆盖任务正确性、证据质量、交互成本，兼顾效果和效率

  - 稀疏证据的结论可复用在推荐系统用户行为理解、商品评论审核等高冗余数据场景，仅抓取少量关键特征即可完成决策，降低端到端模型的冗余计算开销

  - 零样本跨域泛化能力优异，可直接迁移到不同业务场景的内容审核任务，无需针对新场景标注大量训练数据，降低冷启动成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态视频虚假信息检测多采用全量输入单轮推理范式，冗余内容占比高，关键证据易被淹没，不仅算力消耗大，还容易出现决策不可靠、可解释性差的问题；而现实场景中虚假信息的核心判别证据往往稀疏分布，无需全量处理即可完成判断。

### 方法关键点
1. 提出SIEVE框架，将证据获取与真伪校验解耦：证据检索Agent在预设读取预算约束下，从按镜头拆分的时间槽多模态通道（OCR/ASR/上下文帧/关键帧）中主动选取证据，打包后交给独立校验器完成真伪判断
2. 四阶段训练：先用强VLM生成合规教师轨迹做Agent SFT，再用高质量证据包训练校验器（训练完成后冻结），最后用GRPO强化学习优化Agent策略，奖励函数同时覆盖判断正确性、证据多样性、交互成本三个维度
3. 校验器仅能访问Agent选中的证据，无法接触全量输入，保证决策完全基于所选证据，避免信息泄露

### 关键实验结果
在中文FakeSV、英文FakeTT两个基准上，SIEVE的Macro-F1分别达92.41%、90.72%，较之前SOTA提升2.44、2.74个百分点；仅8次证据读取即可覆盖97%的可纠错样本，12次读取达到性能饱和，远低于全量处理的算力消耗；零样本跨域测试FakeVV数据集，ACC达73.2%，超过GPT-5.5的67.8%。

### 核心结论
高冗余多模态任务中，智能体主动筛选的少量稀疏关键证据，效果优于全量输入的暴力处理，同时还能输出可解释的决策路径。
