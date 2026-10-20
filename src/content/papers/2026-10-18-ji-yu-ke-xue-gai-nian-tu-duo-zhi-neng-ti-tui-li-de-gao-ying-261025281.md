---
title: 'Bridging Concepts: Multi-Agent Reasoning over Scientific Concept Graphs for
  High-Impact Research Prediction'
title_zh: 基于科学概念图多智能体推理的高影响力研究预测方法
authors:
- Donggyu Yoon
- Minsung Hwang
- Juneha Baek
- Donghyuk Shin
- Joyce Jiyoung Whang
affiliations:
- KAIST
arxiv_id: '2610.25281'
url: https://arxiv.org/abs/2610.25281
pdf_url: https://arxiv.org/pdf/2610.25281
published: '2026-10-18'
collected: '2026-10-20'
category: MultiAgent
direction: 多智体协作 · 知识图谱高潜力链接预测
tags:
- Multi-Agent
- Knowledge Graph
- Link Prediction
- Feature Engineering
- Impact Forecasting
one_liner: 提出MiroGraph多智能体框架，自动完成特征与分类器设计，精准预测高影响力跨概念研究组合
practical_value: '- 可复用「多智能体分工做特征工程+分类器自动设计」的架构，解决电商推荐场景中新类目+爆款属性等动态实体组合的潜力预测问题

  - 构建领域知识图谱时可参考「LLM分层提取概念+HDBSCAN聚类归一化」的自动化流水线，大幅降低人工标注成本

  - 动态图链接预测/冷启动推荐任务中，可将结构、语义、趋势三类特征分离建模，显著提升对未见过的新实体/新组合的泛化能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有高影响力跨概念研究预测方法依赖手动构建科学概念图与手工特征，泛化能力弱，无法适配训练阶段未见过的新兴概念，且难以同时兼顾拓扑结构、概念语义、时序趋势三类关键信号。
### 方法关键点
- 自动化构建科学概念图（SCG）：用GPT-4o-mini从论文标题/摘要中分层提取细粒度研究概念，经HDBSCAN聚类归一化去重后，边关联共现论文的年度引用数据，按时间切片构建数据集避免时序泄露
- MiroGraph多智能体推理架构：1）特征设计Agent根据SCG全局统计特性自动生成结构、语义、趋势三类特征schema；2）三个专用Agent分别计算特征值：结构Agent生成可执行代码计算拓扑特征，语义Agent计算概念关联/协同度，趋势Agent分析引用时序特征；3）分类器设计Agent自动生成候选分类器，选择验证集最优模型输出预测结果
### 关键实验
在CIKM、KDD、SIGIR三大顶会论文构建的3个SCG数据集上测试，对比Impact4Cast、TGN、DyGFormer等12个基线，MiroGraph在所有6种测试设置下Macro F1均为最优，相比最优基线在SCG-CIKM测试集提升2.89%、SCG-KDD测试集提升0.9%，在含28%~51%未见过概念的Eval设置下仍保持SOTA，泛化性显著优于传统时序图模型。
### 核心结论
直接输入子图让LLM端到端推理的效果远弱于多智能体分工提取特征再建模的方案，自动化特征与分类器设计是提升未见过实体泛化能力的核心。
