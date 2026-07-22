---
title: 'DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable
  LLM Data Pipelines'
title_zh: DataFlow-Harness：构建可编辑LLM数据流水线的代码Agent平台
authors:
- Runming He
- Zhen Hao Wong
- Hao Liang
- Zimo Meng
- Chengyu Shen
- Xiaochen Ma
- Wentao Zhang
affiliations:
- Peking University
- Institute for Advanced Algorithms Research, Shanghai
- Zhongguancun Academy
arxiv_id: '2607.16617'
url: https://arxiv.org/abs/2607.16617
pdf_url: https://arxiv.org/pdf/2607.16617
published: '2026-07-17'
collected: '2026-07-22'
category: Agent
direction: 代码Agent · 数据流水线自动化构建
tags:
- Code-Agent
- Model-Context-Protocol
- Data-Pipeline
- DAG
- Workflow-Automation
one_liner: 通过MCP+流程技能+可视化交互，让代码Agent生成可持久编辑的平台原生数据流水线DAG
practical_value: '- 搭建推荐/广告样本/特征流水线时，可复用「MCP实时算子对接+流程技能引导+结构化变更校验」架构，将常用特征清洗、样本过滤规则封装为技能和算子库，让Agent自动生成可编辑的平台原生DAG，替代一次性Python脚本，降低维护成本

  - 构建RAG、生成式推荐的训练数据集流水线时，可借鉴其双模态交互设计，同时提供Agent对话入口和可视化DAG编辑器，支持算法同学快速调整数据处理逻辑，无需手动改代码

  - 内部Agent开发平台建设时，可参考其平台接地的设计思路，不要让Agent自由生成代码，而是约束其在平台已有的算子、规则范围内做结构化操作，兼顾Agent的自动化能力和平台的治理要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM代码Agent多生成一次性自由格式脚本，无法直接转化为企业级平台可持久化、可视化、可编辑的流水线资产，存在自然语言需求到落地流水线的NL2Pipeline断层，工业场景下的可审计、可复用、可治理需求无法满足。
### 方法关键点
- 用DataFlow-Skills封装领域流程知识，包括算子选择逻辑、兼容性规则、流水线构建步骤，给Agent提供显式 procedural 引导，减少无意义的推理尝试
- 基于MCP层对接实时算子注册表和流水线状态，所有Agent操作均为结构化的增删改算子、调整连接关系等突变操作，每次变更前自动校验DAG合法性、上下游算子schema兼容性，校验通过才提交到后端
- 提供DataFlow-WebUI双模态交互，对话界面支持自然语言输入需求，可视化DAG编辑器支持人工直接调整流水线，所有变更实时同步，支持Agent和人协同迭代
### 关键结果
在12个工业数据处理任务benchmark上：端到端通过率93.3%，仅比最强脚本生成基线低0.9个百分点，比仅用MCP的方案高10个百分点；相比Vanilla Claude Code，成本降低72.5%，生成延迟降低49.9%；相比上下文感知Claude Code，成本降低42.8%。下游训练验证显示，其生成的流水线产出的数据训练的模型，数学推理平均精度高1.7个点，通用SFT平均精度高2.3个点。
最值得记住的一句话：Agent落地工业场景的核心不是最大化自由生成能力，而是要深度对接现有平台的资产、规则和治理要求，在约束范围内实现自动化
