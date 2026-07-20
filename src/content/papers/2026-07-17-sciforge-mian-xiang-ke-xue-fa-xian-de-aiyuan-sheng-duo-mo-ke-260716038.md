---
title: 'SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery'
title_zh: SciForge：面向科学发现的AI原生多模态科研工作平台
authors:
- SciForge Team
- Zhangyang Gao
- Minghao Fang
- Yifei Liu
- Hanhui Yang
- Xinyu Gu
- Shixiang Tang
- Siqi Sun
- Lei Bai
- Cheng Tan
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2607.16038'
url: https://arxiv.org/abs/2607.16038
pdf_url: https://arxiv.org/pdf/2607.16038
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent 科研工作流自动化平台
tags:
- Agent
- Workflow Engine
- Multimodal
- Traceability
- Open Source
one_liner: 开源多模态科研Agent工作平台，支持目标管控、可溯源、多模态推理等五大核心能力
practical_value: '- translate-then-reason架构可复用在电商多模态数据处理流程：商品图、评论、详情页等异构数据先过领域翻译器转成结构化语义，再输入Agent推理，大幅提升任务准确率

  - Evidence-DAG全链路溯源机制可迁移到推荐物料审核、推荐理由生成场景，全链路可审计，满足电商合规要求

  - 模块化Agent服务设计（搜索/解析/工作流执行等独立可调用）可复用在电商运营Agent平台，按需调用模块，降低维护成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有通用AI助手无法整合论文、代码、数据集、模型输出等异构科研资产，也无法保留连贯可审计的研究状态，科研自动化与协作效率低。

### 方法关键点
围绕五大核心支柱设计：1）目标导向的科研决策管控，内置评审关口与共享评审面；2）translate-then-reason多模态处理，异构科研对象先经过领域翻译器处理再输入Agent推理；3）证据治理，通过Evidence-DAG实现声明到来源链的全链路可溯源；4）多角色协作决策机制，后续将支持团队共享工作空间；5）面向真实科研场景落地。系统采用分层架构：轻量交互层、Agent运行时与工作流引擎、证据审计边车、科学模型路由模块。

### 关键结果
系统已开源，覆盖8个端到端科研用例，可支撑基因发现、蛋白质设计、分子优化等多天Agent科研冲刺任务，支持桌面端运行+移动端监管。
