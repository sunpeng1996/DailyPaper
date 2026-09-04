---
title: 'Rethinking On-Policy Distillation of Large Language Models II: One Training
  Example'
title_zh: 大模型On-Policy蒸馏再思考II：仅用单个训练样本的蒸馏
authors:
- Zixuan Fu
- Bingxiang He
- Yuxin Zuo
- Haohuan Huang
- Jinqian Zhang
- Ruhang Xiao
- Cheng Qian
- Qinyu Luo
- Huan-ang Gao
- Yudong Wang
affiliations:
- Tsinghua University
- University of Chinese Academy of Sciences
- Northeastern University
- University of Illinois Urbana-Champaign
- Johns Hopkins University
arxiv_id: '2609.04172'
url: https://arxiv.org/abs/2609.04172
pdf_url: https://arxiv.org/pdf/2609.04172
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 大模型训练 · On-Policy蒸馏效率优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- Training Efficiency
- LLM Fine-tuning
- Multi-Teacher Distillation
one_liner: 证明单条训练query可恢复全量OPD 72%增益，16条语义多样query即可匹配全量数据训练效果
practical_value: '- 做LLM驱动的电商导购Agent、生成式推荐模型蒸馏时，无需囤积大量训练query，仅需16条左右语义差异大的样本即可达到全量数据90%+效果，大幅降低数据采集/标注成本

  - 用OPD做电商营销文案生成、智能客服应答等垂直场景小模型蒸馏时，可优先优化吸收速率而非增加训练数据量，比如调整学习率、复用batch多轮训练提升效率，OPD核心瓶颈是算法吸收能力而非数据供给

  - 多场景多教师蒸馏（如同时做推荐理由生成、售后应答、商品文案三个场景）时，每个场景仅需16条代表性query即可对齐全量数据训练效果，大幅降低多任务训练数据集构建成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
OPD已广泛用于Qwen3、GLM-5、DeepSeek-V4等前沿大模型后训练，但过往研究仅关注算法层面优化，完全忽略训练数据的作用，不清楚OPD达到最优效果所需的数据量阈值，数据与算法的交互机制也不明确，极大限制了OPD训练效率的优化空间。

### 方法关键点
- 采用One-Shot OPD极端实验设定，仅用单条训练query开展OPD训练，拆解数据供给和算法吸收两个效率维度的独立影响
- 定义state coverage指标，量化训练query生成的rollout所能覆盖的全量数据OPD访问过的语义状态簇比例
- 定义absorption rate指标，衡量每步训练能缩小的师生模型差距比例，分析训练过程中的对齐效率
- 覆盖单域OPD、多教师MOPD、RLVR等不同训练范式，对比小样本训练效果差异

### 关键结果
在数学推理、代码生成、指令跟随、Agent工具调用4个域测试，覆盖3个模型家族，以全量数据OPD为基线：
1. 单条query即可达到71.5%的state coverage，恢复全量OPD 72%的性能增益，效果不受query难度、响应长度、采样温度影响
2. 16条语义多样的query即可达到98.9%的state coverage，性能完全匹配全量数据OPD；多教师MOPD下每个域16条query同样匹配全量训练效果
3. 即使是无任务内容的模板、跨域WildChat query也能接近真实query的训练效果，OPD的1000步增益是同设定下RLVR的2倍以上

### 核心结论
OPD是数据过供给、算法饥饿的训练范式，瓶颈不在于训练数据量，而在于模型吸收监督信号的速率
