---
title: A Self-Calibrating Agentic AI Framework for Autonomous Edge Resource Allocation
title_zh: 面向边缘资源自主分配的自校准Agentic AI框架
authors:
- Fin Gentzen
- Marla Grunewald
- Iulisloi Zacarias
- Mounir Bensalem
- Admela Jukan
affiliations:
- Technische Universität Braunschweig, Germany
arxiv_id: '2607.22400'
url: https://arxiv.org/abs/2607.22400
pdf_url: https://arxiv.org/pdf/2607.22400
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent架构 · 边缘资源分配优化
tags:
- Agentic AI
- Self-Calibration
- Edge Computing
- RAG
- ARIMA
- Workload Profiling
one_liner: 提出无需人工监督的自校准Agent框架，融合LLM、RAG与ARIMA实现边缘零知识工作负载的高效资源分配
practical_value: '- 可复用「LLM零-shot预估 + RAG历史召回 + 主动校准」的Agent分层决策架构，解决冷启动下无先验知识的资源预估问题，可直接用于推荐系统新模型上线前的GPU/CPU资源预估场景

  - ARIMA跳步优化策略可直接迁移到时间序列预测提速场景，在保证精度不变的前提下将预测速度提升52%，适合广告/推荐实时指标预测类业务

  - 多模块置信度校验+失败重试的自校准机制，可用于优化LLM Agent工作流稳定性，降低推荐/广告系统中LLM推理hallucination带来的决策错误'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent部署在开放环境时缺乏可靠真值、长期运行容易出现漂移，而边缘环境硬件异构、资源受限，零知识工作负载（无先验元数据）的资源分配准确率低、容易导致SLA违约，现有依赖预训练或人工标注的方案无法适配动态边缘场景。

### 方法关键点
- 核心AI Workload Agent包含4个互补模块：LLM零秒预估（静态代码分析快速输出初步资源预测）、主动profiling（沙箱执行部分样本+ARIMA预测生成真值存入知识库）、LLM+RAG预估（召回历史相似工作负载的真值数据提升预测准确率）、重校准模块（触发规则校验不通过时的重试逻辑）
- 提出ARIMA跳步搜索算法，通过三种跳步策略动态跳过不必要的参数搜索，在严格时间预算下快速收敛到符合精度要求的预测结果
- 构建统一的资源模型，同时支持离散内存、统一内存架构的CPU/GPU/内存占用建模

### 关键实验
数据集：公开53个AI工作负载基准，覆盖8种模型架构、6种数据集、3种异构硬件（树莓派5、Jetson Thor、GPU工作站）；对比基线：纯零-shot LLM Agent、纯profiling、标准ARIMA。核心结果：资源预测准确率比基线LLM Agent高91.7%，预测速度比纯profiling快71.7%；跳步ARIMA比标准ARIMA快52%且精度一致；最优场景下预测MAPE从200%以上降到个位数。

最值得记住的一句话：Agent系统的稳定性不能只依赖LLM本身的能力，结合统计预测、动态校准和历史知识库的分层架构，是解决无先验冷启动问题、降低长期运行漂移的有效路径。
