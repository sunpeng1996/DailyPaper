---
title: Harness Engineering for Software Engineering via Modular Executable Dev-Primitives
title_zh: 基于模块化可执行开发原语的软件工程Agent调度框架HERMES
authors:
- Haibo Jin
- Xinjie Li
- Peng Kuang
- Haohan Wang
affiliations:
- University of Illinois Urbana-Champaign
- The Pennsylvania State University
arxiv_id: '2610.07832'
url: https://arxiv.org/abs/2610.07832
pdf_url: https://arxiv.org/pdf/2610.07832
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: Agent 长周期软件工程多智能体协作
tags:
- Agent
- MultiAgent
- LLM4Code
- ModularAgent
- LongHorizonTask
one_liner: 提出绑定代码组件的Dev-Primitives抽象与HERMES框架，提升长周期软件工程Agent表现并降本
practical_value: '- 可复用「业务模块绑定专属轻量LLM」的设计：将推荐/广告系统的召回、排序、运营规则等模块分别绑定小模型，仅跨模块协调时调用大模型，降低全链路推理成本

  - 动态激活+错误归因的调度逻辑可迁移至多Agent推荐系统：任务触发时仅激活相关模块Agent，运行报错后仅重跑归因到的故障模块，大幅降低长链路任务的重复计算开销

  - 异构模型分配策略可直接复用：将算力向任务调度、错误诊断模块倾斜，执行层模块用轻量LoRA微调小模型即可覆盖80%以上效果，平衡性能与成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有带终端访问的LLM在长周期软件工程任务中存在严重上下文爆炸、语义漂移问题，代码状态分散在多份文件、配置、测试用例中，Agent需反复重构状态导致效率极低，大仓库场景下定位相关组件的难度进一步放大。

### 方法关键点
- 提出Dev-Primitives抽象：每份代码/配置/测试文件绑定一个专属轻量LLM，支持自然语言推理、跨组件通信、本地自修改，组件状态无需上传至中央Agent上下文
- 设计HERMES框架：包含两个核心机制，一是依赖感知的动态激活机制，仅实例化任务相关的Dev-Primitives；二是错误诊断机制，将运行报错映射到需修改的对应组件，仅重激活相关原语迭代修正
- 支持异构模型配置：激活、诊断模块可使用大模型，Dev-Primitives用小模型，进一步降低推理成本

### 关键实验
在SWE-bench Verified、SWE Refactor Bench、Terminal-Bench 4.0、DevOps-Gym四个基准上测试，相比同配置基线平均提升12.4%；使用Qwen3-8B作为Dev-Primitives、搭配大模型做激活诊断时，性能仅比全链路用GPT-5.6 Sol低4.5%，推理成本在Terminal-Bench 4.0上降低26.2%。

最值得记住的一句话：Agent编排设计对最终效果的影响不亚于模型本身，将能力绑定到具体业务组件而非预设角色，可大幅提升长周期任务的鲁棒性并降低成本
