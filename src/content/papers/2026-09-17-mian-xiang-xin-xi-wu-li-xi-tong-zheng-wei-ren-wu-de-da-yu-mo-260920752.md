---
title: Large Language Models as Falsifiers for Cyber-Physical Systems
title_zh: 面向信息物理系统证伪任务的大语言模型方法
authors:
- Ali ArjomandBigdeli
- Jiawei Zhou
- Stanley Bak
affiliations:
- Stony Brook University, USA
arxiv_id: '2609.20752'
url: https://arxiv.org/abs/2609.20752
pdf_url: https://arxiv.org/pdf/2609.20752
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: 大语言模型 · CPS证伪优化
tags:
- LLM
- Optimization
- Falsification
- Cyber-Physical-Systems
- Signal-Temporal-Logic
one_liner: 提出融合语义信息的LLM驱动CPS证伪框架，采样效率优于现有多类传统优化工具
practical_value: '- 本研究核心面向CPS证伪领域，电商/推荐/Agent业务可直接借鉴点有限，以学术贡献为主

  - 若开展基于LLM的黑盒优化类任务，可参考将数值特征映射为自然语言语义标签的技巧，提升LLM对优化目标的理解度

  - 迭代优化prompt时可加入临界值对应的关键见证信息，有效降低优化所需的采样次数'
score: 3
source: arxiv-cs.AI
depth: abstract
---

### 动机
信息物理系统（CPS）的信号时序逻辑（STL）规范证伪传统依赖黑盒数值优化方法，采样效率低，而LLM配合迭代prompt已展现出优秀的优化能力，二者此前未形成有效结合。
### 方法关键点
提出LLM-Falsifier框架，在通用prompt优化基础上，额外为LLM输入三类传统数值优化器不具备的语义信息：输入输出的自然语言命名、输出轨迹数据、最小鲁棒性值对应的关键时间见证信息，通过迭代prompt最小化STL鲁棒度完成证伪搜索。
### 关键结果
在ARCH-COMP证伪基准上，按找到反例所需平均仿真次数统计，21个测试规范中有14个的表现优于基于代理优化、贝叶斯优化、搜索测试等范式的现有证伪工具。
