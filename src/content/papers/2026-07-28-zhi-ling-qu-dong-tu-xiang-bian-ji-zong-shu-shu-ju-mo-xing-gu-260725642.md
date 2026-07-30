---
title: 'Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and
  Applications'
title_zh: 指令驱动图像编辑综述：数据、模型、评估与应用
authors:
- Xianghao Zang
- Zijian Jiang
- Jiarong Cheng
- Qianrui Teng
- Ying He
- Yuxuan Mu
- Chao Ban
- Huayu Zhang
- Lanxiang Zhou
- Zerun Feng
affiliations:
- 中国电信人工智能研究院（TeleAI）
arxiv_id: '2607.25642'
url: https://arxiv.org/abs/2607.25642
pdf_url: https://arxiv.org/pdf/2607.25642
published: '2026-07-28'
collected: '2026-07-30'
category: Multimodal
direction: 多模态 · 指令驱动图像编辑综述
tags:
- Instruction-based Image Editing
- VLM
- Diffusion Model
- Evaluation Benchmark
- Multimodal
one_liner: 系统梳理指令驱动图像编辑全链路进展，提出CDD-IIE诊断基准，对比主流开源方案能力边界
practical_value: '- 可复用IIE任务分类体系搭建电商商品图一键编辑工具，支撑主图换背景、加营销标签、改价标等场景降低素材制作成本

  - 参考CDD-IIE Bench的多维度评估框架，搭建自有文生图/图生图业务效果评测体系，减少人工打分的主观偏差

  - 选型开源图像编辑方案时可直接复用论文的实测对比结论，匹配业务对编辑精度、生成速度、鲁棒性的差异化需求'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统图像编辑工具依赖复杂手动操作，LLM与VLM技术突破催生了实用化指令驱动图像编辑（IIE）需求，但领域缺乏系统梳理与统一评估标准，阻碍产业落地。
### 方法关键点
1. 搭建5维IIE研究框架，覆盖任务分类、训练数据构建、架构演进（GAN→扩散/自回归范式）、评估体系、商用方案盘点；
2. 提出CDD-IIE Bench多维度诊断基准，可严谨衡量模型多维度性能；
3. 实测主流开源IIE方案，明确各方案的能力边界与局限性。
### 关键结果
系统梳理了IIE技术演进全链路里程碑，CDD-IIE Bench相较现有评估体系覆盖维度更全、诊断性更强，开源方案对比结论可直接支撑产业级选型。
