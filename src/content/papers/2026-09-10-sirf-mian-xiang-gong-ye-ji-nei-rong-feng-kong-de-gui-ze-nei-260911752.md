---
title: 'SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk
  Control'
title_zh: SIRF：面向工业级内容风控的规则内化风险基础模型
authors:
- Suwan Wu
- Yumeng Lin
- Pengcheng Yuan
- Xiaolong Jiang
affiliations:
- Xiaohongshu Inc.
- Tianjin University
arxiv_id: '2609.11752'
url: https://arxiv.org/abs/2609.11752
pdf_url: https://arxiv.org/pdf/2609.11752
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: 大模型规则内化 · 工业内容风控
tags:
- Continual Pre-training
- Content Moderation
- Synthetic Data
- Low-latency Inference
- Foundation Model
one_liner: 通过70M合成token的规则内化持续预训练，低延迟风控模型P95精度下黑产召回提升15.1pp
practical_value: '- 高precision+低延迟的分类决策场景（如电商违规治理、广告审核）可优先用规则内化CPT替代RAG/长prompt注入，既降推理开销，又提升高置信区间召回率

  - 规则类知识注入可复用EntiGraph+MAGA+领域CoT的无额外人工标注合成范式，低成本生成领域预训练语料

  - 高stakes决策场景可直接取LLM输出首token概率作为置信度排序依据，无需依赖CoT或后处理校准，即可实现阈值动态调整

  - 千万级token的定向领域CPT几乎不损伤大模型通用能力，可快速通过轻量SFT迁移到同领域其他子任务'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工业内容风控属于高stakes决策场景，核心约束不是平均准确率，而是高precision下的风险自动处理占比+秒级延迟：现有RAG/长prompt注入规则的方案存在检索和上下文开销，无法满足延迟要求；纯分类器方案需要覆盖所有规则分支的海量标注，长尾规则难以落地。
### 方法关键点
- 规则语料无标注合成：通过EntiGraph实体规则拆解、MAGA多视角改写、账号级CoT推理蒸馏三个路径，仅基于现有规则文档和账号特征，无额外人工标注生成70M风控领域预训练语料
- 两阶段训练：先做规则导向的持续预训练（CPT）将平台风控规则内化到模型权重，再做轻量领域SFT对齐判决输出格式，训练/部署无gap
- 低延迟部署：仅输出判决标签，取输出首token概率作为置信度，支持运营动态调整阈值无需重训，无需中间推理步骤
### 关键结果
- 同源对照实验仅差CPT阶段，SIRF-8B-SFT的Black Recall@P95达71.3，比Qwen3-8B-SFT基线高15.1pp，性能超过400B级开源/闭源大模型
- 上线作为规则引擎的二级判决层，多恢复20%被误罚的正常样本；跨冻结场景迁移仅需轻量SFT，即可降低70%相对误判
- 规则内化后prompt可裁剪13%，高并发下端到端延迟降低18%、QPS提升23%，10个通用基准测试显示模型通用能力几乎无损失
### 核心结论
高stakes决策场景的优化目标不是平均准确率，而是高precision约束下的可自动处理覆盖度
