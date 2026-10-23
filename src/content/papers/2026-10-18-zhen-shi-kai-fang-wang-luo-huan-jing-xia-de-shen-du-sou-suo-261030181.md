---
title: Deep Search in Real-World Web Environments
title_zh: 真实开放网络环境下的深度搜索能力评估基准
authors:
- Xiaomin Yu
- Hongliang Chen
- Zhe Huang
- Shilin Yan
- Shao-Rong Su
- Xuqiao Ma
- Feiyang Wang
- Jiayu Chen
- Jiwei Fang
- Yu Yan
affiliations:
- HKUST(GZ)
- FDU
- UW
- IC
- NTU
arxiv_id: '2610.30181'
url: https://arxiv.org/abs/2610.30181
pdf_url: https://arxiv.org/pdf/2610.30181
published: '2026-10-18'
collected: '2026-10-23'
category: Agent
direction: Agent 开放网络深度搜索能力测评
tags:
- Deep Search
- Web Agent
- Benchmark
- Tool Use
- Multi-modal Reasoning
one_liner: 构建OpenDS-World基准评测12款前沿模型的真实网络深度搜索能力，最优模型准确率仅39%
practical_value: '- 可复用其任务构建方法：从初始锚点反向生成多步约束的复杂检索任务，可用于构建电商商品/资讯的深度搜索Agent测试集，验证跨模态、跨格式信息检索能力

  - 工具调用优化参考：高性能模型（如GPT-6 Astra）的工具调用比例平衡（搜索占比~57%、GUI操作占比~32%）、失败后优先切换工具的策略，可用于优化电商导购Agent的工具调度逻辑

  - 预算管理机制参考：其1小时时间+100次工具调用的双层预算控制、低收益路径提前终止的设计，可直接复用在业务级Agent的成本管控模块，降低推理和API调用成本

  - 多模态证据链整合思路：其跨文本/图像/音视频/结构化数据的证据关联方法，可用于电商场景下用户短视频提问到商品匹配的全链路检索逻辑设计'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有深度搜索Agent的评估多基于静态检索环境，未覆盖真实网络的多模态信息、异构格式、交互访问三类核心复杂度，无法系统评估智能体在真实场景下的多步搜索、工具协同、跨源证据整合能力。
### 方法关键点
- 定义OpenDS开放网络深度搜索任务，要求Agent自主探索真实网络，跨多模态、异构格式、交互访问的信息源完成证据关联，输出唯一事实答案
- 构建OpenDS-World基准，包含200个经人工校验的跨8个领域的复杂任务，覆盖4种模态、42种资源格式、7类访问要求，所有任务的证据链可溯源、答案唯一
- 搭建统一测试框架，为所有模型提供搜索、GUI操作、音视频解析三类工具，统一设置3600秒时长+100次工具调用的预算，采用LLM as Judge评估答案准确率
### 关键结果
- 测试12个前沿大模型，最优的GPT-6 Astra整体准确率仅39.0%，人类测试者整体准确率仅21.1%，42.5%的任务无任何人解出
- 资源消耗与准确率无正相关：Gemini 3.8 Flash的token消耗是GPT-6 Astra的5.22倍，准确率反而低2.5个百分点；DeepSeek-V4-Pro耗时是GPT-6 Astra的2.39倍，准确率仅12.5%
- 80%的Qwen3.8-Flash任务因工具调用预算耗尽终止，而GPT-6 Astra的自然终止率达69%，工具失败后优先切换工具的策略可显著降低时间损耗

> 值得记住：真实网络深度搜索的核心瓶颈不是资源投入多少，而是工具调度策略、证据关联能力、低收益路径终止决策的协同优化
