---
title: 'PORT: Preference Optimization via Robust Token-Level Reweighting'
title_zh: PORT：基于鲁棒Token级重加权的偏好优化方法
authors:
- Ding Zhu
- Xiukun Wei
- Tian Xie
- Zhihui Zhu
- Xueru Zhang
- Mohammad Mahdi Khalili
affiliations:
- The Ohio State University
arxiv_id: '2611.12763'
url: https://arxiv.org/abs/2611.12763
pdf_url: https://arxiv.org/pdf/2611.12763
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: 大模型对齐 · 鲁棒偏好优化
tags:
- Preference Optimization
- DPO
- Token-level Reweighting
- Noisy Annotation
- LLM Alignment
one_liner: 提出无需额外反向传播和外部奖励模型的Token级重加权框架，提升偏好优化对标注噪声的鲁棒性
practical_value: '- 做生成式推荐、Agent对齐时，若偏好标注数据噪声高（比如用户交互隐含的偏好存在歧义、驳回的回复中包含有效偏好信息），可复用PORT的Token级重加权思路，无需全序列降权驳回回复，保留有效学习信号

  - 工程上PORT的权重计算仅需单次前向传播，无额外反向开销，可直接嵌入现有DPO训练 pipeline，无需引入外部奖励模型，适配LoRA微调、全量微调等场景，落地成本极低

  - 处理噪声偏好数据时，可复用基于batch内Token log-prob CDF的噪声检测思路，无需额外标注即可识别高风险Token，替代现有全序列过滤策略，减少有效数据浪费'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有DPO等序列级偏好优化方法默认偏好对的全序列标注完全准确，但实际工业场景下偏好标注普遍存在20%-40%的噪声（标注错误、语义歧义、部分内容正确但整体被驳回），全序列统一加权会错误惩罚驳回回复中的有效信息，同时引入梯度偏差；现有Token级优化方法依赖外部奖励模型，带来额外计算开销和奖励泛化风险。

### 方法关键点
- 理论推导得到最优Token权重的上界最小化目标，明确高噪声、高梯度范数的Token应分配更低权重
- 采用batch内所有Token的log-prob经验CDF差值作为代理信号，无需计算真实梯度范数和噪声率，权重计算仅需单次前向传播，无额外反向开销
- 仅修改偏好优化目标的Token加权逻辑，兼容DPO、IPO、SLiC-HF等主流偏好优化算法，无需改动现有训练 pipeline 结构

### 关键结果
在AlpacaFarm、Anthropic HH、PKU-Beaver三个基准数据集上，对比DPO、cDPO、β-DPO、Dr.DPO等10+基线：
- AlpacaFarm 30%标注噪声下，LLaMA2-7B上Port比最优序列级基线高0.4 Gold RM分，GPT胜率高4.4%
- Anthropic HH 40%标注噪声下，Safety Rate比最优基线高0.06，GPT胜率高5%
- 噪声强度越高，PORT的收益越大，batch size≥4即可获得稳定效果，无需超大batch支撑

### 核心结论
偏好标注的噪声往往是局部的，Token级细粒度加权比序列级粗粒度处理能在更低落地成本下获得更好的噪声鲁棒性
