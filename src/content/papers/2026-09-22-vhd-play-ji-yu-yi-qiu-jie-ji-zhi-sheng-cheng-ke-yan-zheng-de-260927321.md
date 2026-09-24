---
title: 'Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved
  Mechanisms'
title_zh: VHD-Play：基于已求解机制生成可验证的智能体RL训练环境
authors:
- Xinjie Shen
- Wei Fan
- Xudong Guo
- Jianhong Tu
- Yang Su
- Chuqiao Kuang
- Yinger Zhang
- Dayiheng Liu
affiliations:
- Georgia Institute of Technology
- Alibaba Group
arxiv_id: '2609.27321'
url: https://arxiv.org/abs/2609.27321
pdf_url: https://arxiv.org/pdf/2609.27321
published: '2026-09-22'
collected: '2026-09-24'
category: Agent
direction: Agent 长周期训练环境自动生成
tags:
- Agent Training
- RL Environment
- Verifiable Reward
- Mechanism-first
- Long-horizon Agent
one_liner: 反转环境构建顺序，基于已求解数学机制生成带可靠奖励的低成本Agent训练环境
practical_value: '- 做电商长周期运营、供应链规划类Agent时，可复用机制优先思路：直接基于已求解的运筹学模型（库存DP、路径规划等）生成训练环境，无需人工开发复杂模拟器，同时保证奖励信号100%准确无偏差

  - 训练长交互Agent时，可借鉴其信息不对称接口设计：区分信息探测和决策动作，强制Agent学习主动信息采集+跨周期全局决策，避免只会解决全信息给定的静态问题

  - 做Agent能力评估时，可复用「书面全信息版/有状态交互版同题对比」范式，精准定位Agent的交互决策短板，而非仅评估基础推理能力'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent落地长周期交互任务（如电商365天自主运营、多轮工具调用、旅行规划）时，极度缺乏低成本、奖励信号可靠的多样化有状态训练环境。现有环境生成流程多为先构建环境再定义奖励规则，存在环境逻辑与奖励不匹配、人工标注/开发成本高、训练出来的交互能力泛化性差等问题，且模型的静态问题求解能力很难直接迁移到动态交互场景。

### 方法关键点
- 机制优先构建逻辑：先采样11类成熟运筹学数学模型（库存DP、背包、路径规划、线性/二次规划等），用官方求解器算出最优解、默认策略解作为固定奖励锚点，再生成环境，保证环境动态和奖励规则同源无偏差
- 语料接地生成：基于真实业务语料将求解后的模型渲染为具体场景、可调用工具和交互接口，完全隐藏模型参数，Agent仅能通过交互动作（探测/决策）获取信息，模拟真实场景的信息不对称性
- 自动准入校验：生成的环境需经过可执行性、奖励一致性校验后才准入训练，单环境生成成本仅0.01-0.03美元，共生成3300个合格环境
- 无偏奖励设计：采用`(当前策略得分-默认策略得分)/(最优解得分-默认策略得分)`做归一化0-1奖励，全程无人工标注、无LLM裁判参与

### 关键实验
基底模型为Qwen3.6-35B-A3B，对比基线为原生Qwen3.6-35B、Qwen3.7-Max：
1. 训练后5类优化任务的平均Agentic得分从0.204提升至0.815，跨8个未见过的机制家族仍有稳定提升
2. 电商365天运营Bench上，训练后模型最终余额为基线的3.4倍，超过Qwen3.7-Max，全程无破产
3. BFCL V4交互类任务平均得分提升2.84分，TravelBench规划得分从0.700提升至0.794

### 核心结论
LLM的静态书面问题解决能力和动态有状态交互能力存在巨大差距，大部分可提升空间来自交互决策训练而非基础推理能力优化
