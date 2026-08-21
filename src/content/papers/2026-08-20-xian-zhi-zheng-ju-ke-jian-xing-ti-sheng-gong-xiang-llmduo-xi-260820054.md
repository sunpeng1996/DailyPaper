---
title: 'What You Can''t See Is What You Learn: Restricted Evidence Visibility Favors
  Compositional Generalization in Shared-Genome Language-Model Societies'
title_zh: 限制证据可见性提升共享LLM多细胞系统的组合泛化能力
authors:
- Narcis Marincat
affiliations:
- Independent Researcher
- University College London
arxiv_id: '2608.20054'
url: https://arxiv.org/abs/2608.20054
pdf_url: https://arxiv.org/pdf/2608.20054
published: '2026-08-20'
collected: '2026-08-21'
category: MultiAgent
direction: 多模块LLM多智能体 组合泛化优化
tags:
- LoRA
- MultiAgent
- Compositional Generalization
- Attention Mask
- Causal Audit
one_liner: 通过仅调整注意力掩码的对照实验，证明限制模块证据可见性可大幅提升多模块LLM的组合泛化能力
practical_value: '- 多模块LLM Agent系统设计时，可通过硬注意力掩码限制每个模块的输入可见范围，避免模型走全量输入记忆捷径，大幅提升OOD场景泛化能力，可落地到电商多步活动规则推理、商品属性组合推荐等场景

  - 多Agent协作链路可采用共享LLM backbone+单份LoRA的架构训练，无需为每个Agent配置独立参数，大幅降低训练与部署成本，适配搜索推荐多阶段Agent协作链路

  - 验证多Agent通信协议的可复用性可采用同语义值隐状态跨episode移植方案，移植后准确率保持90%以上说明通信语义对齐、不依赖上下文，支持生产环境模块化替换

  - 业务A/B实验可借鉴严格变量控制方法：除核心变量外固定初始化、训练流、输入布局，搭配碰撞分层分析排除样本泄露干扰，提升实验结论可信度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多模块神经网络通常给每个模块暴露全量输入，模型容易走全样本记忆捷径，无法学到可复用的局部变换能力，组合泛化能力差，过往研究未严格控制变量验证证据可见性对组合泛化的因果影响。

### 方法关键点
- 架构：4个细胞共享冻结的Qwen2.5-0.5B-Instruct backbone与1个rank-8 LoRA，无细胞专属参数，细胞间仅通过2个896维连续向量通信，是唯一跨细胞信息通路
- 对照设计：10组严格配对的实验组/对照组，仅注意力掩码存在差异：实验组每个细胞仅能关注自身分配的证据span，对照组可关注所有span，其余变量（初始化、训练顺序、token布局、参数）完全一致
- 验证方案：采用同语义值隐状态移植、反事实移植等因果审计方法，验证通信内容的语义一致性与可复用性

### 关键结果
- 9/10的实验组在深度2、3的组合泛化准确率比对照组高至少20pp，深度2中位数优势0.7648，深度3中位数优势0.6050
- 实验组在训练从未出现过的组合函数样本上，深度3中位数优势仍达0.558，排除函数记忆干扰
- 6个审计的实验组中，同语义值隐状态跨episode移植后准确率保持0.94-1.00，通信接口可复用；唯一高性能对照组同值移植准确率仅0.12-0.25，通信状态依赖上下文

**最值得记住的一句话**：限制模块输入可见范围不会降低系统能力，反而会强迫模块通过协作完成任务，大幅提升学到可复用模块化能力的概率。
