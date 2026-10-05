---
title: 'HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing
  Agents'
title_zh: HyperBrowseComp：面向网页浏览Agent的多语言多模态压力测试
authors:
- Alham Fikri Aji
- Faiz Rizki Ramadhan
- Zayd M. K. Zuhri
- Seung Hun Eddie Han
- Ryandito Diandaru
- Qinrong Cui
- Jan Christian Blaise Cruz
- Badrinath Chandana
- Peerawat Chomphooyod
- Ahmed Attia
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Mila – Quebec Artificial Intelligence Institute
- Inception AI
- Alibaba Group
- AI Singapore
arxiv_id: '2610.03574'
url: https://arxiv.org/abs/2610.03574
pdf_url: https://arxiv.org/pdf/2610.03574
published: '2026-10-01'
collected: '2026-10-05'
category: Agent
direction: 网页浏览Agent 多语言多模态评估
tags:
- Web Agent
- Benchmark
- Multilingual
- Multimodal
- Information Retrieval
one_liner: 提出覆盖13种语言8种模态的423条高难度网页浏览Agent基准，最优模型准确率仅31.68%
practical_value: '- 跨境多语言搜索/Agent研发可复用其难度筛选逻辑：先过无网络LLM测试，过滤能用参数知识回答的简单query，锁定高价值优化需求

  - 多模态搜索Agent架构选型可参考结论：大模型与原生搜索生态的协同适配效果远好于通用第三方检索工具，Gemini搭配原生搜索比Exa准确率高9.46个百分点

  - 电商多模态检索场景（如从视频片段找同款、从场景图找线下店铺）可复用其证据链验证逻辑，明确多跳检索的拆解路径

  - 评估自有Agent能力时可借鉴其答案验证设计：先定义唯一可验证的短答案，再用LLM+人工双重校验，避免主观评分偏差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有网页浏览Agent benchmark普遍单语言/单模态、问题易被LLM参数知识命中、难度不足，无法真实衡量Agent在开放网络下跨语言跨模态深度信息查找、多跳推理的实际能力，亟需高难度压力测试基准。

### 方法关键点
- 数据构造：由13种语言的母语使用者原生撰写问题，从公开可验证的答案倒推问题设计，排除可通过非网络路径回答的简单问题
- 难度控制：用7款无网络访问的前沿LLM预测试，过滤掉2款以上模型答对、或单款模型答对的高精度答案类问题，确保所有问题必须通过开放网络检索解决
- 覆盖维度：包含视频、PDF、图像、音频、地图等8种模态，覆盖经济、娱乐、教育等12个领域，问题需多跳推理、跨模态信息整合才能解答

### 关键实验
- 测试5款前沿大模型搭配3种检索架构（原生搜索、Exa、OWL），最优配置（Gemini 3.7 Flash+原生搜索）准确率仅31.68%，57.68%的问题无任何模型答对
- 检索架构影响极大：Exa使Gemini 3.7 Flash准确率降至22.22%，OWL更低至17.73%，证明模型与检索生态的适配度对效果影响远超过模型本身能力
- 人类测评30条样本准确率仅50%，平均耗时89.5分钟，与最优模型表现相当，但二者擅长的问题领域无明显重叠

### 核心结论
当前网页浏览Agent的能力天花板远低于预期，跨语言跨模态多跳检索的核心瓶颈不是模型本身，而是模型与检索工具、多模态解析模块的协同适配效率
