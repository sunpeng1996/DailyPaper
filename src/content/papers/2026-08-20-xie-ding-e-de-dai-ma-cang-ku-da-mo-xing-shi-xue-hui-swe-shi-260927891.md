---
title: 'Schrödinger''s Code Repository: Have LLMs Learned SWE-bench or Memorized It?'
title_zh: 薛定谔的代码仓库：大模型是学会SWE-bench还是靠记忆
authors:
- Silin Chen
- Yufei Yang
- Xiaodong Gu
- Yuling Shi
- Chengcheng Wan
- Haibing Guan
affiliations:
- Shanghai Jiao Tong University
- Xi'an Jiaotong University
- East China Normal University
- Shanghai Innovation Institute
arxiv_id: '2609.27891'
url: https://arxiv.org/abs/2609.27891
pdf_url: https://arxiv.org/pdf/2609.27891
published: '2026-08-20'
collected: '2026-09-24'
category: Eval
direction: Agent能力评估 · 记忆泄露检测
tags:
- Coding Agent
- Evaluation Framework
- Data Leakage
- LLM Memorization
- SWE-bench
one_liner: 提出动态实例化代码仓库的评估框架，区分编码Agent的推理能力与训练数据记忆
practical_value: '- 做业务Agent能力评估时，可引入表层特征动态变换的测试范式，排除训练数据泄露导致的性能虚高

  - 自研电商客服、工单处理等垂直场景Agent时，可构造特征变换后的反记忆测试集，验证真实推理能力

  - 对RAG系统的召回/理解能力测试，可通过改写知识库命名、结构，校验模型是否真正理解内容而非表层匹配'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有代码仓库级编码Agent基准普遍存在训练数据泄露问题，无法区分模型高性能来自真实推理能力，还是对仓库命名、布局等表层线索的记忆。
### 方法关键点
SchrodingerRepo评估框架将测试仓库作为评估时隐变量，仅在Agent进入评估环境时动态实例化，生成语义等价、可执行性不变但表层特征被侵蚀的仓库变体，包含四层变换：问题描述重构、命名空间重映射、文件内布局重排、功能不变代码改写。
### 关键结果
在SWE-bench Verified和SWE-QA上测试主流LLM，移除熟悉的仓库线索后，所有模型性能一致下降，交互成本显著提升，额外成本主要来自仓库探索和定位难度升高，证明当前编码Agent性能部分依赖对仓库表层线索的记忆。
