---
title: 'HALO: Human-Grounded Granular Evaluation of Proactive Agents'
title_zh: HALO：面向主动Agent的以人为基准的细粒度评估框架
authors:
- Wenqi Pei
- Xinyu Wang
- Jinrui Liu
- Cynthia Zhuge
- Jie Sheng
- Zihan Wang
- Tenghao Huang
- Muhao Chen
affiliations:
- University of California, Davis
- 22077AI
- University of Southern California
arxiv_id: '2610.39086'
url: https://arxiv.org/abs/2610.39086
pdf_url: https://arxiv.org/pdf/2610.39086
published: '2026-10-28'
collected: '2026-11-02'
category: Agent
direction: 主动Agent细粒度评估与故障分析
tags:
- Proactive Agent
- Evaluation Benchmark
- Human Annotation
- Agent Calibration
- Retrieval-based Agent
one_liner: 提出跨场景主动Agent细粒度评估基准与8K标注数据集，揭示过干预是核心故障模式
practical_value: '- 做电商/广告主动触达Agent时，可优先校准干预时机与强度，规避过干预（提前推送、过度打扰）占60%+故障的问题，降低用户反感

  - 构建主动服务Agent评估体系时，可复用4级干预分级（L0观察/L1通知/L2准备/L3执行）+细粒度故障诊断维度（时机/强度/证据/相关性），替代简单的二元accept判定

  - 主动推荐Agent的触发逻辑可增加前置校验：干预前优先检索用户权限、历史偏好等本地证据，数据显示有有效证据支撑的通知类干预可接受率提升18个百分点

  - 优化Agent效果时不盲目提升干预率：干预率上升可能因丢失合理克制场景反而导致效果下降，需平衡干预收益与克制收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有主动Agent评估大多依赖自动化分数或二元判定，无法细粒度定位干预失败根因（时机不当、强度失衡、证据不足等），也缺乏对主动干预与合理克制的平衡度量，难以支撑业务级主动Agent的迭代优化。

### 方法关键点
- 构建HALO-Arena评估环境，覆盖Dependency/Blockage/Risk/Opportunity 4类主动需求，横跨10个日常领域、50个用户场景，支持结构化SQL查询+非结构化文档检索两种证据获取方式
- 设计4级干预分级：L0（仅观察/检索，不干预）、L1（仅通知用户）、L2（内部准备，无外部影响）、L3（执行操作，产生外部变更）
- 构造HALO-8K数据集：覆盖10个模型在400个场景下的8000条响应，由20位专家标注可接受性、干预时机/强度问题、证据使用合理性，同时记录推理token数、检索轮次等资源消耗数据

### 关键结果
- 商用模型最高可接受率72.88%，开源模型最高56.63%，存在16个百分点的性能差
- 过干预（时机过早/强度过高）是第一大故障模式，占所有拒绝响应的61.20%
- 检索轮次与模型可接受率强相关（r=0.885），获取到本地有效内容的L1通知类干预可接受率比无内容的高18.2个百分点

**最值得记住的结论**：主动Agent的效果核心不在于干预多频繁，而在于在正确的时机、以合适的强度提供有证据支撑的帮助，同时知道什么时候该保持克制。
