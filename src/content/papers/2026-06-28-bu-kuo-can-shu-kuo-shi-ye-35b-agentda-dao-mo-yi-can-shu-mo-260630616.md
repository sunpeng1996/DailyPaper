---
title: 'Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance
  with a 35B Agent'
title_zh: 不扩参数扩视野：35B Agent达到万亿参数模型性能
authors:
- Lei Bai
- Zongsheng Cao
- Yang Chen
- Zhiyao Cui
- Shangheng Du
- Yue Fan
- Shiyang Feng
- Zijie Guo
- Haonan He
- Liang He
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2606.30616'
url: https://arxiv.org/abs/2606.30616
pdf_url: https://arxiv.org/pdf/2606.30616
published: '2026-06-28'
collected: '2026-06-30'
category: Agent
direction: Agent 长轨迹任务能力缩放
tags:
- LLM Agent
- MoE
- Long-horizon
- Knowledge Distillation
- Agent Scaling
one_liner: 提出35B MoE Agent Agents-A1，靠扩展任务视野而非参数，追平万亿参数模型性能
practical_value: '- 业务端构建大Agent可走「分领域训专家老师+蒸馏到统一学生」的降本路线，不用盲目堆大参数，控制推理部署成本

  - 多轮长流程任务（如深度搜索、智能导购）可复用知识-动作图（KAG）结构存储全流程监督信号，比仅用最终答案训练效果更好

  - 整合多领域异构Agent能力时，可采用领域硬路由+领域归一化蒸馏损失，避免高频大领域梯度压制小众能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前构建高性能Agent的主流路线要么直接堆万亿级模型参数，成本极高，难以落地；走扩展任务视野路线则存在两个核心瓶颈：一是缺少能连接外部知识、动作、观测和验证信号的训练基础设施，二是难以将多个异构领域的差异化能力整合进同一个Agent。该工作探索低成本构建高性能长任务Agent的可行路径。

### 方法关键点
1. 搭建长视野知识-动作基础设施，构建知识-动作图（KAG）存储全流程的状态、动作、观测、验证结果，通过自博弈搜索扩张生成高质量数据，最终得到平均长度45K token的长轨迹训练集；
2. 采用三段式训练流程：第一步全领域Supervised Fine-Tuning对齐通用Agent行为；第二步分领域训练专属专家老师模型，每个领域用针对性的SFT或RL优化能力；第三步提出带Salient Vocabulary Alignment的领域路由On-Policy蒸馏，硬路由每个样本匹配对应领域老师，用领域归一化损失平衡梯度，整合多老师能力到单个35B MoE学生模型。

### 关键结果
对比Kimi-K2.6、DeepSeek-V4-pro两个1T参数基线模型，35B的Agents-A1在多个长任务基准上实现超越：SEAL-0(56.4)、IFBench(80.6)、HiPhO(46.4)、FrontierScience-Olympiad(79.0)、MolBench-Bind(56.8)，在SciCode、HLE、BrowseComp也保持强竞争力。

最值得记住的一句话：做大Agent可以选择扩展任务视野而非单纯扩展模型参数，小模型也能达到万亿参数模型的长任务性能。
