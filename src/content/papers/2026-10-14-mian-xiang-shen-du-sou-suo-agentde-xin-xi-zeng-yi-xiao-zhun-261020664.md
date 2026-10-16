---
title: Information-Gain Calibrated On-Policy Distillation for Deep Search Agents
title_zh: 面向深度搜索Agent的信息增益校准在策略蒸馏方法
authors:
- Chenxi Li
- Xueyang Feng
- Songyang Liu
- Chenxu Wang
- Xiaoying Tang
- Chaozhuo Li
- Litian Zhang
affiliations:
- 香港中文大学（深圳）
- 中国人民大学
- 北京邮电大学
- 北京人工智能研究院（BAAI）
arxiv_id: '2610.20664'
url: https://arxiv.org/abs/2610.20664
pdf_url: https://arxiv.org/pdf/2610.20664
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 搜索Agent · 在策略蒸馏优化
tags:
- On-Policy Distillation
- Search Agent
- Information Gain
- Knowledge Distillation
- LLM Agent
one_liner: 利用检索后信息增益校准在策略蒸馏的两个隐含先验，缓解深度搜索Agent的证据盲监督问题
practical_value: '- 做搜索类Agent蒸馏时，不要仅按token量分配监督权重，可通过每轮动作的信息增益重分配，将更多梯度倾斜给高价值搜索轮次，而非长文本回答合成轮，提升蒸馏效率

  - 工具调用类动作的监督不要只对齐老师的话术偏好，加入工具返回结果的实际效用校准：比如电商导购Agent的查询动作，能召回有效商品的查询就算和老师写法不同也应被奖励，避免惩罚有用的非标查询

  - 蒸馏初期不要直接上强后验校正，用cosine schedule逐步加大校正权重，避免前期学生能力弱时过度惩罚搜索动作，导致学生不敢调用工具

  - 信息增益计算仅需额外用老师对参考答案打分，无需新增rollout，训练开销仅增加10%左右，推理完全无开销，适合工业界落地小参数搜索Agent'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
深度搜索Agent通常需要大模型RL训练获得工具调用能力，部署成本高，在策略蒸馏（OPD）是将大老师能力迁移到小模型的主流方案，但传统OPD存在证据盲监督（EBS）问题：仅用检索前上下文给学生的查询动作打分，不考虑后续返回证据的实际价值，导致高信息价值的搜索轮次监督不足、能召回有效证据的查询因不符合老师话术被误罚。实证显示传统OPD中首次搜索轮贡献51.1%的总信息增益，却仅拿到18%的监督预算，43.7%的查询的老师打分与实际信息效用符号相反。
### 方法关键点
- 信息引导的轮次信用校准（ITC）：用每轮检索后的信息增益绝对值替换原token量占比，重新分配各轮监督权重，用tanh限制极端增益的权重占比，保留回答合成轮的基线监督
- 信息引导的查询偏好校准（IQC）：对搜索动作的关键token，用检索后信息增益的符号调整更新方向，有用查询即使不符合老师偏好也加分，无用查询反之
- 采用cosine schedule逐步增加IQC的校正权重，避免训练初期学生搜索能力弱时被过度惩罚，不敢调用搜索工具
### 关键实验
在6个多模态搜索基准上测试，以8B参数搜索Agent为老师蒸馏2B/4B学生：相比传统OPD，IG-OPD让2B学生平均准确率提升3.4pp，4B学生提升1.7pp；4B学生在MMSearch、BrowseComp-VL两个基准上超过8B老师，金证据召回率相对提升14.7%；训练仅增加11.6%耗时、10.6%显存开销，推理无额外成本。
### 核心结论
工具调用类Agent的蒸馏不要仅做话术模仿对齐，结合环境返回的实际效用校准监督信号，可让小模型突破老师能力上限
