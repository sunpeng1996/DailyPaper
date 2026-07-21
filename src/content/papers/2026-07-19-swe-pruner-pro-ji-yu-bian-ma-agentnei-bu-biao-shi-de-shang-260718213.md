---
title: 'SWE-Pruner Pro: The Coder LLM Already Knows What to Prune'
title_zh: SWE-Pruner Pro：基于编码Agent内部表示的上下文剪枝方法
authors:
- Yuhang Wang
- Yuling Shi
- Shaoqiu Zhang
- Jialiang Liang
- Shilin He
- Siyu Ye
- Yuting Chen
- Kai Cai
- Xiaodong Gu
affiliations:
- 上海交通大学LLM4SE Lab
- Douyin Group
arxiv_id: '2607.18213'
url: https://arxiv.org/abs/2607.18213
pdf_url: https://arxiv.org/pdf/2607.18213
published: '2026-07-19'
collected: '2026-07-21'
category: Agent
direction: Agent 长上下文剪枝效率优化
tags:
- Context Pruning
- Coding Agent
- LLM Efficiency
- Hidden State
- Prompt Compression
one_liner: 复用编码Agent预计算隐状态加轻量头实现无额外模型的上下文剪枝，降本提效不降质
practical_value: '- 多轮Agent上下文管理无需额外部署独立打分模型、也无需让Agent显式输出意图hint，直接复用LLM预填阶段生成的最后一层隐状态做内容重要度过滤，可大幅降低额外开销，适合电商导购Agent、商品问答Agent等场景

  - 训练内容重要度分类头时采用per-sample平衡focal loss，针对每个样本内部的类别不平衡做加权，而非全局平衡，可有效提升小占比关键内容（如用户核心需求、商品核心属性）的召回

  - 给重要度打分模块增加长度感知嵌入，对短输入执行更严格的少剪策略、长输入执行更宽松的多剪策略，可避免短关键信息被误剪，适配长度波动大的用户query、商品详情、商家回复等内容

  - 工程上可将轻量剪枝头与推理引擎端侧集成，复用预填阶段的隐状态与KV cache，无需额外模型调用，仅增加极低推理开销，适合上线高吞吐Agent服务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮编码Agent交互过程中会积累大量冗余工具输出，占总token消耗的70%以上，既推高推理成本又引发长上下文性能退化；现有剪枝方法要么用固定指标无法适配Agent动态意图，要么需要额外独立打分模型和Agent显式输出目标提示，额外开销高，浪费了LLM处理输入时已经计算好的隐状态中天然携带的内容重要度信息。

### 方法关键点
- 直接复用Agent冻结主干在工具响应预填阶段生成的最后一层隐状态，加轻量MLP剪枝头输出每token保留/剪枝概率，按行粒度投票生成最终剪枝结果，无需修改主干、也不需要额外模型调用
- 加入长度感知嵌入，根据工具响应的行数给隐状态加对应嵌入，让剪枝策略适配不同长度输入（短输入少剪避免误删关键信息，长输入多剪降本）
- 训练采用per-sample平衡focal loss，对每个样本内部的保留/剪枝类别分别计算损失再等权合并，解决单样本内类别不平衡问题，提升稀有关键行的召回

### 关键结果数字
在2个MoE开源编码主干（MiMo-V2-Flash、Qwen3-Coder-Next）、4个多轮基准上对比7种剪枝方法：
1. 最高节省39%的prompt+completion token，推理额外开销仅占总生成时长的15%左右
2. 在MiMo-V2-Flash上SWE-Bench Verified任务解决率提升+3.8%，长上下文Oolong基准准确率提升+2.2个点
3. 是唯一在所有测试场景下都能减少token消耗同时基本保留任务效果的剪枝方法

### 核心结论
与其在Agent外部重建剪枝信号，直接读取Agent处理输入时已经形成的内部表示，就足够得到准确的内容重要度判断
