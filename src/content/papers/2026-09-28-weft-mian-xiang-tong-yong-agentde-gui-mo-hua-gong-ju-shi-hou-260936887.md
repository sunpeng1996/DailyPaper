---
title: 'WEFT: Scaling Tool-Use Post-Training for General-Purpose Agents'
title_zh: WEFT：面向通用Agent的规模化工具使用后训练框架
authors:
- Bo Mao
- Hang He
- Linting Wang
- Lizhi Lin
- Maosen Zhou
- Guanming Liu
- Jinxiu Liu
- Tianyu Huai
- Chaoyun Zhang
- Bingxuan Li
affiliations:
- East China Normal University
- Fudan University
- Shanghai Innovation Institute
- Renmin University of China
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2609.36887'
url: https://arxiv.org/abs/2609.36887
pdf_url: https://arxiv.org/pdf/2609.36887
published: '2026-09-28'
collected: '2026-10-05'
category: Agent
direction: Agent工具能力后训练 · 全链路系统优化
tags:
- Tool-Use
- Post-Training
- LLM-Agent
- Reinforcement-Learning
- MCP
one_liner: 提出全链路自进化Agent交互系统的工具使用后训练框架，大幅提升多规模模型工具调用能力
practical_value: '- 电商/广告Agent的工具调用训练数据生成可复用同任务的多视图（完整指令/分步模拟用户请求）+多Harness组合，无需新增任务即可提升训练数据分布丰富度，降低数据构造成本

  - 多步任务SFT轨迹构造可采用前缀保留拒绝采样，仅重采样失败的原子任务段、保留已验证正确前缀，相同轨迹量下训练效果提升1~2个百分点，适合售后、下单等长路径电商Agent训练

  - Agent RL训练可采用原子轮次credit assignment，基于单步任务完成情况分配奖励而非全轨迹平均，避免长任务中局部错误的全局影响，提升训练稳定性，适配搜索推荐Agent的多步决策对齐

  - 大规模Agent rollout工程可复用MegaMCP架构，共享工具服务进程、隔离各会话状态，内存占用降低77%+、冷启动延迟降低50%+，适合业务侧大规模Agent测试、训练数据批量生成'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往工具使用后训练仅孤立扩容可执行环境，而完整Agent交互系统包含环境、任务、执行Harness、评估器四大组件，单扩环境无法保证学习信号可靠性：任务不可行、工具实现缺陷、评估错误会导致正常Agent行为被误惩罚，训练效果无法随环境规模线性提升。

### 方法关键点
- 规模化构建全链路交互系统：覆盖15个领域的8172个MCP、64755个工具，组合生成11884个跨工具多步任务，支持完整任务指令/分步模拟用户请求两种披露视图、多Agent Harness并行rollout，提升交互多样性
- 执行驱动自进化：基于执行trace和状态证据做失败归因，区分Agent策略错误与环境/任务/评估器缺陷，针对性修订组件后重新rollout，从源头提升训练信号可靠性
- 稳定后训练pipeline：前缀保留拒绝采样构造SFT轨迹，仅重采样失败的原子任务段；RL阶段采用原子轮次组相对credit assignment，分配细粒度学习信号；MegaMCP架构共享工具服务、隔离会话状态，支撑大规模并发rollout

### 关键结果
- WEFT-14B较同参基线Agent-World-14B在BFCL V4、τ2-Bench、Claw-Eval基准上分别提升6.41、2.23、12.27个百分点
- 固定任务与rollout预算下，3轮自进化使工具调用错误率相对下降45.5%，下游基准得分提升3.65~5.25个百分点
- MegaMCP较单会话独立部署，内存占用降低77.6%~95.7%，冷启动延迟降低54.1%

### 核心结论
工具使用后训练本质是系统级优化问题，执行经验既可以作为策略训练数据，也可以作为交互系统本身迭代的证据
