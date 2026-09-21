---
title: 'RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use
  Agents'
title_zh: RecreationWorld：面向混合计算机操作Agent的可扩展可验证环境
authors:
- Shuai Bai
- Jiayong Deng
- Yikun Fu
- Chang Gao
- Xuhao Hu
- Mianqiu Huang
- Yizhen Jiang
- Yuheng Jing
- Dehui Kong
- Keliang Li
affiliations:
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2609.22000'
url: https://arxiv.org/abs/2609.22000
pdf_url: https://arxiv.org/pdf/2609.22000
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: 混合计算机操作Agent 训练与评测框架
tags:
- Computer-Use-Agent
- Hybrid-Agent
- Agent-Evaluation
- Agent-Training
- GUI-Agent
one_liner: 发布跨5大操作系统/平台的混合GUI+代码操作Agent的训练框架与基准测试集
practical_value: '- 做电商运营/投放类Agent可直接复用GUI+代码混合执行架构：比如批量商品页装修、自动搭建投放页面的任务，既需要操作前端GUI，也需要修改配置/生成前端代码，混合模式比单模态Agent覆盖场景更广

  - 自研Agent评测体系时可复用「参考系统作为Oracle」的范式：自动生成程序断言+视觉断言的双维度测试用例，无需人工编写大量评测case，大幅降低标注成本

  - Agent训练阶段可参考「探索-实现-验证」闭环轨迹筛选逻辑：只保留高评分的完整操作轨迹做SFT，能提升模型跨任务泛化能力，在电商Agent的投放、客服等场景可直接复用

  - 工程落地时可引入可编程交互Runtime替代单次工具调用：把常用GUI操作封装成SDK给Agent调用，能降低40%输入token、26%耗时、54%推理成本，效果无明显下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）分为GUI交互和终端代码执行两条独立路线，GUI Agent无法修改支撑界面的软件代码，代码Agent看不到自身操作生成的界面效果，而真实数字任务（软件开发、运维、运营工具搭建等）需要两类能力交错执行、信息双向流动，现有基准仅支持单模态能力评测，缺乏可规模化的混合能力训练与评测环境。

### 方法关键点
- 核心任务定义为**应用复现**：给定可运行参考应用，Agent自主决定何时探索界面、何时编码实现、何时运行验证效果，无预设工作流，天然要求混合能力
- 框架原生支持Ubuntu/macOS/Windows/Android/Web五大平台，统一暴露GUI控制+编码工具接口，自动基于参考生成程序断言（读取组件状态、执行结果）+视觉断言（校验布局、样式、渲染效果）的双维度测试用例，完全自动评分
- 基于开源应用规模化生成3.5万条高评分「探索-实现-验证」闭环轨迹，可直接用于SFT训练
- 配套RecreationBench基准，包含250个跨平台、跨领域的复现任务，覆盖不同复杂度的应用场景

### 关键结果
10个前沿大模型在RecreationBench上的最高分为GPT-6 Astra的58.1%，但仅2.8%的任务能100%通过所有测试，混合能力提升空间极大；用生成的轨迹微调Qwen系列模型，在5个分布外基准（编码、GUI操作等）上最高提升17.9个百分点，训练得到的能力可跨场景迁移；采用可编程SDK替代单次MCP工具调用，可降低40%输入token、26%耗时、54%推理成本，任务效果无明显下降。

**最值得记住的一句话**：混合GUI+代码的闭环操作能力是Agent实现通用数字任务的核心基础，可运行参考作为Oracle的评测范式能大幅降低Agent训练与评测的人工成本。
