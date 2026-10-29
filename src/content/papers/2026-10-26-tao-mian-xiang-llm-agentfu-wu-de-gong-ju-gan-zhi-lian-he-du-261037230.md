---
title: 'TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving'
title_zh: TAO：面向LLM Agent服务的工具感知联合调度框架
authors:
- Shuhuai Li
- Shengdong Ye
- Dongdong Ge
- Yinyu Ye
- Jianghao Lin
affiliations:
- Shanghai Jiao Tong University
- Stanford University
arxiv_id: '2610.37230'
url: https://arxiv.org/abs/2610.37230
pdf_url: https://arxiv.org/pdf/2610.37230
published: '2026-10-26'
collected: '2026-10-29'
category: Agent
direction: Agent 推理服务工具感知调度优化
tags:
- LLM Agent
- Scheduling
- KV Cache
- GPU Inference
- Tool Calling
one_liner: 提出面向LLM Agent服务的工具感知联合调度框架，较SOTA最高降26.8%时延、提29.5%解码吞吐量
practical_value: '- 搭建电商对话导购/广告Agent推理服务时，可复用工具返回就绪性信号优先调度即将返回结果的会话，降低TTFT，显著提升用户交互体验

  - 多轮对话式推荐/Agent服务的调度策略可引入带时间衰减的KV cache信用机制，优先调度KV缓存未过期的会话，减少prefill计算开销，提升GPU利用率10%以上

  - 高并发Agent服务调度可借鉴多背包动态规划的求解思路，联合评估多会话的调度价值后做全局最优分配，避免单会话启发式调度的局部最优问题，提升整体吞吐量

  - 工具时延预测可复用「直接进度信号→工具维度历史均值→全局默认值」的降级策略，用极低计算成本获得稳定的就绪性预测结果，适合工业化部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent服务交替执行GPU侧推理、CPU侧外部工具调用，现有调度系统普遍忽略工具返回就绪性信号，且采用启发式单会话调度策略，导致GPU资源浪费、调度决策局部次优，高并发场景下时延高、吞吐量低，严重制约Agent服务的交互体验和资源利用率。
### 方法关键点
- 会话评估层设计三元组价值评分：带时间衰减的KV cache信用（优先调度缓存未过期会话，减少重复prefill开销）、二值工具返回就绪性（优先调度1秒内需要GPU资源的会话）、token占用量（同等条件优先调度大上下文会话），无需手动加权融合多维度信号
- 调度决策层将多会话多节点调度建模为多背包问题，采用动态规划算法做全局最优的会话选择和节点分配，严格满足GPU容量约束，避免单会话启发式调度的局部最优问题
- 工具就绪性预测采用分层降级策略：优先取工具返回进度/超时信号，其次匹配同工具历史时延统计，最后fallback到5秒默认值，预测平均误差仅0.41秒，82.9%的误差控制在0.5秒以内
### 关键实验
覆盖DeepSeek-V4 Flash、Qwen3-32B、GLM-4.7三个主流模型，SWE-Lite、Terminal-Bench等多类Agent工作负载，对比vLLM调度器、Dynamo、ThunderAgent等SOTA基线：12组不同模型-负载-并发度设置中，最高降低端到端时延26.8%，降低首包时间（TTFT）36.3%，提升解码吞吐量29.5%；高并发场景下GLM-4.7任务总运行时间较ThunderAgent缩短15.4%。
### 核心结论
Agent服务调度不能仅依赖GPU侧指标，必须结合工具侧的就绪性信号做全局联合优化，才能在相同硬件成本下获得更优的时延和吞吐量表现
