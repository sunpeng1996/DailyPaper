---
title: Dynamic Commonsense Coordination for Empathetic Response Generation
title_zh: 面向共情回复生成的动态常识协调框架
authors:
- Zhengyu Qi
affiliations:
- Leiden Institute of Advanced Computer Science (LIACS)
- Leiden University, The Netherlands
arxiv_id: '2607.22136'
url: https://arxiv.org/abs/2607.22136
pdf_url: https://arxiv.org/pdf/2607.22136
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: 大模型共情对话生成优化
tags:
- Empathetic Response Generation
- Commonsense Reasoning
- Dynamic Knowledge Retrieval
- Dialogue Generation
- Knowledge Augmented LLM
one_liner: 提出含三个互补模块的动态常识协调框架DCC，提升共情回复生成的情感识别与回复质量
practical_value: '- 电商智能客服Agent的共情回复场景，可复用AGCF模块过滤低相关常识，减少无效回复，降低用户不满概率

  - 个性化推荐话术、售后安抚话术生成场景，可借鉴ICAD动态检索常识记忆的思路，提升话术相关性与温度

  - SCE-AttnRes残差融合上下文与场景常识的方法，可迁移到用户情绪识别任务，提升负向情绪预警准确率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有共情回复生成（ERG）方法在理解、生成阶段复用固定常识表征，无法适配不同阶段的知识需求，限制了情感识别准确率与回复质量。
### 方法关键点
提出DCC动态常识协调框架，包含三个互补模块：
1. 残差式常识交互模块（SCE-AttnRes）：融合上下文与场景常识表征
2. 关联引导常识过滤模块（AGCF）：降低低相关常识关系的权重
3. 迭代式常识感知解码模块（ICAD）：生成阶段动态检索常识记忆
### 关键结果
在Empathetic-Dialogues基准上，相比CEM基线，情感分类准确率、回复多样性均有提升，困惑度持平；LLM盲测显示生成的回复在相关性、连贯性、信息丰富度上表现更优。
