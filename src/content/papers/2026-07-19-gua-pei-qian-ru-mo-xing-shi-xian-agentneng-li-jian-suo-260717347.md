---
title: Adapting Embedding Models for Agent Capability Retrieval
title_zh: 适配嵌入模型实现Agent能力检索
authors:
- Tingwei Chen
- Yunxiao Shi
- Zhengdong Chu
- Qingsong Wen
- Min Xu
affiliations:
- University of Technology Sydney
- Squirrel AI Learning
- University of Virginia
arxiv_id: '2607.17347'
url: https://arxiv.org/abs/2607.17347
pdf_url: https://arxiv.org/pdf/2607.17347
published: '2026-07-19'
collected: '2026-07-21'
category: Agent
direction: Agent能力检索 · 嵌入模型适配
tags:
- Embedding Model
- LoRA
- Agent Retrieval
- Transfer Learning
- Capability Profile
one_liner: 通过LoRA微调通用嵌入模型，实现跨Agent/工具/技能目录的能力检索且效果可跨域迁移
practical_value: '- 做Agent应用商店/工具平台时，可将Agent、工具包、技能统一抽象为Capability Profile，用同一套检索框架召回，降低架构复杂度

  - 通用嵌入模型只需用LoRA在公开AgentSelect数据集微调，就能实现跨未知Agent/技能目录的检索效果提升，无需大量自有标注数据，BGE-base适配后P@1最高提升10.33pp

  - 构建检索评估数据集时，可复用论文的5级难度查询生成prompt模板，覆盖从明确请求到带噪声模糊请求的真实用户场景，提升评估真实性

  - Agent能力检索仅取名称+描述字段作为输入，就能达到全字段相当的效果，同时减少61%的token消耗，降低推理成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
开放Agent市场中Agent、工具包、可复用技能包在同一搜索界面展示，但现有LLM路由、工具检索、技能发现三个方向分别研究，没有统一的检索框架，用户无法通过自然语言查询高效匹配到最合适的可执行单元，通用文本检索模型直接用于能力匹配的效果较差。

### 方法关键点
- 统一表示：将Agent、工具包、技能统一抽象为**Capability Profile**，仅提取公开元数据中的名称、能力描述、绑定工具信息作为检索输入，无需额外内部信息
- 微调方案：对BGE-base、KaLM-v1.5、EasyRec三类开源嵌入模型用LoRA在AgentSelect数据集上微调，采用in-batch负采样+对比损失，所有模型无架构修改，仅微调最后几层q/k/v参数
- 评估数据集构建：新构建ClawHub基准，包含50个真实Agent技能，用大模型生成1000条5级难度的自然语言查询，覆盖明确、带约束、场景化、模糊、带干扰信息的真实用户请求

### 关键实验
对比三类模型微调前后在两个未见过的测试集上的效果：MuleRun（59个原生Agent，972条测试查询）上，BGE-base微调后P@1从0.7212提升到0.7778，MRR@10从0.7806提升到0.8208；ClawHub（50个技能，900条测试查询）上，BGE-base微调后P@1从0.6667提升到0.7700，MRR@10从0.7652提升到0.8532。消融实验显示仅用名称+描述字段，比全字段少用61%token，效果几乎无下降。

### 核心结论
不同类型的可执行Agent单元只要抽象为统一的能力描述，通用嵌入模型经过少量微调就能实现跨域的能力检索效果提升，无需为Agent、工具、技能分别搭建独立检索系统。
