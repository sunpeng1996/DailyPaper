---
title: Dual-Path LLM Reasoning for Multimodal Few-Shot Knowledge Graph Completion
title_zh: 双路径大语言模型推理实现多模态少样本知识图谱补全
authors:
- Jinlan Liu
- Zhiying Tu
- Yongchao Xing
- Yicheng Liu
- Bolin Zhang
- Dianbo Sui
- Dianhui Chu
- Hongliang Sun
affiliations:
- 哈尔滨工业大学（威海）
- 山东省数字服务计算技术与系统重点实验室
- 哈尔滨工业大学青岛研究院
arxiv_id: '2607.26909'
url: https://arxiv.org/abs/2607.26909
pdf_url: https://arxiv.org/pdf/2607.26909
published: '2026-07-29'
collected: '2026-07-31'
category: Reasoning
direction: 多模态少样本知识图谱补全·LLM推理
tags:
- LLM Reasoning
- Knowledge Graph Completion
- Few-shot Learning
- Multimodal KG
- Dual-path Architecture
one_liner: 提出双路径LLM推理框架DuPLeR，缓解多模态少样本KGC的噪声与幻觉问题
practical_value: '- 做电商商品/用户知识图谱补全时，可复用双路径校准思路：将LLM生成的语义先验和factual结构融合，减少幻觉引入的错误关联

  - 少样本场景下引入多模态信息补充实体表征时，可借鉴「查询相关多模态信号调控消息传递」的trick，降低无关模态噪声的干扰

  - 涉及KG支撑的推荐/Agent任务（比如商品关联推荐、问答导购），可直接复用该框架优化冷启动实体/关系的链路预测效果'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
真实业务场景中知识图谱（KG）持续产生新实体、新关系，少样本/零样本下归纳式KG补全（KGC）难度极高；现有方法引入多模态信息、LLM先验补充稀疏上下文时，易引入噪声与幻觉证据，降低补全准确率。
### 方法关键点
1. 提出DuPLeR双路径LLM推理框架，融合多模态LLM输出的类型先验与事实支撑结构，构建校准后的关系图；
2. 对优化后的关系拓扑执行双层结构推理；
3. 设计双路径多模态增强模块，用查询相关的多模态信号调控消息传递，在图传播后补充实体表征。
### 关键结果
在2个多模态KG基准的8个归纳式变体数据集上，数据稀缺场景下KGC性能鲁棒性显著优于基线方法。
