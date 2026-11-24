---
title: 'ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents'
title_zh: ToolSmith：面向多模态搜索智能体的自动工具生成框架
authors:
- Rui Sun
- Junhua Huang
- Luca Zancato
- Md Mofijul Islam
- Kai-Wei Chang
affiliations:
- University of California, Los Angeles
- AWS GenAI
arxiv_id: '2611.31198'
url: https://arxiv.org/abs/2611.31198
pdf_url: https://arxiv.org/pdf/2611.31198
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: 多模态搜索Agent · 自动工具生成
tags:
- Multimodal Agent
- Tool Generation
- Search Agent
- VLM
- Automatic Pipeline
one_liner: 通过四阶段无监督管道为多模态搜索Agent自动生成可复用工具，无需人工维护，跨模型均实现稳定效果增益
practical_value: '- 失败轨迹聚类的能力缺口挖掘方法可直接复用：电商搜品、广告检索类Agent遇到bad case时，先通过LLM self-critique分类失败原因，仅针对工具缺失类case做功能迭代，减少无效开发成本

  - 双门控工具验证逻辑可直接落地业务：生成的工具先做AST静态扫描+沙箱冒烟测试，再由LLM从通用性、边界处理、任务对齐维度打分，避免生成工具带安全风险或冗余，符合业务侧合规要求

  - 推理时按需召回Top K工具的策略可优化现有Agent架构：无需将全量工具放入prompt，仅召回与当前查询相关的扩展工具+基础工具，既降低prompt长度，又减少工具调用错误，适配电商多轮搜索等长上下文场景

  - 工具生成与推理模型的适配结论可指导资源分配：工具生成侧用最强可用大模型，轨迹挖掘用与部署推理同规模的模型，可最大化效果增益，实现大模型生成、小模型部署的降本增效方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态搜索Agent依赖人工编写的固定工具库，维护成本极高，且上线后工具库完全冻结，遇到新查询类型、新证据格式、未知失败模式时无法自主适配；现有优化方向仅聚焦于提升Agent对固定工具的使用效率，未从根本上扩展工具覆盖范围，无法解决工具不足导致的效果天花板。
### 方法关键点
- 四阶段模型无关全自动管道：1）轨迹挖掘：从Agent的失败轨迹中通过LLM自评审筛选出「工具不足」类失败case，聚类为能力缺口；2）复用/生成决策：用TF-IDF匹配能力缺口与现有工具描述，仅无匹配项时进入生成流程；3）工具生成：指定Python接口规范，要求生成工具无硬编码、无危险IO，自动生成带Schema和描述的可调用代码；4）双门控验证：先过沙箱静态检查+冒烟测试，再由LLM从参数通用性、描述抽象性、边界处理、任务对齐四个维度打分，达标后去重加入工具库。
- 推理侧优化：每次查询仅召回Top K相关的生成工具+固定8个基础工具，避免工具列表过长导致的调用错误。
### 关键实验
在3个域内多模态搜索基准（FVQA、InfoSeek、EncyclopedicVQA）、10个未见过的域外基准上测试，对比固定8个基础工具的基线：Qwen3-VL-8B推理时域内准确率提升2.20pp、域外提升1.33pp；Qwen3-VL-32B推理时域外提升达2.98pp；GPT-5推理时域外提升2.40pp，增益随推理模型规模增大而提升。
### 核心结论
多模态搜索Agent的能力上限不仅取决于模型本身，也取决于可调用工具的覆盖范围，自动生成工具是用极低人力成本扩展Agent能力边界的高性价比路径
