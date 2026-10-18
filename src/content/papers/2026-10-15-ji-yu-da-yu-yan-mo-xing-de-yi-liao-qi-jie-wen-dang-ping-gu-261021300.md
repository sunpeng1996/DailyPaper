---
title: Making every stage of medical device document assessment with large language
  models deterministic
title_zh: 基于大语言模型的医疗器械文档评估全流程确定性实现
authors:
- Ryosuke Suzuki
affiliations:
- GFLOPS Co., Ltd., Tokyo, Japan
arxiv_id: '2610.21300'
url: https://arxiv.org/abs/2610.21300
pdf_url: https://arxiv.org/pdf/2610.21300
published: '2026-10-15'
collected: '2026-10-18'
category: LLM
direction: LLM落地 · 确定性部署与可复现性
tags:
- LLM
- Determinism
- RAG Pipeline
- Reproducibility
- Regulatory Compliance
one_liner: 构建全环节可控的LLM评估管线，实现医疗合规场景下可复现可审计的确定性输出
practical_value: '- 做合规要求高的LLM应用（如电商资质审核、广告合规校验）时，可参考全链路确定性管控方案，将GPU型号、推理引擎调度参数纳入配置归档，避免输出波动

  - RAG管线的OCR、切块、embedding、检索、推理每一步都要做不变性校验，排查非模型本身导致的输出差异，提升线上服务稳定性

  - 调用商用LLM接口做确定性要求高的任务时，不能仅依赖厂商提供的确定性采样参数，需提前做重复请求一致性验证，规避服务端隐藏的调度波动'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
医疗合规类文档评估要求可审计、可复现，但现有商用LLM即使开启确定性采样，输出仍存在不可控波动，无法满足场景要求。
### 方法关键点
拆解LLM+RAG评估全链路的波动来源，对OCR、文本切块、embedding、索引、检索、推理每一步做确定性改造，固定GPU型号、推理引擎调度参数、所有组件的运行配置，将所有可变参数纳入可追溯归档范围。
### 关键结果数字
测试14个商用LLM部署，100%存在至少1次同请求输出差异，其中12个部署会出现合规判定标签翻转；自研全确定性管线在同型号GPU下，跨重跑、中断、编辑、不同机器、跨天测试，所有环节输出完全字节一致。
