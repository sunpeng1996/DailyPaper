---
title: 'Agentic Abstention: Do Agents Know When to Stop Instead of Act?'
title_zh: 智能体弃权：LLM智能体是否知道何时该停止而非行动
authors:
- Han Luo
- Bingbing Wen
- Lucy Lu Wang
affiliations:
- University of Leeds
- Southwest Jiaotong University
- University of Washington
- Allen Institute for AI
arxiv_id: '2606.28733'
url: https://arxiv.org/abs/2606.28733
pdf_url: https://arxiv.org/pdf/2606.28733
published: '2026-06-26'
collected: '2026-06-30'
category: Agent
direction: Agent 决策 · 不确定性弃权
tags:
- LLM Agent
- Abstention
- Context Engineering
- Sequential Decision
- Tool Use
one_liner: 定义多轮工具调用智能体的适时弃权问题，提出无需调参的CONVOLVE上下文工程改进方法
practical_value: '- 电商导购Agent、搜索助手Agent可复用CONVOLVE思路，从历史交互蒸馏停止规则注入上下文，减少无效工具调用，降低成本与延迟

  - 针对电商场景中用户需求模糊、目标商品不存在的情况，将适时弃权（主动澄清/告知无货）作为优化目标，体验优于强行推荐错误商品

  - 该论文结论验证：更大模型仅提升最终弃权召回，不提升适时弃权性能，不必盲目堆大模型做停止决策'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent研究大多聚焦提升任务完成率，忽略了任务不可行（用户需求模糊、环境中不存在目标商品、任务前提错误等）时，智能体需要适时停止行动的问题。传统LLM弃权是单轮答案/弃权决策，而多轮交互Agent中，任务不可行往往需要交互后才能发现，属于序列决策问题；不当的持续行动会产生大量无效工具调用，浪费算力、降低用户体验，因此该问题亟待研究。

### 方法关键点
- 定义Agentic Abstention为序列决策问题，动作空间分为三类：完成任务回答、停止弃权、继续交互收集信息，其中弃权包含告知任务不可行、请求用户澄清两种终止动作
- 构建覆盖网络购物、终端任务、交互式QA三类场景的基准数据集，共2.8万+任务，涵盖请求型弃权（指令本身不可行）、环境型弃权（交互后才发现不可行）两类场景
- 提出CONVOLVE上下文工程方法：通过离线分析全交互轨迹，蒸馏提炼可复用的停止规则，形成动态playbook注入Agent上下文，全程无需更新模型参数

### 关键实验结果
在13种LLM、2种Agent架构上评估发现：所有测试模型平均适时弃权召回低于40%，多数模型最终弃权召回也低于50%；WebShop场景下，Llama-3.3-70B原模型的适时弃权召回仅26.7%，加入CONVOLVE后提升至57.4%，整体弃权召回从83.2%提升至100%；验证得到核心结论：模型缩放仅提升最终弃权召回，不提升适时弃权性能；增强推理能提升适时召回但会降低整体召回；小模型学习的停止规则可直接迁移给大模型使用，效果接近大模型自学习的规则。

### 核心结论
可靠的Agent不仅需要更强的任务完成能力，还需要判断何时继续行动不再有用的判断力
