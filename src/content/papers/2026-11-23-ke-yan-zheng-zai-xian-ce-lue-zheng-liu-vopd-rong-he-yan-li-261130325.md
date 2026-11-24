---
title: Verifiable On-Policy Distillation
title_zh: 可验证在线策略蒸馏VOPD：融合验证奖励与稠密蒸馏监督
authors:
- Juntong Shi
- Stefano Ermon
- Jure Leskovec
- Minkai Xu
affiliations:
- Stanford University
- Google DeepMind
arxiv_id: '2611.30325'
url: https://arxiv.org/abs/2611.30325
pdf_url: https://arxiv.org/pdf/2611.30325
published: '2026-11-23'
collected: '2026-11-24'
category: Training
direction: 大模型训练 · 在线策略蒸馏优化
tags:
- On-Policy Distillation
- RLVR
- Knowledge Distillation
- LLM Training
- Reward Modeling
one_liner: 将稀疏可验证奖励转换为稠密监督，提升LLM在线策略蒸馏的性能与训练效率
practical_value: '- 电商/导购Agent小模型蒸馏场景：可将业务侧可验证奖励（如回答正确性、用户点击、转化率）作为VOPD的验证信号，投影到教师模型隐式奖励空间，将稀疏业务反馈转换为稠密token级监督，相比直接叠加RL+蒸馏的方案提升小模型对齐效果

  - 生成式推荐（如推荐文案、Semantic ID生成）场景：利用VOPD的自适应外推机制，当教师输出与业务验证奖励相关性高时强化蒸馏，相关性低时减弱甚至反向调整，避免蒸馏得到不符合业务效果的输出

  - 工程落地层面：VOPD仅额外增加1次冻结参考模型的前向传播，无额外验证器调用开销，相比其他RL+蒸馏融合方案计算成本提升极低，可直接接入现有OPD训练管线'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）可将LLM输出对齐到可自动校验的任务目标，但仅能提供序列级稀疏监督，样本利用效率极低；OPD（在线策略蒸馏）可提供全词表的稠密token级教师监督，但信号不与真实任务验证结果绑定，易蒸馏到不符合任务效果的输出。简单叠加两类优化目标仅能获得边际收益，缺乏将稀疏验证信号转换为稠密监督的统一机制。

### 方法关键点
- 基于OPD的隐式奖励视角，将反向KL蒸馏等价为最大化教师相对于参考模型的隐式奖励问题，把教师监督与验证器反馈统一到同一奖励空间
- 对每个prompt的同组采样回复，计算组内验证器奖励与教师累计隐式奖励的相关系数cx，作为验证信号的投影系数
- 通过Rao-Blackwellization将投影后的验证信号扩展到全词表，无需额外验证器调用即可得到稠密的验证感知token级监督
- 等价于自适应蒸馏外推：cx为正强化向教师蒸馏，cx为负则向初始参考模型回退，避免错误蒸馏

### 关键实验
在8个数学推理benchmark上测试两类蒸馏设置：同尺寸4B模型蒸馏时，VOPD平均准确率66.38，较vanilla OPD提升1.67个点，较固定外推的ExOPD提升1.13个点；4B教师蒸馏到1.7B小模型的强到弱设置下，VOPD平均准确率53.32，较OPD提升2.44个点，训练收敛速度较基线快30%以上。

### 核心结论
将稀疏验证/业务反馈与稠密教师蒸馏信号融合时，先统一到同一奖励空间再做投影，收益远高于简单叠加两类优化目标。
