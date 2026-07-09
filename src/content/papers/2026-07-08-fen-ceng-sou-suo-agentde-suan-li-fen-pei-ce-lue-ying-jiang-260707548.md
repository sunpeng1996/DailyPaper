---
title: 'Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?'
title_zh: 分层搜索Agent的算力分配策略：应将算力集中在任务分解环节
authors:
- Qinnan Cai
- Yibo Zhao
- Xiang Li
affiliations:
- East China Normal University
arxiv_id: '2607.07548'
url: https://arxiv.org/abs/2607.07548
pdf_url: https://arxiv.org/pdf/2607.07548
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: 搜索Agent架构 · 多角色算力分配
tags:
- Search Agent
- Hierarchical Multi-Agent
- Capacity Allocation
- Trajectory Distillation
- Multi-hop QA
one_liner: 通过受控实验明确分层搜索Agent的最优算力分配策略，蒸馏小模型执行器可降本提效
practical_value: '- 搭建搜索/导购/推荐类Agent时，优先把算力集中在上层任务分解、意图理解的主Agent，执行层（商品检索、属性抽取、优惠计算等原子子任务）可采用小模型，边际收益远高于给执行层堆大模型

  - 执行层小模型可复用质量过滤的轨迹蒸馏方案：保留原有正确执行样本避免能力退化，仅补充带明确信息增益的多轮执行样本，可匹配大模型效果同时降低30%+token消耗

  - 复杂电商query搜索、多轮导购场景可直接复用角色拆分架构：主Agent负责拆解用户多轮需求、调度子任务，子Agent各自处理独立原子任务，既解决单Agent上下文膨胀问题，又控制推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前分层搜索Agent普遍采用相同规模大模型承担所有角色，缺乏不同角色的算力分配最优方案指导，无法平衡效果与推理成本；同时单Agent架构存在上下文膨胀、规划与执行能力冲突的问题，大规模落地性价比低。

### 方法关键点
- 将分层搜索拆分为3个独立解耦角色：任务委托（主Agent负责复杂Query分解、子任务调度、终止判断）、执行（子Agent负责检索、证据抽取、返回精简报告）、答案生成（固定为Qwen3-32B，控制混淆变量，仅调整前两个角色的模型规模）
- 执行层小模型采用质量过滤的轨迹蒸馏：保留学生模型正确的单轮检索样本避免能力退化，仅加入教师输出的带有效信息增益的多轮检索样本，训练时掩码掉检索到的原始文本避免过拟合

### 关键实验
在5个多跳QA数据集（HotpotQA、2WikiMultihopQA等共3869条测试样本）上做受控对比：
1. 角色拆分架构比同规模单Agent的Exact Match（EM）提升4.5~8.6个百分点
2. 算力敏感性显著不对称：主Agent规模从1.7B升级到前沿大模型，EM提升~11分；执行层从1.7B升级到前沿大模型，EM仅提升~2.6分
3. 经过蒸馏的1.7B执行器效果超过前沿大模型执行器，同时子Agent token消耗降低37%

### 核心结论
分层Agent的性能天花板由上层任务分解能力决定，执行层即使采用小模型也不会成为瓶颈，优先把算力投入规划层可获得最高ROI
