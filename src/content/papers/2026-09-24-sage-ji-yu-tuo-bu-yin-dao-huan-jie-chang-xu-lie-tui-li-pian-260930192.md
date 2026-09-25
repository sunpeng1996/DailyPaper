---
title: 'SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance'
title_zh: SAGE：基于拓扑引导缓解长序列推理偏差
authors:
- Xinyue Zeng
- Jiawei Zhang
- Yujun Yan
- Dawei Zhou
affiliations:
- Virginia Tech
- University of Wisconsin Madison
- Dartmouth College
arxiv_id: '2609.30192'
url: https://arxiv.org/abs/2609.30192
pdf_url: https://arxiv.org/pdf/2609.30192
published: '2026-09-24'
collected: '2026-09-25'
category: Reasoning
direction: 长序列推理 · 拓扑引导优化
tags:
- Long-Horizon Reasoning
- Structural Guidance
- Sparse Reward
- LLM Training
- Topological Reasoning
one_liner: 提出SAGE框架，结合代数稀疏化与双曲引导，缓解LLM长序列推理两类结构性偏差
practical_value: '- 针对推荐/广告系统长序列用户行为建模、智能导购Agent多步决策类任务，可借鉴代数稀疏化思路，RL训练时对候选动作做算子子空间投影，抑制无效分支探索，降低长路径试错成本

  - 长链路稀疏奖励场景（如大促全链路转化优化、多轮推荐最终GMV归因）可复用双曲结构引导方案，将中间状态嵌入负曲率空间生成稠密深度感知奖励，解决奖励延迟导致的梯度消失问题

  - 业务中用GRPO/RLHF训练推理类模型时，可直接复用SAGE的结构引导增强优势函数的设计，无需额外标注过程监督数据即可提升长序列任务训练效率，降低标注成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM长序列推理在稀疏奖励场景下存在两类结构性偏差：一是探索偏差，模型易陷入局部合理但全局无效的分支；二是累积偏差，小的局部误差随路径深度放大，最终导致任务失败。现有基于结果的RL方法要么依赖密集过程监督、标注成本极高，要么未利用推理空间的结构特征、优化效率极低，难以落地长路径任务。

### 方法关键点
- 提出Symbolic Closure Analysis（SCA）理论框架，将长序列推理建模为局部可允许变换的序列，从理论上证明两类偏差的来源是可行区域占比随路径深度指数下降、稀疏终端奖励不足以修正早期偏差
- 设计SAGE训练框架，包含两类互补的结构引导：①代数稀疏化：将候选动作投影到算子索引的代数子空间，计算候选与当前残差的匹配度，抑制无效分支以缓解探索偏差；②双曲结构引导：将推理状态嵌入庞加莱球，用与目标的双曲距离生成稠密深度信号，缓解累积偏差
- 结构引导仅在训练时注入，推理无额外开销，无需过程监督标注

### 关键结果
覆盖12个推理基准、7类模型家族，对比SFT、GRPO、EMPO、GRPO-PRM等基线：①数学推理任务上，35B参数Qwen3.5结合SAGE后平均准确率达64.86%，超过70B Llama3.3-Instruct 26.38个百分点，比最强基线高2.49个点；②真实世界长序列Andrews-Curtis任务上，成功率较基线提升最高达8倍，有效步骤占比提升19.2~26.0个百分点。

> 值得记住：长序列稀疏奖励场景下，利用任务内在结构生成免标注的引导信号，成本远低于过程监督标注，效果甚至更优。
