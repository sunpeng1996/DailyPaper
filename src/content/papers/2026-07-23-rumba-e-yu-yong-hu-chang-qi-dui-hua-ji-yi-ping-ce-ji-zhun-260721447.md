---
title: 'RUMBA: Russian User Memory Benchmark'
title_zh: RUMBA：俄语用户长期对话记忆评测基准
authors:
- Elizaveta Shevtsova
- Inna Glebkina
- Mark Baushenko
- Pavel Gulyaev
- Alena Fenogenova
affiliations:
- DAIMLD
arxiv_id: '2607.21447'
url: https://arxiv.org/abs/2607.21447
pdf_url: https://arxiv.org/pdf/2607.21447
published: '2026-07-23'
collected: '2026-07-24'
category: Eval
direction: 大语言模型记忆能力评测 · 多语言基准
tags:
- Memory Benchmark
- Long-context LLM
- Conversational Agent
- RAG
- Multilingual Evaluation
one_liner: 首个支持俄英双语的多维度长期对话记忆评测基准，覆盖时序推理、主动遗忘等真实交互场景
practical_value: '- 搭建电商导购、个性化客服等带会话记忆的Agent时，可复用其三维问题标注框架（语义/会话跨度/时序性）拆分任务难度，针对性优化记忆模块瓶颈

  - 记忆系统选型可参考其对比结论：优先测试memOS、简单向量RAG方案，无时间感知的图记忆（如mem0g）时序场景性能明显落后，需谨慎选型

  - 主动遗忘、隐式时序推理是当前记忆系统的共性短板，业务场景中（如用户要求删除历史偏好、查询跨时段消费记录）需单独做逻辑兜底，不要完全依赖记忆框架原生能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM长期记忆评测基准均为英语中心化，且采用扁平分类，无法拆分时序性、会话跨度、语义类型等维度的性能影响，也缺少主动遗忘等真实场景的覆盖，俄语领域更是完全缺失相关基准，无法支撑本地化对话Agent的记忆能力迭代。

### 方法关键点
- 构建三维正交标注体系：语义轴（抽取/推理/弃权三类，含主动删除DeleteInfo子类）、数量轴（单会话/多会话）、时序轴（无时序/有时序，时序下分显式/隐式时间表达），可细粒度定位模型失败原因
- 数据集含85段俄文真实用户撰写的多会话对话（平均34万字符，12-85个会话），配套1543个标注QA对，同时提供对齐验证后的英文子集
- 支持两种评测管线：全上下文长窗口LLM直接评测、RAG/记忆Agent系统检索评测，统一采用领域适配的LLM-as-Judge计算准确率

### 关键结果
- 全上下文长窗口模型性能整体优于RAG/记忆Agent，英文场景平均领先8.64个百分点，俄文领先4.28个百分点；最优模型GPT-5.4准确率可达83.6~84
- 会话跨度是最大难度因子：多会话问题准确率比单会话低20.7~23个百分点，其次是隐式时序表达，准确率比显式时序低19~30个百分点
- 记忆系统中memOS、简单向量RAG性能最优，无时间感知的图记忆mem0g准确率仅35左右，大幅落后其他方案

**最值得记住的一句话**：当前所有记忆系统在多会话隐式时序推理、主动遗忘场景下性能缺口极大，业务落地必须做针对性优化，不能依赖通用方案的开箱效果。
