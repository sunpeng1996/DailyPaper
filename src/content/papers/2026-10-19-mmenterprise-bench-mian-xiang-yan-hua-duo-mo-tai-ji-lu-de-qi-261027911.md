---
title: 'MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal
  Records'
title_zh: MMEnterprise-Bench：面向演化多模态记录的企业智能体评测基准
authors:
- Seohyun Lee
- Jongha Kim
- Dohwan Ko
- Ji Soo Lee
- Seoung Choi
- Jayun Ku
- Hyunwoo J. Kim
affiliations:
- KAIST
- Korea University
arxiv_id: '2610.27911'
url: https://arxiv.org/abs/2610.27911
pdf_url: https://arxiv.org/pdf/2610.27911
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: 企业Agent · 多模态QA评测
tags:
- Enterprise Agent
- Multimodal LLM
- Benchmark
- RAG
- Conflict Resolution
one_liner: 构建面向演化多模态企业记录的智能体QA评测基准，验证现有模型核心性能短板
practical_value: '- 搭建企业内部知识库RAG/Agent时，必须显式设计跨源冲突消解、时间版本校验模块，现有通用多模态LLM在这两类任务上准确率不足40%，纯靠提升检索量无法解决问题

  - 可复用该基准的测试集构造方法：基于真实业务文档模拟协作更新链路，生成覆盖证据推理、冲突消解、不可答三类场景的评测集，用于衡量自有业务Agent的可靠性

  - 实验结论可直接复用：单纯提升召回topK、替换更大参数的召回器仅能提升证据召回率，不会稳定提升最终QA准确率，小模型反而可能因上下文噪声出现负收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前企业级Agent需要处理跨文档、聊天、图表的多源异构记录，而团队协作过程中会产生跨源信息不一致、多历史版本留存两类冲突，现有评测基准未覆盖多模态下的演化冲突场景，无法有效衡量企业Agent的实际可靠性。

### 方法关键点
- 模拟30个真实企业协作项目，基于公开论文/政府报告生成7140条多模态记录（含文本、聊天、邮件、图表、幻灯片等），保留历史版本不覆盖，天然构造跨源、时间两类冲突
- 标注1613道QA对，覆盖三大类8个子任务：证据推理（含抽取、归因、计算等5个子任务）、冲突消解（跨源冲突、时间冲突）、不可答识别
- 评测流程采用标准RAG范式，通过不同召回规模、不同大小召回器的组合测试模型端到端性能，用GPT-5.6 Luna作为自动判分器

### 关键实验
- 测试10款开源/闭源多模态LLM，最强模型GPT-5.6 Sol在召回top10、top50时准确率仅为52.6%、68.0%
- 冲突消解类任务性能极低：跨源冲突准确率11.8%~36.3%，时间冲突准确率13.2%~33.5%；多图推理时准确率仅为单文本场景的1/3
- 召回topK从10提升到100、召回器从2B升到8B仅稳定提升证据召回率，不会一致提升最终QA准确率，小模型甚至会因为上下文噪声出现性能下降

### 核心结论
企业级Agent的核心瓶颈不是召回能力，而是多源多模态证据的冲突消解与时间版本校验能力，单纯堆召回规模解决不了实际问题。
