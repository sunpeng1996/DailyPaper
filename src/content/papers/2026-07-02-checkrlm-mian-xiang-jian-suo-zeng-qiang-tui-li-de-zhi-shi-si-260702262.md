---
title: 'CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented
  Reasoning'
title_zh: CheckRLM：面向检索增强推理的知识-思维一致性校验框架
authors:
- Dingling Xu
- Ruobing Wang
- Qingfei Zhao
- Yukun Yan
- Zhichun Wang
- Daren Zha
- Shi Yu
- Zhenghao Liu
- Shuo Wang
- Xu Han
affiliations:
- 北京师范大学
- 中国科学院信息工程研究所
- 中国科学院大学
- 清华大学
- 东北大学
arxiv_id: '2607.02262'
url: https://arxiv.org/abs/2607.02262
pdf_url: https://arxiv.org/pdf/2607.02262
published: '2026-07-02'
collected: '2026-07-03'
category: RAG
direction: 检索增强生成 · 长推理链事实校验
tags:
- RAG
- Fact Checking
- Reasoning
- DPO
- Hallucination Mitigation
one_liner: 在长推理过程中动态抽取事实声明，基于RAG实时修正错误，缓解误差累积
practical_value: '- 电商咨询Agent、商品属性推理、搜索多跳问答场景可直接复用「段落级事实抽取+RAG校验+最小干预修正」的流程，替代全链路事后校验，降低
  hallucination 的同时减少推理开销

  - 优化RAG检索query时可参考「原始问题+当前推理段抽取的事实声明」的联合构造方式，比单独用推理内容检索的召回准确率更高，还能减少冗余召回

  - 长推理链类任务（比如复杂用户需求拆解、营销文案逻辑校验）优先选择推理中校验而非事后校验，可获得10%+的准确率提升，同时降低20%左右的token消耗'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLM（如o1、DeepSeek-R1）通过长推理链提升复杂任务表现，但推理过程中产生的事实错误会沿链路累积，导致最终结果大幅偏差；传统事后校验无法修正已经偏离的推理轨迹，普通RAG的单次/多步检索也无法适配长推理的动态事实校验需求，知识密集型任务的准确率和成本控制存在明显瓶颈。

### 方法关键点
- 两段式核心架构：① 推理中事实声明识别：按段落切割推理链，仅输入当前推理段+原始问题抽取关键事实声明，避免历史错误噪音；② 局部知识一致性修正：将原始问题+抽取的事实声明联合作为检索query，召回去重后的外部知识，做token级最小代价修正，不破坏原有推理结构。
- 用DPO同时优化事实识别和修正两个模块，基于少量高质量偏好数据引导模型输出精准事实、做最小改动修正，无需额外奖励模型。
- 选择段落级作为校验干预粒度，平衡校验及时性和推理连续性，避免频繁打断推理逻辑。

### 关键结果
在HotpotQA、2WikiMQA、MuSiQue等5个知识密集型QA数据集上，对比Vanilla RAG、Self-RAG、Search-o1等主流基线，基于QwQ-32B backbone的CheckRLM平均F1达45.4%，比SOTA基线Search-o1高3.9个百分点，比Vanilla RAG高13.8个百分点；推理中校验比事后校验F1平均高10%以上，同时比Search-o1降低32%左右的token消耗、15%的推理时间。

> 最值得记住：长推理链的事实修正，早干预比晚干预、局部最小修正比全局重构的性价比高得多
