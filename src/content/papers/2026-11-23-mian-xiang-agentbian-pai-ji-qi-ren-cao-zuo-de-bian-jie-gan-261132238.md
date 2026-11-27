---
title: Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation
title_zh: 面向Agent编排机器人操作的边界感知策略学习
authors:
- Kaipeng Fang
- Yuhao Wang
- Ji Zhang
- Yunsong Zhou
- Jingkuan Song
- Lianli Gao
affiliations:
- University of Electronic Science and Technology of China
- Shanghai Artificial Intelligence Laboratory
- Tongji University
- Shanghai Innovation Institute
arxiv_id: '2611.32238'
url: https://arxiv.org/abs/2611.32238
pdf_url: https://arxiv.org/pdf/2611.32238
published: '2026-11-23'
collected: '2026-11-27'
category: Agent
direction: Agent与执行策略协作边界优化
tags:
- Agent
- Policy Learning
- Multimodal Agent
- Task Orchestration
- Boundary Optimization
one_liner: 提出边界感知策略学习方法，解决Agent与执行策略协作的切换边界问题，提升任务成功率同时降本提效
practical_value: '- Agent与下游执行模块（推荐召回/排序策略、工具调用模块等）的调度可参考显式定义切换边界的思路，避免OOD调用失败

  - 可针对下游模块的核心生效阶段（如推荐用户决策触发段、工具调用有效输入区间）做多样本微调，扩大可靠输入范围、降低Agent调度难度

  - 可复用成功案例自提升流程：收集Agent与下游模块协作的成功案例重训下游模块，逐步扩大其适用边界，减少LLM调用次数、降低API成本和链路耗时'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
多模态Agent编排的机器人系统结合了大模型通用推理能力和视觉运动策略的精准物理控制能力，但两者切换时故障率高：策略仅在有限起始状态下可靠，Agent常超出可靠区域调用，现有全任务训练的策略切换边界窄、难描述，协作可靠性差。

### 方法关键点
提出边界感知策略学习，两步优化切换边界：1. 边界显式训练：用含多样起始姿态的接触段数据微调策略，得到宽且定义清晰的切换边界，可通过简单协议同步给Agent；2. 边界扩展自提升：用筛选后的成功系统运行案例重训策略，将边界向任务更早阶段延伸，让Agent更早完成交接，减少大模型调用次数。

### 关键结果
在RoboTwin 2.0和RoboDojo基准上，比最强基线成功率高26pct，随机RoboTwin 2.0场景成功率达98.4%，同时API成本降低41.3%，执行时间减少37.5%
