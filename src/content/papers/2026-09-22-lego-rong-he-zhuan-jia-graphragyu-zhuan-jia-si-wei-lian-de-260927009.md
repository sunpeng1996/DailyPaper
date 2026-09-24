---
title: 'LEGO: Synergizing Expert GraphRAG and Expert Chain-of-Thought for Legal Reasoning'
title_zh: LEGO：融合专家GraphRAG与专家思维链的法律推理框架
authors:
- Qingjing Chen
- Junkai Zhang
- Shaochun Wang
- Jiahao Ding
- Siyuan Zheng
- Yukun Yan
- Zhi Zheng
- Antonino Rotolo
- Yun Liu
- Weixing Shen
affiliations:
- University of Bologna
- Tsinghua University
- Xiamen University
- Shanghai Jiao Tong University
- Modelbest Inc.
arxiv_id: '2609.27009'
url: https://arxiv.org/abs/2609.27009
pdf_url: https://arxiv.org/pdf/2609.27009
published: '2026-09-22'
collected: '2026-09-24'
category: Reasoning
direction: 垂直领域推理 · 专家GraphRAG+结构化CoT
tags:
- GraphRAG
- Chain-of-Thought
- Knowledge Graph
- Prompt Engineering
- Legal Reasoning
one_liner: 融合专家GraphRAG与结构化CoT的推理框架，8B参数效果比肩千亿级大模型
practical_value: '- 垂类Agent（如电商售后判责、广告合规审查）做RAG时，可引入专家标注的领域规则图谱，用覆盖度+冗余惩罚的贪心检索策略替代纯语义相似度检索，大幅提升多跳规则召回准确率

  - 高可靠性要求的垂类推理场景，可将CoT固化为领域通用三段论结构（如规则-事实-结论），通过强约束prompt规范推理路径，降低小模型推理漂移、幻觉问题

  - 垂直业务可优先选择「小参数基座+领域结构化知识注入」的方案，能在远低于大模型的成本下实现同等甚至更优的推理效果，适配低延时业务需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG/GraphRAG依赖语义相似度检索，忽略垂类专业知识间的规范关联（如规则优先级、例外关系），通用CoT无法保证推理符合专业领域的逻辑约束，导致高风险垂类的多跳推理准确率低、鲁棒性差，尤其法律这类对推理严谨性要求极高的场景问题更突出。
### 方法关键点
- 双模块架构LEGO：由ExpertGraphRAG和ExpertCoT组成，分别解决检索和推理环节的瓶颈
- ExpertGraphRAG基于专家标注的民法典规则图谱，采用Normative Coverage Greedy（NCG）贪心检索算法，优先选择能覆盖新增规则点、冗余度低的条文，输出实例相关的条文子图而非纯语义相似列表
- ExpertCoT强制输出「规则（P）-事实（F）-结论（C）」三段论结构，通过11条明确的prompt约束推理过程，避免规则误用、逻辑漂移等问题
### 关键实验
基于Qwen3-8B基座，在三个民法推理数据集上测试：LawExamQA_Civil（司法考试选择题）、LexRAG_Civil（多轮法律咨询）、PLawBench_Civil（真实案例分析）；对比基线含GPT-5、DeepSeek-V3 671B、同参数各类RAG/CoT方案。核心结果：LawExamQA_Civil整体准确率40.53%，超过GPT-5（37.48%）、DeepSeek-V3 671B（39.97%）；≥4跳复杂推理准确率38.71%，较第二基线高6.45个百分点；两个开放域基准所有维度得分均为第一。
### 最值得记住的一句话
垂直领域复杂推理场景中，用专家结构化知识同时优化检索和推理环节，小参数模型的效果可以比肩甚至超过千亿级通用大模型。
