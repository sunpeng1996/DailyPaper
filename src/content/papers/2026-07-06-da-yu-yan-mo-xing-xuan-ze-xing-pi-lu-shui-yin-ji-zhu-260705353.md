---
title: Selective Disclosure Watermarking for Large Language Models
title_zh: 大语言模型选择性披露水印技术
authors:
- Xuyang Chen
- Xiang Li
- Yangxinyu Xie
- Qi Long
affiliations:
- University of Pennsylvania
arxiv_id: '2607.05353'
url: https://arxiv.org/abs/2607.05353
pdf_url: https://arxiv.org/pdf/2607.05353
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: 大语言模型 · 水印安全
tags:
- Watermarking
- LLM Security
- Selective Disclosure
- Hierarchical Routing
- Metadata Embedding
one_liner: 分层词汇路由框架HeRo实现LLM水印元数据细粒度选择性披露，兼顾文本质量与检测效率
practical_value: '- 生成式推荐/电商AI文案生成场景可接入HeRo水印，给不同层级的审核方/合作方开放对应元数据（如文案生成来源、批次），避免敏感运营数据泄露

  - Agent生成的用户交互消息、推荐理由可嵌入分层水印，出现合规风险时仅向监管方披露完整溯源信息，普通用户侧无法解码，兼顾合规与隐私

  - 该方案不改变LLM原生采样分布、无文本质量损失，可直接通过LoRA微调或推理侧插件接入现有生成式推荐链路，工程改造成本低'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM多比特水印方案存在设计缺陷：验证任意片段的水印信息都需要披露全部嵌入元数据，无访问控制能力，易造成不必要的信息泄露，无法满足生成内容溯源、分级合规的场景需求。

### 方法关键点
Hierarchical Vocabulary Routing（HeRo）水印框架通过递归切分LLM词表，将水印元数据分层存储在不同层级结构中，不同权限的验证方仅能解码对应权限范围内的负载信息；框架保留底层采样过程的无偏性，不会改变生成文本的自然度。

### 关键结果
实验验证方案支持细粒度访问控制，水印检测准确率高、推理延迟低，代码已开源可直接复用。
