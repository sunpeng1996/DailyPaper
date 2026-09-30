---
title: 'Omni-IO Skills: Harnessing Your Agent Omni-Native'
title_zh: Omni-IO Skills：让通用Agent原生支持全模态能力的插拔式Harness框架
authors:
- Yanlin Li
- Mingyang Hao
- Shengqiong Wu
- Hao Fei
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- University of Oxford
arxiv_id: '2609.31847'
url: https://arxiv.org/abs/2609.31847
pdf_url: https://arxiv.org/pdf/2609.31847
published: '2026-09-24'
collected: '2026-09-30'
category: Agent
direction: Agent 全模态能力扩展框架
tags:
- Agent
- Multimodal
- Harness
- Skill Orchestration
- Asset Registry
one_liner: 通过分层Skill、依赖感知编排和持久化资产注册表，零修改让通用Agent获得全模态能力
practical_value: '- 电商多模态营销物料生成场景可直接复用分层Skill设计：原子Skill封装单模态生成/理解能力，专家Skill封装海报/短视频等标准化物料生产流程，场景Skill封装大促等场景的多物料组合逻辑，大幅降低全链路开发成本

  - 依赖感知的DEG编排+Wave调度机制可直接复用：将多步多模态任务拆解为无依赖的并行批次执行，如同时生成商品主图、短视频脚本、详情页文案，任务失败时仅重跑依赖节点，兼顾效率和容错

  - 持久化Asset Registry设计可复用：给每个生成的资产（如商品图、短视频、文案）分配全局唯一ID、记录来源和生成参数，支持跨轮次复用，如修改商品海报时直接复用已生成的模特图、商品属性描述，无需重复生成

  - Provider层解耦设计可复用：Skill只声明语义能力（如图像生成），不绑定具体服务商，可无缝切换不同的文生图/文生视频模型，灵活适配成本和效果需求，适合业务快速迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用Agent原生能力仅覆盖文本、代码等少数模态，扩展模态需重新训练大模型成本极高；而拼接专用模态模型又面临流程编排、中间资产流转、跨轮复用难的问题，无法落地复杂多模态生产任务，如电商营销物料一站式生成、教育内容多模态生产等场景。
### 方法关键点
- 四层架构设计：Skill Entry层封装原子/专家/场景三级分层Skill，MCP工具服务层提供标准化多模态能力接口，Provider配置层实现能力与服务提供商解耦，Asset Registry层持久化所有资产并支持全局引用、跨轮复用。
- Declare Execution Graph（DEG）编排：将多模态任务拆解为带依赖关系的执行节点，通过Wave调度实现无依赖节点并行执行，失败时仅取消下游依赖节点，不影响独立分支运行。
- 内置27种Skill覆盖38个任务：支持文本、图像、音频、视频、文档、3D、代码7种模态的理解、生成、推理、检索全能力。
### 关键实验
在UniM-90全模态基准上测试，对比原生GPT-5.6 Sol和Claude Sonnet 5：
1. 两个模型的输入支持率从40.00%、38.89%提升至100%；
2. 相对Semantic–Quality Coupled Score（SQCS）分别从26.99、27.82提升至74.94、77.78，提升幅度近50个百分点；
3. Strict Structure Score分别达到100.00%、99.78%，完全满足输出结构要求。
### 核心结论
无需修改Agent的推理核心，仅通过Harness层的能力编排即可让通用Agent获得完整全模态能力，是比训练全模态大模型成本更低、迭代更快的落地方案
