---
title: 'MultAttnAttrib: Training-Free Multimodal Attribution in Long Document Question
  Answering'
title_zh: MultAttnAttrib：长文档问答场景下免训练多模态归因方法
authors:
- Dang Quang Thien Tran
- Quang V. Dang
- Vinamra Tyagi
- Sai Soorya Rao Veeravalli
- Trang Nguyen
- Ryan A. Rossi
- Franck Dernoncourt
- Nedim Lipka
- Koustava Goswami
- Samyadeep Basu
arxiv_id: '2607.01420'
url: https://arxiv.org/abs/2607.01420
pdf_url: https://arxiv.org/pdf/2607.01420
published: '2026-06-30'
collected: '2026-07-06'
category: LLM
direction: 多模态大模型 · 免训练归因
tags:
- Multimodal-Attribution
- Training-Free
- Attention-Head
- Long-Document-QA
- MLLM
one_liner: 提出免训练多模态归因方法，复用prefill注意力信号，性能追平GPT-5.4且延迟仅为prompt方法的1/7
practical_value: '- 电商/Agent场景的RAG溯源可复用该思路：无需额外训练，直接从模型prefill阶段的注意力头提取证据定位，延迟仅为prompt加引用方案的1/7，峰值显存降低15GB，适配低延迟QA场景

  - 图文混合内容（如商品详情页、营销素材）的问答归因可借鉴跨模态注意力头筛选+分模态阈值校准方法，比OCR转纯文本再归因的方案准确率高20%以上

  - 生成内容可信度校验场景可直接用预筛选的top-k检索头注意力信号做溯源，无需额外调用LLM验证，性能接近GPT-5.4，适合大规模生成内容质检'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent、QA类系统落地中，生成内容的归因溯源是保障用户信任与模型安全的核心需求，现有归因方案多针对纯文本场景，要么需要微调模型、要么依赖多轮prompt调用，推理成本高；而图文混合长文档场景下的细粒度归因既要定位文本证据也要定位图像证据，相关研究与评测基准均存在缺失。
### 方法关键点
1. 离线预处理仅需少量标注探针数据：用因果中介分析（CMA）筛选跨模态检索注意力头，抑制注意力分布均匀的无效头，再基于探针数据分别校准文本、图像的归因阈值，最大化F1
2. 在线推理仅需1次prefill pass：平均选中头的注意力信号，分别对图像patch、文本滑动窗口打分，经min-max归一化后过预校准阈值输出归因，无命中时fallback到最高得分项
3. 配套发布MULTATTREVAL评测基准，覆盖5个领域，包含纯文本、纯图像、图文混合三类归因场景的标注QA对
### 关键实验结果
基于Qwen3-VL-30B测试，较同底座prompt类baseline的F1提升超20%，图像归因F1达0.776，推理速度是prompt方案的7.3倍，峰值显存降低14.87GB；整体性能与GPT-5.4相当，其中图像归因精度超过所有GPT基线方案。

**最值得记住的一句话**：多模态大模型的检索信号高度集中在极少数注意力头中，仅需轻量校准即可实现低成本、高精度的归因，无需额外训练或复杂prompt工程。
