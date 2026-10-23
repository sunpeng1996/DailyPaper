---
title: 'Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for
  Efficient and Reliable Inference'
title_zh: 基于结构落地的高效可靠推理框架：无需扩模型即可提升推理性能
authors:
- Amirhossein Aghaei
- Liangyan Li
- Shiyi Yang
- Shaohua Wang
- Yan Wang
affiliations:
- Huawei Research Canada
- Huawei Technologies Co., Ltd.
- Central University of Finance and Economics
arxiv_id: '2610.30611'
url: https://arxiv.org/abs/2610.30611
pdf_url: https://arxiv.org/pdf/2610.30611
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent多轮推理 · 结构落地不确定性缩减
tags:
- Agent Reasoning
- Structure Grounding
- Graph Alignment
- Uncertainty Reduction
- Training-free
one_liner: 提出训练免的SGUR框架，通过结构化假设空间的主动不确定性缩减实现高效可靠多轮推理
practical_value: '- 电商客服/导购Agent的多轮需求诊断场景，可复用离线分层领域图谱+在线先验加权部分图匹配的架构，替代传统对话上下文堆叠方案，可降低5倍左右token消耗同时提升匹配准确率

  - 低算力端Agent部署可参考结构约束替代模型规模的思路，用小模型+领域结构化假设空间的设计，即可匹配10倍大模型的推理效果，大幅降低部署成本

  - 多轮query改写/意图识别场景，可复用EIG驱动的主动信息获取策略，每次优先询问信息增益最高的属性，快速缩小候选范围，缩短交互路径提升转化率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的Agent多轮推理依赖token级生成和语义相似度匹配，在观测不完整场景下易产出语义合理但结构无依托的推理结果；纯靠扩大模型规模的路线成本高、边际效益递减，GraphRAG类方案仅将图谱作为检索底座，未用结构约束推理过程，多轮交互下易出现语义漂移、信息冗余等问题。
### 方法关键点
- 离线阶段构建符合领域schema的分层专家图谱数据库，预计算节点特异性权重，对决策相关的关系分配更高权重
- 在线四步闭环推理：1）将当前观测构造为查询图；2）通过路径过滤和结构先验剪枝候选图谱集合；3）用先验加权的部分FGW算法对齐查询图与候选图谱，输出置信度排序；4）基于期望信息增益选择下一个最高价值的询问节点，迭代更新观测
- 完全训练免，无需微调backbone模型，仅依赖外部结构化知识与匹配算法
### 关键实验
基于PrimeKG构建多轮医疗诊断基准，对比GraphRAG、ArchRAG等4个SOTA基线，复杂诊断场景（仅2个初始症状）下Hit@3达92.5%，比最强基线高9.4pp，token消耗仅为基线的1/5；小模型（GPT-5.4-nano）搭配SGUR的效果超过所有大模型搭配基线的效果，保留了大模型版本99.8%的Hit@3性能。
### 核心结论
可靠的多轮Agent推理性能不只取决于模型规模，更取决于推理框架对推理过程的结构约束能力，结构落地的框架可部分替代模型规模的作用
