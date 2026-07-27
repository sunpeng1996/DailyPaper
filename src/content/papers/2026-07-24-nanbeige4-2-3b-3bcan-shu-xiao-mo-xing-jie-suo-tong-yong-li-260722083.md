---
title: 'Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Mode'
title_zh: Nanbeige4.2-3B：3B参数小模型解锁通用Agent能力
authors:
- Nanbeige Lab
- ':'
- Chen Yang
- Chengrui Huang
- Fufeng Lan
- Hanhui Chen
- Hao Zhou
- Huatong Song
- Jiaqi Cao
- Jiaying Zhu
affiliations:
- Nanbeige LLM Lab
- Boss Zhipin
arxiv_id: '2607.22083'
url: https://arxiv.org/abs/2607.22083
pdf_url: https://arxiv.org/pdf/2607.22083
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 小参数通用Agent能力优化
tags:
- Small-LLM
- Agent
- Looped-Transformer
- RLHF
- Tool-Use
one_liner: 采用Looped Transformer与多阶段RL训练，3B参数Agent性能超越Qwen3.5-9B、Gemma4-12B
practical_value: '- 轻量化部署架构选择：可复用Looped Transformer结构，在不增加参数量的前提下提升有效计算深度，适合边缘侧导购Agent、端侧搜索推荐智能助手的低成本落地

  - Agent训练数据构造：可借鉴「真实API+本地模拟+LLM仿真」的混合环境轨迹合成方案，配合执行反馈驱动的turn-level过滤，快速生成高质量电商客服、导购工具调用训练数据

  - RL优化思路复用：可落地多阶段RL pipeline：先用RLHF解决格式错误、生成循环等基础问题，再加长度控制奖励压缩推理成本，最后用过程+结果联合奖励提升长周期Agent任务稳定性

  - SFT课程设计参考：三阶段逐步提升长上下文、Agent数据占比的训练方案，可直接迁移至多轮交互推荐、长序列用户行为建模的微调场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前小参数LLM的Agent能力通常局限于单领域，无法同时覆盖代码、办公、通用工具调用等多场景需求，且易牺牲通用推理性能；而业务侧对低部署成本、高能力的轻量化Agent需求强烈，亟需在有限参数预算下实现通用Agent能力的方案。

### 方法关键点
- 架构：采用Looped Transformer结构，2次复用Transformer层栈，从零预训练28T tokens，不增加参数量的前提下提升模型有效计算深度
- 数据：构建跨代码、工具调用、办公协同三大领域的执行可验证轨迹数据集，混合真实在线服务、本地Python实现、LLM仿真三类环境，基于执行反馈做turn-level质量过滤
- 训练：三阶段SFT课程逐步将上下文长度从64K扩展到256K，同步提升Agent数据占比；多阶段RL依次完成混合思考模式RLHF、长度可控推理RL、过程-结果联合奖励的Agent RL

### 关键结果
在全部通用Agent、代码Agent基准上超越Qwen3.5-9B、Gemma4-12B，其中PinchBench-V2得分74.7%（Qwen3.5-9B为68.2%），SWE-bench Verified得分63.6%（Qwen3.5-9B为53.1%）；推理能力在5/6项公开基准上最优，对齐能力与更大模型持平；OpenClaw框架下本地个人助手任务全维度优于Qwen3.5-9B，办公场景得分领先30%以上。

### 核心结论
小参数模型通过架构创新、高质量执行轨迹数据、针对性RL训练，可实现超越数倍参数量模型的通用Agent能力，大幅降低Agent落地的部署门槛。
