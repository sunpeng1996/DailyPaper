---
title: 'HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents'
title_zh: HybridCUA：面向计算机操作Agent的GUI与CLI协同调度框架
authors:
- Tongbo Chen
- Junbo Niu
- Zhengxi Lu
- Niu Lian
- Fei Tang
- Yuchen Yan
- Yike Hong
- Yong Du
- Yizhou Liu
- Bofan Chen
affiliations:
- Zhejiang University
- Peking University
- Tsinghua University
arxiv_id: '2609.38008'
url: https://arxiv.org/abs/2609.38008
pdf_url: https://arxiv.org/pdf/2609.38008
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: 计算机操作Agent · 多界面协同调度
tags:
- Computer-Use-Agent
- GUI-CLI-Orchestration
- RLVR
- SFT
- Hybrid-Interaction
one_liner: 构建混合交互数据集与CLI感知奖励训练框架，实现计算机操作Agent的GUI-CLI高效协同
practical_value: '- 多工具调度场景可复用「统一动作建模+分粒度奖励」方案：电商运营Agent、智能客服等需要同时操作GUI、调用API、执行脚本的场景，可将所有操作封装为统一格式，用任务级奖励教工具选择逻辑、步骤级奖励教工具执行正确性，避免工具乱用导致效果下降

  - 低资源混合交互数据构建技巧：无需从零采集异构轨迹，可通过现有GUI轨迹改写为工具调用轨迹、强模型生成纯工具轨迹、自由交互生成混合轨迹三种方式低成本构建SFT数据集，大幅降低多工具Agent的数据建设成本

  - 跨场景泛化训练思路：先SFT学动作执行与路由逻辑，再用带场景标签的RL任务做对齐，可迁移到电商全链路自动化、商家服务等跨工具场景，提升跨场景泛化能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机操作Agent（CUA）要么纯依赖GUI交互，长序列任务效率低、误差易累积；要么对接定制化API/工具，工程成本高、跨应用扩展性差。CLI作为系统原生通用接口，可将长GUI操作序列压缩为单条命令，但现有模型不知道何时、如何调用CLI，直接开放CLI权限反而会使OSWorld基准准确率下降2.5~11.5个百分点，成为混合交互落地的核心瓶颈。

### 方法关键点
- 数据层：构建HybridCUA-8K数据集，包含三类轨迹：开源GUI轨迹转统一动作格式的纯GUI轨迹、强模型生成的纯CLI轨迹、自由交互+GUI转CLI改写得到的混合交互轨迹，同时配套3K带CLI优势标注的RLVR任务，标注每类任务是否适合用CLI执行。
- 训练层：两阶段训练，第一阶段用三类混合轨迹做SFT，学习统一动作格式的执行与界面切换逻辑；第二阶段做CLI感知的RL训练，加入任务级`R_CLI`奖励（惩罚不符合场景的CLI调用/不调用）、步骤级`R_exec`奖励（惩罚CLI执行错误），分别优化路由决策与执行准确率。
- 动作层：将GUI（封装为pyautogui代码）与CLI操作统一为bash动作格式，避免多工具分开建模的路由混乱。

### 关键实验
在OSWorld基准上，HybridCUA-9B准确率达53.6%，比同尺寸Qwen3.5-9B基线高14.8个百分点，平均步骤从31.6降到14.0；跨平台到WindowsAgentArena准确率达36.0%，比基线高4个百分点，优于纯GUI、GUI+API的同尺寸方案。

### 核心结论
异构工具协同的核心瓶颈从来不是工具接入，而是让模型学会「什么时候用什么工具、怎么用对工具」的双重能力。
