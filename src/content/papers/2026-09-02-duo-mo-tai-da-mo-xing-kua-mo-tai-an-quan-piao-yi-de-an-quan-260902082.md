---
title: Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large
  Language Models
title_zh: 多模态大模型跨模态安全漂移的安全感知迁移方法
authors:
- Tianqi Xiao
- Shiyao Cui
- Minghao Zhang
- Junxiao Yang
- Renmiao Chen
affiliations:
- 清华大学CoAI组计算机科学与技术系
- 北京邮电大学网络空间安全学院
- 西北工业大学
arxiv_id: '2609.02082'
url: https://arxiv.org/abs/2609.02082
pdf_url: https://arxiv.org/pdf/2609.02082
published: '2026-09-02'
collected: '2026-09-05'
category: LLM
direction: 多模态大模型 · 跨模态安全对齐
tags:
- MLLM
- Safety Alignment
- Cross-Modal Safety Drift
- Representation Transfer
- Frozen Backbone
one_liner: 提出轻量安全感知表征迁移方法SRT，冻住MLLM主干即可缓解跨模态安全漂移且保留效用
practical_value: '- 涉及多模态输入的电商导购Agent、商品内容审核场景可复用SRT方案，无需微调MLLM主干即可提升跨模态场景安全防护能力，大幅降低对齐成本

  - 多模态商品推荐、广告创意审核场景可参考风险cue注意力分析逻辑，优化现有多模态风险识别模块对视觉风险信号的权重分配，提升违规内容检出率

  - 落地MLLM跨模态安全对齐时可复用纯文本LLM的现有安全对齐成果，通过表征迁移思路降低跨模态安全对齐的研发和数据成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态大模型（MLLM）引入视觉模态后存在跨模态安全漂移问题：无害文本查询搭配有害视觉输入时，模型安全响应率远低于纯文本有害查询场景，现有对齐方案对这类风险识别能力不足。
### 方法关键点
首先通过实证分析定位不安全响应模式，发现模型对视觉风险线索注意力不足、触发拒答的信号弱；提出轻量安全感知表征迁移（SRT）方法，冻结MLLM主干的前提下，将纯文本不安全处理的安全信号迁移到跨模态场景，通过方向优化修正表征。
### 关键结果
跨多个主流MLLM和安全基准测试验证，SRT在各类跨模态场景下有效提升安全防护能力，同时几乎不损失原有任务效用，代码已开源。
