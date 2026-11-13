---
title: 'RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving'
title_zh: RSI-PDEbench：面向偏微分方程求解的自进化Agent基准
authors:
- Binghang Lu
- Lang Cao
- Changhong Mou
- Yige Sun
- Cindy Xiangrui Kong
- Zheyuan Deng
- Tian Yuan
- Bing Hu
- Runyu Zhang
- Na Lu
affiliations:
- Purdue University
- University of Illinois Urbana-Champaign
- Utah State University
- Brown University
- Massachusetts Institute of Technology
arxiv_id: '2611.14949'
url: https://arxiv.org/abs/2611.14949
pdf_url: https://arxiv.org/pdf/2611.14949
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 自进化科学计算基准构建
tags:
- Agent
- Self-Improving
- Benchmark
- PDE
- LLM4Science
one_liner: 提出含1001个PDE/FPDE案例的自进化Agent基准及残差引导的自改进求解框架
practical_value: '- 可复用「残差初筛+验证门控」自进化框架：先通过低成本弱信号（如业务侧点击/加购）短list候选方案，再用强验证指标（如GMV）筛选更新，大幅降低无效大模型调用

  - 自进化Agent状态迭代设计可迁移：仅迭代业务策略、经验记忆模块，冻结底座大模型和校验逻辑，平衡迭代灵活性与系统稳定性，适合推荐/广告策略迭代场景

  - 多场景评估范式可复用：分别设计无噪、带噪、OOD三类测试集，对应业务正常流量、噪声流量、冷启动流量的效果验证，保障模型泛化性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
PDE求解需要大量专家投入完成方程发现、参数估计、求解器配置，现有基准多聚焦固定方程的求解任务，缺乏面向未知方程、观测噪声、分布偏移场景的自进化Agent统一评测框架，无法验证LLM Agent是否能自动化端到端PDE求解流程。

### 方法关键点
- 基准构建：RSI-PDEbench包含1001个PDE/分数阶PDE案例，覆盖42类方程模板，设计三类评测设置：Full（无噪观测数据）、Noisy（叠加50% RMS高斯噪声）、Hard-OOD（未见方程模板+参数范围偏移）
- Agent框架：RSI-PDE先通过残差损失初筛最多5个候选方程，再用相对L2反馈迭代优化参数和求解器，通过验证门控判断是否更新策略、记忆和求解器，全程冻结底座大模型权重

### 关键实验
对比单轮基线、原生Agent harness（Claude Code/Codex），在4款前沿大模型上验证效果：三类设置下平均通过率相对单轮基线提升106.5%~181.9%，相对原生harness提升3.0%~19.6%；12组模型-设置对的总大模型调用量降低46.9%。

**最值得记住的一句话**：带验证门控的结构化迭代远优于无约束的原生Agent探索，能在大幅降低调用成本的同时提升效果。
