---
title: 'Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested
  Scattering Layer over LLM Reasoning Paths'
title_zh: 可审计、守恒性保障、博弈论验证的LLM推理路径散射层Deposon
authors:
- Qihao Yuan
affiliations:
- Renmin University of China
arxiv_id: '2609.09001'
url: https://arxiv.org/abs/2609.09001
pdf_url: https://arxiv.org/pdf/2609.09001
published: '2026-09-08'
collected: '2026-09-09'
category: Reasoning
direction: LLM推理路径 · 可审计守恒层
tags:
- Reasoning
- Auditability
- Game Theory
- Scattering Layer
- Conservation
one_liner: 为LLM多步推理路径提供带严格守恒保证的可审计散射层，精度与六关键词规则过滤器无差异
practical_value: '- 电商导购Agent、广告投放策略Agent的决策溯源场景，可借鉴T+R+A=1守恒记账逻辑，为每步推理决策留存可复算的能量分配记录，无需依赖自然语言CoT的真实性，满足合规审计要求

  - 路径筛选场景若当前采用规则过滤器做剪枝，遇到对抗性语义陷阱（如恶意商品标题绕过关键词规则）时，可替换为语义类型标签转能量决策的机制，无需读取标签字符串，规避规则逃逸问题

  - 推荐/搜索系统多信号融合时，可复用该研究的线性融合负结论：线性凸组合融合结构信号与语义信号必然带来效果稀释，需直接采用非线性融合机制，避免无效实验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多步LLM推理的路径剪枝、淘汰过程无留痕，无法事后审计淘汰原因，Chain-of-Thought中间文本也不能保证与内部计算一致，现有可验证方案要么聚焦组织层合规，要么在密码层做校验，缺少推理路径层面的运行时可验证不变量层。

### 方法关键点
* 提出Deposon散射层，将LLM生成的概念分解图每个节点绑定双参数Deposon状态，路径能量按三通道分配：传输T、反射R、不可逆耗散A，构造上严格满足T+R+A=1
* 按节点语义类型分配预定义参数，陷阱节点、运算节点、普通节点的耦合系数差异化设置，能量沿路径递归传递，淘汰路径的耗散能量计入单调递增计数器不可恢复
* 将推理的反向动力学建模为图上的势博弈，定义可审计的标量势函数，用经验协调比ECR量化自利动态和最优解的差距

### 关键结果
* 合成陷阱基准上，统一模式路径筛选准确率100%，远高于诱饵捕获基线的7%/10%
* 真实基准GSM8K、StrategyQA上，散射层精度和六关键词规则过滤器无统计差异（GSM8K 0.85 vs 0.87，McNemar p=0.5；StrategyQA均为0.899）
* 能量审计最大偏差2.2×10^-16，达到双精度机器epsilon水平
* 线性凸组合融合散射层和语义先验会导致效果下降（物理题0.484→0.452），仅非线性融合可能带来增益

### 核心记忆点
该层的核心价值不在推理精度提升，而在每步决策都留下可被第三方用双精度算术复算的守恒账本，完全不依赖中间文本的真实性。
