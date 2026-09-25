---
title: 'PackLab: A Comprehensive Framework for Developing, Training, and Evaluating
  MLLMs in Robotic Bin Packing'
title_zh: PackLab：面向机器人装箱的MLLM开发训练与评估全栈框架
authors:
- Donghao Zhou
- Jia-Hui Pan
- Fan Zhang
- Xingyuan Bu
- Shilong Li
- Xiaojie Gao
- Yun-Hui Liu
- Chi-Wing Fu
- Pheng-Ann Heng
arxiv_id: '2609.23784'
url: https://arxiv.org/abs/2609.23784
pdf_url: https://arxiv.org/pdf/2609.23784
published: '2026-09-19'
collected: '2026-09-25'
category: Multimodal
direction: 多模态大模型 · 长序列决策优化
tags:
- MLLM
- VLM
- Sequential Decision Making
- Benchmark
- Simulation
- Robotics
one_liner: 提出面向机器人装箱场景的MLLM全栈框架，含仿真平台、专用VLM及多难度标准化评测基准
practical_value: '- 仓储履约、订单调度类长序列优化任务可复用「仿真生成大规模训练轨迹+领域专用模型微调+分级评测」的全流程开发范式，降低冷启动成本

  - 多模态Agent动态状态感知+闭环连续决策的设计思路，可迁移到电商智能仓调度、配送路径规划类业务Agent开发

  - 垂直场景定制微调的专用MLLM性能显著优于通用MLLM，业务落地优先做领域适配而非直接调用通用大模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
机器人装箱属于长时序sequential decision任务，每个物品放置会影响后续可用空间，现有方法多依赖手工几何启发式规则，或在预定义配置下训练的RL策略，通用MLLM在异构装箱场景的闭环序列决策潜力未被充分挖掘。
### 方法关键点
推出全栈框架PackLab，包含三大核心组件：
1. PackLab-Suite：物理仿真平台，可规模化生成多样化装箱训练轨迹，同时验证决策的物理落地效果
2. PackLab-VLM：装箱专用MLLM，可感知物品、容器的动态状态，闭环联合决策待装物品与放置位置
3. PackLab-Bench：覆盖多难度等级的标准化装箱评测场景，支持体系化模型效果评估
### 关键结果
在不同物品集、容器配置的测试中，PackLab-VLM平均性能全面优于传统启发式规则、传统RL方法、通用MLLM。
